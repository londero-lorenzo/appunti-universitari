---
title: Creazione di un Processo
aliases:
  - Creazione di un Processo
created: 2025-08-18
---
>[!abstract]
>Questa sezione introduce l'operazione di creazione di un processo e la sua implicazione a livello di sistema operativo.

---

# Creazione di un Processo

Ogni processo può creare altri processi invocando una specifica [[sistemi-operativi/teoria/02--struttura-sistemi-operativi/system_call|System Call]] (`fork()` in UNIX).
Il processo creatore è detto *padre*, quello creato è detto *figlio*.

>[!question] Cosa succede quando un processo padre crea un processo figlio?
>- il processo figlio avrà un nuovo PID e [[sistemi-operativi/teoria/03--processi-e-thread/processi/nozione/pcb_e_context_switch#Process Control Block (PCB)|PCB]]
>- il [[sistemi-operativi/teoria/03--processi-e-thread/processi/nozione/pcb_e_context_switch#Process Control Block (PCB)|PCB]] del padre conterrà informazioni per identificare i suoi figlio (*e viceversa*)

>[!note]
>Vengono così create gerarchie di processi, tutti i processi **discendono dal processo `init` (PID = 1)**

Sorgono ulteriori domande su cosa accade quando un processo ne genera un altro, non esiste una risposta in quanto l'implementazione è a discrezione del programmatore.

>[!question] Come procedono i due processi?
>- padre e figlio continuano ad eseguire in modo concorrente?
>- padre attende la terminazione del figlio?

>[!question] Che codice esegue il figlio?
>- il processo figlio è un duplicato quasi identico al padre?
>- il processo figlio carica ed esegue un codice diverso da quello del padre?

>[!question] Quali risorse vengono condivise tra i due processi?
>- il processo figlio condivide tutte (o parte) delle risorse del padre?
>- nessuna risorsa viene condivisa (il figlio dovrà acquisire le risorse che necessita)

---

### Schema comune tipico di UNIX

In un sistema UNIX il processo figlio sarà una **copia identica del padre**, con le **stesse risorse assegnate**, erediterà l'[[sistemi-operativi/teoria/03--processi-e-thread/processi/nozione/pcb_e_context_switch#^cf70d8|execution context]] del padre con l'unica differenza del [[sistemi-operativi/teoria/03--processi-e-thread/processi/nozione/pcb_e_context_switch#^effbe9|PID]]

>[!example] Esempio dello schema
>![schema_comune_di_creazione_unix|100%](/sistemi-operativi/teoria/03--processi-e-thread/assets/schema_comune_di_creazione_unix.svg)

---

## 📚 Fonti

- Slide (Processi): _[Processi - hand03p.pdf](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand03p.pdf)_
- Autore: A. Formisano  
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025