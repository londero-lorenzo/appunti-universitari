---
title: "2 Processi Software"
aliases: ["2 Processi Software"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "2-processi-software"]
created: 2025-10-20
---
### Code and Fix
+ Ha numerose limitazioni che lo rendono inadeguato per lo sviluppo di software professionale
>[!example]
>In sistemi di grandi dimensioni a cui lavorano team numerosi, la comunicazione e la divisione dei compiti possono essere difficoltose

>[!tip]
>Necessità di approcci più organizzati allo sviluppo del software


>[!definition]
>Processo Software
>> insieme strutturato di attività tecniche, collaborative e manageriali che porta alla creazione di un prodotto software

+ Elevata qualità di un processo predicibile e controllato permette di migliorare:
	+ qualità del prodotto finale
	+ tempi per portare il prodotto sul mercato
	+ i costi affrontati dall'organizzazione

### No free lunch
+ Non esiste un processo software universale
+ non esiste un unico metodo di ingegneria del software che può essere applicato a tutti questi sistemi
+ processo utilizzato in aziende dipende:
	+ dal tipo di software che si sta sviluppando
	+ dalle richieste del cliente
	+ dalle capacità delle persone che scrivono il software
# Attività dei processi software

## Attività fondamentali
+ Ciascun processo è composto da attività fondamentali
+ Tutti i processi software condividono queste attività fondamentali
+ Queste attività possono essere organizzate e realizzate in modi diversi in processi diversi

## 4 attività fondamentali

+ **Acquisizione, analisi e specifica dei requisiti**: definire le funzionalità e i vincoli operativi del software da produrre (clienti e ingegneri)
+ **Progettazione e Sviluppo**: progettazione e programmazione del codice che realizza la funzionalità individuale
+ **Verifica e validazione**: convalidare che il software sia esattamente ciò che il cliente richiede e che sia sviluppato correttamente
+ **Evoluzione:** modificare il software per soddisfare eventuali cambiamenti dei requisiti del cliente e del contesto operativo

## Studio di affidabilità
+ Stabilisce se lo sviluppo debba essere avviato:
	+ Se esiste un mercato per il software
	+ Se il software sia tecnicamente ed economicamente realistico
+ Definisce quali sono le alternative possibili e le scelte più ragionevoli, stimando le risorse necessarie per ciascuna alternativa

## Studio di fattibilità
>[!definition]
>>Stabilisce se lo sviluppo debba essere avviato, ossia:
>>- Se esiste un mercato per il software
>>- Se il software sia tecnicamente ed economicamente realistico

+ Quali sono le alternative possibili
+ Le scelte più ragionevoli
+ Stimare le risorse (finanziarie e umane) necessarie per ciascuna alternativa

Report di fattibilità:
+ Definizione del problema
+ Valutazione Costi/Benefici
+ Risorse finanziarie e umane
+ Soluzioni alternative
+ Tempi di consegna e modalità di sviluppo
>[!tip]
>Tale studio dovrebbe essere relativamente rapido e poco costoso

## Acquisizione, analisi e specifica dei requisiti
+ Attività per stabilire **cosa** il software dovrà fare (**non come**)
+ Specificare le funzionalità e le qualità che deve possedere, **senza vincolare** la progettazione e l'implementazione
+ Definisce tramite l'interazione con il committente funzioni, vincoli, prestazioni, interfacce e qualsiasi altra caratteristica che il sistema dovrà soddisfare
>[!warning] Attività critica: 
>un errore in questa fase può costare molto in seguito nelle fasi di progettazione e implementazione
## Ingegneria dei requisiti
+ Sviluppa metodi per raccogliere, documentare, classificare e analizzare i requisiti
	1. **Deduzione e analisi dei requisiti**: comprensione di cosa richiedono o si aspettano dal software i portatori di interesse
	2. **Specifica dei requisiti:** traduzione delle informazioni acquisite in specifiche che descrivono in dettaglio i requisiti
	3. **Convalida dei requisiti:** controllo che i requisiti siano realistici coerenti e completi. Permette di correggere eventuali errori

### Deduzione e analisi
+ Deduzione richiede spirito critico e può coinvolgere
	+ osservazione di sistemi già esistenti
	+ discussione con i possibili utenti
+ Durante l'**analisi** può avvenire lo sviluppo di uno o più modelli e prototipi, che aiutano gli analisti a capire il sistema da specificare

### Specifica
+ Traduce le informazioni dedotte in un insieme di requisiti
+ Può produrre due tipi di requisiti:
	+ Requisiti di **sistema**:
		+ descrizione dettagliata delle funzionalità
		+ caratteristiche che devono essere fornite
		+ utile agli sviluppatori
	+ Requisiti **utente**:
		+ proposizioni astratte dei requisiti del sistema per i clienti e gli utenti finali

