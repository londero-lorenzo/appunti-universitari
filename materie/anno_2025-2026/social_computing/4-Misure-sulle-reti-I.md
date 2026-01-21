---
title: 4-Misure-sulle-reti-I
aliases:
  - 4-Misure-sulle-reti-I
tags:
  - università
  - materie
  - anno-2025-2026
  - social-computing
created: 2025-10-10
description: (INCLUDE SLIDE 4-5)
---

# Misure sulle reti

Misure con lo scopo di trovare chi è più importante o influente in una rete sociale, o misurazione dei pattern di interazione più tipici tra diversi individui.
Per definire queste relazioni vengono usate misure **quantitative**.

### Misure di centralità:

La centralità di un nodo in una rete non comporta la centralità 'geografica', ma è la misura (numero) che indica quanto un nodo è centrale sulla base di alcune definizioni.
Su reti vere è molto difficile/impossibile trovare il nodo centrale.

##### Klout: 
era un servizio che studiava e offriva analisi sulle influenze dei diversi personaggi sui social media, offrendo un grado di influenza per ogni persona analizzata.

>[!tip]
>Non è banale distinguere tra influenza e centralità

Le misure di centralità sono diverse:
+ Degree centrality
+ Betweenness centrality
+ Closeness centrality
e le vediamo di seguito...


## Centralità 'semplice'
### Centralità di grado:
Più alto è il grado, più alta è la centralità del nodo.
C'è la versione per grafi indiretti e anche per diretti con in-degree e out-degree
>[!tip]
>generalmente in-degree (prestigio di un nodo) è più interessante di out-degree (quanto un nodo è gregario).

Formule (dove $C\_i$ è la centralità di un nodo $v\_i$ definita dal grado $d\_i$):
+ Per grafi indiretti:
$$C\_d(v\_i)=d\_i$$
+ Per archi in-degree di grafi diretti:
$$C\_d(v\_i)=d\_i^{in}$$
+ Per archi out-degree di grafi diretti:
$$C\_d(v\_i)=d\_i^{out}$$
	(Si possono usare e sommare anche la combinazione di in-degree e out-degree).

>[!problem]
>Per analizzare due diversi nodi appartenenti a due diversi grafici avrò bisogno di una sorta di normalizzazione in quanto il primo nodo potrebbe avere un grado di centralità maggiore del secondo, ma magari il primo nodo è collegato a metà dei nodi del suo grafo, mentre il secondo è collegato a tutti i nodi del suo grafo. Serve una normalizzazione per porli sullo stesso piano.

Diverse opzioni di normalizzazione:
+ Normalizzazione per grado massimo possibile (sostanzialmente quanti collegamenti presenta il nodo):
$$C\_d^{norm}(v\_i) = \frac{d\_i}{n-1}$$
+ Normalizzazione per grado massimo effettivo:
$$C\_d^{max}(v\_i) = \frac{d\_i}{max\_jd\_j}$$
+ Normalizzazione per somma dei gradi:
$$C\_d^{sum}(v\_i) = \frac{d\_i}{\sum\_jd\_j}= \frac{d\_i}{2|E|} = \frac{d\_i}{2m}$$

>[!warning]
>Le diverse formule di normalizzazione non possono essere usate tutte insieme ma tutti i dati devono avere lo stesso tipo di normalizzazione.

### Centralità di betweenness:
Tipicamente voglio andare dal nodo a al nodo b in cammini più brevi, la beetweenness calcola quanto un nodo si trova in questi cammini brevi, ovvero quanto un nodo è importante nel connettere altri nodi tramite cammini (guardando solo i **cammini minimi**).

##### Formula:
$$C\_b(v\_i)= \sum\_{s\neq t\neq v\_i}\frac{\sigma\_{st}(v\_i)}{\sigma\_{st}}$$
+ Considero tutte le combinazioni di coppie di nodi e per ognuna calcolo (cammini che passano per un nodo v)/(numero totale di cammini minimi) --> ottengo un valore che testimonia quanto un nodo è 'in mezzo' a questi cammini minimi.

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-10-10 114648.png|350]]

