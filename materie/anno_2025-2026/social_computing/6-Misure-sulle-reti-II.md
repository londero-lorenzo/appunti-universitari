---
title: 6-Misure-sulle-reti-II
aliases:
  - 6-Misure-sulle-reti-II
tags:
  - università
  - materie
  - anno-2025-2026
  - social-computing
  - 6-Misure-sulle-reti-II
created: 2025-10-17
description: (INCLUDE SLIDE 6-7)
---
### Misure

Domande a cui rispondono le diverse misure:

>[!question]
>Chi sono gli individui/attori più importanti in una rete?
>- **Centralità** (che abbiamo visto)
>
>Quali pattern di interazione sono comuni fra amici?
>- **Reciprocità** e **Transitività**
>- **Bilanciamento** e Status
>
>Quali individui sono simili e come li trovo?
>- **Similitudine**

___

## Social Network Analysis (SNA)

>[!definition]
>SNA
>>Disciplina storica che misura le relazioni tra le persone:
>>- Amicizia
>>- Collaborazioni
>>- Citazioni (bibliometria)

>[!example]
>Un grafo che rappresenta la collaborazione tra le diverse persone è un grafo con dei nodi (rappresentanti le persone) collegati tramite archi ad altri nodi con cui collaborano.

## Terminologia:
+ **Local bridge**: Un arco tra due nodi che sarebbero lontani tra loro senza quello
	+ "di grado k": con k la distanza che ci sarebbe tra i due nodi senza quel arco.
	  NON C'ENTRA NIENTE CON IL DEGREE DEL NODO
+ **Global bridge**: Arco che, se rimosso, disconnetterebbe l'intera rete

___

+ **Triangolo**: Sottografo connesso di tre nodi.
+ **Collegamento debole (Weak tie)**: collegamento che appartiene solo ad un triangolo o a pochi triangoli. (sinonimo di collegamento con una persona "di conoscenza")
+ **Collegamento forte (Strong tie)**: collegamento che appartiene a molti triangoli (sinonimo di collegamento con una persona "di forte amicizia")

___

+ **Geodesic**: Percorso più corto tra due nodi (la distanza è il numero di archi)
+ **Diameter** della rete: Il più lungo geodesic della rete (distanza maggiore tra due nodi)
+ **Grado** di un nodo: Numero di archi indegree e outdegree
+ **Degree distribution**: Per ogni grado, il numero di nodi che hanno quel grado
+ **Density**: Proporzione di archi: Numero di archi / numero massimo di archi
	+ Max: ((numero di nodi nella rete)$\*$(numero di nodi nella rete -1))/2
+ **Coefficiente di clustering** (C) di un nodo: (numero di archi tra i sui vicini) / (numero massimo di archi)
	+ Max: per n vicini --> n(n-1)/2
	+ C di una rete: media tra tutti i valori C dei nodi della rete


___

>[!tip]
>"**The strength of weak ties**"
>Solitamente per far arrivare un messaggio alla maggior parte della gente possibile bisogna mandarlo (controintuitivamente) attraverso i collegamenti deboli, in quanto solitamente collegano diversi nuclei di nodi.
>Infatti rimuovendo collegamenti forti le distanze non cambiano molto, invece rimuovendo i collegamenti deboli la rete tende a diventare disconnessa.

___

>[!example]
>In un esperimento si è voluta misurare le relazioni tra la centralità e i valori di hubness e authority degli algoritmi PageRank e HITS, ponendo per l'occasione uguali i due valori hubness = authority.
>Si è potuto evincere come un nodo presentasse i valori più alti qualunue fosse l'algoritmo utilizzato e il tipo di centralità (grado, vicinanza, betweenness) utilizzato, risultati resi ancora più evidenti una volta normalizzati i valori ricavati, come si può notare dall'immagine sotto con il nodo 'Mike' che è il più centrale.

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-10-17 214008.png|550]]

___

## Transitività e Reciprocità

Indicano delle situazioni tipiche che si formano nelle reti di 'amicizia':
+ **Reciprocità**: (Se io sono tuo amico, tu sei amico mio)
+ **Transitività**: (Se io sono amico tuo e tu sei amico suo, allora io sono amico suo)

### Transitività

Algebricamente: $aRb \land bRc \rightarrow aRc$ 

All'aumento della transitività ci sono grafi più densi e si è più vicini ad un grafo completo.

>[!question]
>Possiamo stimare quanto un grafo sia vicino ad essere completo misurandone la transitività?
>
>Non del tutto, grafo completo e alta transitività sono disuguali: aggiungendo archi a caso in un grafo già denso non aumento molto la transitività.

#### Indici di transitività (solitamente su grafi indiretti)
+ **Coefficiente di clustering locale:** 
	+ Relativo ad un singolo nodo, misura la transitività a livello dei singoli nodi, ovvero quanto i nodi vicini a $v$ sono a loro volta connessi
	+ Formula: $C(v\_i) =$ (Numero di coppie di vicini di $v\_i$ che sono connesse)/ (Numero di coppie di vicini di $v\_i$) 
