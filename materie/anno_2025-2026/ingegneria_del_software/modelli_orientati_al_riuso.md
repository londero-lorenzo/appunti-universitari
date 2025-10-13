---
title: "Modelli Orientati Al Riuso"
aliases: ["Modelli Orientati Al Riuso"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "modelli-orientati-al-riuso"]
created: 2025-10-13
---
# Modelli orientati al riuso

Riuso non avviene soltanto in maniera informale
+ Approccio orientato al riuso di:
	+ Componenti software riutilizzabili
	+ Interi sistemi
+ Sfrutta **framework di integrazione** per comporre i componenti
+ **Componenti riutilizzabili** e **COTS** possono essere configurati per adattare il loro comportamento ai requisiti utente
+ Approccio diffuso grazie ad appositi standard per la specifica dei componenti 



Requisiti essenziali sono specificati in maniera non eccessivamente dettagliata (breve descrizione dei requisiti e delle funzionalità essenziali del sistema)

+ Vengono ricercati componenti e sistemi che possono fornire le funzionalità specificate nei requisiti
+ Candidati vengono valutati per vedere se soddisfano i requisiti essenziali e se sono disponibili per essere utilizzati

+ requisiti vengono perfezionati utilizzando le informazioni sulle applicazioni e sui componenti riutilizzabili che sono stati trovati
+ specifica viene aggiornata con i requisiti perfezionati

Se è disponibile un sistema di applicazioni pronto all'uso che soddisfa i requisiti, esso può essere configurato per creare il nuovo sistema

## Vantaggi
+ Riduce la quantità di software da sviluppare ex novo
+ Riduco costi e rischi
+ Maggiore velocità nella consegna

## Svantaggi
+ Compromessi nei requisiti ----> Sistema potrebbe non soddisfare tutte le reali necessità degli utenti
+ Evoluzione dei componenti riutilizzabili non è controllata direttamente

# Modelli trasformazionali
+ Le specifiche sono definite attraverso linguaggi formali
	+ specifiche algebriche (per tipi di dato astratto)
	+ Modelli di stato
+ Uso di tecniche di **model checking** per provare la correttezza
+ Specifiche formali trasformate automaticamente in software finale

+ Requisiti specificati formalmente nelle fasi di analisi
+ Comprensione chiara e non ambigua dei requisiti
+ specifiche sono verificate automaticamente prima di essere trasformate da opportuni strumenti

+ descrizione formale trasformata in una meno atratta

## Problemi
+ Necessità di competenze specifiche in linguaggi formali
+ Difficile specificare formalmente alcune parti del sistema
+ Difficoltà del cliente nella convalida dei requisiti

## Applicabilità
+ Non adatti per sistemi di grandi dimensioni
+ Usati per parti critiche:
	+ validità dimostrata **by construction** (es. ho componente critico)

