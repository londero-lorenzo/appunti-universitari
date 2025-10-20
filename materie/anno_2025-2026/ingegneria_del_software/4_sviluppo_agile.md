---
title: "4 Sviluppo Agile"
aliases: ["4 Sviluppo Agile"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "4-sviluppo-agile"]
created: 2025-10-20
---

# Motivazioni

Fino al 2000:
+ **meno del 30%** dei progetti software avevano successo
+ **progetti grandi fallivano** più spesso
+ solo **metà delle feature richieste** era effettivamente rilasciata

## Instabilità dei requisiti
+ **requisiti non chiari, instabili e variabili**
+ numerose prescrizioni, quantità di documenti e eccessiva rigidità = **processo di sviluppo plan-driven pesante**
+ richiesto un approccio **flessibile e "leggero"**
## Successi dei processi Plan-Driven
+ sono fondamentali per alcuni **sistemi critici**:
	+ sviluppati da **team numerosi** e geograficamente dislocati
	+ processi che durano **lunghi periodi**
	+ Software che sarà **usato a lungo**
## Insuccessi dei processi Plan-Driven
+ Si **adattano poco** al **contesto dinamico**
+ si **adattano poco** alla necessità di **consegna rapida** di molti progetti
+ eccessivo **overhead** (es. produzione di documentazione)
+ poco flessibili ai **cambiamenti** nei requisiti

# Sviluppo rapido del software

+ **Nuove opportunità** in un contesto globale in **rapido cambiamento**
	+ software deve **evolvere rapidamente** per riflettere i cambiamenti nelle necessità dei committenti e utenti finali
+ Presenza di **prodotti concorrenti**
	+ Software deve essere **consegnato presto** per essere **competitivo sul mercato**
>[!tip]
**Rapidità** dello sviluppo e consegna è spesso il requisito più critico per i sistemi software.

## Agilità

+ Efficace risposta: **rapida e flessibile ai cambiamenti**
+ **efficace comunicazione** fra tutti gli stakeholder
+ portare il **cliente nel team di lavoro** per feedback rapido

>[!tip]
>Agilità consente di avere una rapida, incrementale consegna del software.

## Caratteristiche 

