---
title: "16 Testing"
aliases: ["16 Testing"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "16-testing"]
created: 2025-12-17
---
## Verifica e Validazione
- **Verifica** "Are we building the software right?"
	- software deve soddisfare:
		- specifica dei requisiti
		- standard stabiliti all'inizio del ciclo di sviluppo
- **Validazione** "Are we building the right software?"
	- il software risolve il giusto problema
	- supportando l'utilizzo atteso e soddisfacendo i bisogni degli utenti nell'ambiente operativo

## Testing e debugging
>[!definition]
>Testing
>>Processo di esecuzione del software allo scopo di scoprirne eventuali malfunzionamenti.

- Presenza di malfunzionamenti = presenza di difetti nel software

# Errore, difetto, malfunzionamento
## Errore
- Situazione = incomprensione umana
### Tipologie
- Durante la comprensione dei requisiti del problema
- Durante elaborazione di una soluzione al prolema
- nel comprendere o utilizzare strumenti
- durante la programmazione: per distrazione, superficialità o problemi di comunicazione
## Difetto
- Errore umano nel software
	- natura **statica**: codice sintatticamente o semanticamente sbagliato
	- il codice difettoso non viene mai esercitato
		- potrebbe passare inosservato perché non scatenerebbe nessun malfunzionamento del software durante l'esecuzione

## Malfunzionamento
- Incapacità del software di comportarsi secondo le aspettative o le specifiche
	- natura **dinamica**: accade solo in un certo istante
		- può essere osservato solo mediante esecuzione
	- **crash**

- il difetto è causato da uno o più errori
- difetto può causare uno o più malfunzionamenti
>[!example]
>- Errore: di digitazione
>- Difetto: * invece di +
>- Malfunzionamento: durante l'esecuzione il risultato è diverso da quello atteso

# Casi di test

- Durante il testing: software esercitato da un insieme di input e ne viene valutato il comportamento
- Un caso di test è molto utile se è in grado di scoprire un malfunzionamento non ancora scoperto da altri casi di test
- Non basta definire gli input di ciascun caso di test
- si deve definire anche l'output, pre-condizioni e post-condizioni

### ID
Aiuta a specificare e comunicare il caso di test
### Descrizione
Può indicare il requisito che il caso di test intende testare
### Valori di input
Indicano il modo in cui il programma sarà testato
### Precondizioni
Sono condizioni che devono essere verificate affinché il caso di test venga eseguito
### Output attesi
Rappresentano il comportamento atteso dal software con gli input 
### Postcondizioni attese
Condizioni in cui si dovrebbe trovare il sistema dopo l'esecuzione del caso di test
>[!tip] Dopo l'esecuzione del caso di test è possibile conoscere l'output effettivo e le postcondizioni effettive

- **Malfunzionamento rilevato:** se almeno un valore di output o una postcondizione riscontrati dopo l'esecuzione del caso di test sono diversi da quelli attesi
- **Malfunzionamento non rilevato**: altrimenti

## Test Suite
- Insieme di casi di test che mira a rilevare la presenza di più difetti possibili
>[!warning] Selezionare in maniera appropriata i casi di test appartenenti alla test suite.

## Oracolo
- Conosce il comportamento atteso per ogni caso di test
- Permette di confrontare il risultato atteso con quello effettivo
### Tipi
- Oracolo umano
- Oracolo automatico:
	- generato da specifiche formali
	- software con stesse funzionalità
	- versione precedente del software
# Obiettivi del testing
>[!warning] Testing rileva la presenza di malfunzionamenti, non identifica i difetti.

>[!definition]
>Debugging
>> Processo di scoperta dei difetti a partire dai malfunzionamenti rilevati.
>> Si occupa di identificare e rimuovere le cause di un malfunzionamento

>[!definition]
>Analisi dell'affidabilità
>> Fornisce una stima della probabilità che il software operi senza malfunzionamenti per un determinato periodo di tempo e in uno specifico ambiente.

## Testing ideale ed esaustivo
- Testing è **ideale** se l'assenza di malfunzionamenti rilevati implica la correttezza del programma
- Testing è **esaustivo** se contiene tutte le possibili combinazioni dei dati di ingresso del programma
	- Test esaustivo è ideale
- Casi non banali: test esaustivo non è pratico ed è infallibile a causa di costi elevatissimi
- Selezionare casi di test che **approssimino** un test ideale e diano fiducia sulla qualità del software
## Selezione dei casi di test
Bontà di una test suite si può misurare in:
**Efficacia:** $\frac{\textrm{malfunzionamenti trovati}}{\textrm{malfunzionamenti da trovare}}$

**Efficienza:** $\frac{\textrm{test che rilevano malfunzionamenti}}{\textrm{test totali}}$

- Quando si vuole test meno costoso
>[!tip] Bisognerebbe trovare il maggior numero possibile di malfunzionamenti con il minor numero possibile di casi di test

## Test di Dijkstra
- Il testing non può dimostrare la correttezza del software
- La correttezza di un programma è un problema indecidibile
- il processo di testing deve fornire fiducia del software mostrando che è pronto per l'uso
## Testing e malfunzionamenti

