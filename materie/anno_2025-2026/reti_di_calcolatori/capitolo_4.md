---
title: "Capitolo 4"
aliases: ["Capitolo 4"]
tags: [università, "materie", "anno-2025-2026", "reti-di-calcolatori", "capitolo-4"]
created: 2026-04-10
---
# Problemi
- Come costruiamo un sistema di instradamento che possa gestire centinaia di migliaia di reti e miliardi di nodi ?
- Come gestiamo l'esaurimento dello spazio di indirizzamento IPv4?
- Come migliorare le funzionalità di internet?

# Interdominio
- Internet è organizzato come **sistemi autonomi** i quali sono sotto il controllo di una singola entità amministrativa
- **Sistemi autonomi**
	- corrisponde a un dominio amministrativo
	- es: Università, aziende, backbone network
- una rete interna di un'azienda potrebbe essere un singolo sistema autonomo, come una rete di un singolo Internet service provider
## Route Propagation
• Idea: fornire un ulteriore modo per **aggregare gerarchicamente le informazioni di routing** in una rete Internet di grandi dimensioni
	• Migliora la **scalabilità**
• Divide il problema del routing in due parti:
- routing **all’interno di un singolo sistema autonomo (AS)**
- routing **tra sistemi autonomi diversi**
• Un altro nome per i sistemi autonomi in Internet è **domini di routing**
• Gerarchia a due livelli per la propagazione delle rotte:
- protocollo di routing **inter-dominio** (standard a livello Internet)
- protocollo di routing **intra-dominio** (ogni AS sceglie il proprio)
### Protocolli Inter-domain
#### Exterior Gateway Protocol (EGP)
- topologia ad albero
- non permette alla topologia di assumere forme più generali
#### Border Gateway Protocol (BGP)
- Internet è un insieme di sistemi autonomi arbitrariamente interconnessi
- oggi Internet è formata dall'interconnessione di più **reti backbone** (reti fornitrici di servizi gestite da compagnie private ) e da **siti connessi** l'uno all'altro in modi diversi
- alcune grandi aziende sono direttamente connesse ad uno o più backbone, mentre altre si connettono a fornitori più piccoli di servizi non di tipo backbone
- molti fornitori hanno come clienti solo "consumer" (persone come noi con PC a casa) e devono connettersi anche loro a fornitori backbone
- molti fornitori si interconnettono l'un l'altro in un singolo **peering point**

#### BGP-4
![[materie/anno_2025-2026/reti_di_calcolatori/assets/BGP.jpg]]
- **Traffico locale:** traffico che ha origine o termina in nodi che si trovano all'interno di un AS
- **Traffico transito:** traffico che attraversa un AS
- Classificazione AS:
	- **Tipo stub**: ha una sola connessione verso un altro AS e quindi trasporta soltanto traffico locale (es. Small corporation)
	- **Tipo multihomed**: ha connessioni con più AS ma rifiuta di trasportare traffico in transito (es. Large corporation)
	- **Transito**: ha connessioni con più AS ed è progettato per trasportare sia traffico locale sia traffico in transito (es. Backbone providers)

>[!tip] Obiettivo
>Trovare un percorso qualsiasi verso la destinazione finale che sia privo di cicli (loop-free).
>- Siamo più interessati alla raggiungibilità che all'ottimizzazione
>- identificazione di un percorso che sia prossimo all'ottimale è un grande risultato

- **Scalabilità**: un router backbone in Internet deve inoltrare i pacchetti destinati a qualsiasi punto nella rete
	- ha una tabella di instradamento che ha una corrispondenza per qualsiasi IP valido
- **Natura autonoma dei domini:**
	- ciascun dominio può eseguire protocolli di instradamento diversi quindi usare qualsiasi schema per assegnare i costi ai percorsi
	- **impossibile calcolare costi** significativi per percorsi che attraversino più AS
	- costo uguale a 1000 per un fornitore potrebbe rappresentare un ottimo percorso ma potrebbe essere inaccettabile per un altro
- **Problema della fiducia:** 
	- Fornitore A potrebbe essere scettico nel cedere ad alcune affermazioni di B
	- per paura che B pubblicizzi informazioni di instradamento sbagliate

