---
title: "Capitolo 1"
aliases: ["Capitolo 1"]
tags: [università, "materie", "anno-2025-2026", "reti-di-calcolatori", "capitolo-1"]
created: 2025-10-06
---
# Reti
+ nodi indipendenti
+ scambio informazioni
+ usando canali di comunicazione
+ un compito non può essere eseguito da un singolo nodo

## Features
+ Scopo generale:
	+ non ottimizzate per un'applicazione specifica
	+ più applicazioni possono coesistere
+ Flessibilità e apertura:
	+ nuove features possono essere aggiunte dinamicamente


# Foundations

## Applications
Le persone tendono ad identificare la rete tramite le applicazioni
+ World Wide Web
+ Email
+ Social
+ ecc...

## Connectivity

### Point-to-Point
+ Possono collegare solo due nodi.
+ lunghezza arbitraria
### Multiple access
+ coordinarsi nell'accesso al mezzo
+ rischio di conflitti


Collegare più dispostivi attraverso gli **switch** per instradare i messaggi.

+ Commutazione di circuito: durante la comunicazione si crea un canale dal capo all'altro che dura tutta la durata della comunicazione.
+ Commutazione di pacchetto: i messaggi vengono visti come elementi atomici che vengono passati da un nodo all'altro. (**Store-and-forward**)

>[!definition]
>Router
>>Nodo di interconnessione. Permettono le interconnessioni tra reti.

Mezzo condiviso da due o più nodi.
Due o più reti connesse da un router.

# Reliability

>[!question] Perché una rete fallisce ?
>> - computer interrompono il loro funzionamento e riavviati
>> - fibre tagliate
>> - interferenze elettromagnetiche modificano i bit nei dati
>> - switch esauriscono il proprio spazio di memorizzazione
>> - software che gestisce tutto può inoltrare i pacchetti verso l'ignoto

> [!warning]
> ## Requisito principale di una rete
>> Mascheramento di alcuni malfunzionamenti in modo da far apparire la rete più affidabile di quanto non sia alle app che la usano.

## Classi di malfunzionamenti

### Errori di bit:
+ un valore 1 viene trasformato in uno 0 o viceversa
+ Burst error: modificati più bit consecutivi
### Errori a livello di pacchetto
+ il pacchetto contiene un errore di bit non recuperabile
+ uno dei nodi che deve gestire il pacchetto (uno switch) non ha spazio per memorizzarlo (sovraccarico) e quindi lo elimina (**congestione**)
+ il software in uno dei nodi compie un errore: potrebbe erroneamente inoltrare un pacchetto sulla linea sbagliata
### Errore a livello di nodo e linea di collegamento
+ linea fisica interrotta oppure computer a cui è connessa non funziona

>[!warning]
>Guasti non devono rendere completamente inutilizzabile la rete.
>> In una rete a commutazione di pacchetto è possibile aggirare un nodo o una linea guasti

>[!tip]
> ## Definizione di canali utili
> Coinvolge sia la comprensione dei requisiti delle applicazioni sia l'identificazione dei limiti della tecnologia sottostante.

>[!definition]
>Divario semantico
>> colmare il divario fra ciò che si attende l'applicazione e ciò che può essere fornito dalla tecnologia sottostante.

# Architettura

>[!tip]
>Le reti non rimangono fisse così come sono progettate ma devono poter **evolvere** per incorporare modifiche.

## Stratificazione
+ difficile implementare tutte le funzioni in un singolo pezzo di codice/hardware
+ adottare un'architettura a strati
	+ ogni livello costruito su quello sottostante aggiungendo nuove funzionalità

### Caratteristiche:
+ scompone i problema di costruire una rete in sottoproblemi più gestibili;
+ consente una progettazione più modulare: se si decide di aggiungere qualche nuovo servizio, sarà da modificare le funzionalità di un solo livello

>[!definition]
>Protocollo
>>Oggetti astratti che compongono gli strati di un sistema di rete. Fornisce un servizio di comunicazione che gli oggetti del livello superiore usano per scambiarsi messaggi.

## Interfacce
>[!definition]
>Interfaccia del servizio
>> oggetti sullo stesso calcolatore che usano i servizi di comunicazione del protocollo stesso.

