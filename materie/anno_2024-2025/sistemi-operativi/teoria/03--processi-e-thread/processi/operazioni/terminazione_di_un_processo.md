---
title: Terminazione di un Processo
aliases:
  - Terminazione di un Processo
created: 2025-08-19
---
>[!abstract]
>In questa sezione si introduce il concetto di terminazione di un processo e delle sue implicazioni a livello del sistema operativo.

---
# Terminazione di un Processo
Esistono due condizioni per cui un processo viene terminato:
## Terminazione in condizioni normali
In condizioni normali un processo termina eseguendo l'ultima istruzione del suo programma e richiedendo la sua terminazione tramite la [[sistemi-operativi/teoria/02--struttura-sistemi-operativi/system_call#Cos'è una System Call|system call]] `exit()` al sistema operativo.

In questo caso il sistema operativo:
- disalloca le risorse concesse al processo terminato
- **trasmette al processo padre eventuali informazioni/dati relativi alla terminazione del figlio**
## Terminazioni in condizioni anormali
Queste terminazioni avvengono per:
- **errori** o **violazioni** compiute dal processo
- richiesta di terminazione da parte di un altro processo
- in alcuni S.O. un processo viene terminato se il suo creatore termina

---

# Meccanismo di terminazione in Android
I S.O. di dispositivi mobili possono dover gestire scarsità di risorse, per questo motivo una soluzione consiste nel terminare uno o più processi, scegliendo quale processo partizionandoli in classi:

| Tipo di Processo               | Descrizione                                                                      |
| ------------------------------ | -------------------------------------------------------------------------------- |
| *processo **in primo piano** * | visibile sullo schermo, usato dall’utente                                        |
| *processo **visibile** *       | non visibile in primo piano ma funzionale a processi in primo piano              |
| *processo **di servizio** *    | che esegue in background funzionalità evidenti all’utente (es. streaming musica) |
| *processo **in background** *  | attività non visibile all’utente                                                 |
| *processo **vuoto** *          | non contiene componenti attive associate ad app                                  |

---

# Meccanismo di terminazione in UNIX
In **UNIX** è previsto che ogni processo abbia un padre, questo permette che **è sempre possibile trasmettere lo status di uscita di un processo che termina al processo padre.**
Quando il padre esegue la `wait()` riceve, tramite il S.O., il PID e l'exit status del processo terminato, _in questo modo ogni processo padre può venire a conoscenza di quale processo è terminato e quale è stato l'esito di terminazione_.

>[!danger]
>La completa disallocazione delle risorse di un processo terminato può avvenire **SOLO** se il padre esegue la `wait()`.
>Fino a quando ciò non accade il processo terminato resta in uno stato **<span style="color: red">zombie</span>**.
>>[!note]
>>Per permettere questo meccanismo, qualora il padre termini prima del figlio, quest’ultimo viene **adottato** dal processo `init`

---

## 📚 Fonti

- Slide (Processi): _[Processi - hand03p.pdf](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand03p.pdf)_
- Autore: A. Formisano  
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025