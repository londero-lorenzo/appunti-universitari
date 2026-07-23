---
title: "Backend"
aliases: ["Backend"]
tags: [università, "materie", "anno-2025-2026", "internet-of-things", "progetto", "esposizione-esame", "backend"]
created: 2026-07-23
---
## Vista d'insieme

Il backend è FastAPI, splittato per **dominio** (dal 21/07/2026). Ogni dominio ha (fino a) 3 file paralleli: uno **schema** (contratto dati), un **service** (logica), un **router** (HTTP). `main.py` (~70 righe) fa solo l'assembly: crea l'app, CORS, hook MQTT startup/shutdown, e monta i router.

```
config.py    → costanti da env (STORAGE_ROOT, FACE_MATCH_TOLERANCE, timeout...)
deps.py      → dependency condivise: get_db, get_or_404, commit_or_409/flush_or_409, parsing date
schemas/     → modelli Pydantic richiesta/risposta (I/O dell'API)
services/    → business logic (nessun endpoint qui, solo funzioni pure/DB)
routers/     → endpoint HTTP: parse richiesta → chiama service → restituisce risposta
models.py    → ORM SQLAlchemy (le tabelle reali)
```

Regola d'oro da citare: **i router sono "thin"** — non contengono logica, solo orchestrazione. Tutta la logica interessante vive in `services/`.

## I 5 domini di `services/` + `routers/`

**1. `intercoms.py`** — identità e ciclo di vita dei citofoni

- Genera username/topic MQTT dal serial number, calcola stato runtime (`ONLINE`/`OFFLINE`/`UNKNOWN`) da `last_heartbeat_at` vs timeout configurabile
- Risolve l'IP "giusto" da usare per contattare il citofono in LAN, con precedenza: IP manuale → IP riportato → IP risolto → hostname `.local` (perché `.local` spesso non si risolve in rete)
- Dispatch comandi (`start-continuous-capture`, `stop-continuous-capture`, `capture-once`) via MQTT — controlla che il citofono sia online prima di pubblicare
- Router: CRUD citofoni, provisioning dopo pairing, stato runtime, comandi

**2. `images.py`** — la pipeline core di face recognition

- Salvataggio immagini + thumbnail su disco (`STORAGE_ROOT/owners/<slug>/...`)
- `find_best_person_match`: confronta un nuovo embedding con quelli delle persone già note dello stesso owner (`face_recognition.compare_faces`, tolleranza da config) — voto a maggioranza tra gli embedding storici della persona
- `process_image_server_side`: per ogni volto rilevato crea `CapturedImageFace` + `CapturedImageFaceEmbedding`, poi o lo assegna a una persona esistente o ne crea una nuova (`DetectedPerson`)
- `analyze_candidate_image_server_side`: stessa logica ma **senza persistere nulla** — usata dal citofono in continuous-capture per decidere se un frame vale la pena di essere inviato come capture definitiva
- Router: upload/analisi capture (con alias sotto `/prototype/...` e `/local/v1/...`, vedi sotto)

**3. `gallery.py`** — building blocks condivisi per la UI (galleria/dettaglio)

- Costruisce URL pubblici per thumbnail/file, verifica se il file è ancora disponibile (non "purgato")
- `build_gallery_item`/`build_captured_image_detail`: aggregano capture + evento + volti + assegnazioni in DTO pronti per il frontend
- È il modulo "a monte": `people.py` e `overlay.py` importano da qui, mai il contrario (regola di dipendenza esplicita nella skill)

**4. `people.py`** — lifecycle delle persone rilevate