+ **Documentazione minima**
	+ **focus sul codice**
	+ **no specifiche dettagliate** (congelate all'inizio): requisiti che evolvono con il passare del tempo
	+ **overhead** di documentazione limitati
+ **Consegna rapida ed incrementale**:
	+ sistema sviluppato in **incrementi rilasciati frequentemente**
	+ **stakeholder** coinvolti nella specifica e nella valutazione di ogni incremento, **definendo insieme gli incrementi successivi**
+ **Strumenti di supporto**:
	+ utilizzo di strumenti al supporto del processo di sviluppo (es. automatizzazione dei test)
## Processi Plan-Driven VS Agili

+ Plan-DRiven:
	+ attività pianificate in **anticipo**
	+ avanzamento misurato rispetto a quanto previsto dal piano
	+ **fasi** del processo **distinte tra loro**
	+ output di ciascuna fase sono necessari per fase successiva
+ Agili:
	+ pianificazione **incrementale e continua**
	+ più **facile modificare il processo** per adeguarsi alle modifiche dei requisiti del cliente 
	+ **requisiti, progettazione e implementazione** avvengono **insieme** 


Pratiche plan-driven e agili possono coesistere nello stesso processo:
+ Processi agili producono documentazione di progettazione quando ritenuto necessario
+ possono includere **attività pianificate**
+ scopo dei documenti è **supportare la comunicazione** anche se incompleti e imprecisi
+ Processi Plan-Driven possono essere **incrementali**

>[!tip]
>Per grandi sistemi occorre trovare un **compromesso tra processi pianificati e agili.**

>[!warning] Disclaimer
>+ modelli a sviluppo incrementale tra i processi plan-driven
>+ processi agili pongono ancora **maggiore enfasi sull'incrementalità** e sulla **rapidità degli incrementi**
>+ processi plan-driven organizzati in **incrementi pianificati**

# Principi Agili
+ **Coinvolgimento del cliente**:
+ clienti sono coinvolti in tutto il processo
+ clienti intervengono a ciascuna iterazione del prodotto:
	+ valutano e validano l'iterazione
	+ forniscono nuovi requisiti del sistema
	+ modifiche alle iterazioni
	+ priorità a ciascun requisito richiesto


+ **Accettare i cambiamenti**:
	+ prodotto **non** deve essere **pianificato rigidamente**
	+ **prevedere** che i **requisiti** del sistema **potranno cambiare**
+ **Mantenere la semplicità**:
	+ il **prodotto** e il **processo** di sviluppo devono essere **più semplici possibili**
	+ quando possibile bisogna lavorare attivamente per **eliminare la complessità del sistema**

+ **Sviluppo incrementale**:
	+ software sviluppato e consegnato **incrementalmente**
	+ il cliente specifica i requisiti da includere in ciascun incremento
+ **Persone, non processi**:
	+ processo di sviluppo **non** deve essere **fortemente prescrittivo**
	+ membri del team devono essere **liberi di sviluppare software secondo i loro metodi**
	+ **capacità** di ogni membro **sfruttate al meglio** e **non ingabbiate**

## Applicabilità dei modelli agili

+ Prodotti di **piccole o medie dimensioni**
+ Prodotti **personalizzati** per cui c'è un **chiaro impegno del cliente** nell'essere coinvolto nel processo di sviluppo

+ Prodotti in cui ci sono **pochi stakeholder** e non bisogna rispettare rigidi regolamenti
+ Team **fisicamente vicini,** in modo che le comunicazioni siano informali e facilitate

>[!example]
>- Il prodotto evolve attraverso multiple brevi iterazioni
>- Iterazioni hanno durata costante (2-3 settimane)
>- Si rilascia un'applicazione funzionante al termine di ogni iterazione
>- Con ogni nuova release si aggiungono quante più **caratteristiche** è possibile tra quelle con la **più alta priorità** richieste dal cliente 
>- Cliente **rivede ogni nuovo incremento**
>- Cliente può **ridefinire le priorità** per la prossima iterazione

## Vantaggi
+ Consegne predicibili
+ **Rapida risposta** ai cambiamenti dei bisogni utente
+ **Rischi attenuati** grazie a cicli di consegna più brevi
+ Alta produttività
+ Clienti soddisfatti, **successo** dei progetti prodotto **evolve attraverso multiple brevi iterazioni**

# Tecniche agili

+ **Extreme Programming**
+ SCRUM
+ Feature Driven Development
+ Crystal
+ DSDM Lean Software Development

## Extreme Programming
>[!definition]
>>Metodo più conosciuto: spinge normali pratiche di sviluppo a livelli "estremi".

![[materie/anno_2025-2026/ingegneria_del_software/assets/extreme_programming.jpg]]
+ Approccio **iterativo** estremo
+ Piccoli e frequenti incrementi rilasciati al cliente (es. ogni 2 settimane)
### Selezione delle storie utente per questa release
+ Requisiti espressi come **storie utente**
+ storie utente sono **semplici scenari** utilizzati come base per decidere **quale funzionalità deve essere inclusa** in un incremento del sistema
### Suddivisione delle storie in task
+ Scenari divisi in **task** più semplici **implementati direttamente** (senza pesante progettazione e documentazione)
+ task costituiscono le **unità principali dell'implementazione**

### Pianificazione della release
+ Agilità non è assenza di pianificazione
+ Agilità = **pianificazione flessibile**
+ pianificazione non appesantita da **documentazione eccessiva**
### Sviluppo/integrazione/test del software
+ Programmatori lavorano a coppie
+ Sviluppando test per ogni task **prima di scrivere il codice**
+ Tutti i test devono essere stati **eseguiti con successo** quando il nuovo codice viene integrato nel sistema
### Release del software / Valutazione del sistema
+ il cliente **coinvolto nello sviluppo**
+ cliente **valida la release** corrente, 
+ fornisce **requisiti nuovi** o modificati
+ partecipa alla selezione delle storie utente
+ definisce i **test di accettabilità**
## Extreme Programming e Principi agili
+ **Coinvolgimento del cliente**: rappresentante del cliente è **on-site**
+ **Accettare cambiamenti**: appena un task è concluso, viene integrato nel sistema
+ **Sviluppo incrementale**: piccoli e frequenti rilasci che aggiungono in modo incrementale **nuove funzionalità**
+ **Mantenere la semplicità**: progetto **più semplice possibile**:
	+ soddisfi i requisiti correnti
	+ costante **miglioramento del codice**
	+ **refactoring**
+ **Persone, non processi**:
	+ programmazione in coppia
	+ proprietà collettiva del codice
	+ orari di lavoro non troppo lunghi
	+ non troppi straordinari
## Influenza dell'Extreme Programming
- Nella pratica XP non è quasi mai adottato
- Non pratico perché richiede un **cambio radicale** nel modo di lavorare di un'organizzazione
- pratiche chiave dell'XP ---> approcci agili
	- Storie utente 
	- Refactoring
	- Sviluppo preceduto dai test
	- Pair programming

### Storie utente
+ Descrivono i requisiti degli utenti come **scenari d'uso** in cui l'utente potrebbe trovarsi
+ Scritti da cliente e team su schede (**story cards**) che il team di sviluppo suddivide in **task** da implementare
+ Task rivelati sono la **base per definire la pianificazione** delle **iterazioni** e le **stime dei costi** 
+ il cliente è parte del team
+ compito del cliente: prendere **decisioni su requisiti** con il team
+ Cliente e team definiscono una **priorità e una stima dei costi** per ciascuna storia, criteri di accettazione
+ cliente e team scelgono le storie incluse nella prossima versione
>[!example]
>Story Card
>![[materie/anno_2025-2026/ingegneria_del_software/assets/story_card.jpg]]

>[!example]
>Suddivisione di task
>![[materie/anno_2025-2026/ingegneria_del_software/assets/suddivisione_task.jpg]]
#### Pro
+ integrano la **deduzione dei requisiti** con lo **sviluppo** invece di apposite attività di ingegneria dei requisiti, in modo da gestire i **cambiamenti nei requisiti**
+ Più semplice relazionarsi con storie utente, anziché con un tradizionale documento di requisiti
+ **coinvolgono maggiormente** l'utente
+ ordinate in base a quelle che possono fornire **supporto utile all'azienda**
+ Se i requisiti cambiano, vengono aggiunte **story cards** e le storie non ancora realizzate possono essere modificate o scartate
#### Contro
+ **Non semplice** stabilire se le storie utente **coprono completamente** i requisiti del sistema
+ Clienti esperti potrebbero **omettere scenari** o **task considerati ovvi** ma che non lo sono per gli sviluppatori
+ descrizione **incompleta** del requisito

### Refactoring

+ progettare pensando al **cambiamento** (riducendo costi e manutenzione futura)
+ XP **rinuncia** a gestire in **anticipo cambiamenti**
+ XP propone un **continuo miglioramento del codice**: rende più semplice l'implementazione di eventuali modifiche future
+ È un processo di miglioramento del codice che viene riorganizzato e riscritto per renderlo **più efficiente e comprensibile** (**senza cambiare funzionalità**)

+ Team di sviluppo cerca **aspetti del software** da migliorare e implementa immediatamente
+ miglioramento può riguardare anche situazioni in cui **non c'è una necessità immediata**
+ un codice di più alta qualità: 
	+ **riduce la necessità di documentazione** 
	+ **facilita le modifiche future**

>[!example]
>Refractoring
>- rimozione **codice duplicato**
>- **rinominare** classi, attributi e metodi
>- creazione di **librerie** con **codice utile** a più classi o progetti
## Pro
+ sviluppo incrementale: porta al **deterioramento** del codice
+ **refractoring continuo** mitiga il deterioramento
+ tool per **automatizzare** alcune operazioni di refractoring
## Contro
+ refractoring a livello di codice **non basta per supportare un cambiamento**
+ necessaria una modifica dell'**intera architettura** (più costosa)
+ trovare un **compromesso** tra tempo dedicato allo sviluppo di nuove funzionalità e refractoring

# Sviluppo preceduto dai test
>[!definition]
>XP testing fondamentale: 
>>Software testato dopo ciascun cambiamento.

## Caratteristiche fondamentali
+ **Sviluppo test-driven**: i casi di test da soddisfare sono **scritti prima** del codice quindi **guidano lo sviluppo**
+ **Automatizzare dei test**: strumenti che **eseguono automaticamente i test** a ogni rilascio di un nuova versione
+ **Coinvolgimento del cliente**: cliente coinvolto nello **sviluppo dei test** di accettazione delle storie da implementare nell'iterazione successiva

## Sviluppo Test-Driven TDD

+ Scrivere test **prima del codice**: chiarisce i requisiti da implementare
+ **aspetto cruciale** in assenza di specifiche accuratamente documentate che guidino i test di sistema (approcci plan-driven)
+ test scritti come **programmi** (eseguiti automaticamente)
	+ ogni test simula l'**invio degli input** e **controlla l'output**
+ possibile eseguire i test **mentre si programma** così si scoprono subito eventuali problemi nel codice

+ test pre-esistenti e nuovi test: eseguiti quando una **nuova funzionalità viene aggiunta**
	+ permette di verificare che la nuova funzionalità **non abbia introdotto errori**
+ sviluppo non può procedere finché tutti i **test** **non sono stati superati**

+ Sviluppo test-driven parte delle schede utente suddivise in task
![[materie/anno_2025-2026/ingegneria_del_software/assets/test_driven.jpg]]
+ definire per ciascun task il **caso di test**: correttezza del codice del relativo task
![[materie/anno_2025-2026/ingegneria_del_software/assets/test_driven_2.jpg]]
## Automazione dei test
+ test scritti come **programmi eseguibili**
+ simula l'**immissione** di un **determinato input**
+ framework facilitano la **scrittura** ed **esecuzione** 
+ **test** eseguiti ogni volta che una **nuova funzionalità è aggiunta**
+ automatizzazione rende più **facile e rapida** la fase di **verifica e validazione**
### Pro
+ Scrittura del test implica la **definizione di un'interfaccia** e una **specifica comportamentale** della funzionalità da sviluppare
	+ riduciamo incomprensioni, ambiguità e omissioni
### Contro
+ Pratica **onerosa** per il cliente
+ sforzo per tenere aggiornati i **test interessati** **dalle modifiche del codice**
+ test potrebbero essere **incompleti**: **non verificano** tutti i possibili scenari che potrebbero verificarsi (per ragioni di tempo)

# Pair Programming

+ Programmatori lavorano in **coppie**:
	+ stessa postazione
	+ coppie variano continuamente
+ refractoring viene incoraggiato
	+ più facile che il team ne benefici
+ software di proprietà **dell'intero team**:
	+ **singoli** ritenuti responsabili dei problemi nel codice (**egoless programming**)
	+ team ha la **responsabilità collettiva** della risoluzione di questi problemi

>[!question] Programmando a coppie si dimezza la produttività ?
## Pro 
+ aiuta a sviluppare il **senso di proprietà del codice** nel team
+ **diffondere la conoscenza** nell'ambito del team
+ processo di **revisione informale**:
	+ sviluppatori verificano reciprocamente il proprio lavoro
	+ ogni linea di codice è controllata da più di una persona
+ **riduce** i rischi di **fallimento** dovuto a turn-over
## Contro
+ la programmazione in coppie può essere **meno efficiente** di quella individuale
# Scrum

## Gestione della progettazione
+ **pianificazione informale** proposta dai primi seguaci dei metodi agili scontrata con l'**esigenza di visibilità** del processo da parte dei **manager**
+ manager devono controllare il processo per sapere se raggiungerà i **suoi obiettivi**
	+ sarà consegnato in tempo e nei limiti di budget previsti
+ offre un framework per **organizzare agilmente progetti**
+ fornire una **visibilità esterna** su quello che accade all'**interno del team**

![[materie/anno_2025-2026/ingegneria_del_software/assets/scrum.jpg]]
### Product Backlog
+ ogni sprint parte dal **product backlog** (lista degli elementi)
	+ caratteristiche del prodotto
	+ requisiti
	+ miglioramento dell'ingegnerizzazione
+ versione iniziale del product backlog può essere derivata da un
	+ **documento dei requisiti**
	+ **da una lista delle storie utente**
>[!tip]
>Backlog non riguarda sempre e solo codice, ma anche architettura o documentazione.

### Selezione degli elementi
+ All'inizio di ogni ciclo il product owner **stabilisce le priorità** del product backlog
	+ per definire quali sono gli **elementi più importanti** da sviluppare in quel ciclo

>[!definition]
>Product owner
>>Deve identificare:
>> - i requisiti del prodotto
>> - stabilirne le priorità
>> - rivedere continuamente il product backlog
>> per garantire che il progetto **continui a soddisfare** i requisiti critici.
>> Può essere: un cliente, product manager o altro rappresentante degli stakeholder.

### Piano dello sprint
+ **tutti i membri** del team **vengono coinvolti** nella **scelta degli elementi con priorità più alta** che dovranno essere completi
+ valutano il **tempo richiesto** per completare questi elementi **in base alla velocità**

>[!tip]
>La velocità raggiunta nei precedenti sprint rappresenta una stima quanto lavoro del product backlog può essere svolto **in un singolo sprint**.

### Sprint Scrum
+ pianificazione dello sprint porta alla creazione di uno **sprint backlog**
+ team **organizza** il lavoro e **avvia** lo sprint
+ team di sviluppo ha **dimensioni contenute**
>[!tip]
>Lo sprint è un'interazione dello sviluppo (~2-4 settimane)

### Software potenzialmente rilasciabile 
+ **riunione giornaliera** del team di Scrum
	+ esamina l'**avanzamento del lavoro**
	+ stabilisce la **priorità del lavoro** da svolgere quel giorno
+ scrum dovrebbe essere un breve **incontro faccia a faccia** di tutti i membri del team

>[!definition]
>Scrum master
>> Responsabilità di garantire che il processo Scrum sia eseguito e di guidare il team nell'uso efficiente di Scrum.
>> Interfaccia con il resto della società ma non Project Manager classico.

+ incremento del software che è consegnato da uno sprint è potenzialmente rilasciabile
	+ deve trovarsi in **uno stato finito**
	+ non occorre altro lavoro (come il testing)
+ Non è sempre **realizzabile** nella pratica
### Revisione dello sprint e del lavoro da fare
+ alla fine di ogni sprint:
	+ **riunione di verifica** che coinvolge tutti i membri del team
		+ obiettivo 1: **migliorare il processo**
		+ obiettivo 2: **input sul prodotto** e sul suo stato per la **revisione** del product backlog
