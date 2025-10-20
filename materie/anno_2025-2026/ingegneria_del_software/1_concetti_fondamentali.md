---
title: "1 Concetti Fondamentali"
aliases: ["1 Concetti Fondamentali"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "1-concetti-fondamentali"]
created: 2025-10-20
---

>[!definition]
>Software
>>insieme di **programmi** per computer e la relativa **documentazione**

>[!tip]
>Anche la documentazione prodotta durante lo sviluppo, come, modelli di progetto, manuali utente, siti web di supporto.

Economie di tutte le nazioni industrializzate dipendono dal software.
Sempre più sistemi controllati dal software.

# Tipologie di software professionale
## Software generico
+ prodotto **autonomamente** da una organizzazione per incontrare le necessità dei clienti
+ produttore **ha controllo sulle specifiche** del software
## Software su richiesta
+ Software sviluppato da un'organizzazione su commissione di uno specifico cliente
+ produttore deve attenersi alle specifiche indicate dal cliente
## Software personalizzabile
+ sistema generico adattato alle richieste di un particolare cliente
+ Esempio: SAP è un ERP
>[!definition]
>Enterprise Resource Planning
>> Sistema generico utile a più aziende. 
>> Viene adattato a una specifica azienda inserendo le informazioni relative alle regole e ai processi aziendali, ai report richiesti ecc...

# Complessità e costi

Software può diventare estremamente complesso, difficile da capire e costoso da modificare

+ Nuove tecniche e tecnologie permettono di sviluppare software sempre più grandi e complessi
+ Lo sviluppo software richiede sempre meno tempo 
+ mercato in continua evoluzione ----> rilascio rapido dei sistemi
+ Successo o insuccesso di un progetto software è legato spesso all'applicazione dell'ingegneria del software per garantire la qualità del software

# Sviluppo professionale di software di qualità

## Sviluppo personale
(Sviluppato durante l'apprendimento delle basi dell'informatica)
+ difficilmente il software sarà riusato in futuro da altri utenti
+ non necessario scrivere una guida, né documento di progetto
+ non necessario raggiungere alti livelli di qualità
## Sviluppo professionale
+ software sarà usato da altre persone diverse dai propri sviluppatori 
+ sviluppo in team e, quindi, probabilmente il software sarà modificato e mantenuto da altri sviluppatori
+ software deve possedere caratteristiche di qualità

## Qualità del software
Software di qualità deve fornire le **funzionalità** ma anche le **prestazioni richieste**.

### Caratteristiche:
+ **Accettabilità:** 
	+ software deve essere **accettato** dai suoi utenti
	+ **comprensibile**
	+ **usabile** e **compatibile** con altri sistemi utilizzati dagli utenti
+ **Fidatezza e Protezione:** 
	+ software non deve causare **danni fisici** o **economici**
	+ **utenti malintenzionati** non devono poter **accedere** o **danneggiare** il sistema
+ **Efficienza:** non deve **sprecare** le risorse del sistema
+ **Mantenibilità:** software deve poter **evolvere** per soddisfare le nuove richieste dei clienti
>[!tip]
**Caratteri qualitativi** dipendono dalla sua **applicazione** 

>[!example]
>+ Sistema di controllo aereo **deve essere sicuro**
>+ Gioco interattivo **deve rispondere velocemente**
>+ Un software che risiede su piccoli processori embedded **deve essere molto efficiente**
>+ Software utilizzato in una grande azienda con sedi dislocate **deve essere mantenibile**

# Ingegneria del software
## Nascita dell'ingegneria del software
+ Negli anni 70 i costi del software in un PC aumentano rispetto ai costi dell'hardware
+ costi della manutenzione **maggiori** di quelli di sviluppo
>[!warning] **Problema:** 
sviluppare software facilmente mantenibile in maniera economicamente vantaggiosa.
+ Gennaio 1969 Garmisch **Crisi del Software**
	+ Sistemi software sempre più **complessi**, **difficili da mantenere**, **inaffidabili**, più **costosi** del previsti, rilasciati in **ritardo**
