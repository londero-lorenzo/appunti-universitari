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


#### Vantaggi
+ intestazione nei pacchetti molto più bassa
+ posso verificare che le proprietà che scelgo siano garantite
#### Svantaggi
+ sensibili ai guasti
+ si deve rifare il circuito

# Bridges e LAN Switches

legge i frame verifica i CRC e li inoltra

pacchetto non arriva perché la configurazione interna degli switch non è aggiornata rispetto alla topologia della rete

se il bridge riceve un frame che ha indirizzo broadcast (tutti uno)

B3 inoltra sul ramo C e B5 sul ramo D e B1 lo inoltra su tutte le porte

## Spanning Tree Algorithm

+ **Rapid Spanning Tree:** protocollo usato da tutti gli switch
+ switch fra di loro si parlano
	+ scambiano messaggi (frame ethernet specifici) relativi alla rete
+ ogni bridge deve capire quali sono le porte su cui vuole fowardare i frame
+ eleggere un bridge come la root di un albero (quello con ID più basso)
+ bridge si scambiano messaggi (BPDU)
	+ ogni messaggio è una tripla (X, d, Y)
		+ **Y**: ID del bridge che genera il messaggio
		+ **X** ID del bridge root secondo Y
		+ **d** distanza tra X e Y in base a quante LAN deve attraversare
	+ ID bridge è composto dall'indirizzo MAC e 16 bit di priorità (di cui solo i primi 4 sono la priorità reale)