#### BGP speaker
Ogni AS ha almeno un nodo che avrà la funzione di **annunciatore BGP**: effettua gli annunci per tutto l'AS

- Ogni AS ha uno o più **gateway di confine** che non coincidono con gli speaker
	- sono i router tramite cui i pacchetti escono ed entrano dal sistema autonomo

#### eBGP e iBGP
- **External BGP:** usato tra i router appartenenti a diversi AS
- **Internal BGP:** usato tra router dentro lo stesso ASs
![[materie/anno_2025-2026/reti_di_calcolatori/assets/e-iBGP.jpg]]

#### Integrazione tra instradamento interdominio e intradominio
- tutti i router usano iBGP e un protocollo di instradamento di intradominio (RIP, OSPF, ...)
- router di confine usano anche eBGP verso altri AS
- c'è una tabella BGP valida per tutto l'AS, che è propagata ai router interni tramite iBGP
![[materie/anno_2025-2026/reti_di_calcolatori/assets/intra-interdomain_routing.jpg]]

>[!warning]
>- BGP non appartiene a nessuna delle principali classi di protocolli di instradamento (vettori di distanza e link-state)
>- BGP pubblicizza **percorsi completi** sotto forma di elenchi di AS tramite i quali si può raggiungere una particolare rete

#### Prevenzione di loop e politica di instradamento
>[!warning] Un router BGP ignora un percorso se:
>- il suo AS appare in esso (evita loop)
>- se viola alcune politiche del AS

#### Esempio
![[materie/anno_2025-2026/reti_di_calcolatori/assets/bgp_example.jpg]]
- speaker per AS 2 avverte raggiungibilità a P e Q
	- la rete 128.96, 192.4.153, 192.4.32, e 192.4.3 possono essere raggiunte direttamente da AS 2
- lo speaker per la backbone network avverte di conseguenza:
	- reti 128.96, 192.4.153, 192.4.32, e 192.4.3 possono essere raggiunte attraverso il cammino <AS 1, AS 2>
- gli speaker possono anche cancellare i cammini registrati in precedenza

#### Problemi
- I numeri degli AS usati in BGP devono essere univoci
	- Se per esempio AS 2 può identificare se stesso nel cammino di AS dell'esempio di prima solo se nessun altro AS identifica se stesso nello stesso modo
- Numeri di AS sono numeri a 32-bit assegnati da un'autorità centrale
- Circa 60.000 AS al momento

# Next Generation IPv6
- Indirizzi da 128-bit
	- spazio di indirizzi dell'ordine di $3\times10^{38}$
- Multicast
- supporto per servizi in tempo reale
- supporto per autenticazione e sicurezza
- Autoconfigurazione: capacità degli host di configurarsi automaticamente con indirizzo IP e nome dominio
- migliore funzionalità di instradamento (supporto host mobili)
- End-to-end fragmentation
- estendibile

## Indirizzi
- Non usano le classi: spazio di indirizzamento suddiviso in base **ai bit iniziali**
- Notazione: x:x:x:x:x:x:x:x (x = 16-bit hex number)
	- Esempio: 47CD:0000:0000:0000:0000:0000:A456:0124
	- gli zeri sono compressi: 47CD::A456:124
	- compatibili con IPv4: ::128.42.1.87
	- Localhost: 0000:0000:0000:0000:0000:0000:0000:0001, i.e. ::1
- Assegnamento:
	- basato sui provider (come IPv4)
	- geografico
### Header
![[materie/anno_2025-2026/reti_di_calcolatori/assets/ipv6_header.jpg]]
- 40-byte intestazione base
- 64 kB payload
#### Priorità
- **Traffic Class**: definisce la priorità di un datagramma rispetto agli altri della stessa sorgente
- utile in caso che alcuni datagrammi debbano essere scartati causa congestione
- Possibili valori:
	- 0=Traffico generico
	- 1=Traffico Background (NNTP)
	- 2= traffico senza attesa (SMTP)
	- 3 e 5 = riservato
	- 4=Traffico con attesa (FTP, HTTP)
	- 6=Traffico interattivo (TELNET, SSH)
	- 7=Traffico di controllo (OSPF, RIP, SNMP,...)
	- 8-15= Traffico che non dipende da congestione ordinato da ridondanza (audio/video)
