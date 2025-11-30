---
title: "16-17-Networkx-Pyvis"
aliases: ["16-17-Networkx-Pyvis"]
tags: [università, "materie", "anno-2025-2026", "social-computing", "16-17-NetworkX-Pyvis"]
created: 2025-11-30
---
Le due slide si concentrano principalmente sulla **rappresentazione, l'analisi e la visualizzazione dei grafi** utilizzando le librerie Python **NetworkX** e **Pyvis**.

# Fondamenti dei Grafi e Rappresentazione Teorica

I grafi sono strutture dati scritte come G=(V,E), dove V è l'insieme dei nodi/vertici e E è l'insieme degli archi che collegano coppie di nodi.

+ **Tipologie:** I grafi possono essere **Diretti** (es. Twitter, dove seguire non implica reciprocità) o **Non Diretti** (es. Facebook, dove l'amicizia è reciproca).

+ **Matrici di Rappresentazione:**
	+ **Matrice di Adiacenza (A):** Matrice quadrata dove l'entrata Aij​ è 1 se esiste un arco da i a j, e 0 altrimenti. Nei grafi pesati (weighted graphs), l'entrata corrisponde al peso dell'arco.
	+ **Matrice di Incidenza:** Le righe rappresentano i nodi e le colonne rappresentano gli archi. In una matrice di incidenza orientata (per grafi diretti), si usa +1 per la destinazione e -1 per la sorgente di un arco.

+ **Densità:** La densità di un grafo misura quanti archi sono presenti rispetto al numero massimo possibile di archi.

___
## NetworkX: Creazione, Manipolazione e Attributi

NetworkX è una libreria Python utilizzata per la **creazione, l'analisi e la visualizzazione dei grafi**. Offre strutture dati, algoritmi e misure di analisi della struttura di rete.

+ **Nodi e Archi:**
	+ **Nodi:** Possono essere qualsiasi oggetto **immutabile** (ad esempio, un intero, una stringa di testo, una tupla, un'immagine), ma non strutture dati mutabili come liste o dizionari.
	+ **Creazione:** Un grafo vuoto si costruisce con `networkx.Graph()`. Nodi e archi possono essere aggiunti singolarmente (`add_node(n)`, `add_edge(n1, n2)`) o in blocco da liste o altri contenitori iterabili (`add_nodes_from(list)`, `add_edges_from(list)`).
	+ **Rimozione:** Nodi e archi possono essere rimossi in modo simile all'aggiunta (`remove_node(n)`, `remove_edge(n1, n2)`).

+ **Attributi:** Attributi come etichette, colori o pesi possono essere allegati a grafi, nodi o archi. Per i grafi pesati, il "peso" può rappresentare proprietà quantitative o qualitative, come il numero di interazioni tra utenti nelle reti sociali.

+ **Esplorazione:** Si può esaminare il contenuto del grafo usando `graph.nodes()`, `graph.edges()` e ottenere il numero totale di elementi. `graph.adj[n]` mostra i vicini di un nodo. `graph.degree[n]` mostra il grado del nodo.

+ **Grafi Diretti (*DiGraph*):** La classe `DiGraph` fornisce metodi specifici. Il concetto di "vicini" è equivalente a "successors". I "predecessors" sono nodi che hanno un arco diretto che punta verso il nodo in questione. Il grado (degree) di un `DiGraph` è la somma di `in_degree` e `out_degree`.

___
## Generazione e Operazioni sui Grafi

I grafi possono essere costruiti non solo elemento per elemento, ma anche generati usando metodi diversi:

+ **Operazioni Classiche:** Applicazioni di operazioni come **Unione** (che combina due grafi, assicurando nomi di nodo unici), **Prodotto Cartesiano** o il **Complemento di un Grafo** (stesso insieme di nodi, ma gli archi collegano solo i nodi che _non_ erano collegati nel grafo originale).

+ **Grafi Classici Predefiniti:** Grafi specifici richiamabili (es. Petersen Graph, Tetrahedral Graph).

+ **Generatore Costruttivo:** Basato su regole o pattern. Esempi includono il **Grafo Completo (**Kn​**)**, dove ogni coppia di nodi è connessa da un arco, e il **Barbell Graph**, composto da due grafi completi collegati da un percorso.

+ **Generatore Stocastico:** Crea grafi basati su modelli probabilistici. Esempi sono il **Grafo Erdős-Rényi** o **Grafo Binomiale** (Gn,p​), e il **Grafo Barabási-Albert**, dove i nuovi nodi si attaccano preferenzialmente a quelli con un alto grado.

___
## Applicazioni e Case Study

I grafi sono utilizzati per modellare diversi scenari reali:

+ **Reti Sociali:** Nodi che rappresentano persone e archi che rappresentano relazioni (amici, colleghi). Twitter è un esempio di grafo diretto; Facebook, di grafo non diretto.

+ **Scienza e Medicina:** Molecole in Chimica (atomi = nodi, legami = archi); reti di co-autori in ambito accademico; Imaging Medico per rilevare gliomi in risonanze magnetiche; Bioinformatica (strutture molecolari).

+ **Case Study (Game of Thrones):** Si usa un dataset di personaggi di _Game of Thrones_. Un arco collega due personaggi se i loro nomi appaiono entro 15 parole l'uno dall'altro. Il **peso** dell'arco rappresenta il numero di interazioni tra i personaggi. È possibile estrarre un **Grafo Ridotto (Ego Graph)** che si concentra su un singolo nodo e i suoi vicini entro una distanza specificata.

___
## Pyvis: Visualizzazione Interattiva

Pyvis è una libreria specificamente progettata per **creare e visualizzare grafi di rete interattivi** in un browser.

+ **Funzionalità:** Permette di trascinare i nodi, zoomare e ispezionare le connessioni, ed è adatta per la visualizzazione intuitiva di grafi di grandi dimensioni.

+ **Integrazione NetworkX:** Pyvis può visualizzare direttamente i grafi creati con NetworkX utilizzando la funzione `.from_nx()`. Gli attributi di nodo e arco di NetworkX (come titolo, colore, dimensione) vengono automaticamente riutilizzati da Pyvis per la visualizzazione dinamica.

+ **Layout:** Gli algoritmi di layout determinano la disposizione spaziale degli elementi del grafo. Esempi di layout per la funzione di disegno includono circolare, casuale, spettrale (che usa il Laplaciano del grafo), e a spirale. Le proprietà dei nodi, come il `title`, possono essere usate per mostrare descrizioni quando si passa il mouse sopra il nodo nella vista HTML.

___
## Misure e Analisi dei Grafi

Le misure dei grafi sono essenziali per l'analisi quantitativa, aiutando a comprendere l'importanza dei nodi e il comportamento della rete. Per confrontare visivamente le misure, si possono colorare i nodi in base al valore della metrica scelta (l'intensità del colore mostra il valore).

+ **Degree Centrality (Centralità di Grado):** Misura il numero di connessioni dirette di un nodo. Indica il nodo più connesso.

+ **Betweenness Centrality (Centralità di Intermediazione):** Misura la frequenza con cui un nodo si trova sui percorsi più brevi tra gli altri nodi. Identifica i **nodi ponte** critici per collegare diverse parti della rete.

+ **In-Degree Centrality (Centralità del Grado Entrante):** Usata per i grafi diretti, conta le connessioni in ingresso. I nodi con un valore più alto sono considerati più popolari o influenti.

+ **PageRank:** Stima quanto spesso un nodo verrebbe raggiunto se qualcuno si muovesse casualmente nella rete. Un nodo è importante se riceve molti link, specialmente da nodi già altamente connessi.

+ **Clique Massima:** Il più grande gruppo di nodi in cui ogni membro è collegato a tutti gli altri. Spesso rappresenta una comunità centrale o un gruppo fortemente unito.

___

## Connessione tra NetworkX e Pyvis

Il punto di connessione chiave è il metodo `from_nx()` della classe `Network` di Pyvis.

+ Si crea un oggetto grafo in NetworkX (ad esempio, `G = nx.Graph()`).
+ Si popola `G` con nodi e archi.
+ Si esegue l'analisi con NetworkX e si **aggiungono gli attributi** calcolati (come la dimensione o il colore in base al punteggio di centralità) ai nodi del grafo `G`.
+ Si passa l'oggetto grafo di NetworkX (`G`) a Pyvis.

In sintesi, **NetworkX** gestisce la logica di rete e l'analisi, mentre **Pyvis** si occupa di trasformare il modello analizzato in una **visualizzazione dinamica e condivisibile**.