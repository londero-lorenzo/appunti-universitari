---
title: Sistema Mono-Multi Programmato
aliases:
  - Sistema Mono-Multi Programmato
tags: []
created: 2025-06-29
---
# Sistemi Mono/Multi-programmati

## Sistema Monoprogrammato

- In memoria risiedono solo il Sistema Operativo e **al più un applicativo**.
- Il sistema esegue **un solo lavoro (job) alla volta**.
- Nei sistemi *batch* il S.O. è rudimentale: si limita a **trasferire il controllo** da un job al successivo.

 >[!example]-
 >Schema struttura:
> 	![[sistemi-operativi/teoria/01--introduzione/introduzione_schema.md#^frame=vIAApZjm67VvFXv0uGVOt]]

---

## Sistema Multiprogrammato

- Più programmi possono risiedere contemporaneamente nella **memoria principale**.
- Il S.O. **seleziona** un programma e lo esegue fino a:
  - il termine dell’esecuzione,
  - o l’attesa di un evento esterno (es. I/O).
- In caso di attesa, il S.O. **passa all’esecuzione** di un altro programma in memoria.

>[!info]
>_Questa proprietà prende il nome di **multiprogrammazione**_

> [!example]-
>  Schema struttura:
> 	![[sistemi-operativi/teoria/01--introduzione/introduzione_schema.md#^frame=uSFmpqFl4wp4WvUHvhJ7w]]

---

## Time Sharing

- Tecnica della multiprogrammazione.
- Impiega **cambi di contesto (context switch)** a intervalli regolari, decisi dal S.O.
- Ogni utente ha l’impressione di avere **una CPU dedicata**.
- Introduce un’interazione più diretta tra utente e sistema.
- Concetti fondamentali introdotti:
  - **Processo**
  - **CPU Scheduling**

---

## Esecuzione Sequenziale vs Time Sharing

> 💡 Esempio con tre job `P1`, `P2`, `P3` che alternano fasi CPU e I/O:
- Nell'esecuzione sequenziale, i tempi morti per I/O restano inutilizzati.
- Con il *time sharing*, questi tempi vengono sfruttati per altri processi → **maggiore efficienza globale**.

> [!todo]
> Aggiungere un diagramma Excalidraw o un'immagine esplicativa

---

## Nozione di Processo

> [!info]
> Semplice:
> >Un **processo** è un programma **caricato in memoria** e **pronto per l’esecuzione**.
> 
> 
> Completa:
> >Un processo è un'**attività unitaria di elaborazione**, caratterizzata da un singolo **flusso sequenziale di esecuzione**, uno **stato corrente**, ed una collezione di **risorse** assegnate dal sistema

- Più processi possono coesistere in memoria centrale.
- Se la memoria non è sufficiente:
  - alcuni processi vengono tenuti in **memoria secondaria** (job pool).
- Il S.O. decide:
  1. quali processi caricare in memoria (**job scheduling**),
  2. quale processo eseguire (**CPU scheduling**),
  3. quando eseguire lo **[[#Tecniche a Supporto della Multiprogrammazione#Swapping|swap-out]]** (spostamento nella memoria secondaria).

---

## Definizioni Alternative di Processo

Un processo può essere definito come:

- un’istanza di un programma in esecuzione,
- un’attività assegnabile a un processore,
- una **unità di elaborazione sequenziale** dotata di:
  - stato corrente,
  - risorse allocate,
  - e un flusso esecutivo.

> ☝️ Attenzione alla terminologia:
> - *job*, *processo*, *task* possono essere usati in contesti diversi con sfumature differenti.

---

## Tecniche a Supporto della Multiprogrammazione

### Swapping
- Migrazione dei processi tra memoria principale e secondaria.
- Permette l’alternanza nell’uso della memoria disponibile.

### Memoria Virtuale
- Introduce uno **spazio di indirizzamento logico** indipendente dalla memoria fisica.
- Consente l’esecuzione di processi **non completamente caricati** in memoria.


---

## 📚 Fonti

- Contenuto: _Sistemi Mono/Multi-programmati_
- Slide: Introduzione ai Sistemi Operativi
- Slide: _[Introduzione Ai Sistemi Operativi](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand01.pdf)_
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025

