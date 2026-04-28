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
- 64 bit = 8 bytes
![[materie/anno_2025-2026/reti_di_calcolatori/assets/udp_heade.jpg]]

- assicura la correttezza del messaggio tramite un checksum
- UDP calcola il proprio checksum su:
	- tutta l'intestazione UDP
	- sul contenuto del corpo del messaggio
	- su una parte chiamata **pseudoheader**
>[!definition]
>Pseudoheader
>>Composta da tre campi dell'intestazione IP:
>>- numero di protocollo
>>- indirizzo IP del mittente
>>- indirizzo IP del destinatario
>>- campo che contiene la lunghezza del pacchetto UDP

## API per servizi UDP
- ogni socket ha una coda di input e output mantenuta nel kernel
- le applicazioni accedono alle code usando system calls `sendmsg()` o `recvmsg()`
- messaggi sono spediti e letti nel suo insieme
	- un processo non può leggere messaggi in chunk più piccoli

## Simple demultiplexer (UDP)
- quando datagrammi arrivano all'host sono controllati e accodati alla coda della porta associata
- processi applicativi leggono i pacchetti seguendo la politica FIFO ad un pacchetto alla volta
- se la coda non ha spazio libero, il datagramma è scartato senza avviso
- se la porta non è associata ad una coda il datagramma è scartato
- datagrammi da sorgenti differenti destinati alla stessa porta possono essere interlacciati

## Caratteristiche dell'UDP
- comunicazione **connectionless**
- datagrammi non sono numerati, non appartengono ad una sessione/connessione
	- consegnati indipendetemente
- non c'è controllo di errori
- no controllo di flusso
	- mittente non viene notificato della perdita di pacchetti o se il ricevitore è congestionato
- incapsulamento in IP
	- possibilmente con frammentazione

## UDP è:
• **orientato alle transazioni**, adatto a protocolli semplici di tipo **richiesta-risposta**, come il **Domain Name System** o il **Network Time Protocol**.

• **semplice**, adatto al **bootstrap** o ad altri scopi che non richiedono uno stack protocollare completo, come **DHCP** e **TFTP**.

• **senza stato**, adatto a gestire un numero molto elevato di client, ad esempio nelle applicazioni di **streaming multimediale**, come l’**IPTV**.

## UDP è fatto apposta per:
• **Applicazioni in tempo reale**, come **Voice over IP** e **giochi online**, dove può essere preferibile perdere un datagramma piuttosto che ritardare la consegna dei dati ai processi in attesa di quelli mancanti.

• **Comunicazione unidirezionale**, ad esempio per comunicazioni **broadcast** e **multicast**, come la scoperta dei servizi e la condivisione di informazioni.

• **Implementazione di specifici protocolli di trasporto end-to-end nello spazio utente**, come **QUIC** di Google o **RPC** di Sun.

# TCP
- a differenza di UDP, TCP offre i seguenti servizi:
	- Affidabilità
	- Connection oriented
	- servizio di flusso di byte

## Controllo di flusso VS Controllo della congestione

- **Controllo di flusso**: consente al ricevitore di **limitare la quantità** di dati che il mittente può inviare in un certo istante
- **Controllo della congestione**: serve per controllare la **velocità** con cui TCP invia i dati per impedire al mittente di sovraccaricare la rete
- TCP deve affrontare questi due problemi
- di conseguenza larghezza di banda end-to-end e delay sono definiti dal ricevitore e dal collegamento/switch più lento lungo il cammino da sorgente a destinazione

## Problemi end-to-end
- nel cuore di TCP c'è l'algoritmo **sliding window**
- TCP viene eseguito in Internet invece che su una linea di collegamento punto-punto
	- TCP consente **connessioni logiche** tra processi che sono in esecuzione su due calcolatori qualsiasi in Internet
		- Esplicita fase di instaurazione della connessione: le parti coinvolte nella connessione si accordano per scambiarsi dati reciprocamente
- TCP ha valori dei tempi di **RTT molto diversi**
- I pacchetti possono essere **riordinati** mentre attraversano Internet
-  **Per il controllo di flusso**: TCP ha bisogno di un meccanismo tramite il quale ciascun lato della connessione possa sapere **quali risorse** **l’altro lato** è in grado di dedicare alla connessione.
- **Per il controllo della congestione**: TCP ha bisogno di un meccanismo tramite il quale il **lato mittente** possa conoscere la **capacità** della rete.

## Segmento TCP
- TCP è **orientato ai byte**: il mittente invia i byte in una connessione TCP e il destinatario legge i byte della connessione
- **Non vengono mantenuti i confini tra i messaggi**.
	- Altri protocolli invece li mantengono, ad esempio **SCTP**.
- Anche se l’espressione **“flusso di byte”** descrive il servizio che TCP offre ai processi applicativi, TCP non trasmette direttamente singoli byte su Internet.
- sull'host sorgente, TCP memorizza un numero sufficiente di byte ricevuti dal processo applicativo finché non ha riempito un pacchetto di dimensioni ragionevoli dopodiché invia tale pacchetto al proprio pari sull'host destinatario
- sull'host destinatario, TCP svuota quindi all'interno di un buffer il contenuto del pacchetto ricevuto, dopodiché il processo ricevente leggerà da questo buffer quanto vorrà
- i pacchetti scambiati fra pari entità del protocollo TCP sono chiamati **segmenti**

>[!question] Come TCP gestisce il flusso di byte?
>![[materie/anno_2025-2026/reti_di_calcolatori/assets/tcp_byte_stream.jpg]]

## Intestazione TCP
![[materie/anno_2025-2026/reti_di_calcolatori/assets/tcp_header.jpg]]

- SrcPort: porta sorgente
- DstPort: porta destinazione
- **Acknowledgment**, **SequenceNum** e **AdvertiseWindow** sono coinvolti nella gestione dell'algoritmo sliding window di TCP
- dato che TCP è un protocollo orientato ai byte, ogni byte di dati ha un numero di sequenza
- **SequenceNum**: numero di sequenza del primo byte di dati trasportato in quel segmento
- **Acknowledgment** e **AdvertiseWindow**: informazioni in merito al flusso dei dati che scorre nell'altra direzione
- **Il campo 6 bit Flags**: usato per trasportare informazioni di controllo fra pari entità di una connessione TCP
- I segnali possibili sono SYN, FIN, RESET, PUSH, URG e ACK
- I segnali SYN e FIN sono usati quando si instaura e si termina rispettivamente una connessione TCP
- Il segnale ACK assume valore 1 ogni volta che il campo Acknowledgment è valido e quindi il ricevitore vi deve porre attenzione
- il segnale URG al valore 1 significa che il segmento contiene dati urgenti in questo caso il campo UrgPtr indica dove iniziano i dati non urgenti contenuti nel segmento
	- mentre i dati urgenti sono contenuti all'inizio del corpo del segmento fino al valore di UrgPtr byte all'interno del segmento stesso
- il segnale PUSH indica che il mittente ha invocato l'operazione push chiedendo al ricevente di segnalare questo fatto al processo ricevente
- il segnale di RESET al valore 1 vuol dire che il ricevente è stato confuso (riceve un segmento che non si aspettava) per cui vuole terminare bruscamente la connessione
- il campo Checksum viene usato come descritto in UDP