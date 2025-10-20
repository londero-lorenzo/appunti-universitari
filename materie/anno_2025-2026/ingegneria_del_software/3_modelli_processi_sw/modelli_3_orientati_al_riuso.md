---
title: "Modelli 3 Orientati Al Riuso"
aliases: ["Modelli 3 Orientati Al Riuso"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "modelli-3-orientati-al-riuso"]
created: 2025-10-20
---
# Modelli orientati al riuso

Riuso non avviene soltanto in maniera informale
+ Approccio orientato al riuso di:
	+ Componenti software riutilizzabili
	+ Interi sistemi
+ Sfrutta **framework di integrazione** per comporre i componenti
+ **Componenti riutilizzabili** e **COTS** possono essere configurati per adattare il loro comportamento ai requisiti utente
+ Approccio diffuso grazie ad appositi standard per la specifica dei componenti 

![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=vYdmZkIa]]
## Specifica dei requisiti

Requisiti essenziali sono specificati in maniera non eccessivamente dettagliata 
>[!example]
> breve descrizione dei requisiti e delle funzionalità essenziali del sistema

## Ricerca del software / Valutazione del software
+ Vengono ricercati **componenti e sistemi** che possono fornire le funzionalità specificate nei requisiti
+ Candidati vengono **valutati** per vedere se soddisfano i requisiti essenziali e se sono disponibili per essere utilizzati
## Perfezionamento dei requisiti
+ **requisiti perfezionati** utilizzando le informazioni:
	+ sulle applicazioni
	+ sui componenti riutilizzabili che sono stati trovati
+ **specifica** viene aggiornata con i requisiti perfezionati
## Configurazione del sistema delle applicazioni
Se è disponibile un **sistema di applicazioni** pronto all'uso che soddisfa i requisiti, esso può essere configurato per creare il nuovo sistema.

## Adattamento e sviluppo dei componenti / Integrazione del sistema
Se non è disponibile un sistema: singoli componenti riutilizzabili possono essere modificati e integrati con nuovi componenti appositamente sviluppati per creare il sistema finale.
## Vantaggi
+ Riduce la **quantità** di software da sviluppare ex novo
+ Riduco **costi e rischi**
+ **Maggiore velocità** nella consegna
## Svantaggi
+ Compromessi nei requisiti ----> Sistema potrebbe non soddisfare tutte le reali necessità degli utenti
+ Evoluzione dei componenti riutilizzabili non è controllata direttamente


