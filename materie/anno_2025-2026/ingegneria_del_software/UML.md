---
title: "Uml"
aliases: ["Uml"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "UML"]
created: 2025-10-27
---
# Intro UML
## Motivazione
- impensabile comprendere sistemi complessi
- codice incomprensibile
- forme più astratte per discutere tra di noi
- modellazione

## Modellazione
Processo che sviluppa **modelli astratti** di un sistema, non una rappresentazione alternativa
### Rappresentazione
Mantiene tutte le informazioni sull'entità che rappresenta
### Astrazione
**Semplifica** un sistema evidenziandone le **caratteristiche più salienti**

>[!tip]
>Ad un sistema possono corrispondere più modelli
>- Ogni modello rappresenta una differente vista o prospettiva del sistema

## Terminologia
- **Modello**: astrazione che descrive un sistema o un sotto sistema
- **Vista**: descrizione di aspetti specifici da una certa prospettiva
- **Notazione**: insieme di elementi grafici o testuali e regole per rappresentare le viste

## Linguaggi di modellazione
+ nati da un'esigenza
+ linguaggio UML: linguaggio **unificato** utilizzato in tutte le attività di modellazione

- Si basa su un singolo **meta-modello**
- definisce i concetti del linguaggio di modellazione: indica quali sono le regole per costruire modelli UML
- UML **non** è una metodologia:
	- il suo obiettivo è di fornire un supporto al processo di sviluppo software
- Usato all'interno dei processi di sviluppo che adottano le proprie metodologie
### Regole
+ **Prescritte**: regole stabilite da organismi standardizzanti che definiscono:
	+ lessico
	+ sintassi
	+ semantica
+ **Descrittive**: stabilite per convenzione comune
	+ possono essere meglio comprese guardando come l'UML viene usato nella pratica
>[!tip]
>Bisogna conoscere sempre le convenzioni particolari:
>- della specifica organizzazione
>- del singolo progetto

## UML
Può essere usato come:
- **Bozza**: per tracciare un modello informale di un sistema da realizzare o descrivere un sistema esistente
- **Progetto dettagliato**: per realizzare un modello completo della soluzione architetturale del sistema
- **Linguaggio di programmazione**: in grado di modellare in maniera completa e precisa il software

### Bozze espressività > compltezza
>[!definition]
>- Aiutare la comunicazione e discussione delle idee
>- Esplorare soluzioni alternative

- diagrammi **non devono essere esaustivi** e definire tutti gli aspetti del codice
- non si rispetta tutte le regole formali dello standard
### Progetto dettagliato: espressività + completezza
>[!definition]
>>Aiutare la comprensione e la completezza

- progettista sviluppa modello di progetto che lo sviluppatore dovrà realizzare (salvandolo in file condivisi)
- **completezza e non ambiguità** del modello **aiutano** il programmatore 
	- programmatore sarà guidato dal modello
	- non dovrà avere aspetti ambigui da interpretare

### UML come linguaggio di programmazione
- approccio **MDA** (**Model Driven Architecture**)
- stabilire una sintassi e una semantica precisi per UML che portino alla **generazione automatica** di codice eseguibile che rappresenti il modello
- modellare precisamente anche **la logica del progetto**
- **Vantaggio**: generare codice per diverse piattaforme target partendo da un modello indipendente dalla piattaforma 

## Informazioni soppresse
- Assenza di qualche informazione nel diagramma $\neq$ informazione non esiste
- Alcuni aspetti del problema potrebbero essere assenti da un diagramma
	- perché non sono ancora trattati nella fase in cui è stato disegnato
>[!example]
>La precisa sequenza di eventi per realizzare una funzionalità può **non** essere pronta durante l'analisi dei requisiti in cui sono **abbozzati i casi d'uso**

## Tipi di diagrammi UML
### Diagrammi strutturali
>[!definition]
>>Modellano l'organizzazione del sistema (class diagrams, package diagrams, deployment diagrams)

### Diagrammi Comportamentali
>[!definition]
>> Modellano il **comportamento** e le **interazioni** tra le **entità** del sistema

Rappresentano i **deliverables** di diverse fasi del ciclo di vita del software:
- attività di analisi dei requisiti
- attività di progettazione (sia di basso che alto livello)
## Prospettive UML
### Prospettiva esterna
Modellati in contesto operativo del sistema
### Prospettiva delle interazioni
Modellate le interazioni tra il contesto e il sistema o tra diverse componenti del sistema
### Prospettiva strutturale
Modellate l'organizzazione del sistema e/o la struttura dei dati
### Prospettiva comportamentale
Modellati il **comportamento dinamico** del sistema e come esso risponde agli eventi

## Integrare UML nel processo di sviluppo
UML può essere utilizzato in varie fasi del processo di sviluppo:

- **Analisi dei requisiti**:
	- facilita la deduzione dei requisiti
	- la notazione non deve essere troppo complessa per favorire la comunicazione con cliente