>[!example]
>Un protocollo di tipo *richiesta/risposta* potrebbe supportare le operazioni mediante le quali un'applicazione può inviare e ricevere messaggi.

>[!definition]
>Interfaccia di livello o peer-to-peer
>>definisce la forma e significato dei messaggi scambiati tra le controparti del protocollo.

>[!example]
>Un protocollo definisce un servizio di tipo *richiesta/risposta* comunica con la sua controparte


## Incapsulamento
Allegare un'**intestazione** (header) per la corretta lettura del messaggio al messaggio da inviare, eventualmente per ricostruire un messaggio diviso in più segmenti.

>[!definition]
>Intestazione
>> Struttura dati usata fra le controparti di pari livello per comunicare fra loro.
>è formato da uno stack dei metodi usati (TCP, IP,...) (ovvero le intestazioni dei passaggi precedenti che formano il pacchetto finale) e si guarda dal basso verso l'alto

Processo di incapsulamento viene ripetuto ad ogni livello del grafo di protocolli.

### Multiplexing e Demultiplexing

>[!example]
>Se avessimo messaggi provenienti da **due diverse applicazioni** dovremmo **multiplarli** sul canale del calcolatore sorgente e **demultiplarli** nel calcolatore destinazione e consegnarli all'applicazione corretta.

Il protocollo aggiunge un identificativo relativo all'applicazione a cui appartengono i messaggi: **chiave di demultiplazione**.

# ISO/OSI

## Livello fisico
>[!definition]
>>Gestisce la trasmissione di flussi non strutturati di bit attraverso una linea di comunicazione

### Dispositivi

>[!definition]
>Ripetitore
>> - Connette due dispositivi utilizzando stesso tipo di media fisico in modo che appaiano come un unico segmento;
>> - **Ripristina il segnale:** il segnale tende a degradarsi durante il tragitto quindi il ripetitore lo **decodifica** e lo **rigenera** per poterlo inviare di nuovo con la stessa qualità;
>> - Amplificare e ripetere il segnale fisico che trasporta i bit senza cambiare il contenuto dei dati;
>> - **Commutazione di bit:** dati sono costituiti da singoli bit.

## Livello collegamento dati
>[!definition]
>> Raccoglie poi un flusso di bit in un aggregato più grande denominato **frame**.

Livello tipicamente realizzato:
+ con gli adattatori di rete 
+ software di controllo dei dispositivi (**driver**) in esecuzione tramite l' OS del nodo
>[!warning]
>>Sono i frame, e non i bit, ad essere scambiati tra gli host
### Dispositivi
>[!definition]
>Bridge
>> - Connette due link differenti
>> - **Commuta i frame:** ogni frame che arriva viene esaminato e se non contiene errori viene inoltrato;
>> - **Controllo errori e forwarding**
>> - **Header invariati, ma codifiche fisiche diverse**: Il bridge solitamente non modifica gli header dei frame (gli indirizzi MAC), ma può operare con media fisici diversi (ad esempio, può ricevere un frame su una connessione in fibra ottica e inviarlo su una connessione in rame).
>> - **Switch come bridge multiporta**: Un **switch** è fondamentalmente un bridge che ha più porte (collegamenti), consentendo di gestire più segmenti di rete contemporaneamente. Ogni porta di uno switch funge da bridge per un collegamento separato.

## Livello di rete
>[!definition]
>>Gestisce l'instradamento fra i nodi in una rete a commutazione di pacchetto.

>[!definition]
>Pacchetto
>> Com'è chiamato il dato atomico scambiato tra i nodi in questo livello.

