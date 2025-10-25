---
title: "5 Tipologie di Requisiti"
aliases: ["5 Tipologie di Requisiti"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "5-tipologie-di-requisiti"]
created: 2025-10-20
---
# Tipologie di requisiti

+ definire
	+ quali **esigenze del cliente** il sistema deve fornire
	+ entro quali **vincoli operativi**
+ se il sistema funziona correttamente ma **non rispetta i vincoli**: non sarà di interesse per il cliente
>[!definition]
>Requisito
>>Descrizione di qualcosa che il sistema dovrà fare oppure di una proprietà o vincolo operativo che si desidera per il sistema.

+ Formulazione astratta e ad alto livello, spesso in linguaggio naturale
+ specifica dettagliata

## Ingegneria dei requisiti
+ definizione così ampia è necessaria poiché **un requisito può avere vari scopi** nella pratica:
	+ può essere la base per una gara fra fornitori concorrenti
		+ deve essere aperto ad interpretazioni diverse
	+ può essere la **base del contratto** stesso
		+ deve essere definito in dettaglio
+ **ingegneria dei requisiti** è:
	+ il processo di ricerca
	+ analisi
	+ documentazione
	+ verifica dei requisiti
+ tale processo è finalizzato a stabilire
	+ le funzionalità del software
	+ i vincoli operativi
	+ i vincoli di sviluppo

+ l'ingegneria dei requisiti è fondamentale:
	+ perché errori nella definizione dei requisiti si propagano nei passi successivi del processo di sviluppo
	+ il costo per porvi rimedio cresce
+ correggere errori nei requisiti **in fase operazionale** costa dalle 50 alle 200 volte in più che in **fase di analisi e specifica dei requisiti**

## Requisiti utente
+ frasi in linguaggio naturale (anche diagrammi)
	+ relative alle funzionalità che il sistema deve fornire e i suoi vincoli operativi
+ ad **alto livello** (possono contenere dettagli)
+ descritti usando linguaggio naturale e diagrammi:
	+ **comprensibili a tutti gli utenti**
	+ anche utenti privi di conoscenze tecniche

## Requisiti sistema
+ documento strutturato che fornisce **descrizione dettagliata**:
	+ delle funzionalità del sistema
	+ dei vincoli operativi
+ definisce cosa dovrà essere sviluppato
+ può essere parte del contratto fra **cliente e sviluppatore**

>[!example]
>Requisito utente può essere espanso in più requisiti di sistema:
>**Requisito utente**:
>1. sistema genererà mensilmente dei rapporti che riportano il costo dei farmaci prescritti da ciascuna clinica durante il mese
>**Requisiti di Sistema**:
>- nell'ultimo giorno lavorativo di ogni mese, dovrà essere generata una sintesi dei farmaci prescritti, loro costo e le cliniche che li hanno prescritti
>- sarà creato un rapporto per ciascuna clinica; dovranno essere elencati i nomi dei singoli farmaci, il numero totale di prescrizioni, numero delle dosi prescritte e il costo totale dei farmaci prescritti
>- accesso ai rapporti dei costi dei farmaci dovrà essere limitato agli utenti autorizzati, come indicato nella lista di controllo degli accessi

## Lettore delle specifiche dei requisiti
+ lettori dei requisiti utente non si occupano del modo in cui il sistema sarà implementato
+ lettori dei requisiti del sistema hanno bisogno di sapere con più precisione **che cosa il sistema dovrà fare**

# Requisi funzionali e non funzionali

## Tipi di requisiti
+ **Requisiti funzionali**
	+ ciò che il sistema dovrebbe fare:
		+ reagire agli input in vari scenari di utilizzo
+ **Requisiti non funzionali**
	+ vincoli sulle funzionalità offerte dal sistema
	+ vincoli sul processo di sviluppo
	+ **requisiti di qualità**
>[!tip]
>Requisiti non sono indipendenti tra loro (possono generare o limitare altri requisiti)

>[!example]
>"Limitare l'accesso agli utenti autorizzati", è un requisito non funzionale ma introduce requisiti funzionali come le funzioni di autenticazione e recupero password.

## Requisiti funzionali
+ descrivono le funzionalità che dovranno essere offerte dal sistema
+ possono essere espressi a due livelli di astrazione
	+ **Requisiti funzionali utente**: descrizioni ad alto livello su ciò che il **sistema farà**
	+ **Requisiti funzionali del sistema**: descrizioni dettagliate delle funzionalità:
		+ input
		+ output
		+ eccezioni

>[!example]
>Sistema per gestire informazioni relative a pazienti di una clinica.
>1. utente deve poter cercare gli appuntamenti nelle liste relative a ciascun medico
>2. sistema deve generare ogni giorno: l'elenco dei pazienti di quel giorno per ogni medico
>3. Tutti i dipendenti della clinica saranno identificati in modo univoco dalla propria matricola (USER_ID) a 8 cifre

