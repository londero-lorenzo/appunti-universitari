---
title: Modelli Fondamentali per l'IPC
aliases:
  - Modelli Fondamentali per l'IPC
created: 2025-08-19
---
# Modelli Fondamentali per l'IPC

>[!abstract]
>Questa sezione introduce i due principali modelli per l'Inter-Process Communication.

---
## Modelli Fondamentali
I modelli fondamentali per l’Inter-Process Communication (IPC) sono due:
1. **Shared memory** (memoria condivisa) 
2. **Message passing** (scambio di messaggi)

---
### Shared Memory
Questo modello prevede l'esistenza di un **ambiente globale** accessibile dai processi.  
Implica quindi la presenza di uno spazio di memoria indirizzabile da tutti i processi che cooperano.

#### Funzionamento
1. Il **blocco di memoria** viene concesso (solitamente) **dal S.O.** come risposta a una invocazione da parte di un processo (`shmget()` su System V, `shm_open()` su POSIX);
2. **Ogni processo** che vuole utilizzare tale blocco di memoria deve **annettere il blocco al proprio spazio di indirizzamento** (`shmat()` su Unix System V);
3. Il **S.O. delega** ai processi **l'uso e la gestione** della memoria condivisa.

>[!warning]
>Il S.O. non fornisce automaticamente meccanismi di sincronizzazione: i processi devono coordinarsi autonomamente (es. semafori, mutex) per evitare condizioni di race.

---
### Message Passing
Questo modello si basa sull’invio e la ricezione di messaggi.  

Prevede l'esistenza di:
- un **canale di comunicazione**;
- due operazioni base:
  - `send`: usata dal mittente per inviare un messaggio sul canale;
  - `receive`: usata per prelevare/ricevere un messaggio dal canale.

Sorgono alcune domande fondamentali sulle caratteristiche di questo modello:

>[!question] Lo stesso canale può essere utilizzato da più di due processi?
  
>[!question] Tra due processi ci può essere più di un canale?  

>[!question] Il canale è monodirezionale o bidirezionale?  

>[!question] Come vengono gestiti i messaggi?

>[!note]
>Non esiste una risposta univoca: sistemi diversi realizzano le primitive `send` e `receive` in modi differenti, a seconda delle scelte progettuali.

Per approfondire:  
- [Caratteristiche della Comunicazione](./caratteristiche_della_comunicazione.md)

---
#### Esempio di comunicazione: `unnamed pipe` di UNIX

UNIX (standard System V) offre una forma elementare di comunicazione tramite la system call:  
`int pipe(int pipefd[2])`

La system call definisce:
- un **canale monodirezionale**: una *unnamed pipe*
  - utilizzabile tra più processi (con limiti di visibilità dovuti all'anonimità);  
  - tipicamente tra due processi: un produttore e un consumatore;  
  - limiti imposti dal S.O. riguardano:
    - massimo numero di pipe creabili (per processo e per sistema);  
    - dimensione massima del buffer associato alla pipe.  
- due **descrittori**:
  - `pipefd[0]` → per leggere;
  - `pipefd[1]` → per scrivere.
- due **primitive**:
  - `write()` → per inviare;
  - `read()` → per ricevere.
- **Tipologia di messaggi**: sequenze di byte (stream di dati, non record strutturati).


---

#### Comunicazioni nei Sistemi Client-Server

Oltre alle `pipe`, esistono altre tipologie di canali usati soprattutto in architetture client-server:

| Tipologia                  | Descrizione                                                                 |
| -------------------------- | --------------------------------------------------------------------------- |
| **Socket**                 | Due socket costituiscono un canale di comunicazione bidirezionale tra processi. |
| **Remote Procedure Call**  | Invocazione di una procedura eseguita da un processo remoto, con il sistema che nasconde i dettagli di comunicazione. |

---

##### Socket
In UNIX (system call `socket()`) due socket formano un canale di comunicazione bidirezionale.  

Possono essere:
- **Unix-socket**: tra processi sullo stesso sistema operativo, tramite il file system;
- **Internet-socket**: tra processi su nodi diversi in rete, identificati da *IP + porta*.  

In genere si adotta uno schema client-server:
- il server crea e mette in ascolto la socket;
- il client crea una socket e si connette alla controparte.

---

##### Remote Procedure Call (RPC)
L’RPC permette a un processo di invocare una procedura come se fosse locale, anche se l’esecuzione avviene su un sistema remoto.  

Funzionamento tipico:
1. Il processo client invoca la procedura → la chiamata è intercettata dal sistema RPC;
2. La richiesta (con eventuali parametri) è inviata al server remoto tramite una porta dedicata;
3. Il server inoltra la richiesta all’esecutore locale e raccoglie il risultato;
4. Il risultato è inviato al client, che lo riceve come se fosse il valore di ritorno di una funzione locale.

>[!note]
>L’RPC maschera i dettagli di comunicazione, fornendo al programmatore un’interfaccia simile a quella delle procedure locali.  
>Non sempre è limitata al modello client-server: ad esempio, in Android può avvenire anche tra processi peer.


---

## 📚 Fonti

- Slide (Processi): _[Processi - hand03p.pdf](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand03p.pdf)_
- Autore: A. Formisano  
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025