- Sceglie la "preview" di una persona (foto preferita o fallback), con vincolo: solo capture con **un solo volto** possono essere preview/favorite (altrimenti l'immagine sarebbe ambigua)
- Soft-delete con purge selettivo dei file: quando elimini una persona, i file vengono cancellati dal disco tranne l'immagine di preview (preservata), per liberare spazio senza perdere il riferimento visivo

**5. `overlay.py`** — rendering di debug

- Disegna bounding box + etichette (nome/stato/id persona) sopra il JPEG con OpenCV, per ispezione visiva nella dashboard (`?overlay=true` sul file endpoint)

Più due router senza service dedicato: `home_owners.py` (CRUD owner minimale) e `events.py` (update/listing eventi campanello).

## Pairing: un dominio a parte

`pairing.py` (schema+router, logica dentro `services/intercoms.py`) gestisce l'handshake device→hub: il citofono crea un "candidate" con il suo serial number, il frontend lo approva/rifiuta, e solo dopo approvazione il citofono può fare provisioning reale (`POST /prototype/home-intercoms`) ottenendo credenziali MQTT.

## Un filo conduttore utile per la demo

Segui una singola richiesta end-to-end, è il modo più efficace di spiegarlo a esame:

1. Citofono in continuous-capture manda un frame a `POST /captures/analyze` → `services/images.analyze_candidate_image_server_side` (nessuna scrittura DB, solo decisione)
2. Quando decide di "premere il campanello": `POST .../captures` → `services/images.create_and_process_capture` → salva immagine+thumbnail, crea `CapturedImage` + `DoorbellEvent`, poi `process_image_server_side` rileva volti, calcola embedding, fa matching con `find_best_person_match`, crea/aggiorna `DetectedPerson`
3. Frontend polla `GET /prototype/doorbell-events/recent` e mostra la galleria via `GET /prototype/captured-images` → `services/gallery.build_gallery_item`

**Dettaglio interessante da menzionare**: esistono due percorsi HTTP identici per upload/analisi capture — `/api/prototype/...` (`routers/captures.py`) e `/local/v1/...` (`routers/local.py`) — entrambi chiamano _le stesse_ funzioni di `services/images.py`. È un alias verso l'architettura futura hub-centrica (`/local/v1` è il path che userà davvero il citofono quando ci sarà autenticazione forte), non duplicazione di logica.

Se vuoi, posso prepararti anche uno schema visuale (diagramma) di queste dipendenze da usare come slide.

## Vista d'insieme

Il backend è un'app **FastAPI** con architettura a livelli, separata per dominio dal 21/7/2026. Prima era un unico `main.py` da 2800 righe; ora è divisa così (dal basso, "moduli foglia", verso l'alto):

```
database.py + models.py   →  livello dati (SQLAlchemy)
config.py + deps.py       →  fondamenta condivise (costanti env, dependency FastAPI)
mqtt_client.py            →  integrazione MQTT (heartbeat/status/eventi citofoni)
schemas/                  →  contratti I/O (Pydantic), per dominio
services/                 →  logica di business, per dominio
routers/                  →  endpoint HTTP, per dominio
main.py                   →  assembly finale (~70 righe)
```

Il principio guida: **i router sono "thin"** (parsing richiesta → chiamata a un service → risposta), tutta la logica vive nei `services/`.

## 1. Livello dati

