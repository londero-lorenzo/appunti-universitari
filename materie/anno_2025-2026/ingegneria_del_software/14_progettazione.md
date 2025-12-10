---
title: "14 Progettazione"
aliases: ["14 Progettazione"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "14-progettazione"]
created: 2025-12-10
---
# Progettazione del software
## Attività di progettazione
Collegamento tra l'ingegneria dei requisiti e la progettazione di dettaglio di ciascun componente.

## Progettazione: finalità
>[!definition]
>Progettare
>>Eseguire un processo di risoluzione di un problema il cui obiettivo è trovare e descrivere un modo:
>>- per implementare i requisiti funzionali
>>- rispettando i vincoli imposti dai requisiti non funzionali
>>- in conformità con una serie di principi di buona qualità

## Decisioni di progettazione
- progettista affronta una serie di problemi di progettazione
- ciascun problema ha normalmente una serie di soluzioni alternative **design options**
- progettista effettua una serie di **design decision** per risolvere ciascun problema
	- scegliendo la migliore fra le alternative possibili in base ai requisiti del sistema
	- dipende anche dal background e l'esperienza degli architetti
>[!definition]
>Design space:
>>Insieme dei possibili progetti che saranno implementabili scegliendo tra le varie alternative.

## Strategie: 

### Top-down
1. Progettare la struttura di altissimo livello del sistema
>[!example] Definire l'architettura del software e il tipo di database che sarà impiegato.

2. Si procede gradualmente con decisioni più dettagliate riguardanti aspetti di basso livello:
	- formato dei dati
	- algoritmi implementati
	- interfacce utente

### Bottom-Up
1. Si progettano i componenti basilari di basso livello e si decide poi come collegarli insieme per ottenere i componenti di più alto livello.
2. Si procede per livelli di astrazione sempre più alti

- Processo di progettazione = serie di decisioni da prendere
- Non esiste un processo unico: 
	- dipende dal sistema
	- dipende dalle conoscenze ed esperienze del team
- Misto dei due approcci Top-Down e Bottom-Up
	- Top-Down per definire la struttura del sistema
	- Bottom-Up progettare componenti riusabili in altri punti del sistema

# Progettazione architetturale
- comprendere come organizzare il software 
- identifica i componenti strutturali del sistema
- relazioni e interfacce
- output  = modello architetturale che descrive come è organizzato il sistema e come comunicano i componenti
## Architettura, requisiti e prestazioni
- Architettura influisce su **prestazioni, robustezza, distribuzione e manutenibilità** di un sistema
- Singoli componenti implementano i **requisiti funzionali** di un sistema
	- l'architettura ha un'influenza predominante sulle caratteristiche non funzionali

### Requisiti non funzionali e stili architetturali
- **Performance:** preferire componenti grandi, localizzando le operazioni critiche e minimizzare le comunicazioni
- **Protezione:** usare architettura a strati, posizionando le risorse critiche negli strati interni (con convalida ad ogni strato)
- **Sicurezza funzionale**: concentrare le funzionalità critiche per la sicurezza in un numero limitato di sottosistemi per fornire meccanismi di protezione e ridurne i costi
- **Disponibilità:** componenti ridondanti e meccanismi per la tolleranza ai guasti
- **Manutenibilità**: utilizzare componenti piccoli facilmente sostituibili modificabili
## Progettazione architetturale e Agilità
Attività di progettazione architetturale può scontrarsi con i seguenti principi agili:
- **Documentazione minima:** necessità di produrre un progetto architetturale è accettata nei metodi agili nelle fasi inziali del processo di sviluppo
- **Refactoring:** rifattorizzare i singoli componenti ma rifattorizzare l'intera architettura è costoso poiché ciascun cambiamento all'architettura può interessare numerosi componenti
## Vantaggi di progettazione esplicita
- fornisce una presentazione del sistema ad alto livello che consente il confronto tra stakeholder
- durante la progettazione è analizzata la conformità del sistema ai requisiti non funzionali
- modello architetturale può essere riusato per sistemi con requisiti simili
# Pattern architetturali
- architettura può essere **riusabile** per un insieme di sistemi
- sistemi nello stesso dominio = architetture simili che riflettono concetti fondamentali
- analizzare cosa hai in comune con le classi di applicazioni più generali e stabilire quanto può essere riutilizzato 
>[!example] Linee di prodotti sono costruite attorno a un'architettura di base con varianti che specificano specifiche richieste dei clienti.

