---
title: Code di Processi
aliases:
  - Code di Processi
created: 2025-08-18
---
# Code di Processi

>[!abstract]
>In questo capitolo vengono introdotti i concetti di *Code* e *Scheduling* per permettere ai processi che eseguono in competizione di utilizzare le risorse a loro necessarie.

---

>[!question] A cosa servono le code?
A garantire che ogni processo possa accedere alle risorse che gli servono.

>[!question] Quante code esistono?
>Tante quante le varie categorie di risorse disponibili

---
## Tipo di code

Esistono diverse code, associate a diverse risorse.

| Coda             | Descrizione                                                                                                |
| ---------------- | ---------------------------------------------------------------------------------------------------------- |
| **job queue**    | (coda dei processi) raccoglie tutti i (PCB dei) processi presenti nel sistema                              |
| **ready queue**  | (coda dei processi pronti) raccoglie tutti i (PCB dei) processi ready                                      |
| **device queue** | (coda del dispositivo) raccoglie tutti i (PCB dei) processi in attesa di un particolare dispositivo di I/O |

>[!example] Esempio di Code di Processi e Risorse
> <!-- TODO(sistemi-operativi):  aggiungere schema di esempio (slide 14) -->

>[!question] Quando un processo viene inserito in una coda?
>Quando si verifica un evento (richiesta), in questi casi si applica il *diagramma di accodamento*:
>![diagramma_di_accodamento|100%](/sistemi-operativi/teoria/03--processi-e-thread/assets/diagramma_di_accodamento.svg)

---

## Scheduler

>[!definition]
>Scheduler
>>Meccanismo decisionale per scegliere quale processo ha la priorità per accedere ad una determinata risorsa

### Due tipi di scheduler principali
I due principali scheduler sono:

| Scheduler                | Descrizione                                                                                                                                                                                                                                                           |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Long term scheduler**  | decide quali processi devono essere caricati in memoria centrale (_quindi inseriti nella `ready queue`_), questo influenza il **[[sistemi-operativi/teoria/01--introduzione/sistema_mono-multi_programmato#Sistema Multiprogrammato\|grado di multiprogrammazione]]** |
| **Short term scheduler** | scegliere a quale processo, tra quelli nella ready queue, assegnare la CPU                                                                                                                                                                                            |

#### Bonus
Spesso è possibile trovare un terzo scheduler, detto di medio termine

| Scheduler                 | Descrizione                                                                                                                                                       |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Medium term scheduler** | compie operazioni di spostamento dei processi dalla memoria principale a quella secondaria o viceversa, questo per modulare il carico a cui è soggetto il sistema |

Le operazioni di spostamento vengono chiamate `swap-out` e `swap-in`, usate di norma solo su processo **già parzialmente seguiti**.

<!-- TODO(sistemi-operativi): aggiungere schema swap in/out (slide 17) -->

Lo **swapping** viene attivato quando è necessario cambiare dinamicamente il grado di multiprogrammazione del sistema per migliorare l'utilizzo della CPU

Un processo swapped-out viene detto **swapped**, si possono avere processi:
 - `ready + swapped` -> "pronto per eseguire, ma attualmente su disco"
 -  `waiting + swapped` -> "in attesa di un evento, ma attualmente su disco"

---
## 📚 Fonti

- Slide (Processi): _[Processi - hand03p.pdf](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand03p.pdf)_
- Autore: A. Formisano  
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025