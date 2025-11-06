---
title: "Capitolo 3"
aliases: ["Capitolo 3"]
tags: [università, "materie", "anno-2025-2026", "reti-di-calcolatori", "capitolo-3"]
created: 2025-10-23
---
# Commutazione e inoltro
## Switch
>[!definition]
>>Dispositivo che permette di collegare diversi spezzoni di rete locale per formare una rete più grande

+ quando i collegamenti sono omogenei
	+ indirizzi che si usano in Wi-Fi e Ethernet sono tutti "uguali"
+ ha conoscenze delle **posizioni dei vari dispositivi**
+ riceve pacchetti sulle interfacce e le inoltra sulle altre interfacce in maniera **intelligente**
+ **store and forward**
	+ decodifica il frame ma non rimanda il frame su tutte le interfacce
	+ ha delle tabelle che gli permettono di decidere su che interfaccia specifica inoltrare il pacchetto
	+ lo forwarda sul link scelto

## Topologia a stella
+ dispositivo centrale è lo switch
+ attorno ci sono degli host collegati allo switch
+ non abbiamo più problemi di collisione
+ pacchetti possono perdersi se lo switch dovesse andare in **congestione**
+ non c'è condivisione di mezzo vero e proprio

### Proprietà
+ Anche se switch ha un numero prefissato di ingressi/uscite che **limita il numero di host** che possono essere connessi si possono costruire **grandi reti** interconnettendo un certo numero di switch
+ usando linee punto-punto possiamo connettere uno switch ad un altro switch oppure host per realizzare **reti ad ampia estensione geografica**
+ aggiunta di nuovo host collegandolo ad uno switch non implica necessariamente che gli host precedentemente connessi osserveranno una **diminuzione di prestazioni**
>[!tip]
>Garantire un elevato throughput aggregato è uno degli obiettivi della progettazione di uno switch.
 
+ switch possono essere scalati: li trovi con vari quantità di porte
+ latenza aumenta per via della distanza tra i dispositivi
+ switch combinati

Livello 3 andiamo a risolvere i problemi di interconnessione tra reti generiche.

+ modulare, economica
+ performance non dipendono dal numero di host collegati ma dalle capacità interne del **processore**

>[!question] Come fa il commutatore a decidere quale porta di uscita utilizzare per inviare il pacchetto?
>Si cerca nell'intestazione del pacchetto un **identificatore** da usare per prendere la decisione.

### Modalità di utilizzo dell'dentificatore
+ **Datagramma** (connectionless approach)
+ **Virtual circuit** (Connection-oiented)
+ **Source routing**

>[!tip]
Ogni host ha un indirizzo **univoco**:
> - level 2: MAC address
> - level 3: IP address

### Connectionless
>[!definition]
>>Ciascun pacchetto deve contenere **informazioni sufficienti** per consentire a qualsiasi switch di decidere come fargli raggiungere la propria destinazione.
>>Ogni pacchetto contiene l'indirizzo di destinazione completo.
+ non hanno una memoria gli switch
+ ogni pacchetto è a se
+ si fa tutto  in base alle informazioni che reca il pacchetto 
>[!example]
>![[materie/anno_2025-2026/reti_di_calcolatori/assets/connectionless.jpg]]
>- Nella rete seguente gli host hanno indirizzi A, B, C
>- Per decidere come inoltrare un pacchetto:
>	- switch consulta una **tabella di inoltro**:
>	- la tabella mostra le **informazioni di inoltro**
>	- consente allo **switch 2** di inoltrare i datagrammi nella rete dell'esempio

| Dest. | Port |
| ----- | ---- |
| A     | 3    |
| B     | 0    |
| C     | 3    |
| D     | 3    |
| E     | 2    |
| F     | 1    |
| G     | 0    |
| H     | 0    |

+ nessuno switch ha la visione completa della rete
+ non si è ancora stabilizzata la configurazione quindi può perdere pacchetti
+ tabelle possono essere programmate a mano dall'admin di rete
+ algoritmi di apprendimento delle posizioni per compilare le tabelle
#### Caratteristiche delle reti datagram
+ host può inviare un pacchetto ovunque in ogni momento
	+ ogni pacchetto in ingresso ad uno switch può venire **inoltrato immediatamente**
>[!warning]
>Questo contrasta con il comportamento delle reti **orientate alla connessione**.
>Perché è richiesto lo stabilirsi di uno **stato di connessione** prima di inviare il primo pacchetto di dati.

+ quando un host invia un pacchetto:
	+ non ha modo di sapere se la rete sia **in grado di consegnarlo**
	+ non sa se l'host destinazione **sia operativo**