- **Progettazione**: modelli più **tecnici** e **dettagliati** per descrivere il sistema agli ingegneri che lo devono implementare
- **Documentazione (dopo implementazione)**: modelli **rendono più semplice** la descrizione di **parti complesse** o **convogliano messaggi** in maniera intuitiva e immediata
- **Comprensione di software per-esistente**: evoluzione o reverse-engineering 
>[!tip] Processi iterativi
>Nei processi iterativi ogni iterazione **arricchisce** i diagrammi delle iterazioni precedenti.

# Diagrammi dei casi d'uso

## Diagramma comportamentale: 
>[!definition]
>>Modella il comportamento esterno del sistema (senza specificare nel dettaglio)
>>+ modella l'interazione tra il sistema e gli agenti esterni

- usato nella fase di definizione dei requisiti
- identifica i requisiti **funzionali**
- forma grafica e narrativa delle interazioni tra utenti e sistema
- Risponde alla comanda "Com'è usato il sistema ?"

- sistema visto come una **black box** (dettagli interni non specificati)
- sistema analizzato dal punto di vista degli utenti
- compilato a valle di interviste al committente

## Scenari e casi d'uso
### Esempio
Un cliente arriva alla cassa con alcuni articoli da acquistare. Il cassiere usa un POS per registrare ogni articolo acquistato. Il sistema mostra il totale e i dettagli per ogni articolo. Il cliente inserisce i dati della propria carta di credito, che il sistema convalida e registra. Il sistema aggiorna l’inventario. Il cliente ottiene una ricevuta e se ne va.

- I dati sulla carta di credito avrebbero potuto essere errati oppure il cliente avrebbe potuto preferire pagare in contanti.
- Questi due sarebbero stati altri **scenari alternativi**, simili a quello originale perché ne condividono la finalità
>[!definition]
>**Scenario**: 
>>Sequenza di **passi** che caratterizzano una particolare interazione tra un utente e il sistema

>[!definition]
>**Caso d'uso**: 
>>Insieme di scenari che hanno in comune lo scopo finale dell'utente

>[!example]
>Nell'esempio di prima:
>- caso d'uso = "Acquista prodotto"
>- tre possibili scenari
>- attori = cliente e cassiere


- interazione tra un attore e il sistema per svolgere unità di lavoro utile
- **non rivela** l'organizzazione interna del sistema
- dice **cosa deve fare** il sistema
- l'insieme dei casi = funzionalità che il sistema offre
- descrizione di un caso d'uso specifica cosa fa il sistema in seguito a uno stimolo
	- può partire da un attore o dal sistema
- caso d'uso corrisponde ad un compito:
	- che l'attore chiede al sistema di eseguire 
	- che il sistema esegue autonomamente
- **Attori**: possibili utenti

## Elementi dei casi d'uso
### Subject (confini del sistema)
- Il limite tra ciò che è interno al sistema e ciò che è esterno
- rettangolo = perimetro che delimita il sistema
- quello che è interno ai confini sarà:
	- progettato
	- realizzato
	- verificato e validato

### Attore
- **ruolo** che l'utente del caso d'uso svolge nell'interagire col sistema
- attori sono **esterni** al sistema
- un attore può essere:
	- classe di persone fisiche
	- altro sistema software
	- hardware esterno 
- **primario**: perseguono lo scopo
	- può fornire lo stimolo che avvia il caso d'uso
	- interagisce dopo che il caso d'uso è stato avviato
- **secondario**: attori con cui il sistema interagisce per svolgere con successo il caso d'uso
>[!example]
>Nell'esempio precedente:
>- cliente = attore primario
>- cassiere = attore secondario
### Caso d'uso
+ sequenza di azioni
+ unità di lavoro utile che sistema esegue in seguito all'evento innescato dal caso d'uso
	+ stimolato dall'attore primario per eseguire un compito che il sistema deve eseguire
	+ sistema può iniziare caso d'uso e interagire con uno o più attori esterni per eseguire un compito
>[!example]
>Nell'esempio precedente:
>caso d'uso  = Acquista Prodotti

![[materie/anno_2025-2026/ingegneria_del_software/assets/casi_d_uso.jpg]]

- un attore può partecipare a più casi d'uso
- ci sono più clienti quindi potrebbero esserci più attori
- stessa persona può ricoprire ruoli diversi = interpretare più attori
![[materie/anno_2025-2026/ingegneria_del_software/assets/casi_d_uso_2.jpg]]
## Descrizione scenari
### Scenari
Descrivere molteplici scenari.
- Sequenza di **azioni/interazioni** fra sistema e attori
>[!example] Caso d'uso "Effettua Ordine"
>1. il cliente richiede l'elenco dei prodotti
>2. sistema propone i prodotti disponibili
>3. cliente sceglie i prodotti che desidera
>4. sistema fornisce il costo totale dei prodotti selezionati
>5. cliente conferma l'ordine
>6. sistema comunica l'accettazione dell'ordine

- attenzione rivolta all'**interazione** non alle attività interne al sistema
- definisce cosa accade nel sistema in seguito all'evento di innesco
	- come e quando caso d'uso inizia
	- chi lo inizia
	- interazione tra attori e casi d'uso
	- cosa viene scambiato
	- come e quando c'è bisogno di dati memorizzati o di memorizzare dati
	- come e quando il caso d'uso termina
