---
title: "10-Distribuzione"
aliases: ["10-Distribuzione"]
tags: [università, "materie", "anno-2025-2026", "internet-of-things", "10-Distribuzione"]
created: 2025-11-16
---

# Distribuzione

>[!problem]
>In seguito allo sviluppo di un prototipo si pone il problema della sua **distribuzione** ed **installazione**.

+ Servono alti software (es. DBMS) da incapsulare nella distribuzione per il corretto funzionamento del software.
+ Serve quindi uno strumento che impacchetti tutte le componenti necessarie per la distribuzione, installazione ed esecuzione del progetto in altre macchine.

## Docker

>[!definition]
>Docker
>>Piattaforma che consente la distribuzione del software e dell'ambiente utile al suo funzionamento in unità chiamate **container**.
>>Permette quindi di impacchettare un'applicazione con tutte le parti di cui ha bisogno, come librerie e altre dipendenze in un unico pacchetto

### Caratteristiche
+ Piattaforma leggera, aperta e sicura
+ Funziona in modo nativo si Linux o Windows Server
+ Si basa sul concetto di **immagine** e **contenitore**.

### Virtualizzazione
>[!definition]
>Virtualizzazione
>>Possibilità di astrarre le componenti hardware, cioè fisiche, degli elaboratori al fine di renderle disponibili al software in forma di risorsa virtuale.

>[!tip]
>Tramite questo processo è quindi possibile installare sistemi operativi su hardware virtuale.

>[!definition]
>Macchina virtuale
>>L'insieme delle componenti hardware virtuali (Disco fisso, RAM, CPU, scheda di rete) prende il nome di macchina virtuale

+ La virtualizzazione consiste quindi nella creazione di una rappresentazione software di qualcosa, come applicazioni virtuali, server, risorse di archiviazione e reti.

>[!definition]
>Containerization
>>La virtualizzazione a livello di sistema operativo.

+ Essa si riferisce a una funzionalità del sistema operativo in cui il kernel consente l'esistenza di più istanze isolate dello spazio utente.

>[!tip]
>Tali istanze, dette container, possono apparire come veri computer dal punto di vista dei programmi in esecuzione in essi.

>[!warning]
>I programmi in esecuzione all'interno di un contenitore possono vedere solo i contenuti e i dispositivi assegnati ad esso.

+ Istituzione dei CaaS: Containers as a Service

___

### Docker container
+ Consente di isolare le applicazioni l'una dall'altra.
+ Condivide lo stesso kernel del sistema operativo.

### Docker Image
>[!definition]
>Image
>>Un'immagine è un modello di sola lettura contenente le specifiche per la creazione di un contenitore.

+ è possibile creare le proprie immagini o utilizzare solo quelle create da altri e pubblicate in un registro.

### Docker Engine
Applicazione client-server con i seguenti componenti:
+ **Server daemon**
+ **API di tipo REST** che specifica le interfacce che i programmi possono usare per comunicare con il demone (daemon)
+ **client di tipo CLI** (Command Line Interface): comando docker

### Docker Registry
+ Un registro docker memorizza le immagini Docker.
+ **Docker Hub** è un registro pubblico che chiunque può utilizzare.
+ è comunque possibile utilizzare un registro privato.