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
![[materie/anno_2025-2026/reti_di_calcolatori/reti_di_calcolatori.excalidraw.md#^frame=4aU4JFfp]]
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