### Convalida
Controlla che i requisiti siano realistici, coerenti e completi
+ Durante possono essere rilevati errori nel documento dei requisiti
+ Il documento dei requisiti dovrà essere modificato in presenza di errori, in modo da correggerli

### Documento dei requisiti
+ Al termine della convalida si ha un documento che definisce l'insieme dei requisiti
+ Tale documento è più o meno dettagliato e formale a seconda del processo
+ deve essere comprensibile, preciso, completo, coerente, non ambiguo, modificabile
+ Inoltre, in questa fase è predisposto un **piano di test** del sistema

Quando analizziamo il software possono apparire degli elementi che non avevamo preso in considerazione o visto.

# Progettazione e sviluppo
+ Conversione delle specifiche in un sistema eseguibile da consegnare al cliente che conta in due fasi
	+ **Progettazione:** progettare una struttura del software realizzi le specifiche
	+ **Sviluppo**: implementazione dei componenti definiti nel progetto
>[!tip]
>Le attività di progettazione e sviluppo possono essere intrecciate in alcuni processi software (es. processi agili) mentre lo sviluppo segue rigidamente la progettazione in altri processi (es. sviluppo di software critici)

## Progettazione
+ attività sono intrecciate e interdipendenti
+ con quali dati deve interagire
+ si sviluppa il progetto in varie fasi, aggiungendo dettagli o correggendo difetti
+ le nuove informazioni sul progetto influenzano le precedenti scelte progettuali (revisioni)

### Informazioni sulla piattaforma
+ dovrà interfacciarsi con la **piattaforma software**
+ piattaforma include altri sistemi software (SO, database e applicazioni)
### Progettazione dell'architettura
+ **progettazione dell'architettura** consiste nell'identificazione della struttura complessiva del sistema, componenti principali e delle loro relazioni
+ Progetto di alto livello
+ output 
### Progettazione dell'interfaccia
+ Definisce come un componente può essere usato da altri componenti senza conoscerne l'implementazione
+ specifica dell'interfaccia non deve essere ambigua
+ componenti possono essere progettati e sviluppati separatamente rispettando la specifica dell'interfaccia
### Progettazione e scelta dei componenti
+ **scelta dei componenti:** riusati componenti esistenti
+ **progettazione dei componenti**: se non ce ne sono disponibili ne vengono progettati di nuovi
+ programmatore decide sui dettagli dell'implementazione
+ **progetto di dettaglio**

### Output
Progetto del software che descrive:
+ struttura del software che si deve implementare
+ modelli e strutture dati usati dal sistema
+ interfacce tra i componenti del sistema

# Verifica e Validazione
+ **Verifica:** mostrare che un sistema è conforme alle sue specifiche. Se nella prima fase abbiamo estratto delle specifiche andiamo a vedere se dopo la fase di codice e modellazione il codice faccia quello che abbiamo progettato
+ **Validazione:** mostrare che un sistema soddisfi le aspettative del cliente
+ **Testing**: tecnica più utilizzata che consiste nell'eseguire il sistema utilizzando dati di prova ricavati dalle specifiche

>[!tip]
>Può richiedere processi di controllo:
>- ispezioni
>- revisioni

## Test dei componenti
Granularità può variare da progetto a progetto:
+ componenti possono essere entità semplici (funzioni, classi di oggetti, gruppi coerenti di queste entità)
Ciascun componente è testato separatamente per appurare il corretto funzionamento in **isolamento**.

## Test del sistema
+ Testare sistema **completo**
	+ per sistemi complessi può richiedere più stadi
	+ i componenti sono **integrati** in sottosistemi prima di arrivare al sistema completo
+ Errori potrebbero essere causati da:
	+ interazioni impreviste tra i componenti
+ Verifica la **conformità** ai requisiti funzionali e non del sistema

## Test del cliente
+ sistema testato con i dati reali del cliente
+ potrebbero essere rilevati problemi con i requisiti
	+ se le funzionalità non soddisfano le necessità dell'utente
	+ se le prestazioni sono inaccettabili
+ dimostra se il software soddisfa il cliente

## Testing iterativo
+ i difetti scoperti possono portare la ripetizione di altri stadi del processo di test

>[!example]
>Alcuni errori nei componenti del programma possono apparire durante il test del sistema o il cliente può stimolare il sistema in modi non previsti dai dati simulati.

# Evoluzione
+ Adattare a nuove funzionalità
+ software viene modificato continuamente nel corso della sua vita per adeguarlo ai cambiamenti dei requisiti
+ fase più lunga del ciclo di vita del software
+ attività può avvenire dopo il rilascio