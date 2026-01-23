---
title: 20-(Micro)task-Design
aliases:
  - 20-(Micro)task-Design
tags:
  - università
  - materie
  - anno-2025-2026
  - social-computing
created: 2025-12-12
---
# Obiettivo: capire come progettare un task

>[!example]
>Ad esempio si può rispondere ad un task sia attraverso un radio button oppure con una scelta multipla, oppure con un input text libero o inserendo una variabile.

### Relevance
Richiedere la rilevanza di una page web in una query, ovvero capire se un documento mostrato è rilevante o pertinente rispetto ad un'interrogazione (query) a un motore di ricerca.
Utilità:
+ Molte query, molte pagine web
+ Valutazione dell'efficacia di un motore di ricerca
##### Relevance assessment 1 (Binario)
Prima variante:
+ Rilevanza binaria: o lo è o non lo è
##### Relevance assessment 2 (Categorie)
Seconda variante:
+ Relevance a categorie (Good, Fair, Not relevant)
+ Si vuole sempre capire la relevance a una query
##### Relevance assessment 3 (Web page)
+ Esplicitamente su pagine web
+ Sempre relevance a categorie
##### Relevance assessment 4 (A/B test)
+ Pairwise, confronti di coppia
+ Scegliere il migliore fra una coppia

>[!example]
>Individuazione fake news:
>Potrebbe essere un task da lasciar fare al crowd, anche se in realtà è proprio il crowd che le crea le fake news.
>Vengono quindi utilizzati dei meccanismi di misurazione, con confronti a coppie, bias, scale diverse, pairwise, ecc...

___
### Scale fini

>[!question] Meglio una scala a 6 valori o una scala a 100 valori?

In base alla diversa scala si è voluto controllare la veridicità attraverso ogni worker di alcuni statement, alcuni veri e alcuni falsi. Ogni worker doveva quindi giudicare appunto attraverso la scala a 6 valori o quella a 100 valori.

#### Pairwise comparison
Consiste nei confronti a coppie, ma già per 6 statement per ogni worker vengono coppie nell'ordine delle $6^2$ con 15 combinazioni possibili, a cui aggiungerne 2 per il quality check (coppia già mostrata ma invertita per capire l'attenzione del worker). Quindi ogni worker valuta 17 coppie.

Ci sono tante possibilità e bisogna fare molte scelte, prendere tante decisioni:
+ Serve un metodo, una metodologia, un modo di lavorare, con prove, tentativi, ecc...

---

## Come progettare un microtask
#### Microtask design workflow

>[!warning]
>Progettare un task su amazon mechanical turk non è molto diverso dallo scrivere codice.

Progettare un task è molto simile all'approccio di ingegneria del software o programmazione orientata agli oggetti.

**Workflow della programmazione**
+ Si parte dal problema
+ Si pensa ad un'idea/algoritmo
+ Versioni intermedie in pseudocodice
+ Faccio una prima versione (prototipo)

**Workflow delle microtask**
+ Problema 
+ Idea
+ prototipo di HIT
+ Rilascio in laboratorio
+ Test pilota
+ In produzione
+ Da ripetere ciascuna task più e più volte. Le volte necessarie

### Step
1. Capire per bene il problema
2. Idea di soluzione:
	1. Capire l'esperimento da fare
	2. Quanti/quali dati, quanta mole di dati, quanto pagare, quanti controlli di qualità
	3. ISTRUZIONI del task: non troppo lunghe e non troppo vaghe. Chiari, concisi e sintetici.
	   Il worker per 5 centesimi non c'ha voglia di leggere robe lunghe e di scervellarsi troppo
	4. Feedback: Capire come raccogliere i feedback, solitamente campo di testo in cui il worker può lasciare dei commenti in maniera opzionale
3. Prototipo di HIT:
4. Rilascio in laboratorio
	1. Sandbox di mturk può essere utile, ma anche Crowd_Frame
	2. Obiettivo: capire se sono presenti dei bug
5. Test pilota (far svolgere il compito sulla piattaforma con worker veri)
6. In produzione (su mturk)
	1. Essere preparati ad aver sbagliato un dettaglio apparentemente insignificante e a dover rifare tutto
	2. Attenzione all'ora del giorno (e al giorno della settimana) in base alla nazionalità dei worker che voglio raggiungere

A questo punto avremo i risultati dei task, con la fase di analisi dei risultati con l'analisi della matrice workers / tasks.

### Software vs. Wetware (umani)

**Software**:
+ non servono motivazioni
+ Istruzioni atomiche chiare
+ errori inesistenti
+ Comportamenti totalmente onesti

**Wetware**:
+ Motivazioni sono fondamentali
+ Possibili incompetenze
+ Errori presenti/frequenti
+ Comportamenti maliziosi/disonesti in alcuni casi

>[!tip] Attitudine
>Ci saranno sicuramente degli errori, incongruenze.
>Quindi è suggerito non buttare via tutto al minimo errore, ma cercare di fare il meglio che si può con i dati che si hanno e usare tutti gli accorgimenti possibili per diminuire effetti degli errori.

___

### Linee guida
Bisogna fare attenzione a:
+ Istruzioni chiare
+ Linguaggio adeguato
+ Ricompense adeguate
+ ecc...

Design problematici solitamente hanno delle liste di cose da NON fare, mentre il worker vuole solo sapere cosa deve fare.

+ Lista di DO (cose da fare) semplice e di immediata comprensione è molto meglio. Addirittura possono non servire le istruzioni, ma già  dall'interfaccia utente si capisce cosa bisogna fare.
+ Query, documento e risposte presentate nella stesa pagina con l'HIT danno una visione di insieme e immediato al worker.


