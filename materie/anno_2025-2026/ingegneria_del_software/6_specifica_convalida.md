---
title: "6 Specifica Convalida"
aliases: ["6 Specifica Convalida"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "6-specifica-convalida"]
created: 2025-10-22
---
# Analisi, specifica e convalida dei requisiti
>[!definition]
>Stakeholder
>>possono essere i clienti, utenti finali, membri del team di sviluppo, ecc...

## Deduzione e analisi dei requisiti
+ capire ambiente operativo
+ come gli stakeholder potrebbero utilizzare il software
+ ingegneri dei requisiti devono lavorare con stakeholder per:
	+ scoprire informazioni sul dominio
	+ sulle funzionalità che i sistema dovrebbe fornire
	+ sulle prestazioni richieste 
	+ altri vincoli operativi

### Deduzione
+ né fornitore né committente sono in grado di estrarre i requisiti di un sistema
	+ committente non ha la conoscenza dei processi software per definire i requisiti
	+ stakeholder potrebbero avere **requisiti contrastanti**
	+ fornitore non ha una conoscenza perfetta del dominio applicativo, e non può esprimere le effettive necessità
### Processo
+ Processo iterativo termina quando il **documento dei requisiti** è **completo**
+ comprensione dei requisiti da parte dell'ingegnere del software migliora ad ogni iterazione
#### Scoperta e comprensione
+ analisti interagiscono con stakeholder per **scoprire i requisiti**
#### Classificazione e organizzazione
+ requisiti scoperti sono una raccolta non strutturata
+ requisiti tra loro correlati devono essere **raggruppati**
#### Negoziazione e priorità
+ più stakeholder = requisiti in conflitto
+ dare priorità ai requisiti
+ trovare e risolverne i conflitti attraverso la **negoziazione**
#### Documentazione
- requisiti documentati
- requisiti diventano input della successiva iterazione
- diversi livelli di documentazione a seconda del processo:
	- bozze di documenti dei requisiti software
	- informalmente su lavagne
	- wiki
	- spazi condivisi

## Tecniche per estrarre i requisiti
+ **Interviste**: si cerca di capire facendo domande agli stakeholder
+ **Etnografia**: osserviamo il cliente o gli utenti finali all'interno dell'ambiente operativo
+ **Storie utente e scenari**: testi narrativi che descrivono scenari pratici di utilizzo del software

### Interviste
+ questionari agli stakeholder:
	+ sul sistema che usano
	+ sistema che deve essere sviluppato
+ comprensione delle necessità degli stakeholder
#### Suggerimenti per interviste
+ **prototipo** può aiutare ad avere i requisiti
+ specialisti del dominio potrebbero usare **terminologia specifica o omettere dettagli** 
+ **dettagli organizzativi o politici** potrebbero essere **non rivelati a degli estranei**
+ intervistatore **open-minded**: evitando preconcetti 
+ evitare domande aperte troppo generiche
### Etnografia
+ analista si immerge nell'ambiente di lavoro in cui il sistema sarà usato
+ osserva il lavoro quotidiano 
+ ci focalizziamo sulle persone che useranno il nostro sistema
+ scoprire **requisiti impliciti** che riflettono processi reali
+ focus su **utenti finali**
#### Motivazioni
+ sistemi software non sono mai isolati
+ utilizzati in contesto sociale e organizzativo che influenza l'utilizzo pratico del sistema

### Storie e scenari
+ Descrizioni ad alto livello di come il sistema può essere utilizzato per svolgere particolari compiti
+ descrivono
	+ cosa fanno le persone
	+ quali informazioni utilizzano e producono
	+ quali sistemi possono utilizzare in questo processo
+ **Storie**: testi narrativi che presentano una descrizione di alto livello del modo in cui il sistema è utilizzato
+ **Scenari**: 
	+ informazioni specifiche spesso strutturate
	+ raccolte come input, output e flusso di eventi durante interazione con il sistema
	+ possono dettagliare parti delle storie

+ Più persone possono facilmente mettersi in relazione con storie e scenari
+ persone trovano più semplice riferirsi a esempi di vita reale
+ più semplice spiegare come si gestirebbe un contesto di lavoro che descrive un requisito

# Specifica dei requisiti 
+ Processo di descrizione dei requisiti utente e di sistema in un documento
+ requisiti **utente**: 
	+ quasi sempre scritti in linguaggio naturale
	+ **comprensibili** da utenti e clienti 
+ requisiti **di sistema**:
	+ possono essere scritti nel linguaggio naturale
	+ o altre notazioni basate su moduli grafici o matematici
## Specifica dei requisiti utente
+ comprensibili dagli utenti del sistema (senza conoscenze tecniche speciali)
+ dovrebbero specificare soltanto il comportamento del sistema visto dall'esterno e i suoi vincoli
+ non dovrebbe includere dettagli sull'**architettura** o **progettazione del sistema**
+ scritti in linguaggio naturale 
	+ tabelle
	+ moduli
	+ diagrammi intuitivi
