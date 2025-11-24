---
title: "10 Diagramma di Sequenza"
aliases: ["10 Diagramma di Sequenza"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "10-diagramma-di-sequenza"]
created: 2025-11-24
---
## Diagrammi UML comportamentali
>[!definition]
>>Modellano il comportamento dinamico degli elementi che compongono il sistema.

## Diagrammi di interazione
>[!definition]
>>Modellano la **collaborazione dinamica** tra oggetti che implementano collettivamente un determinato comportamento.

# Diagrammi di sequenza

>[!definition]
>>Modella le interazioni tra uno o più attori e le parti di un sistema software, nell'ambito dell'esecuzione di uno o più scenari di un caso d'uso.

- Interazioni tra **attori** e gli **oggetti** del sistema sotto forma di **messaggi**
- scambio di messaggi è letto dall'alto in basso
- chiariscono le chiamate tra i partecipanti e le **responsabilità** di ciascuno di essi

## Attore
- riportati sulla sinistra con frecce che modellano le interazioni verso oggetti del sistema
>[!tip]
>Possono **non** essere presenti se lo scenario è avviato da un altro scenario o iniziato dal sistema

## Partecipante o istanze di classe
- nome della classe e identificatore dell'oggetto nel formato **nomeOggetto: nomeClasse**
- informalmente: con un nome che suggerisce che si sta considerando un'istanza di una classe (anOrder, aProduct, ...)
## Lifeline
- mostra in partecipanti attraverso una linea verticale tratteggiata
- rappresentano il periodo temporale di vita dell'oggetto
- lifeline mostra l'**ordinamento** dei messaggi
## Messaggio
- definisce una particolare comunicazione tra le lifeline 
- frecce tra lifeline
- l'ordine dei messaggi ricalca l'ordine sequenziale con il quale essi vengono scambiati
### Scambio messaggi
- Messaggio di **chiamata**: invocare una operazione
- Messaggio di **creazione/distruzione**: creare o distruggere un'istanza
- inviare un segnale o un dato

- Quando una lifeline riceve un messaggio di chiamata, deve esistere una **corrispondente operazione nella classe della lifeline ricevente**
- messaggi possono invocare operazioni in maniera **sincrona** o **asincrona**
## Activation Box

>[!definition]
>>Barre di attivazione sono rettangoli che coprono parte delle lifeline.
>>Sono il periodo di tempo in cui l'istanza è attiva nell'interazione.

>[!example]
>Tempo necessario ad un oggetto per elaborare un messaggio di richiesta

Una lifeline di un partecipante si attiva quando elabora un messaggio:
- durante l'esecuzione l'attivazione si sposta tra le lifeline descrivendo il flusso di controllo
## Messaggi di Auto-Delega e Activation Box innestate
Quando un oggetto invia un messaggio a se stesso.
>[!example]
>Chiamata a un proprio metodo.

Auto-Delega genera un'attivazione innestata.

# Dagli scenari ai diagrammi di sequenza al codice OO

# Paradigmi di modellazione centralizzati e distribuiti
## Centralizzato
- Un singolo oggetto ha il controllo
- Gli altri forniscono servizi
### Pro
Semplice soluzione che tende a raccogliere in un solo punto tutta l'elaborazione
### Contro
La logica che gestisce alcuni attributi si potrebbe trovare in classi diverse, rendendo non intuitiva la manutenzione del sistema
## Distribuito
Le responsabilità sono distribuite tra gli oggetti partecipanti
### Pro
- Conforme al paradigma OO
- facilita la manutenzione: raccoglie nello stesso oggetto dati e logica
- permette di usare il polimorfismo invece della logica condizionale
### Contro
Può risultare dispersivo e difficile da leggere in fase di analisi

# Creazione e distruzione degli oggetti
## Creazione
- un messaggio al costruttore di un oggetto può creare un oggetto
- oggetto creato viene disegnato al termine della freccia corrispondente al messaggio
- messaggio costruttore può essere etichettato con il nome **new**
- oggetti staticamente definiti partono dalla cime del diagramma
- se il partecipante fa qualcosa appena creato:
	- la activation box si disegna attaccata al rettangolo
## Distruzione
- indicata con una X
- se la freccia del messaggio tra oggetti termina con X
	- l'oggetto mittente sta distruggendo quello che lo riceve
- una X da sola alla fine della lifeline indica che l'oggetto sta distruggendo se stesso
- dopo la distruzione: oggetto non più disponibile per l'elaborazione
# Frame di interazione e frammenti combinati
>[!definition]
>Frame
>>Evidenziano una parte del diagramma e racchiudono una sottosequenza di messaggi.

- Possono essere composti da uno o più frammenti combinati
- Ogni frame ha:
	- **un operatore:** determina come vengono eseguiti i suoi operandi
	- **uno o più frammenti**
	- **zero o più condizioni di guardia**: stabiliscono se i frammenti corrispondenti devono essere eseguiti
		- ogni frammento può avere la propria guardia


| Operatore | Nome Completo | Semantica                                                                                                                                                                                              | Costrutto                                                                 |
| --------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| opt       | Optional      | Frammento corrispondente è eseguito solo se la sua condizione è vera.                                                                                                                                  | **If-then**                                                               |
| alt       | Alternatives  | Molteplici frammenti in alternativa. Viene eseguito solo il frammento la cui condizione è vera. Ammette else come condizione di guardia.                                                               | **If-then-else**                                                          |
| loop      | Loop          | Ciclo. Frammento eseguito finché la condizione di guardia è verificata.                                                                                                                                | Condizione indicata all'inizio (**while-do**) o alla fine (**do-while**). |
| ref       | Reference     | Il frame rimanda ad un'interazione definita in un altro diagramma. Possono essere indicati dei parametri ed un tipo di ritorno. **Frame deve racchiudre tutte le lifeline coinvolte nell'interazione** |                                                                           |
### Pro
- Permettono di rappresentare costrutti condizionali e iterativi
- Permettono di modellare sia lo scenario principale che quelli alternativi in un caso d'uso
### Contro
- frame appesantiscono il diagramma
- Poco adatti a rappresentare algoritmi complessi (in questi casi meglio **activity** e **statechart diagrams**)
# Quando utilizzare i Sequence Diagram
## Nella fase di Analisi dei Requisiti
- può essere una rappresentazione grafica di uno scenario di un caso d'uso
- il ruolo degli oggetti del sistema sarà ricoperto da un generico oggetto Sistema (ATM nell'esempio)
- Potranno comparire altri oggetti (indicanti alcuni componenti architetturali interni o esterni tipo server, database) se essi rappresentano attori o elementi vincolati nei requisiti
## Nella fase di Progettazione
- Descrivono ancora scenari di casi d'uso
- Partecipanti sono istanze delle classi del sistema
- messaggi sono le responsabilità o operazioni stabilite dal diagramma delle classi
- non dipende dal linguaggio di programmazione
### Esempio
- Vogliamo specificare la dinamica delle funzionalità di Registrazione di uno studente ad una CourseSection
1. Invocare l'operazione di requestToRegister su una CourseSection
2. Creare una istanza di Registration
3. Collegare lo studente alla Registration
4. Aggiungere la Registration alla RegistrationList di CourseSection
![[materie/anno_2025-2026/ingegneria_del_software/assets/sequence_diagram_fase_progettazione.jpg]]
