---
title: "Frontend"
aliases: ["Frontend"]
tags: [università, "materie", "anno-2025-2026", "internet-of-things", "progetto", "esposizione-esame", "frontend"]
created: 2026-07-23
---
## Bootstrap e routing

- **[main.tsx](vscode-webview://0npgoqo9ld7og79e7f1rt5g25cr3pcfvn8d4t15vsc9fmcr5oams/frontend/app/src/main.tsx)**: entrypoint Vite. Monta `<App/>` dentro `BrowserRouter` + `AuthProvider`.
- **[App.tsx](vscode-webview://0npgoqo9ld7og79e7f1rt5g25cr3pcfvn8d4t15vsc9fmcr5oams/frontend/app/src/App.tsx)**: unica tabella di routing dell'app (`react-router-dom`). Tutte le pagine tranne `/login` sono avvolte in `<ProtectedRoute>` (guardia auth) e in `<AppShell>` (layout con sidebar). Rotta dinamica `/intercoms/:intercomId/live` per la live view.

## `api/` — comunicazione col backend

|File|Ruolo|
|---|---|
|`config.ts`|Calcola `API_BASE_URL`: in dev (porta Vite 5173) punta a `http://<host>:8000/api`; in produzione usa `same-origin/api`. Espone anche `resolveApiAssetUrl()` per trasformare i path relativi restituiti dal backend (es. `thumbnail_url`) in URL assoluti|
|`http.ts`|Wrapper unico su `fetch` (`apiRequest<T>`): costruisce l'URL con query string, imposta header JSON (tranne per `FormData`), traduce risposte non-2xx in `ApiError` con il campo `detail` del backend|
|`eyedoor.ts`|**Tutte** le funzioni tipizzate che chiamano gli endpoint del backend (home-owners, home-intercoms, pairing, captured-images, detected-people, doorbell-events) — è l'unico punto che conosce i path REST del backend|

## `auth/` — sessione "prototype"

- **AuthContext.tsx**: non c'è JWT/password reale (coerente con `CLAUDE.md` §1: prototipo senza auth forte). Il "login" è solo: chiama `listHomeOwners()`, cerca l'email in memoria, e se combacia salva l'oggetto `HomeOwner` in `localStorage`. Nessuna verifica password lato backend.
- **ProtectedRoute.tsx**: guardia di routing, redirige a `/login` se `!isAuthenticated`.

## `layout/AppShell.tsx`

Sidebar di navigazione (Dashboard, Citofoni, Galleria, Persone, Eventi) + area contenuto (`<Outlet/>`). Legge `owner`/`logout` da `AuthContext`.

## `components/` — presentazionali puri

`EmptyState`, `ErrorBanner`, `Loader`, `StatusBadge` (mappa enum backend → etichette italiane, es. `matched` → "Riconosciuto"). Nessuna logica di rete.

## `types.ts` e `utils/format.ts`

`types.ts` rispecchia **1:1** gli schemi Pydantic del backend (`HomeIntercom`, `DetectedPerson`, `CapturedImageGalleryItem`, `LiveViewMetadata`...) — utile da mostrare a esame come "contratto condiviso" tra i due stack. `format.ts` sono helper di formattazione data/durata/nome persona.

## `pages/` — una pagina per dominio

|Pagina|Cosa fa|
|---|---|
|`LoginPage`|Form login/registrazione owner demo|
|`DashboardPage`|Aggrega health check + intercoms + people + gallery + eventi in parallelo (`Promise.all`)|
|`IntercomsPage`|Approvazione/rifiuto pairing, CRUD citofono, comandi (start/stop capture continua, scatto singolo), link a live view|
|`IntercomLivePage`|**La pagina più particolare** — vedi sotto|
|`GalleryPage`|Galleria capture con filtri, dettaglio con overlay volti|
|`PeoplePage`|Gestione persone rilevate: etichetta, immagine preferita, soft-delete/delete definitivo|
|`EventsPage`|Tabella eventi doorbell|
## Panoramica: tre canali, due protocolli

```
┌───────────┐   HTTP REST (sempre)    ┌──────────┐   HTTP + MQTT   ┌──────────────────┐
│ Frontend  │ ──────────────────────▶ │ Backend  │ ──────────────▶ │ fake-intercom     │
│ (React)   │ ◀────────────────────── │ (FastAPI)│ ◀────────────── │ (client Python)   │
└───────────┘                         └──────────┘                 └──────────────────┘
      │                                                                     ▲
      └─────────────────── HTTP diretto, SOLO live view ───────────────────┘
                        (bypassa il backend, stessa LAN)
```

Il frontend **non parla mai MQTT** e **non parla mai direttamente col citofono per dati persistenti** — solo per il video grezzo. Vediamo i due canali che riguardano il frontend.

## Canale 1 — Frontend ↔ Backend (HTTP REST, il canale principale)

Tutto passa da qui tranne il flusso video: login/owner, CRUD citofoni, pairing, galleria, persone rilevate, eventi, e anche i **comandi** verso il citofono (avvia/ferma monitoraggio, scatto singolo).

**Come è implementato**:

- `api/config.ts` calcola `API_BASE_URL` (in dev: `http://<host>:8000/api`, in prod: same-origin `/api`)
- `api/http.ts` è l'unico wrapper `fetch` usato da tutta l'app: aggiunge header JSON, traduce errori HTTP in `ApiError`
- `api/eyedoor.ts` contiene una funzione per ogni endpoint (`listHomeIntercoms`, `startIntercomContinuousCapture`, `listCapturedImages`, ecc.), che rispecchia 1:1 i router del backend

**Cosa succede quando il frontend "invia un comando" al citofono** (es. bottone "Avvia monitoraggio" in `IntercomsPage`):

```
Frontend                    Backend                              Citofono (MQTT)
   │  POST /prototype/home-intercoms/{id}/commands/            │
   │      start-continuous-capture ──────────────▶             │
   │                              services/intercoms.py:       │
   │                              dispatch_intercom_command()  │
   │                              verifica che sia online,      │
   │                              pubblica su topic MQTT       │
   │                              "commands" ───────────────────────────▶ mqtt_control_client.py
   │  ◀────────── 200 OK (comando accodato) ─────                        riceve, esegue
```

Il frontend **non aspetta** che il citofono esegua realmente il comando: riceve solo conferma che è stato pubblicato su MQTT, poi ripolla lo stato (`getHomeIntercomRuntimeStatus`) dopo ~1.2s per vedere l'effetto (`IntercomsPage.tsx` / `IntercomLivePage.tsx`, funzione `sendCommand`).

**Polling, non push**: non c'è WebSocket né SSE da nessuna parte. Il frontend rilegge lo stato a intervalli fissi:

- `IntercomsPage`: stato runtime di tutti i citofoni ogni 3.5s
- `IntercomLivePage`: stato runtime ogni 3s + metadata live view ogni 0.7s (solo quando il monitoraggio è attivo)

## Canale 2 — Frontend ↔ Client (fake-intercom), diretto e solo per il video

Questo è il caso speciale, in `IntercomLivePage.tsx`. Il frontend **non riceve mai il video passando dal backend**: apre una connessione HTTP diretta verso il piccolo server FastAPI che il citofono espone in LAN (`device_api.py`, porta 8090 di default).

Perché diretto? Perché il backend fa già da intermediario per tutto il resto, ma il video (MJPEG multipart) è pesante e continuo: instradarlo attraverso il backend sarebbe uno spreco di banda/CPU inutile per un prototipo che gira sulla stessa rete locale.

**Come il frontend trova l'indirizzo del citofono** (non lo conosce a priori):

1. Il citofono pubblica via MQTT (topic `status`) i propri fatti di rete grezzi: hostname `.local`, IP, porta, path (`build_runtime_status_payload` in `main.py` del client)
2. Il **backend** li riceve (`mqtt_client.py`) e li salva in `HomeIntercomRuntimeStatus`; quando il frontend chiama `GET /prototype/home-intercoms/{id}/runtime-status`, il backend calcola un URL "candidato" preferendo IP diretti all'hostname `.local` (spesso non risolvibile) — vedi `services/intercoms.choose_effective_local_host`
3. Il frontend **ricalcola di nuovo** localmente l'host effettivo (`IntercomLivePage.tsx`, funzione `buildDeviceUrl`), con la stessa logica di preferenza, usando i campi grezzi (`manual_ip`, `last_reported_ip`, `effective_host`...) restituiti dal backend

**Cosa scarica poi direttamente dal citofono** (nessun passaggio dal backend):

|Richiesta|Endpoint sul citofono|Contenuto|
|---|---|---|
|`<img src=...>`|`GET /device/v1/live/stream`|MJPEG multipart continuo (il video grezzo)|
|polling ogni 700ms|`GET /device/v1/live/metadata`|bounding box volti + ultimo feedback di riconoscimento ricevuto dal backend|

Il frontend disegna poi da solo, su un `<canvas>` sovrapposto all'`<img>`, i riquadri e le etichette persona leggendo quella metadata (`drawOverlay`) — è un overlay **lato client**, diverso da quello che il backend genera lato server con OpenCV per le immagini statiche della galleria (`?overlay=true`).

## Riepilogo per l'esame

||Protocollo|Passa dal backend?|Push o poll?|
|---|---|---|---|
|Frontend → dati/comandi|HTTP REST|Sì, sempre|Poll (nessun WebSocket)|
|Frontend → video live|HTTP (MJPEG + JSON)|**No, diretto al citofono in LAN**|Poll/stream continuo|
|Backend ↔ citofono (stato/eventi)|MQTT|—|Pub/sub|
|Backend ↔ citofono (immagini)|HTTP|—|Request/response|

L'unica cosa davvero "anomala" da sottolineare a esame è proprio il punto 2: il frontend bypassa il backend per il video, ma dipende comunque dal backend per _sapere dove_ trovare il citofono, perché è il backend che aggrega e calcola l'host effettivo a partire ai dati ricevuti via MQTT