#### Stili di descrizione scenari
- **testuale**: flusso chiaro di eventi da seguire
- **diagrammatici**: diagrammi UML di stato, di sequenza, di interazione

- espresso come sequenza di **passi** numerati
	- ciascun passo corrisponde a un'interazione tra un attore e il sistema
	- il passo deve essere espresso con una frase semplice che indichi:
		- chi lo sta eseguendo
		- qual è il suo intento

- **Scenario principale di successo**: descrive il flusso principale
- **Percorsi alternativi**: possono essere sia di successo che di insuccesso
	- numero del passo in cui si discosta dallo scenario principale
	- condizione deve essere soddisfatta per scatenare tale percorso
	- al termine rientra nel flusso principale
## Pre-Condizioni e Post-Condizioni
**Pre Condizioni**: ciò che il sistema deve assicurarsi prima di eseguire il caso d'uso
**Post Condizioni**: ciò che il sistema deve garantire al termine del caso d'uso

## Descrizione di un caso d'uso

+ Per ogni caso d'uso è opportuno documentare gli scenari (con una scheda strutturata per ciascun scenario)

### IF, WHILE e FOR
Usati per racchiudere gruppi di passi che devono essere ripetuti.

- non devono essere indicati dettagli che rivelino le scelte di progetto del software
- essere il più astratti possibile

# Relazioni fra attori e fra casi d'uso
- attore specializzato conserva le proprietà del generale 
- freccia parte dall'attore specializzato e punta all'attore generale

## Generalizzazione di attori
- permette di astrarre ruoli comuni a più attori
- permette di semplificare i diagrammi

## Relazioni fra casi d'uso
- **Generalizzazione**
- **Inclusione**
- **Estensione**

- simile alla generalizzazione fra classi nella programmazione OO
- caso d'uso generale = diversi casi d'uso simili
- caso d'uso specializzato:
	- eredita comportamento e significato dal generale
	- può aggiungere passi o modificare il comportamento del generale
### Inclusione fra casi d'uso
- formalizza i casi in cui più casi **includono** una serie di azioni comuni
- **comportamento comune a più casi d'uso**
	- diventa caso d'uso incluso nei casi d'uso di partenza
	- caso d'uso base è **incompleto** senza il caso incluso
- Graficamente: dipendenza stereotipata << include >> che parte dal caso base e arriva al caso incluso
- inclusione non contiene info sull'ordine dei casi d'uso
- caso incluso = sequenza di azioni che è eseguita una o più volte dai casi d'uso includenti
>[!tip]
Se un caso d'uso **generale** include un altro caso d'uso le sue **specializzazioni ereditano** tale inclusione

## Estensione

- modella una sequenza opzionale di eventi oppure casi eccezionali
- definisce un nuovo caso che **estende** quello di partenza e varia il comportamento **normale**
- rappresentato con << extend >> che parte dall'estensione e arriva al caso base

+ non contiene informazioni sull'ordine dei casi d'uso
+ estensioni potrebbero essere accessibili **direttamente** da un attore
+ comunicazione tra attore e caso d'uso esteso

# Tutorial Diagrammi
## 1. Definisci confini
- Quali responsabilità rientrano nei confini del sistema che stiamo modellando ?
>[!example] Pagamento alla cassa automatica
>- Stiamo modellando solo la cassa automatica ed il sistema di autorizzazione delle carte di credito è esterno?
>- Oppure la responsabilità delle autorizzazioni ai pagamenti rientra nei confini del sistema?

## 2. Identifica attori
- **Identificare** attori che interagiscono con il sistema
	-  Identifica gli attori che necessitano del sistema per svolgere qualche compito
	- Identifica gli attori cui il sistema si rivolge per svolgere qualche compito
- **raggruppare** persone secondo i **ruoli**
- identificare altri sistemi software e dispositivi esterni che interagiscono con il sistema (altri attori anche)
- considerare funzionalità e compiti di supporto al sistema

## 3. Identifica i casi d'uso
Per ogni attore:
1. Identifica compiti e funzioni
	- identifica i compiti o funzioni di più basso livello che l'attore deve essere in grado di eseguire
	- identifica i compiti che il sistema richiede che l'attore esegua
2. Raggruppa compiti e funzioni in casi d'uso
## 4. Definisci il diagramma dei casi d'uso
- Il diagramma contiene le relazioni tra attori e casi d'uso
- Ogni attore deve partecipare ad almeno un caso d'uso
- Ogni caso d'uso deve avere almeno un attore con cui comunica
- Se due attori partecipano agli stessi casi d'uso considera la possibilità di combinarli in un unico attore

## 5. Struttura i casi d'uso

- Identifica relazioni di estensione
	- specializza i casi d'uso con molti scenari **alternativi**
	- collega i nuovi casi d'uso a quelli di partenza mediante relazione << extend >>
- Identifica le relazioni di inclusione
	- **estrai** parti comuni in casi d'uso diversi
	- **collega** i casi d'uso che condividono una parte comune al nuovo caso d'uso rappresentante il comportamento condiviso mediante l'associazione << include >>
