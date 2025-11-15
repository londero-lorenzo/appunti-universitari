---
title: "Schema-Delle-Slide"
aliases: ["Schema-Delle-Slide"]
tags: [università, "materie", "anno-2025-2026", "internet-of-things", "Schema-delle-Slide"]
created: 2025-11-15
---
# Suddivisione degli argomenti delle slide e come si intrecciano tra di loro

## Fondamenti, Applicazioni e Architettura

### Fondamenti e Applicazioni

+ **Introduzione** (slide 1): Traccia la storia dell'IoT e ne stabilisce le fasi (dimenticabile)

+ **Applicazioni** (slide 2): Esplora gli ambienti di sviluppo dell'IoT, come le Smart Home, Smart City, Automotive, Industry 4.0. Discute anche le criticità fondamentali di privacy e sicurezza.

### Architettura

+ **Architettura** (slide 4): definisce i modelli teorici. Introduce i protocolli di comunicazione nei diversi livelli, i modelli di comunicazione (Request-Response, Push-Pull, Publish-Subscribe) ed esplica i diversi livelli dell'IoT.


>[!tip]
>**Intreccio:**
>L'insieme di questi tre file creano il contesto.
>L'architettura fornisce i modelli che verranno poi implementati concretamente (slide 5 che adesso vediamo) per realizzare le applicazioni introdotte nelle prime due slide.


___

## Flusso dei dati

### Pubblicazione

+ **GPS Tracker** (slide 3): Funge da caso di studio che anticipa molti temi.
  Introduce lettura di porte seriali e creazione di un server socket per pubblicare i dati

+ **Pubblicazione dati** (slide 5): Analizza prima i socket, per poi evidenziarne i limiti. Introduce quindi MQTT come protocollo standard basato sul modello Publish/Subscribe. Include approfondimenti sulla libreria Python per MQTT e sul broker Mosquitto.

### Storage dati

+ **InfluxDB** (seconda parte slide 8): Introduce InfluxDB come un Time Series database, specializzato e ottimizzato per archiviare i dati IoT, tipicamente serie temporali.

### Presentazione dati

+ **Grafana** (slide 6): Introduce Grafana come la piattaforma per l'analisi e il monitoraggio, specializzata nella creazione di dashboard. Grafana si collega a sorgenti dati (come MySQL o PostgreSQL) per interrogare e visualizzare i dati sia storici che in tempo reale.


>[!tip]
>**Intreccio:**
>I dati acquisiti dall'hardware (slide 7-8-9 che adesso vediamo) vengono pubblicati tramite un protocollo (es. MQTT, slide 5) e archiviati in un database (InfluxDB, slide 8; MySQL/PostgreSQL, slide 6). Infine, una piattaforma (Grafana, slide 6) legge da questi database per presentare i dati all'utente.


___

## Hardware e acquisizione dati

+ **Arduino** (slide 7 e 8): Introduce il microcontrollore Arduino. Viene introdotta anche la libreria pyFirmata che permette di controllare Arduino direttamente da Python, e ciò rende la scheda un'estensione hardware del PC.

+ **Rasperry Pi** (slide 9): Introduce il Rasberry Pi come un single-board computer. 

>[!tip]
>**Intreccio:**
>Mostrano come i dati vengono generati. Arduino presentato come soluzione per acquisizione e attuazione semplice, Raspberry come soluzione per compiti più compessi che richiedono un sistema operativo.


---
## Distribuzione e Deployment

+ **Distribuzione** (slide 10 e 11): Viene introdotto Docker come soluzione per la containerizzazione. Esso ermette di impacchettare un'applicazione con tutte le sue dipendenze in un container isolato. Viene poi creata una rete Docker che permette a diversi container (es. Grafano InfluxDB e script Python) di comunicare tra loro. Viene poi introdotto docker-compose, che definisce l'intero stack di servizi in un unico file, permettendo di avviarli e fermarli tutti insieme con un solo comando.

>[!tip]
>Questo argomento è la sintesi. L'hardware (Raspberry) viene utilizzato per ospitare l'intera pipeline software (InfluxDB e Grafana) precedentemente discussa, utilizzando una tecnologia di distribuzione moderna (Docker)