>[!example]
>Guardando l'immagine sopra:
>$C\_b(v\_2)= 2 \* ((1/1) + (1/1) + (2/2) + (1/2) + 0 + 0) = 2\*3.5 = 7$
>
>Spiegazione:
>- Il primo 1/1 rappresenta che v2 è in mazzo a 1 cammino minimo su 1 nel percorso tra v1 e v3
>- Il secondo 1/1 che v2 è in mezzo a 1 cammino minimo su 1 nel percorso tra v1 e v4
>- 2/2 tra v1 e v5
>- 1/2 tra v3 e v4
>- 0 tra v3 e v5
>- 0 tra v4 e v5
>- Il tutto viene moltiplicato per 2 perché per ogni coppia che ho analizzato (a, b) devo calcolare anche il loro inverso (b, a) che avranno lo stesso valore

Anche nel caso della betweenness c'è la versione normalizzata:
$$C\_b^{norm}(v\_i)=\frac{C\_b(v\_i)}{2(\binom{n-1}{2})}$$
Spiegazione: Nel migliore dei casi il nodo $v\_i$ è su tutti i cammini minimi della coppia di nodi analizzata, quindi $\frac{\sigma\_{st}(v\_i)}{\sigma\_{st}}=1$ e ciò porta a $C\_b(v\_i)=(n-1)(n-2)$ che è quindi il valore massimo


### Centralità di vicinanza (closeness):
Un nodo è centrale se da lui riesco a raggiungere velocemente gli altri nodi.

##### Formula:
$$C\_c(v\_i)= \frac{1}{l\_{v\_i}} = \frac{N−1}{\sum\_j​d(i,j)}$$
+ con $l\_{v\_i} = \frac{1}{n-1}\sum\_{v\_j\neq v\_i}l\_{i,j}$
+ Dove:
	+ $l\_{v\_i}$ è la lunghezza media dei cammini più brevi da $v\_i$
	+ $l\_{i,j}$ la lunghezza del cammino più breve da $v\_j$ a $v\_i$
	+ $n$ sono i nodi della rete

Spiegazione:
+ Considero i cammini minimi verso tutti gli altri nodi e il nodo centrale avrà una lunghezza media di tali cammini più bassa

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-10-10 120721.png|350]]

>[!example]
>Osservando l'immagine sopra:
>- $C\_c(v\_1) = 1/((1+2+2+3)/4) = 0.5$
>- $C\_c(v\_2) = 1/((1+1+1+2)/4) = 0.8$
>- e così via...
>
>Spiegazione:
>- Nell'analisi di $C\_c(v\_1)$ al denominatore si fa la somma della distanza minima tra il nodo in analisi e tutti gli altri (distanza $v\_1$-$v\_2$ = 1; distanza $v\_1$-$v\_3$ = 2; distanza $v\_1$-$v\_4$ = 2; distanza $v\_1$-$v\_5$ = 3) fratto il totale di nodi della rete meno 1, ovvero 5-1=4.


### Confronti interessanti tra i tre valori di centralità

|                      | Basso grado                                                                  | Bassa betweenness                                                                                            | Bassa vicinanza                                                                                                                                 |
| -------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Alto grado**       |                                                                              | Le connessioni sono ridondanti e la comunicazione bypassa il nodo                                            | Il nodo è in mezzo ad una comunità separata dal resto della rete                                                                                |
| **Alta betweenness** | Le poche connessione che svolge il nodo sono cruciali per il flow della rete |                                                                                                              | Molto raro. il nodo monopolizza i collegamenti di diversi gruppi che devono quindi passare attraverso di lui per comunicare con un altro gruppo |
| **Alta vicinanza**   | Nodo chiave connesso ad altri nodi importanti/attivi                         | Ci sono probabilmente molte vie nella rete: il nodo è vicino a molti altri, ma come lui anche gli altri nodi |                                                                                                                                                 |


___


## Analisi degli archi Indegree
Ci sono diversi tipi di indegree con diverso peso, in base a da dove viene quel indegree, che se viene da una persona importante avrà più importanza degli altri archi.

>[!question]
>Come misuro l'importanza dei nodi?

Sostanzialmente gli inarchi (indegree) che vengono da nodi più centrali aumentano maggiormente la centralità del nodo in cui vanno.


## Centralità ricorsiva

### PageRank

>[!definition]
>PageRank
>>con PageRank si intende il valore di importanza di ogni pagina

