---
title: Caratteristiche della Comunicazione
aliases:
  - Caratteristiche della Comunicazione
created: 2025-08-19
---
# Caratteristiche della Comunicazione

>[!abstract]
>In questa sezione verranno descritte le varie caratteristiche della comunicazione tramite scambio di messaggi tra processi.

---

## Tre aspetti principali
Gli aspetti principali di una comunicazione per *message passing* sono:

| Aspetto                         | Descrizione                                                                                                    |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| <span style="color:orange">Naming</span> | La comunicazione può essere **<span style="color:cyan">diretta</span>** o **<span style="color:cyan">indiretta</span>** |
| <span style="color:orange">Sincronizzazione</span> | La comunicazione può usare operazioni **<span style="color:cyan">sincrone</span>** o **<span style="color:cyan">asincrone</span>** |
| <span style="color:orange">Buffering</span> | Tipologia di buffer di messaggi; gestione automatica (dal S.O.) o esplicita (da parte dei processi) |

---

### Comunicazione diretta

Si nomina esplicitamente il processo con cui si vuole scambiare il messaggio:
- `send(P, messaggio)` = spedisco il `messaggio` al processo `P`
- `receive(R, messaggio)` = ricevo il `messaggio` dal processo `R`

>[!note]
>Schema **simmetrico**:
> - tra ogni coppia di processi si stabilisce un solo canale
> - ogni canale è associato a esattamente due processi

---

### Comunicazione indiretta

Si utilizzano le <span style="color:indianred">mailbox</span>: ogni messaggio è inviato a una mailbox univocamente identificata:
- `send(Box, msg)` = spedisco il `msg` alla mailbox `Box`
- `receive(Box, msg)` = ricevo il `msg` dalla mailbox `Box`

>[!note]
>Schema **indiretto**:
> - due processi comunicano condividendo la stessa mailbox
> - più canali possono essere usati dagli stessi due processi 
> - ogni canale può essere usato da più di due processi

>[!warning]
>Se una mailbox è usata da più di due processi, sono necessarie politiche di gestione. Ad esempio:
> - Come determinare il destinatario se vi sono più `receive`?  
> - Chi “possiede” la mailbox: il S.O. o un processo?

---

### Primitive sincrone o asincrone

Sia `send` che `receive` possono essere <span style="color:cyan">sincrone</span> (bloccanti) o <span style="color:cyan">asincrone</span> (non bloccanti).  

| Primitiva    | Tipo         | Descrizione                                                                                                   |
| ------------ | ------------ | ------------------------------------------------------------------------------------------------------------- |
| *Invio*      | **Sincrono** | Il <span style="color:orange">processo che spedisce si blocca</span> in attesa che il messaggio sia ricevuto (dal destinatario o dalla mailbox) |
| *Invio*      | **Asincrono** | Il <span style="color:orange">processo che spedisce non attende la ricezione</span>                           |
| *Ricezione*  | **Sincrono** | Il <span style="color:orange">processo che riceve si blocca</span> in attesa che vi sia un messaggio disponibile |
| *Ricezione*  | **Asincrono** | Il <span style="color:orange">processo che riceve non si blocca</span>: o ottiene il messaggio o una notifica di assenza |

---

### Tipologie di code di messaggi

I messaggi spediti vengono “accodati” in attesa della loro ricezione.  
Le code sono temporanee, solitamente gestite dal S.O., e la loro capacità dipende dal modo in cui sono realizzate:

| Capacità                                                     | Descrizione                                                                                   |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| <span style="color:indianred; font-weight:bold">Nulla</span> | Non ci possono essere messaggi in attesa → la `send` deve essere bloccante (**no buffering**) |
| <span style="color:orange; font-weight:bold">Limitata</span> | Esiste un numero massimo di messaggi in coda → la `send` è bloccante solo se la coda è piena  |
| <span style="color:lime; font-weight:bold">Illimitata</span> | La `send` può essere sempre non bloccante                                                     |

---

## 📚 Fonti

- Slide (Processi): _[Processi - hand03p.pdf](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand03p.pdf)_
- Autore: A. Formisano  
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025
