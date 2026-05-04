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

## Diagramma degli stati di TCP
-  Una comunicazione **orientata alla connessione** deve mantenere alcune informazioni sui dati, sui segmenti mancanti, ecc.

- TCP è **stateful**, cioè mantiene uno stato.

- Ogni **socket TCP** si trova in uno specifico **stato**.

- Le transizioni da uno stato all’altro sono causate da eventi, come:

	- esecuzione di comandi a livello applicativo sul socket, ad esempio `accept()`, `connect()`, `close()`;

	- ricezione di segmenti con flag appropriati.

- Le transizioni possono causare l’invio di segmenti con flag appropriati

- Gli **stati** e le **transizioni di stato** di un socket TCP sono definiti dal protocollo tramite un **DFA** (_Deterministic Finite Automaton_), in realtà una **macchina di Mealy**.
- Ogni transizione è attivata da un determinato **evento** e può produrre la trasmissione di un **segmento** con flag appropriati.
- Le fasi principali sono tre:
    1. **Handshaking**: creazione della connessione.
    2. **Data transfer**: fase in cui avviene il trasferimento dei dati.
    3. **Closing**: chiusura della connessione.
- Una connessione può rimanere nello stato **ESTABLISHED** per un tempo illimitato, anche per sempre.
### Fase 1: handshake
- prima di spedire qualsiasi dato, due processi devono stabilire una **connessione**
	- un processo attende per la connessione eseguendo una funzione TCP per l'**apertura passiva**
		- `accept()` Blocking syscall
	- l'altro processo inizia la connessione eseguendo un'**apertura attiva**
		- `connect()` Time-outed syscall
	- i due strati TCP eseguono l'**handshake a tre vie**
1. l'host in apertura passiva sta aspettando
2. entità attiva invia segmento al server (passiva) annunciando il numero iniziale di sequenza che pensa di usare (Flags = SYN, SequenceNum = x)
3. server risponde con un unico segmento SYN+ACK:
	- (Flags = ACK, ACK = x+1) conferma il numero di sequenza del client
	- (Flags = SYN, SequenceNum = y) annuncia il proprio numero di sequenza
	- nel campo Flags di questo msg sono impostati a 1 sia SYN che ACK
4. Il client risponde con un terzo segmento che conferma il numero di sequenza del server (Flags = ACK, ACK = y + 1)
5. ogni entità conferma il numero di sequenza inviandolo aumentato di uno
>[!tip] Il campo Acknowledgment identifica in ogni momento il successivo numero di sequenza che ci si aspetta di ricevere confermando così implicitamente di aver ricevuto tutti i numeri di sequenza precedenti.

>[!question] Perché client e server devono scambiarsi numeri iniziali di sequenza all'instaurazione della connessione ?
>- Sarebbe il caso se ciascuna entità iniziasse con 0
>- TCP richiede che ogni entità coinvolta selezioni a caso un numero iniziale di sequenza per proteggere il protocollo dal fatto che due incarnazioni della stessa connessione riutilizzino troppo presto gli stessi numeri.

#### Casi particolari: apertura attiva simultanea
- Un **client** non sa se un server si trova in **apertura passiva** finché non prova a connettersi.
- Se il server **non** è in apertura passiva, il client riceve un segmento **RST**.
- Può accadere, anche se molto raramente, che anche l’altro host tenti un’**apertura attiva** nello stesso momento.  
    Questo caso si chiama **apertura attiva simultanea** (_simultaneous active opening_).
- In questo caso:
    - entrambi gli host inviano un segmento **SYN**;
    - i due segmenti **si incrociano** nella rete;
    - ciascun host riconosce questa situazione perché riceve un **SYN** dopo aver già inviato un **SYN**;
    - entrambi gli host si comportano quindi come se fossero server, rispondendo con **SYN + ACK**;
    - a quel punto la connessione viene stabilita.