"Il pagerank di una pagina *u* è alto se è linkato da altre pagine con pagerank alto".
**Modi per incrementare il pagerank:**
+ avere molti collegamenti (inarchi)
+ collegamenti da pagine con pagerank alti a loro volta

**Formula PageRank $r(v):$**
$$r(v) = \sum\_{u\in I(v)}(\frac{r(u)}{|O(u)|})$$

Spiegazione: 
+ $I(v)$ è l'insieme delle pagine che hanno un link a $v$
+ $O(v)$ è l'insieme delle pagine che sono linkate da $v$
+ Ogni pagina $u$ ha il suo pagerank $r(u)$
+ La pagina $v$ riceve dalla pagina $u$ una porzione del pagerank di $u$ uguale alla porzione ricevuta da ogni altra pagina linkata da $u$
+ ogni pagina $u$ distribuisce il suo pagerank alle pagine linkate (quelle dentro l'insieme $O(u)$)
	+ più $r(u)$ è alto e più le pagine in $O(u)$ acquisiscono.
	+ più $O(u)$ è basso e più le pagine in $O(u)$ acquisiscono.

>[!example]
>Nell'immagine sotto vogliamo trovare il pagerank del nodo centrale.
>Per ogni nodo appartenente a $I(v)$ svolgo la divisione tra il loro pagerank e la cardinalità dei nodi che linka:
>- 12/4=3
>- 8/4=2
>- 10/2=5
>Il Pagerank di $v$ è quindi 3+2+5=10

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-10-15 115735.png|400]]


Generalmente la definizione più precisa include una fattorizzazione per una variabile c:
$$r(v) = c\*\sum\_{u\in I(v)}(\frac{r(u)}{|O(u)|})$$


>[!problem]
>- Se c'è una parte della rete disconnessa dall'altra certi pagerank possono essere assorbiti, ad esempio una con un pagerank maggiore succhia vie quello minore.
>- Anche nei loop tra più nodi passa il pagerank da uno all'altro senza sapere quando fermarsi e che rank ha veramente ciascuno (La frazione dentro la sommatoria).

### Formalizzazione

#### Vettori e matrici
I diversi pagerank dei nodi possono essere raccolti in un vettore $r$, computato iterativamente e tutto insieme. Inizialmente il vettore avrà determinati valori che andranno poi a cambiare iterativamente, cosa dovuta ad una funzione f, finché applicando f ad una versione di r (ri) ricaverò lo stesso vettore ri --> $f\_{r\_i} = f\_{r\_{i+1}}$ . (talvolta anche se i due vettori non sono proprio uguali se la differenza è minore di una certa soglia posso fermarmi)
Il passaggio da $r\_0$ ai suoi seguiti viene fatto costruendo una matrice P tale che $r\_{i+1} = r\_i\*P$, da ripetere quindi finché non è raggiunta la condizione terminale (raggiungere la **convergenza**): $r{i+1} = r\_i$ oppure $|r{i+1} - r\_i|< \epsilon$

La funzione f è una funzione lineare e moltiplica il vettore per una matrice (prodotto scalare).

### Camminate casuali (random walks)

Utente su una pagina con probabilità uguale per tutti i link seleziona casualmente un link presente e va su un'altra pagina e ripete e per ogni pagina rilascia anche una certa quota di pagerank. 
Ovvero partendo da un pagina random, ad ogni step lo user+browser che viaggia tra le pagine del Web distribuisce il corrispondente PageRank, poi seleziona un link random e continua.
>[!tip]
>Possiamo quindi rimpiazzare la frase "PageRank della pagina $v$" con "probabilità che la random walk dello user + browser sia sulla pagina $v$"

Per stabilire la probabilità che lo user sia in una data pagina si utilizza il limite tendente all'infinito: se esso esiste, c'è uno stato stabile. 
Si può calcolare una certa probabilità che l'utente si trovi su una determinata pagina piuttosto che in un'altra.
>[!example]
>Ad esempio in modo approssimativo è più probabile che un utente si trovi in una pagina con molti inarchi piuttosto che un nodo con pochi inarchi.


### Markov chain

>[!definition]
>Markov chain
>>Lo strumento formale per rappresentare random walks. 
>>Matrice che presenta le probabilità di esistenza di tutti gli archi dei nodi.
>>Ovvero ogni cella i,j rappresenta la probabilità di passar dallo stato i allo stato j, ovvero la probabilità di passare dal nodo i al nodo j attraverso l'in-arco che va da i a j.