>[!tip] Soluzione alla crisi
>Adottare approcci ingegneristici alla produzione del software.
## Ingegneria del software
+ Si occupa di tutti gli aspetti della produzione di software
+ Non basta far funzionare il programma
	+ bisogna rispettare i vincoli organizzativi e di budget

### Organizzazione e creatività
+ Sono richiesti compromessi, imposti da vincoli
+ combinazione tra approccio sistematico e organizzato (processo software) e capacità creative (metodo più adatto tra le possibili alternative)

# Processi Software
>[!definition]
>Processo software
>>> insieme di attività che porta alla creazione o all'evoluzione di un prodotto software

+ **Acquisizione, analisi e specifica dei requisiti:** clienti e ingegneri definiscono le funzionalità e i vincoli operativi del software
+ **Progettazione e Sviluppo:** progettazione e programmazione
+ **Verifica e Validazione:** che il software sia esattamente ciò che il cliente richiede
+ **Evoluzione:** software viene modificato per soddisfare eventuali cambiamenti dei requisiti del cliente e del mercato
## No free lunch
+ non esiste soluzione che risolve tutti i problemi
+ differenti tipi di software richiedono differenti processi di sviluppo che condividono le quattro attività fondamentali
+ non esistono tecniche e metodi che possono essere universalmente utilizzati per tutti i tipi di software

## Metodi e strumenti

+ **Metodi**
	+ approcci strutturati per sviluppare software di qualità a costi contenuti ed entro i tempi
	+ forniscono una guida alle attività dei processi e alla relativa organizzazione
+ **Strumenti:**
	+ sistemi software usati per aiutare le attività dei processi software (analisi, modellazione, debugging, testing)

## Sfide per processi software
+ **Diversità:** metodi per produrre software eseguito su dispositivi **eterogenei**
+ **Consegna**: consegna del software in **tempi rapidi** rispondendo ai cambiamenti del mondo
+ **Fiducia:** tecniche che dimostrino all'utente che può fidarsi del software, garantendo la sicurezza
+ **Scala:** software deve essere distribuito su molti sistemi diversi

## Principi fondamentali dell'ingegneria del software

+ Metodi specifici, tecniche e strumenti utilizzati dipendono da:
	+ l'organizzazione che sviluppo il software
	+ dal tipo di software
	+ dalle persone coinvolte nel processo di sviluppo
+ Non ci sono metodi di ingegneria del software universali che sono applicabili a tutti i sistemi e a tutte le aziende
+ Concetti fondamentali sono **indipendenti dal linguaggio di programmazione** utilizzato

## Processo chiaro
+ Il processo dipende dal tipo di software che sarà sviluppato
+ Indipendentemente dal processo specifico deve essere definito e condiviso
+ persone coinvolte devono avere idee chiare sulle proprie responsabilità
	+ cosa sarà prodotto
	+ le fasi che le coinvolgono
## Fidatezza e prestazioni
+ Fidatezza e prestazioni sono importanti per tutti i sistemi
+ Software dovrà comportarsi come previsto:
	+ senza fallimenti
	+ essere pronto all'uso quando richiesto
+ Software dovrà essere protetto il più possibile contro attacchi esterni
+ Sistema dovrà essere eseguito senza spreco di risorse

## Requisiti

+ Importante capire e gestire la specifica e requisiti (cosa deve fare il software)
+ Sapere cosa si aspettano i clienti e utenti
+ Gestire le loro aspettative
+ Essere rilasciato un sistema **utile** entro i costi e tempi previsti

## Riuso
+ Occorre utilizzare con efficienza le risorse esistenti
+ Riusare software che è già stato sviluppato
>[!warning]
>Non portare dietro i bug del codice già esistente

## Modello di processo software
+ Ciascuna organizzazione utilizza il proprio processo
>[!definition]
>**Modello di processo software**: 
>>Rappresentazione semplificata e astratta che descrive l'intero ciclo di vita del software.

**Lifecycle-based**