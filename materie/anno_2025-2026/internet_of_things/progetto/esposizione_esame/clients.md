---
title: "Clients"
aliases: ["Clients"]
tags: [università, "materie", "anno-2025-2026", "internet-of-things", "progetto", "esposizione-esame", "clients"]
created: 2026-07-23
---
## Struttura e ruolo di ogni file

|File|Ruolo|
|---|---|
|`main.py`|**Entrypoint/orchestratore**: avvia la Device API locale, risolve l'identità (pairing/provisioning), costruisce i client (MQTT, camera, HTTP), gestisce il loop heartbeat e i comandi in arrivo da MQTT|
|`config.py`|`Settings` (dataclass frozen) con tutta la config da env: identità citofono, URL hub, credenziali/topic MQTT, parametri camera e capture continua|
|`registration_client.py`|Handshake **HTTP verso il backend**: crea/pollinga la richiesta di pairing, poi fa il provisioning e persiste l'identità ottenuta su file JSON locale|
|`camera_capture.py`|Astrazione sorgente immagine: `UsbCameraCapture`/`TestImageCapture` (scatto singolo) e `ContinuousCameraStream`/`TestImageStream` (stream continuo). `CAPTURE_SOURCE=camera|
|`continuous_capture.py`|Loop di cattura continua: rileva volti frame-per-frame (thread separato), calcola uno "score" di qualità del frame, decide quando aprire/chiudere una sessione e quando fare upload definitivo vs. solo analisi|
|`captured_image_http_client.py`|Client **HTTP verso il backend** per upload capture definitiva e per l'endpoint di analisi candidato (senza persistenza)|
|`mqtt_control_client.py`|Client **MQTT verso il backend**: pubblica heartbeat/status/eventi, riceve comandi|
|`live_view.py`|`LiveViewFrameBuffer`: buffer thread-safe in memoria con l'ultimo frame JPEG + metadata + log eventi. Il loop di continuous capture è l'unico "produttore" del frame grezzo|
|`device_api.py`|**Server FastAPI locale** (porta separata, default 8090) che espone il buffer di `live_view.py` via HTTP/MJPEG — è la "Device API" del citofono, **non parla mai col backend**|

## Collegamenti client ↔ backend

Ci sono **tre canali distinti**, tutti verso il backend (`HOME_HUB_BASE_URL`):

### 1. HTTP — pairing e provisioning (una tantum, all'avvio)

Gestito da `registration_client.py`, chiamato da `main.py` prima di aprire la sessione MQTT:

1. `POST /api/prototype/intercom-pairing/candidates` → crea/rinfresca un candidato di pairing (il citofono non ha ancora un `home_intercom_id`)
2. Polling `GET /api/prototype/intercom-pairing/candidates/{id}/status` finché lo stato non è `approved` (l'operatore approva da frontend — vedi `routers/pairing.py` sul backend)
3. `POST /api/prototype/home-intercoms` → provisioning: il backend crea `HomeIntercom` + `HomeIntercomMqttUser` e risponde con `home_intercom_id`, `mqtt_username`, i 4 topic MQTT
4. L'identità viene salvata in `INTERCOM_STATE_FILE` (JSON), così i riavvii successivi saltano il pairing (`resolve_intercom_identity`)

### 2. HTTP — invio immagini (durante il funzionamento)

Gestito da `captured_image_http_client.py`, usato sia da `main.py` (capture singola su comando) sia da `continuous_capture.py`:

- `POST /api/prototype/intercoms/{home_intercom_id}/captures` (o l'alias `/local/v1/intercoms/{id}/captures`) → upload multipart definitivo. Sul backend arriva a `services/images.create_and_process_capture` (salvataggio file + face recognition + assegnazione persona)
- `POST .../capture-candidates/analyze` → **solo analisi**, nessuna persistenza sul backend (`services/images.analyze_candidate_image_server_side`); usato dalla capture continua come "assaggio" prima di decidere se fare l'upload definitivo

### 3. MQTT — control plane continuo (bidirezionale via broker Mosquitto)

Gestito da `mqtt_control_client.py`:

- **Citofono → backend**: `heartbeat` (ogni `HEARTBEAT_INTERVAL_SECONDS`), `status` (stato runtime + info live-view, letto da `mqtt_client.py` sul backend che aggiorna `HomeIntercomRuntimeStatus`), `events` (es. `continuous_session_started/ended`, `capture_failed`, `continuous_frame_uploaded`)
- **Backend → citofono**: `commands` — `capture_once`, `start_continuous_capture`, `stop_continuous_capture`, `registration_required` (gestiti in `main.py:handle_command`, dispatchati dal backend via `services/intercoms.dispatch_intercom_command`)

### 4. Device API locale — NON tocca il backend

`device_api.py` apre un **secondo server HTTP indipendente** (porta `DEVICE_API_PORT`, default 8090) che espone `live/stream` (MJPEG), `live/frame`, `live/status`, `live/metadata`, `live/events`. Il backend **non fa da proxy**: pubblica solo, via MQTT `status`, i fatti di rete grezzi (hostname/IP/porta) che il backend stesso usa per calcolare l'URL con cui il **frontend** raggiunge direttamente questa Device API sulla LAN (`services/intercoms.build_local_url` sul backend). Per l'esame: è importante distinguere questo canale "diretto LAN" dai due canali HTTP/MQTT verso il backend sopra.

## Flusso end-to-end (utile da raccontare a esame)

```
avvio processo
 └─ main.py avvia device_api.py (server locale) in un thread
 └─ registration_client.py: pairing HTTP → provisioning HTTP → identità salvata
 └─ mqtt_control_client.py si connette, si iscrive a "commands"
 └─ loop principale: pubblica heartbeat + status ogni N secondi

comando "start_continuous_capture" arriva via MQTT
 └─ continuous_capture.py apre lo stream camera, thread di detection separato
 └─ per ogni frame: aggiorna live_view.py (visibile via device_api.py)
 └─ quando una finestra di rilevamento è "stabile": analizza o carica via HTTP
      → captured_image_http_client.py → backend → face recognition → risposta
 └─ pubblica eventi MQTT (session_started/ended, frame_uploaded...)
```