>[!tip]
>Per ogni riga la somma della riga deve essere 1 (l'insieme delle probabilità degli archi di un nodo deve essere uguale a 1).


>[!example]
>Ad esempio nell'immagine sotto una volta che l'utente entra in nodo3 non esce più e al limite all'infinito prima o poi l'utente finisce in 3, quindi la probabilità per l'utente di essere in 3 è uguale a 1.

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-10-15 115649.png|300]]

Possiamo rappresentare la posizione corrente in uno stato $i$ (essere in un nodo $i$) attraverso un vettore $x$ dove ogni valore si riferisce ad un nodo ed ogni valore è uguale a 0 tranne un valore $i$ che sarà la posizione corrente e sarà uguale a 1.
La corrispondente riga $i$ della matrice di transizione P, indicherà tutte le probabilità di procedere verso tutti gli stati possibili partendo da $i$.

La camminata corrisponde a: $x\_{i+1}=x\_i\*P$ 

>[!example]
>Nell'esempio sotto il limite all'infinito sarà (1/4, 3/4) e lo sappiamo perché la moltiplicazione vettore con matrice fatto due volte porta allo stesso risultato, con:
>- $x\_0 = (1, 0)$, oppure $x\_0 = (0, 1)$, oppure $x\_0 = (1/2, 1/2)$
>Indipendentemente da quale $x\_0$ utilizzare inizialmente, la moltiplicazione tra $x\_0$ per la matrice di di transizione P fatta due volte porterà allo stesso risultato svolto due volte, ovvero $x\_1=x\_2=(1/4, 3/4)$, quindi la probabilità diventa stazionaria e stabile.

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-10-15 121206.png|450]]

Quindi noi stiamo cercando la distribuzione stabile, ovvero $x\_{i+1}= x\_i$, ovvero $x=x\*P$.

>[!tip]
>Le catene di markov che portano convergenza sono stabili.
>Le catene di Markov che portano convergenza sono dette **ergodiche**.

>[!warning]
>Una catena di Markov nel Web non può assolutamente essere ergodica perché il Web non è connesso e per questo problema hanno sviluppato la soluzione del *teletrasporto*.

In realtà può esserci una catena connessa ma non ergodica, ad esempio se gli archi in entrata e uscita tra due nodi hanno una probabilità uguale a 1:
in questo caso è possibile essere in ogni stato in ogni step, con probabilità maggiore di 0.

### Teletrasporto

>[!definition]
>Teletrasporto
>>Con teletrasporto si intende che cliccando su un link a caso vado su una pagina a caso per una probabilità molto bassa, rendendo ogni pagina del Web linkata ad un'altra pagina o anche a sé stessa, creando così una pseudo-connessione del Web.
>>- Tecnica che permette anche di sfuggire al cul-de-sac, vicolo cieco, ovvero se entro in un nodo senza out-degree.

___

### **Formula completa del PageRank**:
$$r\_{i+1}= r\_i\*P' = (1-d)\*r\_i\*P+d\*r\_i\*\begin{pmatrix} {1/N} & ... & 1/N\\ ... & ... & ...\\ 1/N & ... &1/N \end{pmatrix}$$
**Spiegazione**:
+ $d$: probabilità di teletrasporto
+ $N$: numero di nodi/pagine
+ $P$: matrice di adiacenza senza teletrasporto
+ $P'$: matrice di adiacenza con teletrasporto  


>[!problem]
>Problema con il web, che al momento ha 50 miliardi di pagine che fanno quindi una matrice  di 50miliardi x 50miliardi, da moltiplicare ogni volta per il vettore.

**Risoluzione**:
+ I valori che arrivano a convergenza prima degli altri posso eliminarli perché sono già arrivati a convergenza quindi man mano che vanno avanti i passaggi il vettore e la matrice diventano più piccole e più gestibili.


### Pseudocodice PageRank:

`pagerank(G, d = 0.15, epsilon = 0, num = +inf):
	`N = |G|
	`A = (1-d) * adjacency(G) + d * 1/N
	`r[0] = 1/N
	`for i in [1,num[ :
		`r[i] = r[i-1] * A
		`if abs(r[i] – r[i-1]) <= epsilon:
			`return r[i]
	`return r[i]`

