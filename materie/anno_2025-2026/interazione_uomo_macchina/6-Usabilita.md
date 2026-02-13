---
title: "6-Usabilita"
aliases: ["6-Usabilita"]
tags: [università, "materie", "anno-2025-2026", "interazione-uomo-macchina", "6-Usabilita"]
created: 2025-12-05
---
# Usabilità

### Introduzione all'usabilità
L'usabilità è un concetto a molte dimensioni, e ciascuna dipende dalla tipologia dell'applicazione.
>[!example]
>+ In un chiosco di ufficio turistico è importante la facilità di apprendimento, in quanto lo userò pochissimo nella mia vita.
>+ In un gestionale invece posso anche avere una curva di apprendimento più lunga ma lo userò per molto più tempo nella mia vita.

### Benefici dell'usabilità
+ Aumentare efficienza e produttività
+ Ridurre errori
+ Ridurre addestramento
+ Ridurre bisogno di supporto   /   Aumentare l'accettazione del supporto tecnico
+ Aumentare vendite

### Problemi di usabilità
Si differiscono in diversi livelli:
+ **Esecuzione**
+ **Valutazione**

+ Si parte dall'**obiettivo** dell'utente che si va a concretizzarsi in un'**intenzione**, quindi adesso passa all'azione, che corrisponde all'**esecuzione** che viene svolta dal computer.
+ Tramite la **percezione** vedo se l'azione ha svolto una conclusione e la analizzo svolgendo una **interpretazione** del risultato, per poi fornire una **valutazione** sul risultato ottenuto.

![[materie/anno_2025-2026/interazione_uomo_macchina/assets/Screenshot 2025-12-05 145626.png]]

___
### Mapping

>[!example]
>+ Nel congegno con forno e fornelli messi insieme bisogna indovinare la manopola da girare per accendere un fornello. in base all layout delle manopole posso capire che le due manopole da sole sono per il forno e le altre 4 per i fornelli. Il gas giusto sarà indicato dal disegnino sopra alle manopole.
>+ Mettere le manopole in griglia tipo quadrato invece che in linea retta avrebbe aiutato il riconoscimento della manopola ma avrebbe privato spazio al forno probabilmente.
>+ Si poteva fare anche un mapping cromatico con un colore diverso per ogni fornello.
>+ Variare la grandezza dei pomelli in base alla grandezza dei fuochi
>+ Oppure mettere i pomelli vicino al corrispettivo fuoco, o sulla stessa linea del piano di cottura.
>+ Cambiare il mapping dei fuochi e mettendoli in fila come i pomelli.

### Metodi per la valutazione dell'usabilità

**Cosa si può valutare**:
+ Elementi iniziali di progettazione (mock-up, scenari, task analysis)
+ Prototipi iniziali, in cui il software è relativo all'interfaccia utente ma le funzionalità non sono ancora state implementate
+ Prototipi avanzati, buona parte dell'interfaccia utente  e delle funzionalità relative sono state implementate

#### Scopi della valutazione:
+ **Valutazione formativa**
	+ mira a supportare la progettazione
+ **Valutazione riassuntiva**
	+ Convalida della qualità, requisiti per nuovi sistemi


# Approcci alla valutazione di usabilità

+ Osservazione utenti
+ Feedback degli utenti
+ Modelli
+ Ispezione da parte di esperti
___
### Valutazione basata sui modelli

+ **Modelli**: Prevedere caratteristiche del sistema (es. efficienza) senza coinvolgere ulteriori utenti
	+ **KLM** (keystroke-level model) **GOMS** (Goals, Operators, Methods, Selection rules)
		+ Operatori sono intesi come azioni elementari necessarie per raggiungere gli obiettivi utente, intesi come risultati che si vogliono ottenere
		+ I metodi che raggruppano gli operatori necessari per raggiungere gli obiettivi
		+ Regole di selezione indicano quando è più opportuno seguire un modello o un altro
		+ Modello usato per **predire il tempo per raggiungere l'obiettivo**
		+ KLM è una tabella usata per determinare i tempi delle singole task, utilizzata successivamente per definire la durata degli operatori.