### Fase 2: Trasferimento dati
- entrambi i lati si trovano nello stato ESTABLISHED
- ogni segmento trasporta dati in **una direzione** e l'acknowledge dei dati nella direzione opposta
- i due flussi sono indipendenti
- TCP mantiene i dati nei buffer
	- in uscita: prima di assemblare un segmento
	- in entrata: prima di passarlo alle applicazioni
- questo potrebbe far perdere latenza e causare delay, che potrebbe essere brutto brutto per le applicazioni interattive
- L’applicazione mittente può richiedere il **data pushing**, cioè l’invio dei dati **senza buffering**, tramite un flag speciale.
	- Se la richiesta viene accettata, il TCP del mittente invia i dati **il prima possibile**, senza mantenerli nel buffer, attivando il bit **PSH**.
	- Il TCP del destinatario, quando trova **PSH = 1**, consegna i dati all’applicazione ricevente **il prima possibile**, cioè senza buffering
#### URG data
- TCP è **strettamente sequenziale**.
- A volte può essere utile consegnare alcuni dati **fuori sequenza**, ad esempio per:
    - segnalazioni urgenti;
    - comandi di interruzione;
    - comandi di abort.
- L’applicazione può richiedere una **consegna urgente** durante una `send`.
- Se la richiesta viene accettata:
    - il TCP del mittente inserisce i **dati urgenti** all’inizio del segmento successivo;
    - attiva il bit **URG**;
    - imposta di conseguenza l’**urgent pointer**.
- Il TCP del destinatario, quando trova **URG = 1**:
    - separa i dati urgenti da quelli standard;
    - consegna immediatamente i dati urgenti all’applicazione;
    - può farlo anche se quei dati arrivano **fuori ordine**.
### Fase 3: chiusura
- Dopo un certo tempo, uno dei due host può richiedere la **chiusura della connessione**.
- La chiusura è causata dalla system call **`close()`** eseguita da una delle due parti.
- La parte che chiama `close()` viene chiamata **initiator**, cioè **iniziatore della chiusura**.

> [!warning] Attenzione  
> L’**initiator della chiusura** non è necessariamente lo stesso host che aveva iniziato la connessione nella fase di apertura.  
> Qualsiasi delle due parti può iniziare la sequenza di chiusura.

- L’altra parte risponde eseguendo la **sequenza del responder**, cioè del **risponditore**.
- Nel raro caso in cui entrambe le parti inizino la sequenza di chiusura nello stesso momento, si parla di **simultaneous close**, cioè **chiusura simultanea**.
- **Host A** inizia la procedura di chiusura inviando un segmento con **FIN = 1** e passando allo stato **FIN-WAIT-1**.
- Questo segmento può contenere anche l’ultimo **payload di dati**.

> [!important]  
> Dopo aver inviato il segmento con **FIN = 1**, **A non può più inviare nuovi dati**.

- **Host B** conferma la ricezione del FIN inviando un **ACK** ad A e passando allo stato **CLOSE-WAIT**.
- B notifica la chiusura all’applicazione, cioè segnala una condizione di **end-of-file**.
- Quando A riceve l’ACK, passa allo stato **FIN-WAIT-2**.
- L’applicazione su B può ancora inviare dati ad A.
- A continuerà a ricevere questi dati e a confermarli con opportuni **ACK**.
- Successivamente, anche l’applicazione su B chiude il socket.
- A questo punto B invia un segmento con **FIN = 1** ad A e passa allo stato **LAST-ACK**.
- A riceve il FIN, invia il relativo **ACK** e passa allo stato **TIME-WAIT**.
- B chiude definitivamente il socket quando riceve l’ACK da A.

>[!question] Perché aspettare nello stato `TIME_WAIT`?
>1. Possibile perdita dell’ACK finale
>	- L’**ACK** inviato dopo lo stato **`FIN-WAIT-2`**, come risposta al **FIN** dell’altro host, potrebbe andare perso.
>	- In questo caso, il server potrebbe ritrasmettere il segmento **FIN**.
>	- Se però il client avesse già cancellato tutte le informazioni relative alla connessione, riceverebbe un **FIN** senza sapere chiaramente a quale connessione si riferisce.
> 2. Evitare interferenze da vecchi segmenti
> 	- Alcuni vecchi segmenti della connessione precedente potrebbero essere ancora in circolazione nella rete.
> 	- Se la stessa combinazione di:
> 		- indirizzi IP;
> 		- porte;
> 		- protocollo;
> 	- venisse riutilizzata per una nuova connessione, un vecchio segmento potrebbe arrivare in ritardo ed essere interpretato come valido nella nuova connessione.