### HITS
Algoritmo con lo scopo di separare tutte le pagine in due set:
+ **hub**: aeroporti da dove puoi andare in molti posti, con molti link verso altri posti
+ **authority**: pagine di entità ben riconosciute nel web (w3c, Knuth's home page, ...)

>[!tip]
>'Good hubs link good authorities'.
>'Good authorities are linked by good hubs'.

Il valore hubness del nodo x viene ottenuto dai valori di authority di ogni nodo linkato da x (in uscita).
Il valore authority del nodo x viene ottenuto prendendo i valori di hubbness di ogni nodo linkato a x (in entrata).

L'algoritmo lavora su un Base set formato da:
+ Un iniziale Root Set formato da un insieme di pagine ricavato dal motore di ricerca che analizza la query dell'utente e restituisce un ventaglio di pagine rilevanti per quella query
+ A questo Root Set vengono aggiunti gli insieme di indegree ($I(v)$) e outdegree ($O(v)$) e l'insieme delle pagine forma il Base Set
L'hubness ($h(v)$) e l'authority ($a(v)$) sono ricavati da questo Base Set.

##### Formula:
$\forall x \in BS$ compute $h(x)$ and $a(x)$:
$$h(x) = \sum\_{x->y}a(y)$$
$$a(x) = \sum\_{y->x}h(y)$$

##### Procedura:
+ Inizialmente i valori iniziali di ogni nodo sono impostati a: $h(x)=a(x)=1$ 
+ Ora iterativamente si modificano i valori con le due funzioni
+ Ci si ferma quando i valori delle due proprietà convergono (non variano più)

>[!tip]
>- Il processo iterativo non dipende dalla query, una volta che Il Base Set è definito, la query può essere dimenticata.
>- Come PageRank, HITS è un algoritmo generale e può essere usato su qualsiasi grafo.


Per definire $h$ e $a$ vengono rappresentate due vettori colonna:

>[!example]
>Per stabilire il componente i-esimo di $h(u)$ si sommano tutti i componenti di $a$ moltiplicando per 1 quelle che sono out-pagine di $u\_i$ e moltiplicando per 0 quelle che non sono out-pagine di $u\_i$.
>Sostanzialmente quindi bisogna moltiplicare un vettore riga con valore 1 corrispondente alle out-pagine di $u\_i$ per il vettore colonna $a$, ovvero moltiplicare la riga i-esima della matrice di adiacenza $A$ per $a$.

>[!warning]
>Moltiplicando quindi tutte le righe di $A$ per $a$ si ricaverà tutto il vettore $h$:
>- $h = A\*a$
>
>E di conseguenza:
>- $a=A^T\*h$
>
>Dalle stesse formule ricaviamo che:
>- $h$ è l'autovettore di $A\*A^T$
>- $a$ è l'autovettore di $A^T\*A$


>[!definition]
>$AA^T$
>>Nella matrice $AA^T$ il valore $AA^T[i, j]$ è incrementato quando:
>>$\exists k$ t. c. $A[i, k] = A^T[k,j] = 1$. 
>>Ovvero per ogni nodo che è co-linkato sia da $i$ che da $j$.
>

>[!definition]
>$A^TA$
>>Nella matrice $A^TA$ il valore $A^TA[i, j]$ è incrementato quando:
>>$\exists k$ t. c. $A^T[i, k] = A[k,j] = 1$. 
>>Ovvero per ogni nodo che co-linka sia $i$ che $j$.


___

## Confronto

#### PageRank:
+ ##### Pro:
	+ Non spammabile
	+ Indice di qualità per tutto il Web
	+ Usato in Google
+ ##### Contro:
	+ Non specifico per una query
	+ Pensato per grafi larghi
	+ Computazione complessa

#### HITS:
+ ##### Pro:
	+ Specifico per una query
	+ Funziona anche per grafi piccoli
	+ Fornisce due valori
+ ##### Contro:
	+ Facilmente spammabile (sugli hubs)
	+ Computazione complessa


___


### **Misure sulle reti:**
+ Centralità semplice (Degree, Betweenness, Closeness)
+ Centralità ricorsiva (PageRank, HITS)