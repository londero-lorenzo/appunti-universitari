---
title: System Call
aliases:
  - System Call
created: 2025-06-30
---
# Le System Call

> [!abstract]
> Le system call costituiscono il meccanismo principale con cui i processi utente interagiscono con il sistema operativo.

---

## Cos'è una System Call

> [!definition]
> **System Call** 
>  
> Interfaccia tra i processi utente e il sistema operativo. Permette a un processo di richiedere servizi al kernel, come l'accesso a file o dispositivi.

- Possono essere invocate direttamente da linguaggi come C, C++, Assembly.
- Ogni system call è identificata da un numero che funge da indice in una tabella interna del kernel.
- L’interfaccia delle system call è solitamente gestita da una componente del compilatore chiamata _run-time support interface_[^1], che:
  - imposta i parametri,
  - invoca il kernel tramite trap/interruzione,
  - riceve lo status e i valori di ritorno.

---

## Esecuzione in Modalità Kernel

Le system call eseguono in **modalità kernel**, cioè con privilegi elevati.

Esempio di system call: `open()`


>![[struttura_sistemi_operativi_schema#^frame=lXraSiAzCMQ__mZlvVYKu|100%]]


---

## Passaggio dei Parametri

> [!question]
> Come vengono passati i parametri alle system call?

### Tre metodi principali:
1. **Registri**  
   Parametri caricati direttamente nei registri CPU.
2. **Blocco in memoria**  
   I parametri vengono messi in un blocco di memoria e si passa solo il puntatore.
3. **Stack**  
   Parametri e codice della system call sono "pushati" nello stack.

> [!example]
> Nell’uso di un blocco di memoria, l'indirizzo X contenente i parametri viene messo in un registro. Il kernel controlla che tale indirizzo sia valido (cioè nello spazio utente).

---

## Passaggio Parametri Tramite la Memoria

L'indirizzo dei parametri, che verranno utilizzati dalla system call, viene salvato in un registro,
quando viene invocata la chiamata di sistema il codice della system call controlla che l'indirizzo sia valido.

---

## Schema di Funzionamento (Stack)

1. Parametri e numero system call sullo **stack**
2. **Trap** → cambio modalità utente → modalità **kernel**
3. Viene attivato l’**handler**
4. Esecuzione della system call
5. Ritorno in modalità utente con status e risultati

---

## Tipi di System Call

| Categoria                    | Funzioni principali                                |
| ---------------------------- | -------------------------------------------------- |
| **Controllo dei processi**   | Creazione, terminazione, attesa, attributi, eventi |
| **Gestione file**            | Creazione, apertura, lettura/scrittura, attributi  |
| **Gestione dispositivi**     | Allocazione, rilascio, I/O, attributi, mount       |
| **Informazioni sul sistema** | Stato, data/ora, attributi HW/SW, utenti           |
| **Comunicazione**            | Connessioni, messaggi, memoria condivisa           |

---

## Programmi di Sistema

> [!definition]
> **Programmi di Sistema**
>   
> Software che fornisce un ambiente per sviluppare ed eseguire programmi utente. Fa spesso uso diretto delle system call.

Esempi:
- Gestione file: editor, comandi di manipolazione, browser di file system
- Stato del sistema: monitoraggio, log, configurazione
- Supporto linguaggi: compilatori, interpreti, linker, debugger
- Comunicazione: email, terminali remoti, browser, ecc.

---

## 📚 Fonti

- Contenuto: _Le System Call_
- Slide: [_Struttura dei Sistemi Operativi_](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand02.pdf)
- Autore: A. Formisano
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025


[^1]: Insieme di funzionalità fornite dal compilatore o dal linguaggio per supportare l'esecuzione dei programmi (es. gestione dello stack, delle chiamate di funzione, interfaccia alle system call).

