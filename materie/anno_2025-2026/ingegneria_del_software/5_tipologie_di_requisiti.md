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
>Requisiti sono indipendenti tra loro (possono generare o limitare altri requisiti)

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