+ **Coefficiente di clustering globale**: 
	+ Relativo alla rete, misura la transitività in grafi indiretti. Tre definizioni equivalenti:
		1. **Formula:** C = Cardinalità dei cammini chiusi tra tre nodi/Cardinalità cammini di lunghezza 2
		   **Spiegazione**: Conto i cammini di lunghezza 2 e controllo se esiste il terzo arco (ovvero se il cammino è chiuso e si riconduce al nodo iniziale formando un triangolo)
		2. **Formula:** C = Numero di triangoli $\*$ 6 / Cammini di lunghezza 2
		   **Spiegazione**: Conto i triangoli e moltiplico per 6 (siccome ogni triangolo ha 6 cammini chiusi di lunghezza 2 (quindi con il terzo arco che chiude come prima))
		3. **Formula**: Numero di triangoli $\*$ 3 / Numero di triple di nodi connessi
		   **Spiegazione**: ogni tringolo ha tre triple differenti. Di tutte le triple di nodi connesse, prendo quelle chiuse, ossia il numero di triangoli $\*$ 3.


### Reciprocità

Avviene quando se tu sei amico mio io divento amico tuo.
"Versione semplificata della transitività" in quanto considera cicli di lunghezza 2 (tra due nodi) al posto dei triangoli.

##### Reciprocità globale: 
Conto il numero di coppie reciproche nel grafo
**Formula**:
$$R = \frac{\sum\_{i, j, i<j}A\_{i,j}A\_{j,i}}{|E|/2} = \frac{2}{|E|} \* \frac12 \* Tr(A^2)$$
**Spiegazione**:
+ $A$ è la matrice di adiacenza
+ La sommatoria somma 1 ogni volta che c'è una coppia reciproca, quindi ogni volta che $A\_{i, j}$ = $A\_{j, i}$ = 1.
+ Al denominatore divido per il numero massimo possibile di coppie reciproche dati gli archi in E, ovvero la metà.
+ $A^2$ è per l'appunto la moltiplicazione della matrice di adiacenza $A$ per se stessa. Infatti sarà uguale a 1 se esiste sia l'arco da i a j che l'arco da j a i, e sarà  uguale a 0 altrimenti
+ Il $\frac12$ prima di Tr() è perché ogni coppia reciproca viene contata due volte e prendendo la metà viene invece contata una sola volta.

>[!example]
>Nell'immagine sotto sono presenti tre nodi e la matrice di adiacenza della rete è la seguente: 
>$$A=\begin{bmatrix} 0 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$$
>- Svolgimento: 
>
> $$R = \frac1mTr(A^2) = \frac14 Tr(\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 0 \end{bmatrix})$$
> - Spiegazione:
>   Ogni cella della matrice $A^2$ è composta dalla somma della moltiplicazione tra la riga $i$ e la colonna $j$ e gli archi reciproci producono valori positivi lungo la diagonale di $A^2$. Ogni 1 presente indica un cammino di lunghezza 2 da i a j e sulla diagonale tale cammino torna a $i$ stesso (esempio A $\rightarrow$ B $\rightarrow$ A), mentre gli altri valori 1 non sulla diagonale indicano percorsi di lunghezza due ma che non riportano al nodo da cui sono partiti.

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-10-22 123409.png|200]]

___

### Bilanciamento

Intuizione: 
+ **Bilanciamento sociale**: se X e Y sono grandi amici e Y e Z sono grandi amici, sarebbe strano se X e Z fossero nemici tra loro.
+ **Status sociale**: Se X è superiore a Y e Y è superiore a Z, sarebbe strano se Z fosse superiore a X.

>[!definition]
>Sbilanciamento
>> Se c'è incoerenza nelle relazioni amico/nemico, la rete è sbilanciata.

#### Teoria del bilanciamento sociale
Modella la coerenza nelle relazioni. Si definisce aggiungendo '+' (amicizia, +1) o '-' (inimicizia, -1) sugli archi. 

>[!tip]
>Un triangolo di nodi i, j, k è bilanciato se:
>$$w\_{ij}\cdot w\_{jk}\cdot w\_{ki} \geq 0$$
>con $w\_{ij}$ valore dell'arco fra i nodi $i$ e $j$
>

#### Teoria dello status sociale
Status: quanto un individuo è prestigioso all'interno della società
+ Like(X) se penso che X sia più importante di me
+ Dislike(X) se penso che X non sia più importante di me
Lo status è derivato dalla direzione degli archi, e infatti i cicli sono problematici perché vuol dire che uno è più importante di un altro che invece si considerava più importante transitivamente.

___

### Distribuzioni 'reali'