> [!important]  
> Lo stato **`TIME_WAIT`** serve quindi a mantenere temporaneamente le informazioni della connessione, in modo da poter rispondere correttamente a eventuali ritrasmissioni del **FIN**

> [!note]  Questo fenomeno è pericoloso perché una nuova connessione con gli stessi parametri potrebbe essere disturbata da segmenti appartenenti alla connessione precedente
#### Durata dell’attesa
- Il tempo di attesa nello stato **`TIME_WAIT`** è pari a **due volte il Maximum Segment Lifetime**, cioè:

```
TIME_WAIT = 2 × MSL
```

- **MSL** significa **Maximum Segment Lifetime**, ovvero il tempo massimo per cui un segmento può rimanere in circolazione nella rete.
- Questo parametro è definito dal sistema.
- Di solito è circa **1–2 minuti**, ma può essere ridotto.

## Rivisitazione sliding window
1. garantisce la consegna affidabile dei dati
2. garantisce che i dati vengano consegnati nella sequenza corretta
3. consente il controllo di flusso tra il mittente e il destinatario
![[materie/anno_2025-2026/reti_di_calcolatori/assets/sliding_window_revisited.jpg]]
- Lato mittente: LastByteAcked $\leq$ LastByteSent $\leq$ LastByteWritten
	- **LastByteAcked** indica l’ultimo byte confermato tramite ACK.
	- Più precisamente, corrisponde al valore dell’**Acknowledgment** più avanzato ricevuto, **meno 1** 
- Lato ricevente: LastByteRead $<$ NextByteExpected $\leq$ LastByteRcvd + 1
	- **NextByteExpected** è il valore che il ricevitore invia al mittente nel campo **Acknowledgment** dell’header TCP.
### Controllo di flusso TCP
- Per evitare di **sovraccaricare il buffer del ricevitore**, deve valere:
$$  
LastByteRcvd - LastByteRead \leq MaxRcvBuffer  
$$

- Quindi il ricevitore può ancora accettare questa quantità di dati:

$$  
AdvertisedWindow = MaxRcvBuffer - ((NextByteExpected - 1) - LastByteRead)  
$$

- Questo è il valore che il ricevitore invia al mittente nel campo **Window** dell’header TCP.

---
## Vincolo lato mittente

- Il mittente, dall’altra parte, non deve mai inviare al ricevitore più dati di quanti quest’ultimo possa memorizzare nel proprio buffer.
    
- Deve quindi valere:

$$  
LastByteSent - LastByteAcked \leq AdvertisedWindow  
$$

- Questa quantità include anche i dati già inviati ma **non ancora confermati** tramite ACK.
    
- Di conseguenza, il limite effettivo sui dati che il mittente può ancora inviare è:
    
$$  
EffectiveWindow = AdvertisedWindow - (LastByteSent - LastByteAcked)  
$$

cioè:

$$  
EffectiveWindow = AdvertisedWindow - (LastByteSent - (Acknowledgment - 1))  
$$

quindi:

$$  
EffectiveWindow = AdvertisedWindow - (LastByteSent + 1 - Acknowledgment)  
$$

dove **Acknowledgment** è il valore più aggiornato ricevuto dal mittente.

#### Vincolo sul buffer di invio TCP

- Inoltre, poiché il processo applicativo mittente non può sovraccaricare il **buffer di invio**, deve sempre valere:

LastByteWritten−LastByteAcked≤MaxSendBufferLastByteWritten - LastByteAcked \leq MaxSendBufferLastByteWritten−LastByteAcked≤MaxSendBuffer

- Questo significa che, se il processo mittente prova a scrivere **y byte**, ma vale la condizione:

(LastByteWritten−LastByteAcked)+y>MaxSendBuffer(LastByteWritten - LastByteAcked) + y > MaxSendBuffer(LastByteWritten−LastByteAcked)+y>MaxSendBuffer

allora l’operazione di **`write`** viene bloccata.

- La `write` rimane bloccata finché non si libera spazio nel buffer di invio.
- Lo spazio si libera quando una quantità sufficiente di dati viene:
    - inviata al ricevitore;
    - confermata dal ricevitore tramite **ACK**.

---

#### Effetto sul controllo di flusso

- In questo modo, riducendo la finestra a **0**, il processo ricevente può:
    - rallentare la trasmissione dal processo mittente;
    - oppure fermarla completamente.

> [!important]  
> Il controllo di flusso TCP permette quindi al ricevitore di regolare la velocità del mittente in base allo spazio disponibile nel proprio buffer.

### Riapertura della finestra TCP

- Il mittente può ricominciare a trasmettere quando la finestra si apre di nuovo, cioè quando il processo ricevente consuma alcuni dati dal buffer.
    
- La nuova finestra può essere notificata dal ricevitore nei segmenti che invia al mittente, se il ricevitore ha dati da mandare al mittente, cioè nel flusso nella direzione opposta.
    

---

### Problema: il ricevitore non ha dati da inviare

- Ma cosa succede se il ricevitore non ha dati da inviare al mittente?
    
- In quel caso, il mittente potrebbe non scoprire mai che la finestra si è riaperta.
    

> [!warning]  
> Se la finestra era stata annunciata come **0** e il ricevitore non invia più segmenti, il mittente rimarrebbe bloccato indefinitamente.

---

### Probe segment

- Per questo motivo, se il mittente sa che:
    

$$  
AdvertisedWindow = 0  
$$

allora aspetta un segmento dal ricevitore fino a un certo **timeout**.

- Se entro quel timeout non riceve nessun segmento, invia un **probe segment** di **1 byte**.
    
- Questo segmento serve a “stimolare” una risposta **ACK** da parte del ricevitore, contenente il valore aggiornato della finestra corrente.
    

---

### Backoff esponenziale

- Il timeout tra un probe e il successivo viene aumentato in modo **esponenziale**.
    
- Questo meccanismo prende il nome di **backoff algorithm**.
    

> [!important]  
> Il probe segment evita che il mittente rimanga bloccato per sempre quando la finestra del ricevitore torna disponibile, ma il ricevitore non ha dati propri da inviare.

## Protezione contro il wraparound
- Come nel protocollo **Sliding Window**, dobbiamo garantire che non ci siano due dati ancora non confermati, in questo caso **byte**, con lo stesso **numero di sequenza**.
- La condizione che avevamo visto era:
$$
window width< \frac{maximum\ sequence\ number}{2}​
$$
equivalente a:
$$
maximum sequence number>2×window width
$$
- In TCP:
    - **SequenceNum**: 32 bit;
    - **AdvertisedWindow**: 16 bit.
- Quindi il requisito dell’algoritmo **Sliding Window** è soddisfatto, perché:

$$
2^{32} \gg 2 \times 2^{16}
$$

- Le implementazioni recenti hanno più bit per **AdvertisedWindow**, ma la condizione continua comunque a valere.
### Importanza dello spazio dei numeri di sequenza a 32 bit

- È importante considerare la dimensione dello spazio dei **sequence number** a 32 bit.
    
- Il numero di sequenza usato su una determinata connessione potrebbe andare in **wraparound**, cioè ricominciare da capo dopo aver raggiunto il valore massimo.
    
- Questo significa che:
    
    - un byte con numero di sequenza **x** potrebbe essere inviato in un certo momento;
        
    - successivamente, un secondo byte con lo stesso numero di sequenza **x** potrebbe essere inviato di nuovo.
        

---

### Ruolo del Maximum Segment Lifetime

- I pacchetti non possono sopravvivere in Internet per un tempo superiore al **Maximum Segment Lifetime**, abbreviato **MSL**.
    
