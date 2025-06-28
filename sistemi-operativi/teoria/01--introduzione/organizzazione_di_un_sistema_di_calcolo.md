---
title: Organizzazione di Un Sistema di Calcolo
aliases:
  - Organizzazione di Un Sistema di Calcolo
tags:
  - 01--introduzione
created: 2025-06-28
---
# Organizzazione di un Sistema di Calcolo

> ⚠️ Questa sezione introduce concetti che verranno trattati in modo più approfondito nei capitoli successivi.  
> Per chiarezza, abbiamo deciso di raccogliere qui tutti i contenuti in **un singolo file**, suddiviso per sezioni.

---

## Architettura generale

In uno schema semplificato, un sistema di calcolo è composto da:

- **CPU (o CPU multiple)**
- **Controller dei dispositivi (device controller)**
- **Bus di sistema**, condiviso da CPU e controller per accedere alla memoria
- **Memoria principale (RAM)** e memoria secondaria

Sia la CPU che i controller possono accedere alla memoria tramite il bus e operano **concorrentemente**.

---

## Interruzioni

### Funzionamento generale dei dispositivi di I/O

- Ogni dispositivo è controllato da un **controller** con un proprio **buffer locale**.
- La **CPU legge o scrive** nel buffer del controller.
- Il controller **scrive o legge** sul dispositivo vero e proprio.
- La sincronizzazione tra CPU e controller avviene tramite **interruzioni**.

### Gestione delle interruzioni

1. Il controller invia un **segnale di interruzione** alla CPU.
2. La CPU intercetta il segnale e **identifica il tipo di interruzione**.
3. Viene invocata una **procedura di servizio** appropriata.
4. La CPU salva il proprio stato, esegue la gestione e **ripristina lo stato** al termine.
5. Spesso si utilizza una struttura chiamata **vettore delle interruzioni**.

---

## Memoria

### Tipologie

- **Memoria principale (RAM)**:
  - Accessibile direttamente dalla CPU
  - Volatile (perde dati allo spegnimento)
- **Memoria secondaria**:
  - Persistente (dischi, SSD, chiavette USB, ecc.)
  - Usata per archiviare dati a lungo termine
  - Interfacciata tramite un **controller** specifico

### Gerarchia di memoria

Concetto chiave: diverse tipologie di memoria organizzate per **velocità e costo**.  
Dalla più veloce e costosa (registri CPU) alla più lenta ed economica (dischi, SSD).

### DMA – Accesso Diretto alla Memoria

Il **DMA (Direct Memory Access)** è una tecnica per migliorare le prestazioni di I/O:

- La CPU **inizia l’operazione**, poi delega tutto al controller.
- Il controller **trasferisce i dati** tra il suo buffer e la memoria principale.
- Alla fine, segnala il completamento alla CPU.
- Vantaggio: la CPU può continuare ad eseguire istruzioni **in parallelo** al trasferimento.

---

## ## Fonti

- Contenuto: _Organizzazione di un Sistema di Calcolo_: _Gestione delle Interruzioni_ e _La Memoria_
- Slide: _[Introduzione Ai Sistemi Operativi](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand01.pdf)_
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025
