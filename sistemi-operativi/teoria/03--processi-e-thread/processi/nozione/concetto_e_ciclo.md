---
title: Concetto e Ciclo
aliases:
  - Concetto e Ciclo
created: 2025-07-02
---
# Concetto e ciclo di vita del processo

>[!abstract]
>Questa sezione introduce il concetto di **processo** nei sistemi operativi, descrivendone la struttura fondamentale, l'evoluzione nel tempo attraverso il **ciclo di vita** e le **transizioni tra stati** principali.

---

## Che cos'è un processo?

>[!definition]
>Processo
>>Un **processo** è un'entità dinamica che rappresenta un programma in esecuzione. È distinto dal programma stesso, che è invece un'entità statica (insieme di istruzioni).  

Un'analogia utile è:
> *Il programma è lo spartito, il processo è la musica eseguita.*

---

### 🔁 Da programma a processo

- Un programma può essere eseguito da più processi (con input o contesti diversi).
- Ogni processo ha:
	- Una **code region** (sezione di testo)
	- Un **program counter**
	- Un **insieme di registri**
	- Una **data region**
	- Una **stack region**
	- Un insieme di **attributi di controllo** (PID, priorità, privilegi, limiti, ecc.)
	- **Risorse associate** (memoria, file aperti, dispositivi di I/O)

---

## 🧠 Immagine di un processo

La struttura di un processo include tutte le informazioni necessarie al suo stato e alla sua esecuzione.

>[!example]
>![immagine_processo_small](/sistemi-operativi/teoria/03--processi-e-thread/assets/immagine_processo_small.svg)

---

## 📈 Ciclo di vita di un processo

Un processo può trovarsi in uno dei seguenti stati fondamentali:

- `new`: appena creato
- `ready`: pronto per essere eseguito
- `running`: in esecuzione sulla CPU
- `waiting` (o `blocked`, `sleeping`): in attesa di un evento esterno
- `terminated`: ha concluso l’esecuzione

---

## 🔄 Transizioni tra stati

Le transizioni principali tra stati includono:

- `new → ready`: quando il processo viene caricato in memoria
- `ready → running`: assegnazione della CPU (detta *dispatch*)
- `running → waiting`: richiesta di I/O o evento esterno
- `waiting → ready`: completamento dell’evento atteso
- `running → ready`: *preemption* da parte del SO
- `running → terminated`: fine del programma o interruzione forzata

Il modulo del sistema operativo che gestisce l’assegnazione della CPU si chiama **dispatcher**.

>[!example]
>![transizione_tra_stati](/sistemi-operativi/teoria/03--processi-e-thread/assets/transizione_tra_stati.svg)

---

## 🧵 Note aggiuntive

- Le transizioni e gli stati possono variare tra diversi sistemi operativi.
- In UNIX, ad esempio, esistono stati più dettagliati (es. `preempted`, `zombie`, `swapped`, ecc.), trattati in un file a parte.

---

## 📚 Fonti

- Slide (Processi): _[Processi - hand03p.pdf](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand03p.pdf)_
- Autore: A. Formisano  
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025