- Il valore predefinito di **MSL** è di circa **120 secondi**.
    
- Dobbiamo quindi assicurarci che il numero di sequenza **non vada in wraparound entro un periodo di 120 secondi**.
    

> [!important]  
> Se il numero di sequenza si ripetesse troppo rapidamente, un vecchio segmento ancora presente nella rete potrebbe essere confuso con un segmento nuovo della stessa connessione.

---

### Da cosa dipende il problema?

- Il rischio di wraparound dipende da quanto velocemente i dati possono essere trasmessi su Internet.
    
- Più la connessione è veloce, più rapidamente vengono consumati i numeri di sequenza disponibili.
    
- Se la velocità è molto alta, lo spazio a **32 bit** potrebbe teoricamente esaurirsi e ricominciare da capo prima che i vecchi segmenti siano sicuramente scomparsi dalla rete.

### Mantenere piena la pipe

- Il campo **AdvertisedWindow** deve essere abbastanza grande da permettere al mittente di mantenere la **pipe piena**.
    

> [!note]  
> Naturalmente, il ricevitore è libero di **non aprire la finestra** fino alla dimensione massima consentita dal campo **AdvertisedWindow**.

- Se il ricevitore ha abbastanza spazio nel buffer, la finestra deve essere aperta abbastanza da permettere il trasferimento di una quantità di dati pari a:
    

$$  
delay \times bandwidth  
$$

cioè il prodotto tra **ritardo** e **larghezza di banda**.

---

#### Limite della finestra a 16 bit

- Un campo da **16 bit** permette una finestra massima di:
    

$$  
2^{16} = 64 \text{ kB}  
$$

- Questa dimensione può non essere sufficiente per le cosiddette **long fat lines**, cioè linee con:
    

$$  
delay \times bandwidth \gg 12500 \text{ bytes}  
$$

- In altre parole, su collegamenti con **alta banda** e/o **alto ritardo**, una finestra da 64 kB potrebbe essere troppo piccola per sfruttare pienamente la capacità della rete.
    

---

#### Window scaling in TCP

- TCP permette di impostare un **fattore di scaling** durante il protocollo di **handshake**.
    
- Il fattore di scaling può arrivare fino a:
    

$$  
2^{14}  
$$

- Quindi la finestra può arrivare fino a circa **1 GB**:
    

$$  
2^{16} \times 2^{14} = 2^{30}  
$$

> [!important]  
> Il **window scaling** serve quindi ad aumentare la dimensione effettiva della finestra TCP, permettendo prestazioni migliori su collegamenti ad alta capacità e alto ritardo.

## Attivazione della trasmissione in TCP

- Come decide TCP quando trasmettere un segmento?
    
- TCP supporta un’astrazione a **flusso di byte** (_byte stream_).
    
- I programmi applicativi scrivono byte all’interno degli stream.
    
- Spetta a TCP decidere quando ha raccolto abbastanza byte da poter inviare un segmento.
    
- Per il momento ignoriamo il **controllo di flusso**: assumiamo che la finestra sia completamente aperta, come accade tipicamente all’inizio della connessione.
    

---

### Meccanismi che attivano la trasmissione

TCP ha tre meccanismi principali per attivare la trasmissione di un segmento.

#### 1. Raggiungimento della Maximum Segment Size

- TCP mantiene una variabile chiamata **Maximum Segment Size**, abbreviata **MSS**.
    
- TCP invia un segmento non appena ha raccolto **MSS byte** dal processo mittente.
    
- La **MSS** è solitamente impostata alla dimensione del segmento più grande che TCP può inviare senza causare frammentazione da parte di IP locale.
    
- In formula:
    

$$  
MSS = MTU - (TCP\ header + IP\ header)  
$$

dove:

- **MTU** è la dimensione massima del pacchetto trasmissibile sulla rete direttamente connessa;
    
- **TCP header** è l’intestazione TCP;
    
- **IP header** è l’intestazione IP.
    

---

#### 2. Richiesta esplicita del processo mittente

