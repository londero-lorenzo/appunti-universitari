---
title: "Capitolo 5"
aliases: ["Capitolo 5"]
tags: [università, "materie", "anno-2025-2026", "reti-di-calcolatori", "capitolo-5"]
created: 2026-04-26
---
# Protocolli end-to-end

## Limitazioni dei protocolli di rete

- protocoli di rete implementano un servizio **host-to-host, best-effort**
- limitazioni tipiche della rete su cui opera il protocollo di trasporto
	- eliminazione messaggi
	- modificare l'ordine dei messaggi
	- consegnare copie di uno stesso messaggio
	- imporre un limite finito alla dimensione dei messaggi
	- consegnare i messaggi con un ritardo indefinitamente lungo

## Proprietà fornite da un protocollo di trasporto
- garanzia di consegna del messaggio
- consegna dei messaggi nello stesso ordine in vengono inviati
- consegna di una sola copia di ciascun messaggio
- supporto per messaggi di dimensione arbitraria
- supporto per la sincronizzazione fra il mittente e destinatario
- possibilità, per il ricevente, di applicare un controllo di flusso nei confronti del mittente
- supporto per più processi applicativi in ciascun host
>[!tip] Sfida dei protocolli di trasporto
>Sviluppare algoritmi che trasformino le proprietà, della rete sottostante nel servizio di alto livello richiesto dai programmi applicativi.

## Posizione dello strato di trasporto
![[materie/anno_2025-2026/reti_di_calcolatori/assets/posizione_strato_trasporto.jpg]]
- alcune funzionalità (come QoS e Congestion control) non stanno in un unico strato, ma richiedono la collaborazione di più strati
- protocolli end-to-end implementano comunicazione tra processi
	- può essere **connection-oriented** o **connectionless**
	- ci sono molti endpoint dentro un nodo => serve un altro livello di indirizzamento per identificarli

## Indirizzamento end-to-end nel TCP/IP
- gli endpoint dello strato di trasporto di Internet sono le **porte**
- Numero di porta va da 0 a 65535 (16 bit)
- in ogni connessione sono coinvolti due numeri di porta
	- uno per l'host del processo A
	- uno per l'host del processo B
- e anche l'indirizzo dell'host dove sta runnando il processo
	- più processi su un host $\equiv$ più porte sullo stesso indirizzo di rete

## Socket
- un endpoint è chiamato **socket**
	- creati da system calls
- il suo indirizzo è formato da <IP, porta>
	- IP identifica l'host 
	- numero di porta identifica il processo con quell'host
- due processi, per comunicare, devono avere un socket ciascuno, e usare lo stesso protocollo di trasporto
- ad ogni istante, una comunicazione è **interamente identificata da delle tuple**:
	- <IP_A, port_A, IP_B, port_B, protocollo>
## Modello client/server
- di solito due processi comunicano secondo il modello client/server
- **Server:**
	- un processo offre un servizio (accesso ad una risorsa)
	- sempre in esecuzione
	- aspetta per la richiesta del client
- **Client:**
	- vuole usare il servizio
	- può essere attivo solo quando necessario
	- piazza richieste al server

### Porte per il modello client/server
- per iniziare la comunicazione: client deve essere in grado di conoscere le porte del server
- server può imparare l'indirizzo del client quando è contattato
- di solito i server usano una porta **ben conosciuta**: server Web: 80 o server email: 25
- client usando porte **dinamiche**
	- scelte random e possibilmente una per comunicazione
## Range IANA
- **Porte conosciute**: usate da server ufficiali
	- possono essere usate solo da processi livello admin
- **Porte registrate**: potrebbero avere un uso standard, ma non ristretto ad un processo admin
- **Dinamiche**: libere per tutti;
	- di solito allocate dal kernel al client le quali non specificano nessuna porta
## Due tipi di comunicazione
- **Connection oriented:**
	- deve essere stabilita una connessione prima di scambiarsi i dati $\equiv$ più costoso
	- datagrammi appartengono ad una connessione, quindi più sotto controllo $\equiv$ più affidabile
	- In TCP/IP: implementato da TCP e STCP
- **Connectionless**:
	- ogni messaggio è spedito senza stabilire una connessione $\equiv$ risposta più rapida
	- ogni datagramma è indipendente
	- di solito non è affidabile
	- In TCP/IP implementato da UDP

# UDP
- estende il servizio di consegna host-to-host svolto dalla rete sottostante in un servizio di comunicazione tra processi
- aggiunge un livello di demultiplexing: consente così la condivisione della rete tra più processi applicativi
## Intestazione UDP
- 64 bit
![[materie/anno_2025-2026/reti_di_calcolatori/assets/udp_heade.jpg]]