#### Flow label
- Numero casuale a 20-bit, assegnato dalla sorgente
- datagrammi appartengono allo stesso flusso sono segnati con lo stesso valore
- questo identificatore può essere usato dai router per implementare un servizio coerente a tutti i datagrammi dello stesso flusso:
	- stesso instradamento
	- Qualità del servizio: utilizzo di risorse riservate

## Transizione da IPv4 a IPv6 
- IPv4 e IPv6 non sono compatibili
- IPv4 dovrebbe essere rimpiazzato da IPv6
- Molto difficile: troppi host da aggiornare
	- non può essere fatto in un colpo solo
	- non può essere forzato
- 3 tecniche per supportare la transizione
	- Operatività a doppia pila
	- Tunneling
	- Traduzione dell'intestazione
### Operatività a doppia pila
- i nodi IPv6 eseguono i prottocolli IPv6 e IPv4
- usano il campo Version per per decidere quale pila di protocolli debba elaborare il pacchetto in arrivo
- due protocolli al livello 3: l'host appartiene a due internetworks separate
- applicazioni devono avere a che fare con entrambi gli indirizzi
	- più lavoro per gli sviluppatori
### Tunneling
- crea dei tunnel o ponti da una regione IPv6 ad un'altra incapsulando datagrammi IPv6 con un'intestazione IPv4
- host possono comunicare in IPv6
- i benefici dell'IPv6 sono persi nella regione IPv4
### Header Translation
- permette di trasmettere  un datagramma IPv6 ad un host che ha solo IPv4
- router di destinazione rimpiazzano l'intestazione IPv6 con l'equivalente IPv4 e viceversa
- simile al NAT ma la traduzione è tra indirizzi e intestazioni IPv4 e IPv6
# Internet Multicast
>[!definition] 
>Multicast
>>Possibilità di mandare un messaggio ad un gruppo di host riceventi, senza conoscerli o specificarli

- Uno a molti: Sorgente specifica multicast (SSM)
	- un host ricevente specifica a un gruppo multicast dove uno specifico host sta spedendo:
		- stazioni radio broadcast
		- news
		- aggiornamenti software per più host
- Molti a molti: tutte le sorgenti multicast ASM
	- teleconferenze
	- videogiochi multiplayer
	- simulazioni distribuite
## Multicast senza multicast?
- senza supporto per il multicast una sorgente ha bisogno di mandare un pacchetto separato con i dati identici ad ogni membro del gruppo
	- questo consuma più banda
	- traffico non è neanche distribuito, è concentrato sull'host sorgente
	- sorgente necessita di mantenere traccia degli indirizzi IP di ogni membro del gruppo
		- gruppo potrebbe essere dinamico
	- differenze di delay fra diverse destinazioni aumentano
## Multicast in IP
- usare IP multicast per mandare lo stesso identico pacchetto ad ogni membro del gruppo
	- un host manda una singola copia del pacchetto, indirizzato all'indirizzo multicast del gruppo
	- ogni membro del gruppo riceve una copia del pacchetto
	- l'host sorgente non ha bisogno di sapere l'indirizzo unicast di ogni host
	- pacchetti sono duplicati dai router lungo il percorso quando serve
- IP provvedono un livello IP multicast molti a molti basato sui **gruppi multicast**
	- ogni gruppo ha il suo indirizzo IP multicast nella classe D (224.0.0.0 – 239.255.255.255)
	- Gli indirizzi del gruppo sono assegnati in vari modi
		- 224.0.0.0/24: definito dall'IANA ma ristretto a reti locali
		- 224.0.1.0/24: gruppi globali, assegnato staticamente dall'IANA 
		- dinamicamente per un tempo limitato usando il protocollo SAP/SDP
## Management gruppo multicast
- un host può entrare e lasciare il gruppo
- un host può essere in più gruppi
- un host segnala il suo desiderio di entrare o lasciare un gruppo multicast comunicando con il suo router locale usando un protocollo speciale
	- in IPv4: Internet Group Management Protocol IGMP
	- in IPv6: Multicast Listener Discovery MLD
- il router ha la responsabilità di far funzionare correttamente il multicast con riguardo per gli host

