---
title: PCB e Context Switch
aliases:
  - PCB e Context Switch
created: 2025-07-02
---
# Process Control Block e Context Switch

>[!abstract]
>Questa sezione approfondisce la rappresentazione interna di un processo tramite il **Process Control Block (PCB)** e il ruolo critico che questo assume durante un **context switch**. Viene inoltre presentata la struttura della process table e l'organizzazione della memoria nei contesti user e kernel mode.

---

## Process Control Block (PCB)

>[!definition]
>Process Control Block
>>Il **PCB** è una struttura dati mantenuta dal sistema operativo che contiene tutte le informazioni necessarie per la gestione e il controllo di un processo.



### Contenuti tipici del PCB:

- **Identificatore del processo** (PID)
	 ^effbe9
- **Stato del processo** (es. ready, running, waiting…)
    
- **Program counter** (istruzione successiva da eseguire)
    
- **Registri della CPU** salvati
    
- **Informazioni di scheduling** (priorità, stato, tempo di CPU utilizzato…)
    
- **Informazioni sulla memoria** (es. tabelle di paging)
    
- **Stato delle risorse di I/O** (file aperti, dispositivi)


>[!note]
> Il PCB definisce il **contesto di esecuzione** del processo.
>Tutti i PCB sono raccolti all’interno della **process table**.

^cf70d8

---

## Process Table

>[!definition]
>Process Table
>>Struttura mantenuta dal sistema operativo (globale o per utente) che consente di tenere traccia dell'intero insieme di processi attivi nel sistema.

>[!example]
>![process_table](/sistemi-operativi/teoria/03--processi-e-thread/assets/process_table.svg)

---

## Immagine di un processo: user e kernel mode

Un processo viene rappresentato in memoria con varie **sezioni distinte**. In questo esempio è riportata la raffigurazione di un immagine di un processo per un sistema che abbia una duplice modalità di funzionamento: 


<table>
  <thead>
    <tr>
      <th>Sezione</th>
      <th>Descrizione</th>
      <th>Immagine</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="color: #a5d8ff; font-size: 1.1em"><i>Process Identification</i></td>
      <td>Contiene informazioni come PID, UID, e riferimenti al processo padre.</td>
      <td rowspan="7">
      <img src="/sistemi-operativi/teoria/03--processi-e-thread/assets/immagine_processo.svg" alt= "immagine di un processo">
      </td>
    </tr>
    <tr>
      <td style="color: #a5d8ff; font-size: 1.1em"><i>Processor State Information</i></td>
      <td>Stato dei registri, PC, PSW e altri dati legati al contesto di esecuzione.</td>
    </tr>
    <tr>
      <td style="color: #a5d8ff; font-size: 1.1em"><i>Process Control Information</i></td>
      <td>Include priorità, stato, limiti di esecuzione, e informazioni sullo scheduling.</td>
    </tr>
    <tr>
      <td style="color: #ffec99; font-size: 1.1em"><i>User Stack</i></td>
      <td>Stack usato dal processo per memorizzare chiamate di funzione e variabili locali.</td>
    </tr>
    <tr>
      <td style="color: #ffec99; font-size: 1.1em"><i>Private User Address Space</i></td>
      <td>Contiene codice e dati del programma, separati da altri processi.</td>
    </tr>
    <tr>
      <td style="color: #ffc9c9; font-size: 1.1em"><i>Kernel Stack</i></td>
      <td>Stack utilizzato quando il processo entra in modalità kernel (es. system call).</td>
    </tr>
    <tr>
     <td style="color: #96f2d7; font-size: 1.1em"><i>Shared Address Space</i></td>
      <td>Spazio opzionale condiviso con altri processi, utile per IPC.</td>
    </tr>
  </tbody>
</table>

---

## Context Switch

>[!definition]
>Context switch
>>Il context switch è il meccanismo che consente a un sistema operativo di gestire **più processi concorrenti**[^concorrenti], garantendo l'**isolamento** e la **continuità** di esecuzione per ciascuno.

[^concorrenti]: Due processi sono concorrenti quando sono **attivi nello stesso intervallo di tempo**, e le loro esecuzioni **possono interferire** a causa della condivisione di risorse o sincronizzazione. Questo non implica necessariamente esecuzione simultanea (che richiederebbe un sistema multiprocessore), ma può anche verificarsi tramite **interleaving** [^interleaving] su una singola CPU.

[^interleaving]: Tecnica utilizzata su sistemi a processore singolo, che consiste nel passare rapidamente da un processo all'altro, creando l'illusione di un parallelismo. 

>[!question]+ Quando si verifica un context switch?
>Un **context switch** si verifica quando la CPU passa dall’esecuzione di un processo all’esecuzione di un altro. È una delle operazioni più frequenti e delicate in un sistema operativo multitasking.

Durante un context switch:

1. Viene **salvato** il contesto del processo corrente (PCB)
    
2. Viene **ripristinato** il contesto del nuovo processo da eseguire
    
3. Viene aggiornato lo stato dei processi coinvolti


💡 Questo meccanismo è alla base del **time-sharing** nei sistemi multitasking.

<!-- TODO(sistemi-operativi): Creare esempio grafico per PCB e Context Switch -->

---

## 📚 Fonti

- Slide (Processi): _[Processi - hand03p.pdf](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand03p.pdf)_
    
- Autore: A. Formisano
    
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025