Soprattutto nelle degree distribution sui dati normali non sono praticamente mai uniformi, ma sono più grafici che presentano un picco, oppure una power law.

>[!example]
>Ad esempio per la distribuzione della ricchezza nel mondo ci sarà un picco di pochissimi individui (circa lo 0,1%) che possiede circa 3\4 della ricchezza mondiale.
>Altro esempio è la densità di popolazione che è centralizzata in poche aree metropolitane densamente popolate, con invece la maggior parte delle città che hanno una grandezza media.
>
>Stessa cosa succede con i siti web: Molti siti hanno meno di 1000 visualizzazioni al mese, mentre pochissimi siti sono visitati più di 1 milione di volte al giorno 

#### Power law (legge della potenza)
Funzione per calcolare la distribuzione dei gradi della rete, ovvero quanti nodi possiedono un determinato grado.
Formula: $p\_d = ad^{-b}$
+ $a$ è l'intercetta della power law
+ $d$ è il grado del nodo
+ $-b$ esponente della power law. Generalmente tra 2 e 3
+ $p\_d$ è la frazione di nodi con il grado $d$

Di norma una power law dovrebbe assomigliare graficamente ad una iperbole simmetrica alla bisettrice del primo e terzo quadrante. Per capire se una funzione è effettivamente una power law, si plotta in un grafico log-log, in cui dovrebbe diventare una retta, o approssimativamente molto vicina ad una retta.

>[!example]
>Alcuni esempi:
>- Frazione di numeri di telefono che ricevono k chiamate al giorno è circa proporzionale a $1/k^2$
>- La Frazione di utenti che hanno in-degree k è approssimativamente proporzionale a $1/k^2$

>[!tip]
>Sostanzialmente in molte distribuzioni relai come quelle riferite ai social media sono presenti distribuzioni riconducibili ad una power law, che quindi presenta valori piccoli molto comuni e valori grandi estremamente rari ma mai impossibili.

>[!warning]
>Probabilità di valori alti è molto bassa ma mai 0, diversamente quindi dalle teoriche distribuzioni esponenziali come la Gaussiana

##### Concetto di Long Tail
Essendo la coda sull'asse x di una power law molto lunga, nonostante la poca popolarità, messi tutti insieme rappresentano un volume importante.

>[!example]
>Ad esempio Mettendo insieme il volume delle vendite di libri considerati impopolari, formano il 57% delle vendite di Amazon.


___

### Distanza media, piccolo mondo

Se io voglio trasmettere una rumor o una notizia a più gente possibile dovrò comunicare con determinati nodi, con più probabilità di trasmetterla a loro volta ad un maggior numero di utenti, con l'ipotesi che tutti gli utenti lo passano immediatamente a tutti i loro amici.

>[!question]
>- Quanto passa prima che la notizia raggiunga quasi tutti i nodi della rete?
>- Tempo massimo? (corrisponde al diametro)
>- Tempo medio?

Milgram, psicologo sociale degli anni 60, a seguito di un esperimento svolto facendo consegnare a più persone una lettera ad altrettante persone potendola passare solo a loro conoscenti, ne derivò che i gradi di separazione tra due persone qualsiasi è in media di 6 persone: "Il mondo è piccolo".
Successivamente nel 2003 fu svolto lo stesso esperimento via email e il risultato fu ancora circa 6 gradi di separazione.

___

>[!warning]
>**Caffé & Anfetamine**
>![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-10-22 160715.png|200]]

#### Numero di Erdòs

Corrisponde al numero di link per connettere uno scienziato tramite co-autorato di articoli scientifici.
Fra i matematici, quindi:
+ Lunghezza dei cammini media: 4,65 ("mondo piccolo")
+ Lunghezza dei cammini massima: 13

+ Numero di Erdòs mediano: 5
+ Deviazione standard: 1,27

>[!example]
>Einstein ad esempio essendo stato uno scienziato che ha scritto diversi articoli con studiosi molto importanti e conosciuti, ha un numero di Erdòs pari a 2.


Nelle reti reali, ogni coppia di nodi è di solito connessa da un cammino breve. 

>[!example]
>- Su Facebook ad esempio la lunghezza media del cammino più corto tra due utenti è 4,7 nel mondo e 4,3 negli USA. "Circa 4 gradi di separazione".
>- Su Youtube la lunghezza media dei cammini più corti è circa 5.
>- Sul Web è di 16,12. 

___

### Altre proprietà delle reti reali

+ **Struttura core-periferica:**
  Solitamente hanno una struttura core-periferica, ovvero presentano un nucleo più denso con tanti archi e i nodi nella periferia con archi verso il core ma non fra di loro (struttura a "medusa" o "piovra").
+ **Paradosso degli amici:**
   In media il grado dei vicini del nodo $v$ è più alto del grado di $v$. Questo si è rivelato vero ad esempio per il 98% degli utenti Twitter nel 2013.
   "I tuoi amici hanno più amici di te".