- Il processo mittente può chiedere esplicitamente a TCP di inviare i dati.
    
- TCP supporta infatti l’operazione di **push**.
    

> [!note]  
> In questo caso, TCP non aspetta necessariamente di raggiungere la MSS, ma può inviare subito i dati disponibili.

---

#### 3. Scadenza di un timer

- TCP può inviare un segmento anche quando scade un **timer**.
    
- Il segmento risultante contiene tutti i byte attualmente presenti nel buffer di trasmissione.
    
- Tuttavia, la quantità inviata deve sempre rispettare due limiti:
    
    - al massimo la **MSS**;
        
    - al massimo la **EffectiveWindow**.
        

> [!important]  
> Quindi TCP può trasmettere quando ha abbastanza dati per riempire un segmento, quando l’applicazione forza l’invio con una push operation, oppure quando scade un timer.

## Silly Window Syndrome

- L’algoritmo TCP di base a **sliding window** non impone una dimensione minima ai segmenti trasmessi.
    
- Il **Silly Window Syndrome** (**SWS**) è una situazione in cui vengono inviati molti segmenti piccoli e inefficienti, con maggiore overhead, invece di pochi segmenti più grandi.
    
- Questo può accadere quando:
    
    - il destinatario annuncia dimensioni di finestra troppo piccole;
        
    - oppure il mittente è troppo aggressivo nell’inviare immediatamente quantità molto piccole di dati.
        
- Non si tratta di un fallimento dell’algoritmo **sliding window**, che svolge comunque il suo compito di mantenere pieno il buffer del ricevitore.
    
- Si tratta piuttosto di un’inefficienza dovuta all’**overhead di rete**.
    

---

### Caso peggiore del Silly Window Syndrome

- Il caso peggiore si verifica quando:
    
    - **AdvertisedWindow** è pari a `0`;
        
    - il processo ricevente consuma `1 byte`;
        
    - il ricevitore comunica al mittente che **AdvertisedWindow = 1**;
        
    - il mittente invia aggressivamente un segmento da `1 byte`, richiudendo la finestra;
        
    - il ciclo si ripete.
        
- Questo porta a una sequenza di segmenti da `1 byte`.
    
- Ogni segmento da `1 byte` porta però con sé circa `40 byte` di header:
    
    - header IP;
        
    - header TCP.
        

> [!warning]  
> Il problema è che si trasmettono pochissimi dati utili rispetto all’overhead generato dagli header.

---

### Perché conviene aspettare

- Sarebbe meglio che il mittente aspettasse un po’ prima di inviare un segmento.
    
- In questo modo, il processo ricevente avrebbe il tempo di consumare più byte dal buffer.
    
- Di conseguenza, la finestra si aprirebbe di più.
    
- A quel punto, il mittente potrebbe inviare un singolo segmento più grande, invece di molti segmenti minuscoli.

## Algoritmo di Nagle

- Se ci sono dati da inviare, ma la finestra aperta è minore della **MSS**, allora può convenire aspettare un certo tempo prima di inviare i dati disponibili.
    
- Il problema è: **quanto bisogna aspettare?**
    
- Se aspettiamo troppo, danneggiamo le applicazioni interattive, come:
    
    - **Telnet**;
        
    - **SSH**.
        
- Se non aspettiamo abbastanza, rischiamo di inviare molti pacchetti piccoli e di cadere nel **Silly Window Syndrome**.
    

---

### Soluzione di John Nagle

- John Nagle ha introdotto una soluzione elegante basata su un meccanismo **self-clocking**, cioè “auto-temporizzato”.
    

#### Idea chiave

- Finché TCP ha dati **in flight**, cioè dati inviati ma non ancora confermati, il mittente prima o poi riceverà un **ACK**.
    
- Questo **ACK** può essere trattato come se fosse lo scadere di un timer.
    
- Quindi l’arrivo dell’ACK può attivare la trasmissione di altri dati.
    
- Se invece non ci sono dati **in flight**, allora non c’è nessun ACK da aspettare.
    
- In quel caso, TCP può inviare subito i dati presenti nel buffer.
    