## Imprecisione nei requisiti
+ Requisiti imprecisi o ambigui possono essere interpretati in modi diversi da diversi stakeholders
**Punto 1 dell'esempio precedente**
+ cliente intendeva poter navigare tra le liste di tutti i medici (**senza conoscere il nome del medico**)
+ sviluppatore potrebbe intendere che la ricerca verrà fatta specificando prima il nome del medico

## Completezza e consistenza dei requisiti

+ **Completezza**:  tutti i requisiti richiesti dai clienti devono essere **presenti**
+ **Consistenza**: requisiti non devono avere definizioni **contraddittorie** o essere in **conflitto**

+ facile commettere **errori** o **omissioni** in sistemi complessi e di grandi dimensioni
+ Alcune incoerenze possono emergere soltanto durante lo sviluppo del sistema:
	+ specialmente in presenza di molti stakeholder con aspettative differenti e contrastanti

## Requisiti non funzionali
+ non riguardano direttamente le funzionalità del sistema
+ definiscono:
	+ **le proprietà**: affidabilità, tempi di risposta e l'uso della memoria
	+ **vincoli del sistema**: capacità dei dispositivi I/O, rappresentazione dei dati
	+ **vincoli del suo processo di sviluppo**: uso di particolari standard per la documentazione, linguaggi di programmazione specifici,...


## Verificabilità dei requisiti
+ requisiti non funzionali possono essere difficili da definire/verfiicare
+ cliente specifica come **obiettivi generici/vari**:
	+ facilità d'uso, rapida risposta
	+ questi obiettivi causano problemi agli sviluppatori----->libera interpretazione
+ requisiti **verficabili**

>[!example]
>**Obiettivo generico**
>Il sistema deve essere facile da usare per il personale medico e deve essere organizzato in modo tale che gli errori commessi dall'utente siano ridotti al minimo.

>[!example]
>**Requisito verificabile:**
>Il personale medico dovrà essere in grado di usare tutte le funzioni del sistema **dopo due ore di addestramento**; dopodiché il numero medio di errori commessi dagli utenti esperti non dovrà **maggiore di due, per ogni ora di utilizzo del sistema**.

+ i requisiti non funzionali possono essere in conflitto
>[!example]
>- **R1**: un lettore magnetico deve essere installato in ogni computer che si collega al sistema per permettere l'accesso tramite carta d'identità elettronica.
>- **R2**: Il personale medico deve avere la possibilità di accedere al sistema tramite tablet o smartphone, che non sono dotati di lettori magnetici.

## Requisiti di dominio
+ requisiti funzionali/ non funzionali e vincoli derivano dal **dominio applicativo del sistema** (non dalle esigenze degli utenti)
>[!example]
>norme e standard del dominio medico, avionico, ferroviario, ecc...

+ Talvolta le informazioni di dominio sono **ovvie per gli esperti** e quindi vengono tralasciate
+ ingegnere del software potrebbe non conoscere il dominio
	+ quindi potrebbe non capire le caratteristiche dell'ambiente in cui opera il sistema

### Problemi di requisiti di dominio
**Comprensibilità**:
+ espressi nel linguaggio estremamente specializzato del dominio
+ fanno riferimento a concetti specifici del dominio
+ potrebbe non essere immediatamente chiaro
**Esplicitazione**:
+ specialisti del dominio conoscono così bene il dominio stesso, da lasciare fuori dai requisiti informazioni che sembrano ovvie

# Ingegneria dei requisiti

## Tre attività chiave
+ **Deduzione e analisi dei requisiti**
+ **Specifica dei requisiti**
+ **Convalida dei requisiti**

## Modello sequenziale
Sequenzialità sia in avanti che indietro delle tre attività chiave.
![[materie/anno_2025-2026/ingegneria_del_software/assets/Immagine 2025-10-25 171812.png|400]]
## Modello a spirale
Nella pratica il processo è spesso iterativo con fasi interallacciate e non sequenziale, ripetendo le tre fasi iterativamente in maniera sempre più approfondita come una spirale fino ad arrivare alla stipulazione del documento dei requisiti di sistema..
Cresce la conoscenza, si abbassa il rischio e cresce il valore del nostro software.


>[!warning]
>Le definizioni di questo file per i requisiti riguardano per lo più la descrizione classica dei requisiti.
>I requisiti dei processo agili, descritti nel precedente file, potrebbero essere considerati uno spreco di tempo se troppo dettagliati. Inoltre nei metodi agili la specifica dei requisiti non è un'attività separata, ma è considerata come parte dello sviluppo, in base alle priorità dell'utente.