## Concetto di pattern
- pattern = soluzioni a problemi di progettazione comuni
- pattern architetturale = descrizione dell'organizzazione del sistema utilizzata in diversi sistemi software
## Vantaggi
### Riuso
- della conoscenza/esperienza di progettazione
- raramente i problemi sono nuovi e unici
### Presentazione e comunicazione
- stabiliscono una terminologia comune e condivisa che facilita la comunicazione
- prospettiva di alto livello del sistema
- permettono la comprensione e la discussione del progetto architetturale senza gestire i dettagli della progettazione
## Utilizzo dei pattern
- si deve conoscere gli schemi architetturali più comuni (punti di forza e debolezza)
- pattern descrive una **buona pratica** già usata con successo e verificata in altri sistemi
- includere le informazioni su quando il suo utilizzo è appropriato e i dettagli sui suoi vantaggi e svantaggi
- descritti usando template testuali o diagrammi 
## Multi-Layer
- decomposizione **gerarchica** di un sistema in un insieme ordinato di layer
- layer = raggruppamento di sottosistemi che forniscono servizi correlati (utilizzando anche servizi di altri layer)
- sistema complesso può essere costruito stratificando strati aventi via via crescenti livelli di astrazione
- ciascun livello comunica solo con il livello sottostante e non ha conoscenza dei layer dei livelli più alti
- livello più alto vede quello più in basso come un insieme di servizi

### Separazione
Gli elementi che forniscono servizi correlati sono raggruppati nello steso layer e separati dagli altri elementi

### Indipendenza
Possibile progettare e modificare uno strato indipendentemente dagli altri, purché vengano rispettate le interfacce

- Permettono di localizzare le modifiche
- ideale per sistemi multipiattaforma

## Repository
Quando ci sono diversi sotto-sistemi che devono condividere grandi quantità di dati comuni

- Dati condivisi salvati e gestiti da un database centrale a cui tutti i sotto-sistemi possono accedere (**repository**)
- Tutti sotto-sistemi operano con un modello di dati concordato
- repository accessibile a tutti i componenti del sistema
- componenti non si scambiano dati direttamente ma solo attraverso repository 
### Vantaggi
- componenti indipendenti non devono trasmettere dati direttamente tra loro
- repository gestisce tutti i dati in modo coerente
- semplice integrare nuovi componenti che si conformano al modello dei dati condiviso
### Svantaggi
- Difficile e meno efficiente distribuire il repo su più macchine (ridondanza e consistenza dei dati per mantenere coerenti e aggiornate più copie)
- Repository costituisce un single point of failure: tutti i suoi problemi influiscono sull'intero sistema
- difficile integrare componenti non conformi al modello dei dati comune
## Client-Server
- Architettura **distribuita** in cui ciascun servizio è fornito da un server separato
- Client accedono ai server per utilizzare i servizi
### Vantaggi
- server possono essere distribuiti su una rete
- separazione e indipendenza: servizi e serve modificati senza influire su altre parti
- facile aggiungere un nuovo server ed integrarlo con il resto del sistema
### Svantaggi
- servizio può essere single point of failure: potrebbe essere replicato su più server
- prestazioni possono dipendere dai canali di comunicazione
- problemi di gestione se i server sono proprietà di organizzazioni diverse
### Componenti
#### Presentazione
Gestisce interfaccia utente
#### Logica applicativa
Logica e regole di business: come i dati vengono elaborati per rispondere alle esigenze degli utenti
#### Gestione dei dati persistenti
Memorizzazione e gestione dei dati a lungo termine

