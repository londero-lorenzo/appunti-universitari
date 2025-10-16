---
title: 4-Protocolli-e-Architettura
aliases:
  - 4-Protocolli-e-Architettura
tags:
  - università
  - materie
  - anno-2025-2026
  - internet-of-things
created: 2025-10-14
---

(Vedere le Slide 3 con laboratorio sul GPS Tracker)

# Dispositivi IoT:

Dispositivi:
+ dinamici: si adattano all'ambiente
+ auto-configuranti
+ utilizzano protocolli di comunicazione che permettono lo scambio di informazioni fra sistemi eterogenei

>[!definition]
>"Cose"/"Things"
>>dispositivi con identità univoche in grado di svolgere acquisizioni di dati da sensori, di azionare attuatori e monitorarli anche da remoto.

In particolare i dispositivi IoT possono:
+ **scambiare dati**
+ **raccogliere dati ed elaborarli o inviarli**
+ **assolvere certi compiti localmente**

## Progettazione logica

Sistema IoT composti da insiemi a blocchi, che rappresentano varie interfacce per connettersi ad altri dispositivi (sia in modo cablato che wireless), quali sensori, audio/video, Internet, memoria.

Tali dispositivi possiedono poi dei protocolli per ogni livello dell'architettura:
+ Application Layer
	+ HTTP: stateless, request-response
	+ Websocket: comunicazione slient-server full-duplex su TCP (socket bidimensionale)
	+ XMPP: comunicazione real-time di messaggi XML
	+ DDS: comunicazione M2M con modello publish/subscribe
+ Transport Layer
	+ TCP (connessione con stato)
	+ UDP (connessione senza stato)
+ Network Layer
	+ IPv4: indirizzi a 32 bit (finiti nel 2019)
	+ IPv6: indirizzi a 128 bit
	+ 6LoWPAN (fornisce algoritmi di compressione per i datagrammi IPv6)
+ Link Layer
	+ IEEE 802.11 (Wi-Fi)
	+ IEEE 802.15.4 (LoRaWan)
	+ 2G/3G/4G/5G (comunicazione dei dispositivi mobili)


La progettazione logica di un sistema IoT è una rappresentazione astratta delle entità coinvolte senza entrare nei dettagli dell'implementazione, ognuno che specifica una funzione: **applicazione, sicurezza, management, communication, device, servizi**.
Nel caso migliore ogni nodo presenta tutti questi blocchi.

## Modelli di comunicazione

+ **Request-Response**: 
  ad una richiesta del client segue una risposta del server. è senza memoria, non tiene traccia delle caratteristiche del client per le prossime richieste (non si ricorda il login). Per l'utilizzo di memoria dei dati della sessione si utilizzano i cookie.

+ **Publish-Subscribe**: 
	  ***publisher*** (sorgente dei dati) invia i dati al ***broker***, broker gestisce gli argomenti ed invia i dati ai ***costumer*** in base agli interessi (iscrizioni) dei costumers. I costumer si iscrivono agli argomenti gestiti dal broker per ricevere i relativi dati.

+ **Push-Pull**:
  i produttori inviano dati a delle code e i consumatori prelevano i dati da tali code. Le code fungono anche da buffer, siccome i produttori e consumatori possono agire con velocità diverse, in quanto le code servono a disaccoppiare lo scambio di messaggi tra produttori e consumatori.

+ **Exclusive Pair**: Connessione *bidirezionale* e *full-duplex* e utilizza connessione stabile, ovvero una volta che viene stabilita resta aperta finché il client non invia una richiesta di chiusura. generalmente si utilizza un'unica volta con uno scambio intensivo di dati, in quanto l'apertura e la chiusura della connessione sono le azioni più costose.


**API di comunicazione:**
+ basate su REST: vengono definite le regole di comunicazione e sono rese note (solitamente) a chi utilizza l'applicazione.
  Tipo di comunicazione:
	+ Request-response
+ basate su WebSocket: consentono comunicazioni full duplex e bidirezionali fra client e server.
  Tipo di comunicazione:
	+ Exclusive Pair

## Livelli dell'IoT

Un sistema IoT è formato dalle seguenti componenti:
+ Dispositivi
+ Risorse
+ Servizi di controllo
+ Database
+ Web Service
+ Componenti di analisi
+ Applicazioni
### Livello 1:
Un sistema di livello 1 ha un solo nodo: gira solo su una macchina e se si rompe non gira più. Esso acquisisce dati, li memorizza, gli elabora e fa girare l'applicazione. I dati restano li e sono accessibili solo localmente.

### Livello 2:
I dati cominciano a essere tanti, quindi il nodo principale comincia a fare da buffer, con un server secondario da qualche parte con un disco che funge da cloud per memorizzare i dati. Utile se l'attività di analisi non è pesante e può continuare ad essere gestita da un solo nodo.

### Livello 3:
Sempre singolo nodo, che trasferisce in cloud sia i dati che l'applicazione, quindi per attività di analisi pesante.

### Livello 4:
Sistemi multinodo. In locale abbiamo i nodi che acquisiscono dati (quelli con i sensori), e ci sono invece altri nodi detti osservatori che possono ricavare dei dati informativi caricati nel cloud in base alle loro iscrizioni.

### Livello 5:
Presente un nodo coordinatore locale, che controlla i nodi secondari, ponendo dei filtri e impedendo che un nodo danneggiato inserisca dei dati errati in cloud. Soluzione per reti di sensori wireless con molti dati e con attività di analisi pesante.

### Livello 6:
Diversi nodi indipendenti che acquisiscono dati, comandano gli attuatori ed inviano i dati direttamente nel cloud.
Il controllore centralizzato conosce in tempo reale lo stato  di tutti i nodi ed invia loro i comandi di controllo.


____