Questi tre livelli sono implementati in tutti i nodi della rete, compresi switch e host.
### Dispositivi
>[!definition]
>Router
>> - **Collega reti differenti**: Un **router** si occupa di collegare **segmenti di rete differenti**, come ad esempio due reti locali (LAN) o una rete locale con una rete geografica (WAN). Questi segmenti appaiono come un'unica rete per il router.
>> - **Commuta pacchetti**: A livello 3, i dati sono organizzati in **pacchetti**. Il router riceve un pacchetto da un segmento di rete e lo inoltra su un altro segmento. Ogni pacchetto contiene informazioni di routing (come l'indirizzo IP di destinazione) che il router utilizza per determinare la destinazione.
>> - **Modifica dell'header del frame**: Sebbene l'**header di rete** (tipicamente l'indirizzo IP) rimanga invariato, l'**header del frame** che contiene informazioni di livello fisico e di collegamento (come l'indirizzo MAC) viene sostituito dal router per adattarsi alla rete di destinazione. 
## Strato di Trasporto

>[!definition]
>Messaggio
>> Com'è chiamato il dato atomico scambiato tra i nodi in questo livello.

>[!warning]
>> Lo strato di trasporto e gli strati superiori sono solitamente in esecuzione soltanto sugli host terminali, **NON** sugli switch e router intermedi.

### Dispositivi
>[!definition]
>Proxy
>> - **Traduzione tra host diversi**: Un **proxy** funge da intermediario tra il client e il server, **traducendo le comunicazioni** tra due host che potrebbero utilizzare tecnologie o protocolli diversi. Agisce come una sorta di "ponte" tra due applicazioni o reti.
>> - **Commuta messaggi**: Il proxy opera su **messaggi** a livello di applicazione, manipolando i dati trasmessi tra client e server.
>> - **Sostituzione degli header**: Il proxy **modifica gli header di rete e di frame**, che sono specifici della rete di comunicazione, ma **mantiene gli header del protocollo applicativo e di trasporto** (come HTTP o TCP), garantendo che la comunicazione continui a funzionare correttamente a livello di applicazione.
>> - **Accesso a un servizio attraverso un host più vicino**: Il proxy consente ai client di **accedere a un servizio** remoto (B) attraverso un host che può essere più vicino o più sicuro, fungendo da "intermediario". Ad esempio, un proxy può essere utilizzato per accedere a un server dietro un firewall.
>> - **Utilizzo per firewall e controllo traffico**: I proxy sono utili per **oltrepassare firewall**, monitorare il traffico di rete e, in alcuni casi, **filtrare o analizzare i contenuti** che passano attraverso di essi, migliorando la sicurezza e la gestione delle comunicazioni.
## Strato di sessione
>[!definition]
>>Fornisce uno spazio che viene utilizzato per aggregare i diversi flussi di trasporto che possono venire utilizzati come parti di un'unica applicazione.

>[!example]
>Può gestire un flusso audio e un flusso video combinati per far funzionare un'applicazione di teleconferenza
## Strato di presentazione
>[!definition]
>>Si occupa del formato dei dati scambiati tra le controparti.

>[!example]
>Si occupa di decidere se un numero intero venga rappresentato con 16, 32 o 64 bit e se il suo bit più significativo venga trasmesso per primo o per ultimo,  oppure di come venga codificato un flusso video.


## Strato di applicazione
>[!definition]
>>Tra i suoi protocolli troviamo il **File Transfer Protocol (FTP)** che definisce un protocollo mediante il quale le applicazioni di trasferimento file possono interoperare.

# Application Programming Interface

Quasi tutte le piattaforme di elaborazione realizzano i protocolli di rete come parte del proprio OS.

>[!definition]
>API di rete
>>Interfaccia resa disponibile dal OS con il proprio sottosistema di rete.


>[!tip] Supporto Universale a livello industriale
> Vantaggio di avere una singola API è che le applicazioni che ne fanno uso possono essere adattate in un diverso OS.

>[!warning]
>Due sistemi che forniscono la stessa API di rete non significa che il loro **file system**, i loro processi o le loro GUI siano compatibili.

>[!definition] 
>Implementazione:
>>responsabilità di creare una corrispondenza tra l'insieme concreto di operazioni e oggetti dell'API e l'insieme astratto di servizi definiti dal protocollo


## Socket:

>[!definition]
>>Interfaccia che dal punto di vista comunicativo una volta che un programma si attacca può comunicare con altri device, senza sapere cosa c'è sotto.

- La socket prende le informazioni dal livello 4 dello stack ISO/OSI (trasporto).
- Dopo la connessione con la socket, la connessione è bidirezionale.
- Le socket sono utilizzate anche per informazioni che non sono di rete, come le pipe in UNIX (PF_UNIX)(che non vanno in rete) mentre altre vanno in rete (PF_INET). 

### Creare un socket:
```
int socket(int domain, int type, int protocol)
```

+ **Domain**: indica famiglia di protocolli che si sta usando
	+ `PF_INET`: famiglia Internet
	+ `PF_UNIX`: strumenti di *pipe* di UNIX
	+ `PF_PACKET`: accesso diretto all'interfaccia di rete
+ **Type:** semantica di comunicazione
	+ `SOCK_STREAM`: flusso di byte
	+ `SOCK_DGRAM`: servizio orientato ai messaggi
+ **Protocol**:  identifica lo specifico protocollo che si vuole usare
	+ `UNSPEC`: identifica univocamente TCP

>[!definition]
>Handle
>>**Valore restituito** dal **socket** per il socket appena creato, cioè un identificativo che fa riferimento al socket.


### Client-server model with TCP:
#### Parte server:
- **`bind(int socket, struct sockaddr *address, int addr_len)`**: associa il socket ad un indirizzo (dell'entità locale) aperto che appartiene al server.
	- Viene usato con protocolli internet
	- `address`: struttura dati che contiene indirizzo IP e numero di porta TCP.
- **`listen()`**: definisce quante connessioni possono rimanere in sospeso
- **`accept()`**: si mette in attesa del cliente

#### Parte client:
**`connect(int socket, struct sockaddr *address, int addr_len)`**: per connettersi alla socket

+ non termina finché il protocollo TCP non ha stabilito con successo una connessione
+ **`address`**: indirizzo dell'entità remota coinvolta nella comunicazione
+ client specifica soltanto indirizzo del partecipante remoto
+ il sistema ha il compito di inserire le informazioni relative al partecipante locale
+ server rimane in attesa su una porta ben nota
+ al cliente non importa quale porta viene usata: l'OS ne seleziona una libera
##### Connessione stabilita:
- La socket apparirà come un mezzo tramite il quale mandare e ricevere dati (send(), recv()).
```
int send(int socket, char *message, int msg_len, int flags)
int recv(int socket, char *buffer, int buf_len, int flags)
```
+ `send()`: invia il messaggio tramite socket specificato
+ `recv()`: riceve all'interno del buffer un messaggio dal socket specificato
- Se il server è impegnato con un client non può avviare una connessione con un altro client.
- A me programmatore non me ne frega niente di dove sta fisicamente la socket, basta collegarsi ed usarla.

![client_server_model|100%](/materie/anno_2025-2026/reti_di_calcolatori/assets/client_server_model.svg)


# Performance

## Ampiezza di banda e latenza
>[!definition]
>Throughput (ampiezza di banda)
>>Numero di bit al secondo trasmessi nella comunicazione.

>[!example]
>Una rete ha un'ampiezza di banda di 10Mbps e questo significa che è in grado di consegnare 10 milioni di bit ogni secondo. Utile pensare l'ampiezza di banda in termini di tempo necessario per trasmettere un bit: in una rete a 10 Mbps servono 0.1 $\micro s$ per trasmettere ciascun bit.

>[!definition]
>Delay/latenza
>>Tempo tra l'invio del messaggio e il l'invio della risposta
RTT (round-trip-time): tempo tra l'invio del messaggio e il ricevimento della risposta

>[!example]
>Una rete transcontinentale potrebbe avere una latenza di 24 ms, ovvero un messaggio impiega 24ms per viaggiare da un capo all'altro del Nord America.

+ **Ritardo di propagazione:** dovuto alla velocità finita della luce
+ **Trasmissione:** tempo necessario per trasmettere un dato unitario che è in funzione: 
	+ dell'ampiezza di banda **throughput**
	+ dimensione del pacchetto in cui viaggia il dato
+ **Accodamento:** tempo speso in coda dentro switch, router (dipende dal tipo di percorso intrapreso)

Latenza = tempo di propagazione + tempo di trasmissione + tempo di coda
+ propagazione: distanza / velocità del segnale
+ trasmissione: grandezza del messaggio / throughput

>[!warning]
>Ogni host in cui passa il messaggio comporta un latency-time aggiuntivo che viene sommato a quello totale. La stima di delay è quindi un calcolo complicato e non sempre risulta corretto.

## Teoria del segnale

>[!definition]
>Bandwidth (larghezza di banda): 
>>**Ampiezza dell’intervallo di frequenze** occupate da un segnale o supportate da un canale. Si misura in **Hertz (Hz)** ed è una quantità **spettrale** (sulle frequenze).

>[!tip]
> Nella pratica informatica spesso “bandwidth” viene usato come sinonimo di throughput (“quanta banda hai?”), ma **in senso corretto** la bandwidth è **$f₂ − f₁$**, cioè la differenza tra la frequenza massima e minima **effettivamente presenti** (o ammesse) nel segnale/canale.

+ Sinusoide è definita da tre valori:
	+ **Ampiezza** $A$ [qualche unità di misura come volt, pascal, etc]
	+ **Frequenza** $f$ [Hertz = 1/s]
	+ **Fase** $\Phi$ [rad]

>[!definition]
>Formula della sinusoide
>>$\textrm{Sinusoid} x(t) = A\sin (2\pi ft+\Phi)$
>>Periodo $T=1/f$

### Fourier

Un segnale periodico “stazionario” si può scrivere come **somma di sinusoidi** a frequenze multiple della fondamentale:
$$
x(t)= \sum\_i A\_i \sin(2\pi f\_i t + \varphi\_i)
$$
Esempio classico: l’**onda quadra** non è una sinusoide pura; per approssimarla servono molte sinusoidi, in particolare le **armoniche dispari** (f, 3f, 5f, …). Più armoniche includi, più gli “spigoli” diventano netti.

+ Lo spettro $X(f)$ ti dice, per ogni frequenza $f$, **quanto** di quella sinusoide c'è (ampiezza e fase).
+ Se hai un solo tono a $g$, $X(g)$ è diverso da zero e altrove è zero
+ Per un segnale composto, $X(f)$ è diverso da zero su **molte** frequenze

>[!tip]
>La **bandwidth** ideale è l'intervallo tra la minima e la massima frequenza con **contributo non nullo**.

L'idea si generalizza anche ai segnali non periodici (con la trasformata di Fourier). Nella pratica si usa spesso una banda effettiva:
+ Esempio: fino al punto in cui l'**ampiezza** scende sotto una soglia (es. banda a -3 dB).

>[!question] Perché la bandwidth “conta” per la trasmissione di bit ?
> - Un **bit** nel tempo ha una certa **durata** $T\_{b}$. Se il bitrate è $R\_{b}$ bit/s, allora $T\_{b}=1/R\_{b}$.
> 	- 1 Mb/s $\rightarrow T\_{b}= 1\micro s$ per bit
> 	- 2 Mb/s $\rightarrow T\_{b}= 0.5\micro s$ per bit
> - **Bit più corti** = **transizioni più rapide** nel segnale.
> 	- Transizioni rapide richiedono **componenti ad alta frequenza** (più armoniche) $\rightarrow$ **spettro più largo** $\rightarrow$ **maggiore bandwidth necessaria**.
> - Se il **canale** limita le alte frequenze (bandwidth stretta), gli spigoli si "smussano":
> 	- gli impulsi si allargano nel tempo
> 	- si sovrappongono
> 	- bit difficili da distinguere $\rightarrow$ errori

- **Throughput alto** richiede **bit veloci**, quindi un segnale con variazioni rapide → serve **più bandwidth fisica** del canale.
    
- Ma **throughput ≠ bandwidth**: il throughput dipende anche da codifica, rumore, protocolli, ritrasmissioni, ecc. La bandwidth è un **vincolo fisico** che rende possibile (o limita) certe velocità.
## Delay vs throughput

>[!tip]
Ampiezza di banda e latenza definiscono le caratteristiche di prestazione di una linea di connessione ma la loro importanza relativa dipende dall'**applicazione**.

>[!tip]
È meglio un canale con una larghezza di banda maggiore piuttosto che una frequenza più alta, in quanto ad ampiezza di banda maggiore pompo più dati avendo più frequenze a disposizione, indipendentemente dalla frequenza (pompo di più a 5Ghz non perché la frequenza è a 5GHz, ma perché il canale è più largo generalmente).

### Applicazioni in cui predomina la latenza
>[!example]
>Client che invia messaggi di 1 byte ad un server che riceve messaggi di ritorno di 1 byte è vincolato alla latenza. Ipotizzando che per predisporre la risposta non sia necessaria nessuna elaborazione significativa, l'applicazione avrà prestazioni molto diverse su un canale intercontinentale con un **RTT di 100 ms** piuttosto che su un canale in una stanza con un **RTT di 1 ms**

Non è importante che il canale dell'esempio sia a 1 Mbps o 100 Mbps dato che il primo richiede per la trasmissione di 1 byte un tempo di trasmissione di $8\micro s$, mentre il secondo 0.08 $\micro s$.

### Applicazioni in cui predomina l'ampiezza
>[!example]
>Consideriamo un programma che realizzi una biblioteca digitale in cui si deve recupuerare un'immagine di 25 MB: maggiore è l'ampiezza di banda disponibile maggiore sarà la velocità con cui può fornire l'immagine all'utente. **L'ampiezza del canale domina le prestazioni.**
>Supponiamo che il canale abbia un'ampiezza di banda di 10 Mbps: ci vorranno 20 secondi per trasmettere l'immagine rendendo trascurabile il fatto che l'immagine si trovi all'altro capo di un canale con una latenza di 1 ms oppure di 100 ms, perché la differenza tra un tempo di risposta di 20.001 secondi e un tempo di 20.1 secondi non è percepibile dall'utente.

![[materie/anno_2025-2026/reti_di_calcolatori/assets/Immagine 2025-10-04 184058.jpg]]
## Prodotto ritardo x ampiezza di banda

Immaginiamo un canale fra una coppia di processi come ad una conduttura.
+ **Latenza**: lunghezza della conduttura
+ **Ampiezza di banda**: diametro
Il prodotto ritardo x ampiezza rappresenta il **volume**, cioè il **numero di bit** che può contenere.

+ Latenza (misurata come intervallo di tempo) = lunghezza conduttura
+ Si può calcolare quanti bit possono trovarsi all'interno della conduttura, in base all'ampiezza di ciascun bit.

![[materie/anno_2025-2026/reti_di_calcolatori/assets/Immagine 2025-10-05 170203.jpg]]

>[!example]
>Un canale intercontinentale con una latenza di sola andata di 50 ms ed un'ampiezza di banda di 45 Mbps è in grado di contenere
>$50\times 10^{-3}\textrm{secondi}\times 45\times 10^{6}\textrm{bit/secondo}=2.25\times 10^{6} bit$
>circa 280 KB di dati.

>[!warning]
>Importante conoscere
>ritardo x ampiezza di banda = numero di bit che possono essere inviati alla sorgente prima che il primo bit arrivi a destinazione.

>[!question] Se il mittente vuole che il destinatario gli segnali che i bit hanno iniziato ad arrivare ? 
> - bisogna attendere che un altro intervallo di tempo uguale alla latenza perché tale segnale si propaghi fino al mittente
> - il mittente può inviare una quantità di dati pari al doppio del **prodotto ritardo x ampiezza**
> - bit nella conduttura sono "in viaggio":
> 	- se il destinatario segnala di interrompere la trasmissione potrebbe ancora ricevere i dati = prodotto ritardo x ampiezza

>[!warning]
>Se il mittente non riempie la conduttura non sfrutta appieno la potenzialità della rete  

>[!tip]
>Alcune applicazioni sono in grado di dichiarare un limite superiore all'ampiezza di banda di cui hanno bisogno, **applicazioni video** un esempio tipico.

>[!example]
>Vogliamo creare un flusso video con immagini che siano grandi un quarto dell'immagine televisiva normale cioè 352 x 240 pixel.
>Ciascun pixel rappresentato da **24 bit**
>**Dimensione di ciascun frame video:** $(352\times 240 \times 24)/8= 247.5 \textrm{KB}$
>Se l'applicazione deve fornire i frame ad una velocità di 30 fps allora richiede un **throughput** di 75 Mbps.
>Anche se la rete potrebbe fornire un'ampiezza di banda maggiore questo non ha interesse per l'applicazione perché non ha così tanti dati da trasmettere in un dato intervallo di tempo. 

+ Differenza tra due frame consecutivi è spesso minima
+ possibile comprimere il flusso di immagini trasmettendo soltanto le differenze tra frame adiacenti
+ flusso video compresso non viaggia a velocità costante
+ flusso varia nel tempo a causa di vari fattori

Da questi punti si può dire quale sia l'**ampiezza di banda media richiesta**.

>[!warning]
>Intervallo di tempo nel quale viene calcolata la media.

>[!example]
>Supponiamo che l'applicazione video usata prima possa essere compressa fino al punto di richiedere in media 2 Mbps.
>  - se trasmette 1 Mb in 1 secondo
>  - 3 Mb nel successivo intervallo di 1 secondo
>  - allora nell'intervallo di 2 secondi sta trasmettendo alla velocità media di 2 Mbps
>Informazione poco utile per un canale progettato per una velocità $\leq$ 2 Mb in un secondo 
>

Non è possibile valutare un limite superiore per la grandezza dei *burst* di trasmissione di un'applicazione.

>[!definition]
> Burst
>> Velocità di picco che viene mantenuta per un certo intervallo di tempo;
>> Il numero di byte che vengono inviati alla velocità di picco prima di tornare alla velocità media o ad una inferiore.


>[!tip]
>Se la velocità di picco $>$ capacità del canale: dati in eccesso devono essere memorizzati per essere trasmessi più tardi.
>Sapendo quale possa essere la dimensione del burst: si può usare dei **buffer** di capacità sufficiente per contenere i burst.

>[!warning]
>Anche la richiesta di ritardo di un'applicazione può essere formulata in modo più complesso del semplice "il ritardo minore possibile".
>Nel caso del ritsrdo non importa che la latenza di andata sia 100 ms o 500 ms. 
>È importante quanto la latenza **varia** da pacchetto a pacchetto.

>[!definition]
>Jitter
>>Corrisponde alla varianza di delay (veloce poi lento poi veloce poi lento vaffanculo)

>[!example]
>Se un film inizia dopo ma poi il ritardo resta costante il film si gode liscio nonostante cominci dopo. Se invece all'inizio va bene poi deve caricare e poi riparte e cosi via rompe i coglioni come netflix di merda.

>[!example]
>La sorgente invia un pacchetto ogni 33 ms (applicazione video che trasmette 30 fps).
>Se i pacchetti arrivano a destinazione con un ritardo reciproco di 33 ms, possiamo dedurre che il ritardo subito da ciascun pacchetto nella rete è esattamente lo stesso. 
>Se il tempo che intercorre tra l'arrivo a destinazione di due pacchetti è **variabile**: 
>- il ritardo subito dalla sequenza di pacchetti è variabile
>- la rete ha introdotto **jitter** nel flusso di pacchetti.

>[!tip]
>Una tale variabilità non viene introdotta in un'unica connessione fisica, ma si può verificare quando i **pacchetti subiscono ritardi di accodamento** diversi in una rete a commutazione di pacchetto.

### Per capire il jitter
>[!example]
>Supponiamo che i pacchetti trasmessi sulla rete contengano frame video e che per visualizzarli il ricevente abbia bisogno di ricevere un nuovo frame ogni 33 ms.
>Se un frame arriva in anticipo può essere memorizzato dal ricevente finché non viene visualizzato.
>Quando un frame arriva in ritardo il ricevente:
> - non ha il frame che gli serve per aggiornare in tempo lo schermo
> - la qualità del video ne soffre
> - video non fluido

>[!tip]
>Non è necessario **eliminare** il jitter ma basta sapere **quanto vale**.

Se il ricevente conosce il limite superiore e inferiore della latenza che può caratterizzare un pacchetto può **ritardare** il momento in cui inizia la riproduzione video (in cui visualizza il primo frame) per un tempo abbastanza lungo da essere certo in futuro di avere un frame da visualizzare quando serve.

>[!tip]
Il ricevente ritarda il frame, eliminando il problema del jitter, memorizzandolo in un buffer.