+ **no gergo tecnico**
## Specifica dei requisiti di sistema
+ versioni **espanse** dei requisiti utente:
	+ aggiungono dettagli sul **comportamento esterno** del sistema e i **suoi vincoli**
+ **base di partenza** per la progettazione del sistema
+ usati come parte del contratto fra cliente e sviluppatore
+ dovrebbero essere una **specifica completa** e **dettagliata dell'intero sistema**
+ riferimenti all'architettura del sistema
## Specifica dei requisiti vs progetto
+ **In teoria**:
	+ specifica dei requisiti **non dovrebbe contenere informazioni sulla progettazione o implementazione del sistema**
	+ progetto deve descrivere **come i requisiti sono realizzati**
+ **Nella pratica:**
	+ requisiti e progetto sono **inseparabili**
	+ non si può escludere tutte le informazioni sulla progettazione

>[!example]
>1. l’utilizzo di una specifica architettura può essere necessario per soddisfare requisiti non funzionali
>2. è possibile strutturare i requisiti per ogni sotto-sistema per renderli più comprensibili

## Linguaggi per la specifica
+ requisiti spesso espressi in linguaggio naturale (NL)
+ Alternativa al NL:
	+ Linguaggio naturale strutturato o semi-strutturato
	+ Modelli grafici (vedi use case e sequence diagrams)
	+ Specifiche formali (vedi macchine a stati finiti)

### Linguaggio naturale
+ **Pro**:
	+ espressivo, intuitivo e universale: può essere compreso anche da utenti e clienti
+ **Contro:**
	+ mancanza di chiarezza: 
		+ difficile usare il linguaggio in modo conciso e allo stesso tempo preciso e non ambiguo
	+ Confusione:
		+ difficile distinguere varie tipologie di requisiti
		+ diversi requisiti potrebbero essere espressi in una singola frase
#### Linee guida per il linguaggio naturale
+ formato standard **coerente e conciso**:
	+ riduce il **rischio di omissioni**
	+ **semplifica** il controllo dei requisiti
	+ utilizzo coerente del linguaggio:
		+ "deve" per requisiti obbligatori
		+ "dovrebbe" se desiderabili ma non obbligatori
	+ formattazione coerente del testo
		+ per evidenziare punti chiave di un requisito
	+ evitare utilizzo del linguaggio tecnico
	+ spiegare perché un requisito è necessario e chi lo ha proposto 

>[!example]
>Req 3.2: Il sistema deve misurare il livello degli zuccheri nel sangue e rilasciare lʼinsulina, ogni 10 minuti (variazioni degli zuccheri nel sangue sono relativamente lente, quindi non sono necessarie misure più frequenti; misure meno frequenti potrebbero portare a livelli di zuccheri inutilmente elevati).
>- Conciso
>- Usa deve
>- Motiva il requisito
>- formato standard evidenziando le diverse parti del requisito

## Specifiche strutturate
+ linguaggio naturale con struttura predefinita standard per tutti i requisiti
	+ maggiore **uniformità**
+ ciascun elemento fornisce informazioni su un aspetto del requisito
+ **limita la libertà** di chi scrive i requisiti ----> scritti in maniera guidata
+ si possono usare costrutti del linguaggio di programmazione
+ usare formattazione per evidenziare punti chiave di un requisito
## Specifiche strutturare in template


## Specifiche tabellari
+ quando bisogna specificare calcoli complessi ---> difficile non introdurre ambiguità
+ aggiungere informazioni supplementari al linguaggio naturale
	+ tabelle
	+ modelli grafici del sistema
+ utili per descrivere:
	+ **situazioni alternative**
	+ azioni da intraprendere in ciascuna situazione 

#### Vantaggi:
+ conserva **l'espressività** del NL
+ **uniformità** per descrivere le specifiche **riducendo** **variabilità**
+ **Organizza i requisiti** in modo efficace
#### Svantaggi
+ troppo rigido per descrivere alcuni requisiti
+ difficile scrivere i requisiti in modo non ambiguo quando sono **molto complessi**

### Casi d'uso
+ scenari definiti nel linguaggio standard UML
+ descrivono chi interagisce con il sistema
+ arricchiti da **informazioni dettagliate** su ciascuna interazione
+ diagrammi di sequenza sono diagrammi che possono descrivere in maniera più dettagliata le sequenze di eventi che occorrono durante l'utilizzo del sistema
## Documento di specifica dei requisiti del software (SRS)
>[!definition]
>>Definizione ufficiale dei requisiti del software
>>Definise ciò che gli sviluppatori dovrebbero implementare

+ include sia requisiti utente e requisiti di sistema