---

#### Funzionamento dell’algoritmo di Nagle

Quando l’applicazione produce dati da inviare:

```text
if both the available data and the window are ≥ MSS
	send a full segment
else
	if there is unACKed data in flight
		buffer the new data until an ACK arrives
	else
		send all the new data, up to the window, now
```

In italiano:

```text
se sia i dati disponibili sia la finestra sono ≥ MSS
	invia un segmento pieno
altrimenti
	se ci sono dati inviati ma non ancora confermati
		memorizza i nuovi dati nel buffer finché non arriva un ACK
	altrimenti
		invia subito tutti i nuovi dati, fino al limite della finestra
```

> [!important]  
> L’algoritmo di Nagle evita di inviare tanti segmenti piccoli consecutivi.  
> Se c’è già traffico non confermato in rete, TCP aspetta un ACK prima di inviare altro.

## Ritrasmissione adattiva: calcolo del timeout

- Un segmento deve essere **ritrasmesso** se non riceviamo un **ACK** entro un certo tempo.
    
- Il problema è: **come impostare il timeout?**
    
- Il timeout deve adattarsi ai **ritardi della rete**.
    

---

### Algoritmo originale

- Si misura il **SampleRTT** per ogni coppia:
    
    - segmento inviato;
        
    - ACK ricevuto.
        
- Si calcola una media pesata degli RTT.
    

$$  
EstRTT := \alpha \times EstRTT + (1 - \alpha) \times SampleRTT  
$$

- Il valore di $\alpha$ è compreso tra:
    

$$  
0.8 \leq \alpha \leq 0.9  
$$

- Il timeout viene impostato in base a **EstRTT**:
    

$$  
TimeOut = 2 \times EstRTT  
$$

---

### Calcolo del timeout: algoritmo di Karn-Partridge

#### Problema dell’algoritmo originale

- L’**ACK** non conferma propriamente una specifica trasmissione, ma solo la ricezione dei dati.
    
- Quando un segmento viene ritrasmesso e poi arriva un ACK al mittente, è impossibile stabilire se quell’ACK debba essere associato:
    
    - alla **prima trasmissione** del segmento;
        
    - oppure alla **seconda trasmissione**, cioè alla ritrasmissione.
        
- Questo rende ambiguo il calcolo dell’**RTT**.
    

---

#### Soluzione: algoritmo di Karn-Partridge

- L’algoritmo di **Karn-Partridge** è obbligatorio in TCP.
    
- La soluzione prevede due regole:
    
    1. **Non campionare l’RTT quando si effettua una ritrasmissione**.
        
    2. **Raddoppiare il timeout dopo ogni ritrasmissione**.
        

> [!important]  
> In questo modo TCP evita di calcolare RTT sbagliati a partire da ACK ambigui e reagisce aumentando progressivamente il timeout quando la rete mostra segni di ritardo o perdita.

## Prestazioni di TCP

- Le due metriche principali sono:
    
    - **latenza**;
        
    - **throughput**.
        
- Setup sperimentale:
    
    - processore **Xeon 2.4 GHz**;
        
    - doppia **Gigabit Ethernet** in **link aggregation**;
        
    - sistema operativo **Linux**.
        
- Limite del canale a livello **data link**:
    
    - quasi **2 Gbps full duplex**;
        
    - senza perdite.
        

---

### Relazione tra MSS e throughput

- Più grande è la **MSS**, maggiore è il **throughput**.
    
- Tuttavia, sopra **1 KB**, il throughput non aumenta in modo sostanziale.
    
- La **MSS tipica** è:
    

$$  
MSS = 1460 \text{ byte}  
$$

- Questo valore è adatto quando l’interfaccia ha:
    

$$  
MTU = 1500 \text{ byte}  
$$

- Il throughput rimane comunque sotto i **2 Gbps**, a causa di diversi **colli di bottiglia**.
    
- A volte, il collo di bottiglia può essere la **memoria stessa**.
    

> [!important]  
> Nel complesso, TCP può comunque raggiungere throughput molto elevati.