>[!tip] La politica di allocazione di queste componenti porta alla classificazione dell’architettura: 2-tier, 3-tier, n-tier.

### Suddivisione in tier
- **2-tier**: suddivisa in client e server
	- logica applicativa può essere distribuita tra entrambi
- **3-tier:** tre livelli separati
	- Presentazione sul client
	- Logica applicativa su application server
	- Gestione dei dati su un database server
- **n-tier:** estende il modello a tre livelli con altre divisioni logiche o fisiche (Cache Layer, Security Layer)

#### Soluzioni 3-tier
- Client non comunica direttamente con il database
- invia richieste all'application server che interagisce con il database
- separazione migliora modularità e flessibilità, distribuendo la logica su più server per gestire carichi maggiori
## Pipe-And-Filter
- Ogni componente di elaborazione (filtro) svolge una particolare trasformazione dei dati in input e produce dei dati trasformati in output
- dati fluiscono come in un tubo attraverso sequenza di componenti per essere elaborati
- trasformazioni eseguite in sequenza o parallelo
### Vantaggi
- evoluzione del sistema semplice (modificando o aggiungendo nuove trasformazioni)
- trasformazioni possono essere riusate
- componenti possono essere progettati separatamente
#### Svantaggi
- Trasformazioni successive devono rispettare il formato concordato per il trasferimento dati
- Impossibile riusare componenti che usano strutture dati non compatibili o introdurre overhead per la traduzione del formato
- interazione con gli utenti è limitata

>[!tip] Utile per sistemi di elaborazione dati.
## Model-View-Controller
>[!tip] Pattern per sistemi con forte interazione con gli utenti.

- Visualizzare dati generici tramite GUI usando rappresentazioni diverse dei dati stessi
- permette la separazione netta dei componenti di presentazione dei dati dai componenti che li gestiscono
### Componenti
- **Model:** contiene le classi le cui istanze rappresentano i dati da visualizzare e manipolare (manipolare i dati)
- **View:** oggetti usati per presentare i dati all'utente 
- **Controller:** oggetti che controlleranno e gestiranno l'interazione dell'utente sia con il livello view che il model
#### Model
- Regole del business per interpretazione con i dati
- espone a View e Controller le funzionalità per accesso e aggiornamento
- resposabilità di notificare ai componenti della View aggiornamenti verificati dopo richieste del Controller
#### Controller
- Trasforma le interazioni dell'utente sulla View in azioni eseguite sul Model
- corrispondenza tra l'input dell'utente e i processi eseguiti dal Model
- Selezionando le schermate della View necessarie, il Controller implementa la logica di controllo dell'applicazione
#### View
- gestisce la logica di presentazione dei dati
- ogni schermata può implementare viste diverse sui dati e modalità di interazioni diverse
- richiede aggiornamenti dei dati al Model in modo da presentare dati sempre aggiornati
- View delega al Controller l'esecuzione dei processi richiesti dall'utente dopo averne catturato gli input, e la scelta delle eventuali schermate da presentare
![[materie/anno_2025-2026/ingegneria_del_software/assets/mvc.jpg]]
### Aggiornamento dei dati
Sequence diagram
- in risposta a qualche evento il metodo `handleEvent()` viene invocato sul Controller
- Controller esamina lo stato di Model e invoca un suo metodo per cambiare il suo stato
- Model cambia lo stato e notifica a tutte le View registrate
- Ogni View è notificata invocando `update()`
- View esamina Model tramite `getState()`
### Selezione schermata
- Utente seleziona una pagina da mostrare attraverso la View
- View delega al Controller tramite `processSelectPage()`
- Controller decide e/o compone la pagina da visualizzare, e la comunica alla View con `showSelectPage()`
- View costruisce e presenta all'utente la schermata richiesta, controllando se ci sono state modifiche in Model usando `getState()`