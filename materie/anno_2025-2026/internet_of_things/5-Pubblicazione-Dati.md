---
title: 5-Pubblicazione-Dati
aliases:
  - 5-Pubblicazione-Dati
tags:
  - università
  - materie
  - anno-2025-2026
  - internet-of-things
created: 2025-10-16
---
## Comunicare dati tramite socket

I dati dopo l'acquisizione devono essere instradati verso le unità di calcolo che devono analizzarli e prendere decisione di riflesso. E per sistemi semplici scrivere un socket server può essere la soluzione più conveniente.

>[!curiosity]
>Solitamente tutte le librerie python sono interpretate da C, sostanzialmnete prende la libreria di C e ci wrappa sopra l'interfaccia ptrhon, cosa che rende le librerie nativamnete C molto veloci, ma le librerie create con altre librerie python lente, in quanto attingono ad altre librerie che però hanno interprete C, portando molti calcoli

Creazione di una socket di tipo client:
+ `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
Connessione ad un server:
+ `s.connect(("www.uniud.it", 80))`

Socket lato server richiede più passaggi rispetto al client, deve essere legato ad un dominio/indirizzo ed un numero di porta quando si usa TCP:
+ `serversocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
+ `serversocket.bind( indirizzo_locale, numero_di_porta)`
+ `serversocket.listen(numero_di_client_massimi)`

+ Ciclo di servizio:
	+ `while True:
		`(conn, address) = serversocket.accept()
		`ct= threading.Thread(target=handleClient,args=(conn,))
		`ct.start()

+ Se dopo `serversocket.accept()` non c'è nessun client, il server si blocca.
  Invece per ogni connessione accettata crea un nuovo thread e lo fa partire per poi tornare in stato di accept.

>[!tip]
>La socket è al livello 5 di ISO/OSI, livello di connessione

#### Ricevere i dati:
Codice:
`dataBuffer=[]
`while True:
	`data= conn.recv(1024)
	`if not data:
		`break
	`else:
		`dataBuffer.append(data)

Se il nodo connesso ha dei dati, li accodo al buffer, sennò chiudo tutto.
Nel modello standard non so quanti byte verranno in input, ma può essere implementato un sistema di calcolo, come ad esempio inviare un numero di byte fissato (ad esempio 2) in cui codificare la lunghezza (numero di byte) che comporranno il messaggio.

#### Spedire i dati:
Possono essere usati i seguenti metodi:
+ *send(bytes)*: lascia all'applicazione il controllo che il contenuto di *bytes* sia stato completamente spedito.
+ *sendall(bytes)*: continua a spedire i dati finché il contenuto di *bytes* non è stato completamente spedito.

___

### Problemi con le socket:

La programmazione è troppo a basso livello per certi aspetti, ovvero il meccanismo è molto ad hoc, quindi uno deve andare a studiarsi proprio come è fatto il codice, non c'è il riferimento a qualcosa di astratto: è suggerito quindi usare sempre protocolli standard, con suddivisione dei dati in categorie, in modo che se domani aggiungo un sensore aggiungo semplicemente un nuovo topic come argomento di interesse.

**echo server**: il server fa l'eco del client rispondendo con il codice di richiesta: "Hello" --> "Hello".

>[!example]
>Esempio di probemi dovuti alla programmazione a basso livello con l'utilizzo di un client e di un echo server che hanno una dimensione dei buffer non coincidente:
>-  Se il size è abbastanza grande sia nel server che nel client il messaggio viene mandato lungo un'unica stringa e ricevuto come tale.
>- Se il size è molto piccolo nel server ma è grande nel client, o viceversa, il messaggio viene mandato lungo un'unica stringa e ricevuto in più stringhe spezzettando il messaggio, dato che il buffer è più piccolo nel server

#### Altri moduli sulle socket

Esistono altri moduli con classi più semplici per interagire con le socket:
+ modulo 'socketserver'

___


## MQTT (MessageQueueing Telemetry Transport)

Entità e protocollo di interazione di tipo publish/subscribe, e può sfruttare potenzialmente qualunque protocollo di trasporto che offra una connessione bidirezionale, ordinata e senza perdita di dati.

Creato per monitorare lo stato di un oleodotto nel deserto. 
In seguito è stato standardizzato e utilizzato da altre aziende.

Le **entità** utilizzate sono quelle di un protocollo publish/subscribe:
+ Broker (server)
+ Publisher (client)
+ Subscriber (client)

**Tipi di messaggio**:
+ Connect/disconnect
+ Publish/subscribe

**Quality of service** (QoS):
+ At most once: il messaggio viene mandato e non servono ulteriori passaggi per confermare la consegna.
+ At least once: se dopo un certo tempo non arriva l'acknowledge della ricezione del messaggio rispedisco il messaggio, se poi ci sono duplicati pazienza.
+ Exactly once: Il messaggio è mandato solo una volta.

>[!tip]
>L'overhead di messaggi reali scambiati fra client e broker aumenta in modo correlato al livello di QoS richiesto

Nel flow di messaggi MQTT sono presenti anche delle variabili a cui è associato un valore:
+ MID: message identificator
+ DUP: duplicato. Se è uguale a 0 è il primo invio, se ne invio un altro perché non ho ricevuto l'acknowledge sarà DUP=1.
+ QOS: livello di Quality of Service, Può essere 0, 1, 2.

>[!tip]
>MQTT, rispetto agli altri protocolli, è di gran lunga la libreria che da molti anni sta servendo molte applicazioni IoT ed è la più efficace.


>[!curiosity]
>Erlang linguaggio funzionale usato anche per le applicazioni internet dei videogiochi tipo call of duty]

>[!example]
>Esempio di utilizzo di MQTT, che consente di estrarre i dati dal GPS tracker svolto precedentemente della sua porta seriale e di pubblicarli grazie ad un broker (Eclipse Mosquitto), suddivisi in topic.
>(svolto come laboratorio a lezione)

##### Topic di MQTT:
+ semplice (temperatura)
+ strutturato (casa/cucina/forno/temperatura)

#### MQTT vs HTTP:
+ MQTT ha un costo maggiore rappresentato dallo stabilimento della connessione e dalla sua chiusura. Conviene quindi rispetto ad HTTP quando bisogna inviare molti dati usando la stessa connessione, tenuta aperta per tutta la durata della comunicazione.
