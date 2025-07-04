---
title: Principi di Funzionamento di Un Sistema Operativo
aliases:
  - Principi di Funzionamento di Un Sistema Operativo
tags: []
created: 2025-06-29
---
# Principi di Funzionamento di un Sistema Operativo

## Modalità di Funzionamento

>[!danger]
>_In presenza di più processi che **condividono risorse** è necessario garantire che ogni processo non danneggi gli altri._

Per evitare che un processo danneggi gli altri, i moderni S.O. operano in almeno due **modalità**:

- **Modalità utente**: modalità standard in cui opera un processo applicativo.
- **Modalità kernel**: modalità privilegiata che consente l’accesso diretto alle risorse.


La CPU dispone di almeno un **bit di modalità** per distinguere fra queste due situazioni. Solo in modalità kernel è possibile eseguire **istruzioni privilegiate**, come:

- la gestione delle interruzioni,
- la manipolazione delle risorse,
- il passaggio da una modalità all’altra.

---

## System Call

>[!question]
>**Se la gestione delle risorse avviene tramite istruzioni privilegiate, come fa un processo utente, che normalmente esegue in modalità utente, a ottenere risorse?**

Il meccanismo utilizzato è quello delle **system call**:

- Un processo esegue una system call per richiedere un servizio al S.O.
- Questo genera una **trap** (interruzione software).
- Il controllo passa a una **routine interna al S.O.**, in modalità kernel.
- Il servizio viene eseguito, poi il controllo torna al processo utente.

>[!example]+
>Possiamo visualizzare una situazione tipica come segue:
>![[introduzione.excalidraw#^frame=xgIFca_7YQN-dSj_bNy4V|100%]]

---

## Tipologie di Funzionalità del S.O.

### Gestione dei Processi

Il S.O. gestisce:

- la **creazione** e **cancellazione** dei processi,
- la **sospensione** e il **ripristino**,
- la **comunicazione** e **sincronizzazione** tra processi,
- la **gestione degli stalli** (deadlock).

---

### Gestione della Memoria Centrale

Il S.O. gestisce:

- il **monitoraggio** delle porzioni di memoria in uso,
- la **decisione** su quali processi e dati caricare/spostare,
- l’**assegnazione e revoca** dinamica della memoria.

---

### Gestione della Memoria di Massa e dei File

- I file (unità logiche) sono organizzati in **file system**.
- Il S.O. gestisce:
  - creazione, accesso e cancellazione di file e directory,
  - associazione dei file ai dispositivi fisici,
  - strategie di **affidabilità** (backup, copie, ...).

Per la memoria secondaria:

- **gestione dello spazio libero**,
- **allocazione dello spazio**,
- **scheduling del disco**.

Per la memoria terziaria (nastri, supporti ottici):

- gestione specifica dei dispositivi.

---

### Gestione dell’Input/Output

Il S.O. deve fornire funzionalità per la gestione **I/O**:

- **buffering**: aree di memoria per scambiare dati,
- **caching**: spostamento di dati in memorie più veloci,
- **spooling**: gestione asincrona dei dispositivi I/O.

Il S.O. uniforma l’accesso ai dispositivi tramite **device driver**.

---

### Protezione e Sicurezza

>[!definition]
>**Protezione**
>
>Controllo dell’**accesso alle risorse** da parte di utenti e processi.



>[!definition]
>**Sicurezza**
>
>Difesa da **attacchi interni o esterni**
>(denial of service, virus, furto d’identità, ecc.)


> Il S.O. distingue gli utenti tramite **user ID** e **group ID**.

#### Proprietà da garantire:

- **Disponibilità**: il sistema deve essere sempre operativo.
- **Privatezza**: accessi solo ai dati autorizzati.
- **Integrità**: i dati non devono subire modifiche non autorizzate.
- **Autenticazione**: verificare l’identità dell’utente.

---

## 📚 Fonti

- Contenuto: _Organizzazione di un Sistema di Calcolo_: _Gestione delle Interruzioni_ e _La Memoria_
- Slide: _[Introduzione Ai Sistemi Operativi](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand01.pdf)_
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025