+ ciascun pacchetto è inoltrato in modo **indipendente** dai pacchetti precedenti
	+ due pacchetti consecutivi inviati dall'host A all'host B possono seguire due **percorsi diversi**
+ **malfunzionamento** di uno switch o una linea di connessione potrebbe non avere seri effetti sulle comunicazioni nella rete
	+ nel caso si trova un percorso alternativo 
	+ e si aggiorna la tabella di inoltro
### Virtual circuit
>[!definition]
>>Prima di inviare i dati deve essere instaurata una connessione virtuale fra host sorgente e host destinatario.

![[materie/anno_2025-2026/reti_di_calcolatori/assets/connection_oriented.jpg]]
+ se A e B vogliono comunicare
+ suddividiamo in due parti:
#### **Connection setup**:
+ stabilire una connessione in ciascuno degli switch intermedi
	+ lo stato di connessione = informazione inserita nella **tabella dei VC** di ciascuno switch
	+ questa informazione contiene:
		+ **identificatore del circuito virtuale**: identifica univocamente la connessione (trasmesso nell'intestazione dei pacchetti)
		+ interfaccia di ingresso  attraverso cui i pacchetti della VC arrivano allo switch
		+ interfaccia di uscita attraverso cui i pacchetti della VC escono dallo switch
		+ un **VCI** usato per i pacchetti uscenti
	+ quando dobbiamo mettere un frame nell'intestazione non viene messo l'indirizzo del destinatario ma il **numero del circuito virtuale** 
	+ L'indirizzo degli host non viene usato durante la comunicazione ma **solo per creare il circuito**
>[!tip]
>- I valori di ingresso e di uscita **non sono uguali**
>- per cui il valore VCI **non è univoco** per la connessione
>- ha significato solo su una certa linea di connessione
>- **visibilità localizzata alla linea**

##### Metodi per stabilire lo stato di connessione
>[!definition]
>Permanente PVC:
>+ Amministratore di rete configurerà lo stato
>+ può anche eliminarlo

>[!definition]
>SVC (Switched virtual circuit)
>>Circuiti virtuali che nascono quando un host invia nella rete messaggi per instaurare lo stato di connessione.

>[!tip]
>Un host può stabilire ed eliminare dinamicamente senza intervento dell'amministratore di rete.

>[!example]
>![[materie/anno_2025-2026/reti_di_calcolatori/assets/connection_oriented.jpg]]
>Amministratore di rete vuole creare manualmente una VC da A a B
>- deve identificare un percorso da A a B (nella figura esiste un solo percorso)
>- sceglie per ciascuna linea un valore VCI
>	- viene scelto VCI = 5 per la linea da A allo Switch1
>	- valore VCI = 11 da Switch1 a Switch2
>	- nella tabella deve essere presente questa linea
>	- ![[materie/anno_2025-2026/reti_di_calcolatori/assets/tabella_VCI_example.jpg]]
>	- il valore VCI **uscente** in uno switch è **uguale** al valore **entrante** nello **switch successivo**

#### Trasferimento dati

![[materie/anno_2025-2026/reti_di_calcolatori/assets/trasferimento_dati_VC.jpg]]

+ se A vuole inviare un pacchetto all'host B inserisce valore di VCI = 5 nell'intestazione
+ lo invia allo Switch 1
	+ lo riceve sull'interfaccia 2
	+ combina il numero dell'interfaccia e il valore di VCI nell'intestazione per controllare nella tabella dei VC
	+ inoltra il pacchetto sull'interfaccia 1 inserendo VCI = 11
+ pacchetto arriva a Switch 2
	+ cerca interfaccia 3 e VCI = 11
	+ invia il pacchetto verso Switch 3 aggiornando valore VCI nell'intestazione
+ via fino a B

+ host A invia messaggio di configurazione allo Switch 1
	+ in questo messaggio è contenuto **indirizzo di destinazione** di B
	+ che deve essere raggiunto per creare lo stato di connessione in tutti gli **switch intermedi**
+ Switch 1 riceve richiesta di connessione
	+ la invia allo Switch 2
	+ crea una nuova riga di informazioni nella sua **tabella VC**
	+ assegna un valore **VCI** che non sia usato su quell'interfaccia (VCI = 5)
	+ tradotto "quando arriva sulla porta 2 un frame con identificatore 5 invialo sulla porta 1"
+ cosi via si ripete fino all'host B
+ per completare la connessione
	+ B invia una conferma della connessione allo Switch 3 (VCI = 4)
	+ Switch 3 aggiorna la propria tabella con questa informazione
	+ e viene trasmessa l'informazione all'indietro fino all'host A
+ ora tutti hanno le informazioni per far fluire il traffico da A a B
+ quando A non vuole più inviare a B chiude la connessione
	+ invia allo Switch 1 un messaggio di chiusura e lo switch elimina dalla tabella la riga corrispondente 
	+ uguale per gli altri switch

##### Caratteristiche del VC
+ dato che host A deve **attendere** che la richiesta di connessione arrivi dall'altra parte della rete e torni indietro: **c'è un ritardo almeno uguale a RTT**
+ Rispetto al modello datagram **il valore di overhead dell'intestazione** in ciascun pacchetto è ridotto perché ciascun pacchetto dati contiene solo **un piccolo identificatore univoco** solo su una linea
+ In caso di **malfunzionamento**:
	+ **interrompere** la connessione e instaurarne una **nuova**
	+ **chiudere** quella vecchia per liberare **spazio di memorizzazione** nelle tabelle degli switch
>[!question] Come fa uno switch a decidere verso quale linea inoltrare la richiesta di connessione ?
>**Algoritmi di instradamento**

#### Vantaggi
+ intestazione nei pacchetti molto più bassa
+ posso verificare che le proprietà che scelgo siano garantite
+ quando l'host riceve il permesso di trasferire i dati **conosce già abbastanza com'è fatta la rete**
	+ sa che c'è veramente un percorso verso il ricevitore ed è pronto per ricevere i dati
+ si può **assegnare risorse** al circuito virtuale al momento della connessione:
	+ una rete X.25 buffer sono assegnati a ciascun VC quando è inizializzato e il circuito può essere rifiutato da un nodo se non ha abbastanza buffer **disponibili**
#### Svantaggi
+ sensibili ai guasti
+ si deve rifare il circuito

#### Datagram VS Virtual Circuit

+ Datagram:
	+ non ha fase di instaurazione connessione
	+ ogni switch elabora ogni pacchetto in modo **indipendente**
	+ ogni pacchetto in arrivo **compete con tutti gli altri** per lo spazio all'interno del buffer
	+ se non c'è spazio il pacchetto in arrivo viene **eliminato**
+ VC:
	+ fornire a ciascun circuito una diversa **qualità di servizio** (QoS)
	+ rete fornisce qualche **forma di garanzia** relativa alle prestazioni
		+ switch riservano risorse necessarie per soddisfare la garanzia
			+ switch attraversati da un circuito virtuale potrebbero assegnargli una **percentuale dell'ampiezza di banda** delle linee uscenti
			+ potrebbero stabilire una certa tolleranza del **delay**

### Source routing
>[!definition]
>>L'host sorgente fornisce **tutte le informazioni** relative alla topologia della rete necessarie per inoltrare un pacchetto all'interno della rete.

#### Implementazione
+ **Assegnare un numero** a ciascuna uscita di ciascuno switch:
	+ inserirlo nell'intestazione del pacchetto
![source_routing](/materie/anno_2025-2026/reti_di_calcolatori/assets/source_routing.svg)
>[!tip] Dato che ci sono più switch lungo il percorso:
>intestazione deve contenere informazioni per permettere a **ciascun switch** di determinare la giusta uscita.

+ inserire nell'intestazione **elenco ordinato di numeri di porta**
+ far ruotare l'elenco in modo che il successivo switch lungo il percorso sia sempre il primo
![[materie/anno_2025-2026/reti_di_calcolatori/assets/source_routing_example.jpg]]

+ host A deve avere conoscenze sufficienti relative alla topologia della rete per comporre l'intestazione
+ **dimensione variabile** dell'intestazione: dipende da quanti switch ci sono

# Bridges e LAN Switches

>[!definition]
>>Categoria di commutatori usata per inoltrare pacchetti fra reti locali a mezzo fisico condiviso.

>[!example]
>Vogliamo interconnettere due reti Ethernet:
>1. Ripetitore: non funzionerebbe se si eccedessero i limiti fisici di Ethernet
>2. Bridge: inoltra i frame da una rete all'altra
>	- opererebbe in **modalità promiscua**
>	- accetta tutti i frame trasmessi su **entrambe le reti** in modo da inoltrarli

>[!definition]
> Flooding
>>I bridge accettano i frame delle reti locali che arrivano ai propri ingressi e li inoltrano verso tutte le uscite.


## Bridge ad apprendimento (learning bridge)

>[!warning]
>Non c'è bisogno che il bridge inoltri tutti i frame che riceve.

Ogni frame può essere inoltrato solo **al relativo host**.

![[materie/anno_2025-2026/reti_di_calcolatori/assets/learning_bridge.jpg]]
+ ogni volta che un frame da A indirizzato a B arriva sulla porta 1
+ non serve che il bridge lo inoltri sulla porta 2

>[!question] Come può un bridge apprendere su quale porta risiedono i vari host ?
> Caricare una tabelle di inoltro nel bridge.

| Host | Port |
| ---- | ---- |
| A    | 1    |
| B    | 1    |
| C    | 1    |
| X    | 2    |
| Y    | 2    |
| Z    | 2    |

+ se A deve spedire un frame a B
+ il bridge non lo inoltra sulla porta 2 perché A e B sono nella stessa rete locale

#### Ricavare la tabella automaticamente
>[!tip]
>Ogni bridge ispeziona anche **l'indirizzo sorgente** di tutti i frame che riceve.

+ l'host A invia un frame a un host su qualsiasi lato del bridge
+ bridge memorizza l'host mittente e da quale porta proviene ovvero la 1
+ a ciascuna info nella tabella è associato un temporizzatore:
	+ scaduto quello il bridge elimina l'info
	+ per gestire spostamento di un host da una rete all'altra
>[!warning]
>Se il bridge riceve un frame indirizzato ad un host che non è presente nella tabella, il frame viene inoltrato verso tutte le porte di uscita.

+ se bridge riceve un frame con indirizzo:
	+ **Broadcast**: lo inoltra su tutte le porte a parte quella di provenienza
	+ **Multicast**: 
		 1. come il broadcast ma lascia decidere agli host se siano interessati o meno
			+ può generare **traffico** sulle interfacce
		2. Impara quando non ci sono membri del gruppo associati alla porta
## Spanning Tree Algorithm

>[!warning]
>Strategia precedente funziona bene solo se non ci sono **loop** nella rete locale.

![[materie/anno_2025-2026/reti_di_calcolatori/assets/lan_loop.jpg]]

>[!question] Com'è possibile che una rete abbia un loop ?
>1. Un bridge che chiude ad anello potrebbe essere stato aggiunto inconsapevolmente
>2. Anelli sono inseriti di proposito per garantire **ridondanza** in caso di guasto

+ Immaginare la LAN estesa come un grafo che possa avere dei cicli
>[!definition]
>Spanning Tree
>>Sottografo di tale grafo che ne copre tutti i vertici senza avere cicli.

### Idea principale
+ Sono i bridge a scegliere le porte verso le quali inoltreranno i frame:
	+ ciascun bridge ha un **identificatore univoco**
	+ viene nominata la **radice** (bridge con ID più basso)
	+ bridge radice inoltre sempre su tutte le porte
	+ ciascun bridge calcola il **percorso più breve verso la radice** e prende nota di tali porte
	+ viene selezionata una porta come percorso preferito dal bridge
	+ tutti i bridge connessi ad una LAN nominano un unico bridge **designato**:
		+ lui inoltrerà i frame verso la radice
		+ è quello **più prossimo alla radice**
>[!tip]
>Dato che ogni Bridge è connesso a più di una LAN:
>- partecipa alla nomina del bridge designato in ogni LAN di cui fa parte
>- ciascun bridge decide se essere o meno il bridge designato
>- inoltra il frame solo verso le porte per le quali è il bridge designato.

### Messaggi di configurazione
>[!definition]
>BPDU
>>I bridge devono scambiarsi messaggi di configurazione per decidere sono la radice o bridge designato per una certa rete.

BPDU contendono tre informazioni (X,d,Y)
- Y: identificatore del bridge che invia il messaggio
- X: identificatore del bridge radice secondo Y
- d: distanza misurata in **hop** (segmenti), fra il bridge radice e il bridge che invia il messaggio
#### Y
- ID del bridge = indirizzo MAC + 16-bit (primi 4 sono la priorità, gli altri indicano la VLAN)
- Priorità di default è 32769 = 1000 000000000001
- può essere cambiato dall'admin se volesse che un bridge specifico diventi la radice

- all'inizio ciascun bridge pensa di essere la radice
	- invia un messaggio di configurazione su ciascuna delle sue porte (X, 0, Y)
	- identificandosi come radice (segnando distanza pari a 0 da essa)
- bridge verifica che il BPDU ricevuto sia migliore di quello memorizzato come migliore per quella porta
	- viene considerato migliore se:
		- identifica una radice con un **identificatore minore**
		- identifica una radice con lo **stesso ID ma con distanza minore**
		- l'ID della radice e la distanza dalla radice sono uguali ma il bridge che ha inviato il messaggio ha identificatore minore
- se è migliore il bridge:
	- aggiunge 1 al campo **d** 
	- **elimina** la vecchia informazione e **memorizza** quella nuova

#### Quando un bridge riceve un BPDU da cui deduce di non essere la radice:
+ aggiunge 1 al campo distanza dalla radice
+ **smette** di generare **propri messaggi** di configurazione
+ inoltra solo quelli **ricevuti da altri**
#### Quando un bridge riceve un BPDU che indica che non è il bridge designato:
>[!example]
>Messaggio proviene da:
>- bridge più vicino alla radice
>- oppure con stessa distanza ma ID minore
+ smette di inviare messaggi di configurazione da quella porta
#### Sistema stabilizzato
- soltanto il **bridge radice** che continua a generare messaggi di configurazione
- resto dei bridge inoltrano messaggi solo verso le porte dei bridge **designati**
#### Esempio

![[materie/anno_2025-2026/reti_di_calcolatori/assets/spanning_tree_ex.jpg]]
- è appena tornata l'alimentazione nell'edificio che ospita la rete
- tutti i bridge dichiarano di essere la radice
- consideriamo dal nodo **B3**
- B3 riceve (B2, 0, B2)
- poiché 2 < 3 ----> B3 accetta come radice B2
- B3 aggiunge 1 alla distanza da B2 (0)
	- invia (B2, 1, B3) verso B5
- B2 accetta B1 come radice
	- invia (B1, 1, B2) a B3
- B5 accetta B1 come radice
	- invia (B1, 1, B5) verso B3
- B3 accetta B1 come radice
	- nota che B2 e B5 sono più vicini alla radice
	- B3 smette di inoltrare messaggi verso entrambe le proprie interfacce
	- B3 lascia le due porte **non selezionate**
![[materie/anno_2025-2026/reti_di_calcolatori/assets/spanning_tree_ex_2.jpg]]
#### Dopo la stabilizzazione
- Bridge continua ad **inviare periodicamente** messaggi di configurazione
- Gli altri continuano ad inoltrare tali messaggi come prima

#### Guasto
Se un bridge dovesse guastarsi:
- bridge a valle non riceverebbero più messaggi di config
- ripartirebbero per ristabilire chi è la radice e tutto il resto

#### Limitazione
>[!warning]
>- L'algoritmo è in grado di riconfigurare lo spanning tree in caso di guasto
>- Non è in grado di inoltrare frame lungo percorsi alternativi per aggirare il guasto

### Limiti dei bridge

**Non scalano bene**
- Gli algoritmi di spanning tree non scalano: hanno **complessità lineare** e **non sfruttano una struttura gerarchica**.
- Il **broadcast non scala**: genera **troppo traffico** su reti di grandi dimensioni (e in realtà non è nemmeno sempre necessario).

**Non supportano l’eterogeneità**
- Tutte le parti della rete devono usare lo **stesso tipo di indirizzo** e avere **caratteristiche simili** (ad esempio il supporto al broadcast).
- Ma cosa succede se due segmenti della rete ammettono diverse **MTU (Maximum Transmission Unit)**?
    - Ad esempio: Ethernet (802.3) → 1500 byte; WiFi (802.11) → 2346 byte.
    - In una direzione, il bridge deve frammentare un frame in due o più frame, che devono poi essere ricomposti al livello datalink dal ricevitore (frammentazione PAF).

# Interconnessione

>[!definition]
>>Gli utenti di una rete di un certo tipo vogliono essere in grado di comunicare con utenti di reti diverse.

- Costruire una rete interconnessa **eterogenea** e **scalabile**

![[materie/anno_2025-2026/reti_di_calcolatori/assets/protocolli_interconnessione.jpg]]
*Schema di un internetwork, con gli strati di protocolli usati per connettere H1 a H8*
## TCP/IP stack

>[!tip] Strato IP
>Inoltra anche i **pacchetti**.

Datagramma può arrivare all'IP in due modi:
- quando uno strato superiore (TCP o UDP) richiede di spedire dati a un altro host:
	1. payload **incapsulato** in un datagramma IP
	2. datagramma è spedito al prossimo nodo usando un appropriato protocollo datalink
	- un'applicazione può mandare/trasmettere dati attraverso un'interfaccia sottostante senza saperlo
- Un pacchetto è ricevuto da un livello inferiore
	- **indirizzato all'host locale**: l'intestazione IP è rimossa e il payload consegnato allo strato di trasporto
	- **indirizzato a un altro host**: può essere inoltrato usando un'interfaccia
		- usando uno strato inferiore 
## Router
>[!definition]
>> È un host con molte interfacce dalle quali il relativo strato IP inoltra pacchetti da un'interfaccia all'altra.

- operano con strategia **store-and-forward** ma in maniera diversa rispetto agli switch
	- ogni link può usare diverse tecnologie
	- IP datagramma è incapsulato/decapsulato e incapsulato ancora
	- L'inoltro è deciso tramite l'indirizzo IP

## Modello del servizio IP

>[!warning] Problema principale nella definizione di modello di servizio per una internetworking
>Si può fornire un certo servizio tra host solo se tale servizio può essere fornito a tutte le sottostanti reti fisiche.

>[!tip] Definizione del modello IP
>Renderlo **poco esigente** in modo che **qualsiasi** tecnologia di rete all'interno di una internetworking sia in grado di fornire il servizio necessario.

IP diviso in due parti:
- **schema di indirizzamento**: fornisce il modo di identificare tutti gli host nella rete interconnessa
- **modello datagram**: per la consegna dei dati

>[!tip] Modello **best effort**
>IP non fornisce alcuna garanzia sulla consegna dei datagrammi.

I pacchetti possono essere:
- smarriti
- consegnati nell'ordine sbagliato
- un pacchetto può essere consegnato più volte

Schema di **indirizzamento globale**:
+ prevede un modo per identificare tutti gli host nell'internetwork
+ astrae dagli indirizzi (MAC) del livello 2 sottostante

## Formato del pacchetto

| Campo                                             | Lunghezza      | Scopo                                                                                                                                               |
| ------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| HLen                                              | 32 bit         | lunghezza dell'intestazione                                                                                                                         |
| TOS (type of service)                             | 8 bit          | consente il trattamento differenziato dei pacchetti in base alle **necessità** delle applicazioni                                                   |
| Length                                            | 16 bit         | lunghezza del datagramma                                                                                                                            |
| Ident                                             | 16 bit         | usata dalla frammentazione                                                                                                                          |
| Flags + Offset                                    | 3 bit + 13 bit | usata dalla frammentazione e ricostruzione<br>- Flag bit 0: deve essere 0<br>- Flag bit 1: Non frammentare (DF)<br>- Flag bit 2: Più frammenti (MF) |
| TTL (time to live)                                | 8 bit          | catturare quei pacchetti che continuano a viaggiare nei cicli ed eliminarli                                                                         |
| Protocol                                          | 8 bit          | chiave per **demultiplexing**: identifica il protocollo di livello superiore a cui va consegnato il pacchetto                                       |
| Checksum                                          | 16 bit         | algoritmo per il controllo di integrità del pacchetto                                                                                               |
| - Indirizzo mittente <br>- indirizzo destinazione | 32 bit a testa |                                                                                                                                                     |
### TOS
- Priorità in caso di congestione:
	- in congestione i pacchetti con **precedence** più alta vengono serviti prima (o scartati per ultimi)
	- di solito i **datagrammi di controllo di rete** hanno la precedenza massima per mantenere la rete stabile

| Bit | Codice | Significato                 | Cosa fa un router                               |
| --- | ------ | --------------------------- | ----------------------------------------------- |
| /   | 0000   | servizio normale (default)  |                                                 |
| D   | 1000   | Minimizzare il delay        | Code brevi/veloci, link a bassa latenza         |
| T   | 0100   | Massimizzare il throughput  | Link ad alta capacità                           |
| R   | 0010   | Massimizzare l'affidabilità | Evitare link lossy/instabili                    |
| C   | 0001   | Minimizzare il costo        | Usare percorsi più economici anche se più lenti |

### DSCP
Oggi i campi del TOS sono stati rimpiazzati da **DSCP/ECN** (DiffServ), ma il significato concettuale è lo stesso: la rete può fare scelte diverse di instradamento/accodamento a seconda di ciò che l’applicazione chiede.

>[!definition]
>>L'host marca i pacchetti con un **codepoint** (DSCP) e i router applicano un certo **PHB** (Per-Hop Behavior): code a priorità, limiti di banda, ecc...

- se i **3 bit meno significativi del DSCP** sono 000 (xxx000):
	- i 3 bit più alti (xxx) sono interpretati come nel TOS
- se i **3 bit meno significativi del DSCP** sono diversi da 0:
	- i **6 bit più a sinistra** definiscono 64 servizi:
		- xxxxx0: servizio standard IETF
		- xxxx11: servizi definiti dalle autorità locali
		- xxxx01: uso temporaneo
## Frammentazione e ricostruzione

>[!warning]
>Ogni tecnologia di rete ha una propria opinione relativamente a quella che deve essere la **dimensione** di un pacchetto.

>[!definition]
>MTU unità massima trasmissibile
>>Il più grande datagramma IP che può trasportare all'interno di un proprio frame.

- un host può scegliere la dimensione che preferisce
- il valore di **MTU** della rete è un scelta ragionevole
- la frammentazione sarà necessaria solo se il percorso verso la destinazione attraversa una rete con un valore di **MTU inferiore**
- se il protocollo di trasporto fornisce al protocollo IP un frame di dimensione maggiore al MTU allora l'host lo **frammenta**

| Network/protocol | MTU (bytes) |
| ---------------- | ----------- |
| Hyperchannel     | 65535       |
| Token Ring       | 17914       |
| FDDI             | 4352        |
| WiFi             | 2346        |
| Ethernet         | 1500        |
| X.25             | 576         |
| PPP              | Negotiated  |

>[!question] Cosa dovrebbe fare un router se dovesse inoltrare un datagramma di dimensione maggiore all'MTU ?
>- Se il Flag *Non frammentare* (DF) è 1: elimina il datagramma e notifica il mittente (con un ICMP)
>	- forse il mittente può ridurre la dimensione
>- Se DF = 0 il router può procedere con la **frammentazione**

>[!tip]
>Tipicamente la frammentazione avviene in un **router** quando riceve un datagramma da inoltrare verso una rete con MTU inferiore alla dimensione del datagramma.

- per far ricostruire i frammenti dall'host ricevente
- frammenti devono avere tutti lo **stesso identificatore** nel campo *Ident*
	- scelto dall'host sorgente
	- univoco fra tutti i datagrammi
- host ricevente riconosce quei frammenti e li assembla 
	- se manca qualcuno abbandona il processo ed **elimina** i frammenti arrivati
>[!warning]
>Protocollo IP non tenta di recuperare i frammenti mancanti.

### Dimensione di ogni frammento
La dimensione di ogni frammento è scelta dal router in modo che **header+payload $\leq$ MTU**.
- La dimensione del payload è il più grande multiplo di 8 più **piccolo di MTU - lunghezza dell'header**
>[!example]
>- MTU = 536
>- Header = 20 byte
>Allora 536 - 20 = 516 e il multiplo più grande di 8 minore di 516 è 512
>Quindi ogni pacchetto è lungo 512 + 20 byte
### Ricostruzione
- Host ricevente esegue la ricostruzione:
	- arriva un frammento con un nuovo identificatore
	- viene allocato un **buffer** associato a quell'identificatore
	- ogni **payload** di questi frammenti è allocato nel buffer in base al suo **offset**
		- se un frammento arriva due volte, l'ultimo sovrascrive il precedente
	- Arrivati tutti i frammenti
	- Buffer contente il payload ricostruito è passato al livello superiore
### Esempio di frammentazione
- (a) Pacchetto non frammentato
![[materie/anno_2025-2026/reti_di_calcolatori/assets/pacchetto_non_frammentato.jpg]]

- (b) pacchetto frammentato
![[materie/anno_2025-2026/reti_di_calcolatori/assets/pacchetto_frammentato.jpg]]
>[!tip]
>Notare che:
>- offset = offset reale / 8 (64 = 512 / 8)
>- quindi in ogni frammento (tranne l'ultimo) la lunghezza del payload è multiplo di 8

## Indirizzi globali
- Non devono esistere due host con lo stesso indirizzo
- indirizzi IP sono **gerarchici**
	- Prima parte: identifica la rete
	- Seconda parte: identifica l'host all'interno della propria rete
### Classi degli indirizzi
#### Classe A
- indirizzo inizia con **0**
- i **7 bit** successivi identificano la **rete**
- rimangono **24 bit** che sono il **numero di host** nella rete
![ip_classe_a|100%](/materie/anno_2025-2026/reti_di_calcolatori/assets/ip_classe_a.svg)
##### Numero di host
$2^{7}$ = 128 reti possibili
##### Numero di host
$2^{24}-2$ = 16777214
#### Classe B
- indirizzo inizia con **10**
- i successivi **14 bit** identificano la rete
- restanti **16 bit** sono il numero di host nella rete
![ip_classe_b|100%](/materie/anno_2025-2026/reti_di_calcolatori/assets/ip_classe_b.svg)
##### Numero di host
$2^{14}$ = 16384 reti possibili
##### Numero di host
$2^{16}-2$ = 65534
#### Classe C
- indirizzo inizia con **110**
- successivi **21 bit** identificano la rete
- restanti **8 bit** identificano il numero di host nella rete
![ip_classe_c|100%](/materie/anno_2025-2026/reti_di_calcolatori/assets/ip_classe_c.svg)
##### Numero di host
$2^{21}$ = 2097152 reti possibili
##### Numero di host
$2^{8}-2$ = 254
#### Altri indirizzi
- Indirizzo che inizia con **111** non sono usati per indirizzare gli host
- Classe D (1110) è per il **multicast**
- Classe E (1111) non è usata

>[!question] Perché per contare gli host si escludono 2 indirizzi ?
>1. Tutti 0 nella parte dell'host 158.110.0.0 identifica la **rete**
>2. Tutti 1 nella parte dell'host 158.110.255.255 è usato per il **broadcast** della rete

## Inoltro di datagrammi IP

Non può basarsi su indirizzo di destinazione come negli switch nel livello 2.
- Troppi indirizzi (nell'ordine di $10^{9}$)
- Tabelle richiederebbero **troppa memoria**, troppo lento

Inoltrare tramite la **rete di destinazione** ovvero la rete a cui appartiene l'indirizzo di destinazione

Tabelle di inoltro mappano il numero della rete fino al prossimo nodo

### Strategia adottata

- ogni datagramma contiene l'indirizzo di destinazione da cui si può risalire all'**indirizzo di rete di destinazione**
- un nodo verifica se il destinatario è connesso alla propria rete
	- nel caso **inoltra** il pacchetto
- se non è connesso alla rete inoltra il pacchetto a un router che sa come gestirlo
- ogni host ha un router **gateway** con una tabella di inoltro
	- tramite un algoritmo vengono inoltrati i pacchetti

### Esempio di tabella di routing per il router R2
![[materie/anno_2025-2026/reti_di_calcolatori/assets/esempio_rete_inoltro.jpg]]
- In tabelle reali, la destinazione è l'indirizzo di rete
	- 158.110.0.0, 158.111.0.0
- Quindi ogni rete locale deve essere assegnata a un indirizzo di rete diverso
	- Gli host in reti LAN differenti hanno indirizzi di rete differenti

### Algoritmo
```
Se (NetworkNum della destinazione = NetworkNum di una delle mie interfacce)
	consegna il pacchetto alla destinazione mediante tale interfaccia
else if (NetworkNum della destinazione è presente nella mia tabella di inoltro)
	consegna il pacchetto al router NextHop
else
	consegna il pacchetto al router di default
```

Per un host
```
Se (NetworkNum della destinazione = Mio NetworkNum)
	consegna il pacchetto direttamente alla destinazione
else
	Consegna il pacchetto al router di default
```
## Subnetting

- Le reti di classe A e B potrebbero essere troppo grandi per una singola rete fisica
- **Subnet**: aggiunge un altro livello alla gerarchia degli indirizzi
- **Subnet masks** definiscono partizioni degli host 

![subnet_mask|100%](/materie/anno_2025-2026/reti_di_calcolatori/assets/subnet_mask.svg)
### Esempio
![[materie/anno_2025-2026/reti_di_calcolatori/assets/esempio_subnet.jpg]]

Tabella di inoltro del router R1

| SubnetNumber  | SubnetMask      | NextHop     |
| ------------- | --------------- | ----------- |
| 128.96.34.0   | 255.255.255.128 | Interface 0 |
| 128.96.34.128 | 255.255.255.128 | Interface 1 |
| 128.96.33.0   | 255.255.255.0   | R2          |

Subnet Mask 255.255.255.128 = 111111111.11111111.11111111.10000000
-  **7 bit** per gli indirizzi degli host
+ ogni sottorete creata avrà a disposizione $2^{7}-2 = 126$ indirizzi per gli host

### Algoritmo di inoltro

```
\\ D = indirizzo IP di destinazione
for each (SubnetNum, SubnetMask, NextHop)
	D1 = SubnetMask & D
	if D1 = SubnetNum
		if NextHop è un'interfaccia
			manda il datagramma direttamente alla destinazione
		else
			manda il datagramma al NextHop (un router)
		break
if (nessuna entry combacia)
	elimina il datagramma
```

- se nessuna entry combacia usa un router di default
- non è necessario che tutti gli 1 della subnetmask siano continui
	- possono essere create subnet strane
- Possono essere create diverse subnet su una rete fisica
- Subnet sono decise internamente da un amministratore di rete
	- non sono visibili dal resto dell'Internet
	- di solito assegnate per separazioni logiche (diversi uffici, dipartimenti, ecc...) o separazioni fisiche (diverse reti)