>[!example]
>Esempio di tabella KLM per il PC comprende tutte le tempistiche necessarie ad esempio per printare una key, per puntare col mouse, premere un bottone, cliccare due volte, cambiare da mouse a tastiera e viceversa, tempo di attesa dovuto al sistema. Tali azioni rappresentano ognuna un operatore.

>[!tip]
>Per creare queste tabelle KML servono un alto numero di utenti di cui prendere la media, e diverse tabelle variano in base alla piattaforma o agli utenti target.

___
### Valutazione basata su ispezione

+ Applicato da valutatori di un sistema, e produce alla fine un rapporto di usabilità con l'identificazione di possibili problemi
+ Obiettivo: nessun falso positivo (segnalazione errori inesistenti) e pochi falsi negativi (mancata segnalazione errori esistenti)
+ Approcci:
	+ Basati su regole
		+ Principi (coerenza, flessibilità)
		+ Euristiche (tipo Nielsen e Molich)
		+ Linee guida
		+ Regole di stile (tipo regole interne all'azienda, come l'uso di determinati colori)
	+ Basati su cammini (cognitive walkthrough)
		+ Descrizione del prototipo
		+ Descrizione dei task (non lascio provare a caso l'esperto come in quello basato sulle regole)
		+ Indicazioni sulle caratteristiche degli utenti
		+ Lista delle azioni per eseguire i task
		+ Cerca di rispondere a delle domande precedentemente realizzate (es. l'utente cercherà di svolgere l'azione? Noterà che l'azione corretta è disponibile?, ecc...)

___

### Metodi per la valutazione basata sull'osservazione degli utenti

Dipendono da:
+ Luogo:
	+ Laboratorio: si osservano alcuni aspetti senza interferenze esterne. Tuttavia si rischia di mettere in una condizione di pressione l'utente chiamandolo in laboratorio, non rispecchiando il comportamento che avrebbe in uno spazio per lui naturale.
	  Risoluzione potrebbe essere tipo interrogatori in cui l'utente è in una stanza da solo e gli analizzatori sono in un'altra stanza, magari con telecamere o vetri oscurati.
	+ Sul campo: l'utente agisce nel suo ambiente naturale ma rischio gli elementi di disturbo.
>[!example]
>Per esempio le valutazioni di un sistema di pilotaggio aerei. In laboratorio c'è molto più controllo, magari sul numero di utenti che chiamo a provare. Se l'applicazione la butto sullo store può non scaricarla nessuno oppure milioni di utenti.
>Se, un altro esempio, do dei questionari da compilare in remoto, posso avere degli utenti che lo fanno in 30 secondi e quelli che lo fanno in 15 minuti, nonostante il questionario sia in media lungo 3 minuti. Questo perché magari uno si è stufato e ha sparato le rispostea caso e l'altro invece aveva ricevuto una chiamata che ha dilatato i tempi. Nessuno dei due utenti deve quindi venire considerato nell'analisi successiva delle tempistiche

##### Caratteristiche 
In un test sono importanti:
+ Affidabilità
	+ Utenti rappresentativi? (hanno già usato/non hanno già usato; giovani/vecchi)
	+ Se rifaccio il test cambiando gli utenti ottengo gli stessi risultati?
+ Validità
	+ Il test misura qualcosa effettivamente interessante?
	+ Metodo usato è corretto? (es. metriche)

>[!tip]
>La rilevanza dello studio è importante per la buona riuscita del test stesso.

#### Esempi di metriche di usabilità

+ Tempo impiegato per completare un compito
+ Numero di compiti completati in un intervallo fisso di tempo
+ Numero di compiti svolti/non svolti complessivamente
+ Numero di errori (oppure rapporto tra interazioni corrette ed errori)

___

### Metodi per la valutazione basati sull'osservazione degli utenti

##### Organizzare un test su utenti (come l'esperienza di laboratorio fatta)
(IMPORTANTE)

+ Obiettivo del test
+ Durata del test
	+ Problema del **drop out**: ad esempio se faccio un test e voglio valutare se l'utente si ricorda anche in futuro, devo richiamare l'utente in tempi successivi e magari gli utenti ad una certa non sono più disponibili
+ Caratteristiche hardware/software
	+ Caratteristiche che permettono o non permettono di svolgere al meglio l'esperienza. (ad esempio usare una sedia senza e con braccioli in cui l'utente sta più o meno comodo)
+ Condizioni iniziali
	+ Le condizioni ad esempio dell'illuminazione per svolgere il test può influire sul test stesso. Ma anche il volume ad esempio del computer.
	+ Ci possono essere degli extreme outlier rispetto alle condizioni iniziali che ci si aspetta (ad esempio se 98 su 100 hanno circa 10 ore col VR e solo 2 hanno migliaia di ore col VR, essi saranno extreme outlier e solitamente escludo i soggetti per tutto l'esperimento).
+ Utenti/numero utenti
	+ Problema del campionamento degli utenti: fare un test su un app per i medici e su 3000 medici in FVG ne prendo gli unici 30 che sono entusiasti della VR: non sarebbe rappresentativo della classe.
+ Compiti che gli utenti dovranno eseguire:
	+ Una serie di task precisi che l'utente deve eseguire (la procedura), e stabilire una misura che delimita se l'utente ha fatto bene o ha fatto male.

### Esperimenti controllati

>[!example]
>Procedura sperimentale.
>Confronti tra diversi utenti tra il mio farmaco e uno standard oppure non  do loro niente.
>Soggetti devono essere rappresentativi dell'utenza generale e anche in numero sufficiente.
##### Caratteristiche
+ Scelta dei soggetti: deve essere rappresentativa
+ Variabili indipendenti e dipendenti
	+ Più valori di variabili indipendenti voglio misurare e più grande dev'essere il campione
>[!example]
>**Variabile indipendente**: tecnica di interazione di puntamento
>**Variabile dipendente**: numero dei task utilizzati nella tecnica completati con successo

+ Ipotesi, ciò che mi aspetto
	+ Non è detto che tutte le ipotesi che faccio siano giuste, possono anche venire ribaltate
+ Procedura sperimentale: la procedura con la quale viene svolto l'esperimento
	+ Deve essere rigorosa, in alcuni casi si scrive anche le esatte parole da dire. Questo perché è un attimo dare un indizio in più ad un utente rispetto che ad un altro.
+ Analisi statistica

#### Organizzare la partecipazione degli utenti
+ **Between subjects**: ogni utente è assegnato a una sola condizione analizzata
	+ Il between ha sicuramente bisogno di più utenti
	+ **Bilanciamento dei gruppi**: Se ho un ordine di mille utenti, separare in gruppi randomicamente dovrebbe andare bene e separare gruppi egualmente bilanciati.
	  Per un numero inferiore di persone però separare randomicamente rischia di favorire la creazione di gruppi sbilanciati tra loro in base al task che è da fare

+ **Within subjects**: ogni utente esegue i compiti in ciascuna condizione considerata
	+ Cercando però di evitare il **learning effect**, imparare il meccanismo dovuto al fatto di fare task simili più volte.
>[!example]
>Voglio confrontare dei joystick e faccio fare tre volte il task.
>Posso fare il task 3 volte, per evitare l'apprendimento posso formulare i compiti con diverse istruzioni (tipo al primo faccio cambiare la lingua del personaggio e in un altro la lingua del sistema).

#### Analisi statistica
##### p-value
Una misura di quanto un risultato sia dovuto al caso è il valore $p$, ricavato facendo un test statistico sui risultati.
Quindi se il valore $p$ è vicino allo 0 l'analisi è effettivamente corretta e non derivante dal caso, se è vicino a 1 probabilmente è dovuta al caso.
>[!tip]
>Tipicamente si accetta una statistica con $p=0.5

##### Effect size
Per ogni tipo di design può cambiare il misuratore di effect size. 
Questa misura dice "quanto è grande l'effetto".
Ad esempio per il **cohen's d** (una formula che calcola l'effect size):
+ l'effect size è small sotto lo 0,2: c'è piccola differenza che non si vede ad occhio nudo
+ è medium attorno al 0,5: c'è differenza che si vede ad occhio nudo
+ è large sopra lo 0,8: c'è differenza sostanziale evidente

>[!example]
>è medium se la statistica analizzata è il tempo di svolgimento e si vede ad occhio nudo che alcuni utenti ci mettono più tempo di altri a svolgere il task.

___

### Metodi basati su feedback dell'utente

Approcci:
+ Feedback informali dell'utente
+ Questionari (self-report)
	+ Vari tipi di questionari:
		+ **Categoriali** (scelta singola o multipla)
		+ **A scala di risposta** (es. scala di Likert con un tot di valori, con gli estremi della scala vanno da "fortemente in disaccordo" a ""fortemente d'accordo")(System Usability Scale-SUS)
		+ **Ranking** (es. mettere in ordine di piacevolezza diverse esperienze)
		+ **Risposte aperte** (es. cosa hai trovato di difficile utilizzando il software?; non posso farci analisi statistica ma per capire le motivazioni dell'utente)
		
		+ **Questionari on-line**: 
			+ Vantaggi: costi ridotti, efficienza, velocità, campioni vasti geograficamente
			+ Svantaggi: difficoltà di controllo dell'attendibilità dei dati raccolti, difficoltà del monitoraggio del contesto
+ Interviste
	+ Costruire interazione positiva con l'intervistato
	+ Saper ascoltare e riformulare
	+ Atteggiamento semplice ed amichevole
	+ Sapere quali domande fare e come formularle
+ Focus group
	+ Specie di interviste ma ho più persone contemporaneamente. Devo avere un certo numero di persone e delle buone capacità da moderatore. Un po' difficile.

>[!example]
>Scelta del metodo di valutazione:
>+ Capire i tempi di svolgimento di un compito? --> Osservazione con cronometro, oppure utilizzando dei modelli.
>+ Quantificare la soddisfazione dell'utente? --> metodo basato sul feedback dell'utente/Questionario/Intervista.
>+ Primo feedback veloce su idee di design? --> Chiamare degli esperti oppure svolgere delle interviste a degli utenti target.
>+ Valutare prototipo con tutte le funzionalità? --> Utilizzo osservazione e la valutazione.

___

### Strumenti di supporto alla valutazione di usabilità
#### Valutazione remota
+ Utenti lontani dai valutatori
+ Al posto di portare tutti gli utenti in laboratorio (difficile e costoso)
###### Metodi per la valutazione remota
+ Questionari remoti
+ Osservazione remota (es. video-conferenza)
+ Errori critici riportati dall'utente
>[!example]
>Esempio di Remote Evaluation è la scelta tra faccina felice e faccina scontenta, con possibilità di espandere il proprio pensiero.

#### Analisi Web log
+ Informazioni su chi ha visitato il sito, i cammini che i visitatori seguono nel sito, le tempistiche su ciascuna pagina del sito, successo delle attività utente nel sito.
#### Analisi dei movimenti oculari
+ **Saccadi:** Movimento che può compiere l'apparato dell'occhio per spostare l'asse durante l'esplorazione di una scena
+ **Fissazioni:** pausa tra due saccadi successive (intervallo durante il quale viene acquisita l'informazione visiva)
+ **Scanpath**: tracciato che gli occhi compiono

>[!tip]
>Analisi dei movimenti oculari possibili grazie ad un eye tracker, oppure tramite heat map (colori caldi dove guardo di più, freddi dove guardo meno).

---


