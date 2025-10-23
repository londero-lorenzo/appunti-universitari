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
+ ha conoscenze delle posizioni dei vari dispositivi
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

+ switch possono essere scalati: li trovi con vari quantità di porte
+ latenza aumenta per via della distanza tra i dispositivi
+ switch combinati

Livello 3 andiamo a risolvere i problemi di interconnessione tra reti generiche.

+ modulare, economica
+ performance non dipendono dal numero di host collegati ma dalle capacità interne del **processore**

switch guardano il contenuto dell'intestazione per decidere che cosa fare del pacchetto

+ Datagramma (connectionless approach)
+ Virtual circuit (Connection-oiented)
+ Source routing

- ogni host ha un indirizzo univoco:
	- level 2: MAC address
	- level 3: IP address

### Connectionless
+ non hanno una memoria gli switch
+ ogni pacchetto è a se
+ si fa tutto  in base alle informazioni che reca il pacchetto 

+ nessuno switch ha la visione completa della rete
+ non si è ancora stabilizzata la configurazione quindi può perdere pacchetti
+ tabelle possono essere programmate a mano dall'admin di rete
+ algoritmi di apprendimento delle posizioni per compilare le tabelle

### Virtual circuit
+ se A e B vogliono comunicare 
+ devo interrogare gli switch intermedi
+ quando dobbiamo mettere un frame nell'intestazione non viene messo l'indirizzo del destinatario ma il numero del circuito virtuale 
+ L'indirizzo degli host non viene usato durante la comunicazione ma solo per creare il circuito

+ supponiamo che A voglia stabilire un circuito con B
+ A manda una richiesta a S1 identificando B
#### Vantaggi
+ intestazione nei pacchetti molto più bassa
+ posso verificare che le proprietà che scelgo siano garantite
#### Svantaggi
+ sensibili ai guasti
+ si deve rifare il circuito
+ 