---
title: "8-Firmata-Influxdb"
aliases: ["8-Firmata-Influxdb"]
tags: [università, "materie", "anno-2025-2026", "internet-of-things", "8-Firmata-InfluxDB"]
created: 2025-11-16
---
# Firmata

>[!definition]
>Firmata
>>Protocollo generico per la comunicazione su porta seriale fra microcontrollori (es. Arduino)e computer host.

Sostanzialmente consente di controllare il microcontrollore da un computer, mediante un **firmware comune**, senza la necessità di dover cambiare quest'ultimo ad ogni progetto.

>[!tip]
>Caricando quindi lo sketch StandardFirmata ci si può dimenticare dell'IDE Arduino e della programmazione a basso livello della scheda, concentrandoci ad implementare la business logic nel linguaggio di programmazione che preferiamo (es. Python).


___

# InfluxDB

>[!definition]
>InfluxDB
>>InfluxDB è un TSDB, ovvero un Time Series DataBase; ottimizzato per la gestione efficiente di dati organizzati come serie temporali.
>>+ Database di tipo NoSQL e memorizza i dati come "punti".

+ Ogni punto è un insieme di coppie **chiave-valore** (fieldset) ed un **timestamp**.
+ Una serie è un insieme di punti raggruppati in base ad un **tagset** (es. insieme di coppie chiave-valore).
+ Le serie sono raggruppate da un **identificatore di misurazione**.

>[!tip]
>InfluxDB risulta quindi molto utile in attività come il monitoraggio di impianti e l'IoT in generale.

### Caratteristiche

+ Database per **serie temporali**.
+ **NoSQL**: ogni campione in una serie è identificato da un **timestamp** unico.
+ **Interfaccia API REST** con linguaggio di query simile ai database relazionali classici:
	+ eroga risposte in **JSON**.
+ Progettato per essere un componente in una serie di servizi interoperabili:
	+ Compito di **archiviare** e **recuperare** i dati delle serie temporali in modo efficiente.
+ Adatto per:
	+ **IoT** (raccolta e archiviazione di dati sensoriali per prendere decisioni in base all'analisi dei dati)
	+ **Monitoraggio data center**.


### Concetti chiave (terminologia)

+ **Misurazione**: 
	+ Simile al concetto di tabella in un database relazionale classico, contenitore per tag e campi.
	+ Esempio: `temperatura`
+ **Tag**:
	+ Indicano come i dati vengono indicizzati e ricercati: coppia chiave/valore di tipo stringa.
	+ Esempio: `source = 'Arduino Uno'`
+ **Campi (Field)**:
	+ Indicano i dati che vengono memorizzati: chiave stringa con valore di tipo long, double, bool, string....
	+ Esempio: `value = 23`
+ **Politica di conservazione (Retention Policy)**:
	+ Per quanto tempo conservare i dati e cosa farne man mano che invecchiano.
	+ Esempio: Politica "one_day_by_hour": durata 1 d, durata di frammento (shard) 1h, ovvero conserva questi dati per un giorno, crea un nuovo frammento di dati per ogni ora.
+ **Serie (Series)**:
	+ Raccolta di dati che condividono una misurazione (e di conseguenza una politica di conservazione), un tagset ed una chiave di campo (field).
+ **Insieme (Set)**:
	+ Contiene campioni con timestamp univoci e dati di campo arbitrari