- Processo di testing che determina assenza di malfunzionamenti del software può significare:
	- alta qualità del software
	- inadeguatezza dei casi di test: poiché non sono stati in grado di scoprire difetti esistenti
- malfunzionamenti non rilevati da un testing saranno rilevati dagli utenti = costo elevato
## Criteri di terminazione e adeguatezza del testing
- **Criterio temporale:** periodo di tempo predefinito
- **Criterio di costo:** sforzo allocato predefinito
- **Criterio di copertura:** sono stati esercitati un numero predefinito di obiettivi
- **Criterio statistico:** gli ultimi k test cases non hanno rilevato malfunzionamenti
# Testing VS Ispezione
## Analisi dinamica e statica
- Testing = analisi **dinamica**
	- rileva malfunzionamenti di un software mediante l'osservazione del suo comportamento e il confronto con il comportamento atteso
	- Testing possibile solo per software che possa essere eseguito
- Ispezione = analisi **statica**
	- mira alla verifica della correttezza del software senza eseguirlo
	- possibile anche per software incompleto o algoritmi non ancora implementati
### Analisi statica
- Prende in esami i documenti e istruzioni del programma senza eseguirle
- Difficile rilevare malfunzionamenti che dipendono dal valore assunto dinamicamente dalle variabili
#### Pro e contro
- **Vantaggi**
	- Malfunzionamenti possono mascherarne (nascondere) altri durante l’esecuzione dinamica
	- Possono essere ispezionate versioni incomplete di un sistema senza costi aggiuntivi
	- Oltre a cercare i difetti di un programma, un’ispezione può anche valutare attributi di qualità più generali, come la conformità agli standard e la portabilità
- **Svantaggi**
	- L’analisi statica può verificare la conformità con le specifiche ma non quella con le necessità degli utenti
	- L’analisi statica è meno adatta a verificare proprietà non funzionali come usabilità
# Livelli del testing 
- **Test dei componenti:** test di singole unità del software
- **Test d'integrazione:** integra diversi componenti tra loro per rilevare problemi d'interazione
- **Test di sistema:** software è testato dopo che tutti i componenti sono stati integrati
- **Test di validazione:** condotti dall'utente finale per validare i requisiti
## Testing di unità
- Test di unità = testare singoli componenti del sistema in isolamento
- Ciascun unità viene verificata sulla base della propria documentazione
- Avviene spesso durante la fase di implementazione
- Unità possono essere:
	- Metodi di una classe
	- Classi
	- Componenti riusabili che offrono una specifica interfaccia per accedere alle loro funzionalità
- vantaggi: sviluppatori hanno conoscenza del comportamento atteso 
- Sviluppatori tendono a difendere il proprio lavoro e a trovare meno difetti di tester indipendenti 
### Strategie di automatizzazione
**Main based approach:** modo per testare una classe e i suoi metodi
- **Problemi:**
	- il main aggiuntivo sarà anche distribuito nel prodotto finale
	- Per testare comportamenti alternativi saranno necessari più main methods
- Soluzione: usare soluzioni X-Unit

## Testing di integrazione

- Richiede la costruzione incrementale della struttura del sistema partendo dai componenti testati singolarmente
- Componenti in isolamento sono ritenuti corretti
- si deve verificare se ci sono malfunzionamenti durante la comunicazione tra i moduli
- Viene testato il sottosistema ottenuto attraverso l'integrazione di gruppi di componenti che realizzano una determinata funzionalità
## Test di regressione
- Possibilità che dopo una modifica il software sia regredito
- Dopo ogni integrazione si deve eseguire i test precedenti per evitare nuovi malfunzionamenti

## Testing di integrazione: stub e driver
- Moduli guida **driver**: simulano i componenti chiamanti:
	- Accettano i dati dei test case, invocano il componente chiamato e infine stampano i risultati
- Moduli fittizi (**stub**) simulano i componenti gerarchicamente inferiori al componente da testare
	- sono invocati dal componente testato, simulano il funzionamento del componente chiamato
	- funzioni fittizie, la cui correttezza è vera per ipotesi
>[!warning] Driver e stub sono un overhead in quanto devono essere sviluppati ma non fanno parte del prodotto finale.

## Testing di sistema 
- Il software è testato dopo essere stato integrato
- richiede che l'integrazione sia stata completata
- Verifica che tutti gli elementi del sistema siano stati correttamente integrati e che il sistema complessivo soddisfi i requisiti
- test sono definiti sulla base della specifica del sistema
## Testing di accettazione
Test di accettazione condotti dall’utente finale per consentire la
validazione di tutti i requisiti
- **α-Test**: condotto da un team selezionato composto da clienti e/o utilizzatori finali. Avviene in ambiente controllato, presso lo sviluppatore
- **β-Test**: condotto da un numero maggiore di utenti finali con il proprio hardware specifico che possono avere interazioni non previste con il software. Non è presente, solitamente, lo sviluppatore. Può rivelare nuovi difetti o incompatibilità, ma è anche una forma di commercializzazione