- **[database.py](vscode-webview://0npgoqo9ld7og79e7f1rt5g25cr3pcfvn8d4t15vsc9fmcr5oams/backend/app/database.py)**: legge le var d'ambiente Postgres, crea l'`engine` SQLAlchemy e `SessionLocal` (factory di sessioni). Fallisce subito all'avvio se mancano variabili — niente valori di default silenziosi.
- **[models.py](vscode-webview://0npgoqo9ld7og79e7f1rt5g25cr3pcfvn8d4t15vsc9fmcr5oams/backend/app/models.py)**: tutti gli ORM SQLAlchemy + gli enum Python che rispecchiano i tipi enum Postgres (`pg_enum` forza i _valori_ stringa, non i nomi Python, per matchare l'enum DB). Entità chiave e relazioni:
    - `HomeOwner` 1—N `HomeIntercom` 1—N `CapturedImage` 1—N `CapturedImageFace` 1—N `CapturedImageFaceEmbedding`
    - `HomeIntercom` 1—1 `HomeIntercomMqttUser` (credenziali MQTT) e 1—1 `HomeIntercomRuntimeStatus` (stato live)
    - `HomeIntercomPairingRequest`: handshake di pairing prima che un citofono diventi un `HomeIntercom` vero
    - `DetectedPerson` 1—N `DetectedPersonFaceAssignment` (assegna un volto rilevato a una persona, con metodo/score del match)
    - `DoorbellEvent`: un evento (campanello premuto / persona rilevata) con 3 stati indipendenti: `processing_status`, `recognition_status`, `notification_status`

## 2. Fondamenta condivise

- **[config.py](vscode-webview://0npgoqo9ld7og79e7f1rt5g25cr3pcfvn8d4t15vsc9fmcr5oams/backend/app/config.py)**: solo costanti derivate da env (path base API, tolleranza face-match, storage root, timeout offline citofono, ecc.). Nessuna logica.
- **[deps.py](vscode-webview://0npgoqo9ld7og79e7f1rt5g25cr3pcfvn8d4t15vsc9fmcr5oams/backend/app/deps.py)**: dependency FastAPI riutilizzate ovunque: `get_db()` (yield di una sessione DB, sempre chiusa in `finally`), `get_or_404`, `flush_or_409`/`commit_or_409` (traducono `IntegrityError` in HTTP 409), `parse_iso_datetime`, `clean_optional_text`.

## 3. mqtt_client.py

Gestisce il ciclo di vita MQTT lato backend (non è un dominio con router proprio, main.py lo avvia/ferma su startup/shutdown). Si iscrive a 3 topic per citofono: `heartbeat`, `status`, `events` (pattern `eyedoor/intercom/{mqtt_username}/{channel}`). Aggiorna `HomeIntercomRuntimeStatus` nel DB (online/offline, ultimo IP, stato live-view...) e pubblica comandi verso i citofoni (`publish_command`). Se riceve messaggi da uno username sconosciuto, richiede ri-registrazione (`registration_required`).

## 4. schemas/ — cosa raggruppa

Modelli Pydantic richiesta/risposta, un file per dominio (`common`, `home`, `pairing`, `people`, `events`, `captures`, `gallery`). `schemas/__init__.py` fa un **re-export piatto**: qualunque router/service scrive `from schemas import X` senza sapere in quale sottomodulo `X` sia definito davvero. Regola di dipendenza: `captures.py`/`gallery.py` possono importare da `events.py`/`people.py`, mai il contrario.

## 5. services/ — la logica di business (il cuore)

|File|Cosa fa|
|---|---|
|`intercoms.py`|identità/pairing citofono, calcolo runtime status (online/offline da ultimo heartbeat), costruzione URL locali (IP vs hostname `.local`), dispatch comandi via MQTT|
|`images.py`|storage file su disco, **pipeline face recognition**: `face_recognition.face_locations` + `face_encodings` → confronto con embedding esistenti (`compare_faces`, tolleranza da config) → crea `DetectedPerson` nuovo o assegna a uno esistente|
|`gallery.py`|builder di gallery/dettaglio immagini + helper di disponibilità file (condivisi da `people.py` e `overlay.py`)|
|`people.py`|preview di una persona rilevata (foto "migliore"), lifecycle soft-delete con purge/preserve dei file su disco|
|`overlay.py`|rendering JPEG con overlay via OpenCV (box + etichette sulle facce), solo per debug/dashboard|

**Regola di dipendenza a senso unico**: `people.py` e `overlay.py` importano helper da `gallery.py` (mai il contrario) — evita di reintrodurre la duplicazione che lo split doveva risolvere.

## 6. routers/ — endpoint HTTP

|File|Dominio|Note|
|---|---|---|
|`home_owners.py`|CRUD proprietari||
|`pairing.py`|handshake citofono→hub prima del provisioning|stati: waiting → approved/rejected → consumed/expired|
|`intercoms.py`|provisioning, CRUD, runtime status/network, comandi (start/stop capture continua, capture-once)||
|`captures.py`|upload immagine + analisi candidato (usati dal citofono simulato)|espone alias `/prototype/...`|
|`local.py`|stesso flusso di `captures.py` ma sotto prefix `/local/v1`|pensato per la futura architettura "citofono → hub locale"|
|`images.py`|gallery: lista, dettaglio, thumbnail, file (+ overlay opzionale via query param)||
|`people.py`|lista persone rilevate, cambio etichetta/stato, immagine preferita, soft-delete||
|`events.py`|update ed elenco eventi doorbell||

`main.py` monta 2 router principali: `api_router` (prefix da `config.BACKEND_BASE_PATH`, es. `/api`) che include quasi tutti i domini, e `local_router` (prefix `/local/v1`) che include solo `local.py`.

## Esempio di flusso end-to-end (utile da spiegare all'esame)

Upload di una foto scattata dal citofono (`POST /api/prototype/intercoms/{id}/captures`):

1. **router** `captures.py` riceve `UploadFile` + form data → chiama `services/images.create_and_process_capture`
2. **service** `images.py`: crea righe `CapturedImage` + `DoorbellEvent` (status `PENDING`), salva il file normalizzato in JPEG + thumbnail su `STORAGE_ROOT/owners/<slug>/...`
3. Poi `process_image_server_side`: `face_recognition` rileva i volti, per ognuno calcola l'embedding a 128 dimensioni, lo confronta con gli embedding esistenti dello stesso `home_owner` (`find_best_person_match`, maggioranza di match sopra tolleranza) → se trova un match assegna alla `DetectedPerson` esistente, altrimenti ne crea una nuova (`NOT_IDENTIFIED`)
4. Aggiorna `processing_status`/`recognition_status` dell'evento, fa commit, torna uno `schemas.CaptureProcessingResult`
