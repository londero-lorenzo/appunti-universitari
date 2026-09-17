---
title: "Riassuntone Andrea"
aliases: ["Riassuntone Andrea"]
tags: [università, "materie", "anno-2025-2026", "social-computing", "riassuntone-andrea"]
created: 2026-09-17
---
# Definizione di Social Media

>[!definition]
> Social Network
>> Un **web-based services** ovvero un gruppo di applicazioni su internet che utilizzano web 2.0 (ovvero contenuti creati dagli utenti) che consentono agli utenti stessi di:
>> 1. creare un **profilo** pubblico o semi-pubblico 
>> 2. articolare una lista di altri utenti con cui condividono una connessione,
>> 3. visualizzare e attraversare la propria lista di connessioni e quelle stabilite da altri all’interno del sistema.

>[!definition]
>Social Netwok (ancora)
>>tecnologie che facilitano la condivisione di espressioni personali (testo o contenuto multimediale) tramite comunità virtuali

La classificazione dei social media è definita dal livello di **social presence** e il livello di **self-presentation**
# Modello alveare

+ 7 dimensioni
+ **Identità:** quanto uno rivela di se stesso
+ **Presenza:** quanto gli utenti sanno se gli altri sono disponibili
+ **Relazioni:** quanto gli utenti interagiscono tra di loro
+ **Reputazione:** quanto si mette in evidenza di se, status sociale
+ **Gruppi:** quanto gli utenti possono formare comunità
+ **Conversazione:** quanto gli utenti comunicano con gli altri
+ **Condivisione:** quanto gli utenti si scambiano contenuti

---
title: 3-Grafi-e-reti

# Grafi

>[!definition]
>Grafi 
>>I grafi sono composti da nodi e archi.


>[!example]
>I grafi nel web sono composti da nodi che rappresentano le pagine web e archi che rappresentano link ipertestuali fra pagine

**Grandezza del grafo**: |V| = n
**Numero di archi**: |E| = m

Grafi si dividono in:
+ diretti (con archi con le frecce verso una direzione)
+ indiretti (con archi senza frecce)

>[!definition]
>Sottografo
>>un grafo G' è un sottografo di G se:
>>>- $V' \subseteq V$
>>>- $E' \subseteq (V' x V') \cap E$




>[!definition]
>Vicinato
>>Per ogni nodo v in un grafo indiretto l'insieme di nodi collegati con un arco al nodo v

>[!definition]
>Cammino
>> sequenza di archi tali che ogni arco è incidente allo stesso nodo del successivo (che merda di definizione, ricordarsi quella di algoritmi)
>> > 	Diretto: seguendo la direzione degli archi
>> > 	Indiretto: trascurando la direzione degli archi

>[!definition]
>Connettività
>>Un nodo è connesso ad un altro se esiste un cammino tra i due nodi

Un grafo è connesso se esiste un cammino fra ogni coppia di nodi.

>[!definition]
>Componente
>>una componente in un grafo indiretto è un sottografo massimale connesso
>>>Grafi diretti: 
>>>- componente fortemente connessa quando per ogni coppia di nodi u e v c'è un cammino diretto da u a v e uno da v a u
>>>- componente debolmente connessa quando per ogni coppia di nodi u e v c'è un cammino **indiretto** da u a v

Se un grafo è connesso può avere solo una componente.

>[!definition]
>Grado (degree)
>>Il grado di un nodo ($d\_i$) è il numero di archi collegati a quel nodo.

+ In-degree: numero di archi che puntano al nodo
+ Out-degree: numero di archi in uscita dal nodo

>[!definition]
>Degree distribution
>>Per ogni grado, quanti nodi hanno quel grado

## Teoremi

**Teorema 1**: La sommatoria dei gradi in un grafo indiretto è due volte il numero degli archi
$$\sum d\_i = 2|E|$$
 
 **Corollario**:
 + 1. Il numero di nodi con grado dispari è pari
 + 2. In ogni grafo diretto, la sommatoria degli in-degree è uguale alla somma degli out-degree:
$$\sum d^{out}\_{i} = \sum d^{in}\_j$$


## Grafo della degree distribution

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-10-07 112139.png|400]]
+ L'asse delle x rappresenta il grado
+ L'asse delle y rappresenta la frazione e il numero dei nodi che hanno quel grado
+ spesso rappresentato in scala log-log
+ riguardo ai social media (come nel grafico di esempio) di solito è decrescente il che vuol dire che tanti utenti hanno poche amicizie e meno utenti hanno un numero di amici molto alto (i due punti cerchiati in rosso)

___

### Densità di un grafo:

>[!definition]
>Densità
>>Quanti archi ci sono rispetto a tutti gli archi possibili

Grafi indiretti:
 $$D=\frac{2|E|}{|V|(|V|-1)}$$
Grafi diretti:
$$D=\frac{|E|}{|V|(|V|-1)}$$

___
### Rappresentazioni dei grafi:
+ **liste degli archi:**
	+ ogni elemento della lista è una coppia di nodi (che rappresenta un arco); si usa anche per i grafi diretti
+ **liste di adiacenza:**
	+ Per ogni nodo una lista di nodi a cui è connesso; si usa anche per i grafi diretti
+ **matrice di adiacenza (Sociomatrix)**:
	+ matrice che presenta 1 se la coppia di nodi presenta un arco, 0 altrimenti
	+ simmetrica per grafi indiretti, si usa anche per grafi diretti
	+ usata anche per grafi pesati (G(V, E, W))

___
### Algoritmi su grafi:
Gli stessi che abbiamo visto con algoritmi:
+ DFS/BFS (Graph trasversal algorithms)
+ Dijkstra/Floyd-Warshall (shortest path algorithms)
+ Prim/Kruskal (Minimum spanning tree)
e altri...

___

# Rete

>[!definition]
>Rete
>>Un **grande** grafo nel **mondo reale** (gli elementi della rete hanno quindi 'significato').
>>Solitamente tanto grande da non poterlo disegnare in modo informativo.

>[!example]
>**Rete di informazione**:
>- su X posso creare una rete di individui. Se io voglio diffondere un'informazione quali nodi della rete devo colpire? Probabilmente quelli che sono più vicini ad un'altra rete 
>- rete degli indirizzi IP attivi di Internet
>
>**Rete del mondo reale**:
>- rete della catena alimentare animale
>- rete delle autostrade negli Stati Uniti

## Reti sociali

>[!definition]
>Rete sociale
>> Gli elementi i cui elementi formano una struttura sociale

+ I nodi sono definiti **attori**: individui o organizzazioni
+ Gli archi sono definiti **legami**: connessioni fra individui
(a noi interesseranno le reti sociali online, ma esistono anche quelle offline)

Rete può essere:
+ **Diretta** 
>[!example]
>- A segue B
>- A commenta il post di B
>- A reposta il post di B

+ **Indiretta** 
>[!example]
>- A e B sono nello stesso gruppo
>- A e B commentano un post di C

---
title: 4-Misure-sulle-reti-I
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
>$C\_b(v\_2)= 2 \times ((1/1) + (1/1) + (2/2) + (1/2) + 0 + 0) = 2\times 3.5 = 7$
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

|                    | Basso grado                                                                 | Bassa betweenness                                                                                           | Bassa vicinanza                       |
| ------------------ | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------  | ------------------------------------- |
| **Alto grado**     |                                                                             | Le connessioni sono ridondanti e la comunicazione bypassa il nodo                 | Il nodo è in mezzo ad una comunità separata dal resto della rete|
|**Alta betweenness**| Le poche connessione che svolge il nodo sono cruciali per il flow della rete|   | Molto raro. il nodo monopolizza i collegamenti di diversi gruppi che devono quindi passare attraverso di lui per comunicare con un altro gruppo|
|**Alta vicinanza**  | Nodo chiave connesso ad altri nodi importanti/attivi                        | Ci sono probabilmente molte vie nella rete: il nodo è vicino a molti altri, ma come lui anche gli altri nodi|                                       |


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
$$r(v) = c\times\sum\_{u\in I(v)}(\frac{r(u)}{|O(u)|})$$


>[!problem]
>- Se c'è una parte della rete disconnessa dall'altra certi pagerank possono essere assorbiti, ad esempio una con un pagerank maggiore succhia vie quello minore.
>- Anche nei loop tra più nodi passa il pagerank da uno all'altro senza sapere quando fermarsi e che rank ha veramente ciascuno (La frazione dentro la sommatoria).

### Formalizzazione

#### Vettori e matrici
I diversi pagerank dei nodi possono essere raccolti in un vettore $r$, computato iterativamente e tutto insieme. Inizialmente il vettore avrà determinati valori che andranno poi a cambiare iterativamente, cosa dovuta ad una funzione f, finché applicando f ad una versione di r (ri) ricaverò lo stesso vettore ri --> $f\_{r\_i} = f\_{r\_{i+1}}$ . (talvolta anche se i due vettori non sono proprio uguali se la differenza è minore di una certa soglia posso fermarmi)
Il passaggio da $r\_0$ ai suoi seguiti viene fatto costruendo una matrice P tale che $r\_{i+1} = r\_i\times P$, da ripetere quindi finché non è raggiunta la condizione terminale (raggiungere la **convergenza**): $r{i+1} = r\_i$ oppure $|r{i+1} - r\_i|< \epsilon$

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

La camminata corrisponde a: $x\_{i+1}=x\_i\times P$ 

>[!example]
>Nell'esempio sotto il limite all'infinito sarà (1/4, 3/4) e lo sappiamo perché la moltiplicazione vettore con matrice fatto due volte porta allo stesso risultato, con:
>- $x\_0 = (1, 0)$, oppure $x\_0 = (0, 1)$, oppure $x\_0 = (1/2, 1/2)$
>Indipendentemente da quale $x\_0$ utilizzare inizialmente, la moltiplicazione tra $x\_0$ per la matrice di di transizione P fatta due volte porterà allo stesso risultato svolto due volte, ovvero $x\_1=x\_2=(1/4, 3/4)$, quindi la probabilità diventa stazionaria e stabile.

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-10-15 121206.png|450]]

Quindi noi stiamo cercando la distribuzione stabile, ovvero $x\_{i+1}= x\_i$, ovvero $x=x\times P$.

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
$$r\_{i+1}= r\_i\times P' = (1-d)\times r\_i\times P+d\times r\_i\times \begin{pmatrix} {1/N} & ... & 1/N\\ ... & ... & ...\\ 1/N & ... &1/N \end{pmatrix}$$
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
>- $h = A\times a$
>
>E di conseguenza:
>- $a=A^T\times h$
>
>Dalle stesse formule ricaviamo che:
>- $h$ è l'autovettore di $A\times A^T$
>- $a$ è l'autovettore di $A^T\times A$


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

---
title: 6-Misure-sulle-reti-II
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

+ **Geodesic**: Percorso più corto tra due nodi (la distanza è il numero di archi) (geodesic = cammino più breve)
+ **Diameter** della rete: Il più lungo geodesic della rete (distanza minima maggiore tra due nodi della rete)
+ **Grado** di un nodo: Numero di archi indegree e outdegree
+ **Degree distribution**: Per ogni grado, il numero di nodi che hanno quel grado
+ **Density**: Proporzione di archi: Numero di archi / numero massimo di archi
	+ Max: ((numero di nodi nella rete)$\times $(numero di nodi nella rete -1))/2
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
>Si è potuto evincere come un nodo presentasse i valori più alti qualunque fosse l'algoritmo utilizzato e il tipo di centralità (grado, vicinanza, betweenness) utilizzato, risultati resi ancora più evidenti una volta normalizzati i valori ricavati, come si può notare dall'immagine sotto con il nodo 'Mike' che è il più centrale.

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-10-17 214008.png|550]]

___

## Transitività e Reciprocità

Indicano delle situazioni tipiche che si formano nelle reti di 'amicizia':
+ **Reciprocità**: (Se io sono tuo amico, tu sei amico mio)
+ **Transitività**: (Se io sono amico tuo e tu sei amico suo, allora io sono amico suo)

### Transitività

Algebricamente: $aRb \land bRc \rightarrow aRc$ 

All'aumento della transitività ci sono grafi più densi e si è più vicini ad un grafo completo.

>[!question] Possiamo stimare quanto un grafo sia vicino ad essere completo misurandone la transitività?
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
		2. **Formula:** C = Numero di triangoli $\times $ 6 / Cammini di lunghezza 2
		   **Spiegazione**: Conto i triangoli e moltiplico per 6 (siccome ogni triangolo ha 6 cammini chiusi di lunghezza 2 (quindi con il terzo arco che chiude come prima))
		3. **Formula**: Numero di triangoli $\times $ 3 / Numero di triple di nodi connessi
		   **Spiegazione**: ogni triangolo ha tre triple differenti. Di tutte le triple di nodi connesse, prendo quelle chiuse, ossia il numero di triangoli $\times $ 3.


### Reciprocità

Avviene quando se tu sei amico mio io divento amico tuo.
"Versione semplificata della transitività" in quanto considera cicli di lunghezza 2 (tra due nodi) al posto dei triangoli.

##### Reciprocità globale: 
Conto il numero di coppie reciproche nel grafo
**Formula**:
$$R = \frac{\sum\_{i, j, i<j}A\_{i,j}A\_{j,i}}{|E|/2} = \frac{2}{|E|} \times  \frac12 \times  Tr(A^2)$$
**Spiegazione**:
+ $A$ è la matrice di adiacenza
+ La sommatoria somma 1 ogni volta che c'è una coppia reciproca, quindi ogni volta che $A\_{i, j}$ = $A\_{j, i}$ = 1.
+ Al denominatore divido per il numero massimo possibile di coppie reciproche dati gli archi in E, ovvero la metà.
+ $A^2$ è per l'appunto la moltiplicazione della matrice di adiacenza $A$ per se stessa. Infatti sarà uguale a 1 se esiste sia l'arco da i a j che l'arco da j a i, e sarà  uguale a 0 altrimenti
+ Il $\frac12$ prima di Tr() è perché ogni coppia reciproca viene contata due volte e prendendo la metà viene invece contata una sola volta.
+ Tr($A^2$) è la somma dei valori sulla diagonale da sinistra a destra della matrice.

>[!example]
>Nell'immagine sotto sono presenti tre nodi e la matrice di adiacenza della rete è la seguente: 
>$$A=\begin{bmatrix} 0 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$$
>- Svolgimento: 
>
> $$R = \frac1mTr(A^2) = \frac14 Tr(\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 0 \end{bmatrix}) = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}$$
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

Soprattutto nelle degree distribution sui dati normali le distribuzioni non sono praticamente mai uniformi, ma sono più grafici che presentano un picco, oppure una power law.

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
>Sostanzialmente in molte distribuzioni reali come quelle riferite ai social media sono presenti distribuzioni riconducibili ad una power law, che quindi presenta valori piccoli molto comuni e valori grandi estremamente rari ma mai impossibili.

>[!warning]
>Probabilità di valori alti è molto bassa ma mai 0, diversamente quindi dalle teoriche distribuzioni esponenziali come la Gaussiana

##### Concetto di Long Tail
Essendo la coda sull'asse x di una power law molto lunga, nonostante la poca popolarità, messi tutti insieme rappresentano un volume importante.

>[!example]
>Ad esempio Mettendo insieme il volume delle vendite di libri considerati impopolari, formano il 57% delle vendite di Amazon.


___

### Distanza media, piccolo mondo

Se io voglio trasmettere un rumor o una notizia a più gente possibile dovrò comunicare con determinati nodi, con più probabilità di trasmetterla a loro volta ad un maggior numero di utenti, con l'ipotesi che tutti gli utenti la passino immediatamente a tutti i loro amici.

>[!question]
>- Quanto passa prima che la notizia raggiunga quasi tutti i nodi della rete?
>- Tempo massimo (distanza massima)? (corrisponde al diametro)
>- Tempo medio (distanza media)?

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

---
title: 8-Modelli-Delle-Reti
---
# Modelli delle reti

>[!question] Ci sono pattern sottostanti riguardo ai legami di amicizia?
>Sì, ci sono dei modelli di rete sociale.

>[!question] Che processi stocastici (casuali) di creazione degli archi posso immaginarmi?
>Varie possibilità che vedremo in questo capitolo

Utilità dei modelli che generano grafi: 
+ Possiamo ipotizzare che gli stessi processi generativi siano alla base delle reti reali
+ Possiamo studiarle in modo più efficiente ed efficace
+ Possiamo classificare anche le reti in varie tipologie che consentono di giustificare e spiegare fenomeni.

4 modelli classici:
+ **Regolari**
+ **Reti casuali**
+ **Piccolo mondo (WSSW)**
+ **Scale-free**

## Regolare

Reti con una tipologia regolare, non casuali (stocastiche).

>[!example]
>Forme geometriche come il nodo centrale al centro geografico della rete con tutti gli altri nodi attorno oppure in maniera circolare, o a griglia, o a rete triangolare.


>[!tip]
>Nella rete circolare la distanza media è la metà dei nodi che compongono la rete, ad esempio se la rete è di 10 nodi, la distanza media tra due nodi sarà 5, cosa che sicuramente non rappresenta un **piccolo mondo** con questi modelli regolari

Quindi questi modelli hanno:
+ **Distanze** medie spesso grandi.
+ **Coefficiente di clustering** è spesso alto (come si vede sul reticolo triangolare)
+ **Distribuzione dei gradi** è tipicamente con un picco, e capita spesso che tutti i nodi abbiano lo stesso grado.
+ **Connettività** spesso completa e totale.

>[!warning]
>Raramente le reti nel mondo reale seguono questo modello.


___
## Reti casuali

Idea:
+ Ogni arco possibile in una rete ha una probabilità $p$ di esserci, quindi 'tirando una moneta' decido se ci sarà quell'arco nella mia rete, e così avanti per tutti gli archi, ogni presenza di un arco indipendente dagli altri.
+ Nei social media corrisponderebbe a dire che le amicizie si formano totalmente a caso, cosa che non è proprio veritiera (ma vedremo che è comunque un modello utile).

Studi:
+ Connettività
+ Diametro
+ Formazione Giant Component (poi vediamo)
+ Limite termodinamico sui grafi grandi, ovvero cosa succede quando il numero di archi è tendente all'infinito.


2 diversi modelli di grafi casuali:
+ G(n, m)
+ G(n, p)

### G(n, m)

>[!definition]
>G(n, m)
>>Grafo con n nodi e con una disponibilità di m archi piazzati a caso, solitamente senza multi-archi (due archi tra gli stessi nodi) e auto-archi (verso sé stesso).
>>Solitamente su grafi indiretti.
>>
>>Altra definizione equivalente: Scelgo un grafo a caso fra tutti quelli aventi n nodi e m archi.

Puntualizzazioni: 
+ Si studiano i grafi grandi per studiare il $lim\_{n \rightarrow \infty}$ e prendo il caso medio quindi analizzando virtualmente infiniti grafi casuali.
+ Diametro di G(n, m) è la media tra tutti i grafi G(n, m)
+ Grado medio sarà definito come: $2m/n$, in quanto ci sono 2 estremità per ogni arco diviso per la totalità dei nodi.
+ Non ci sono casi speciali (poco interessanti)
+ Di solito le distribuzioni sono con un picco e non a coda lunga come quelle reali. Il caso tipico è rappresentativo per tutte)

### G(n, p)

>[!definition]
>G(n, p)
>>Genero o non genero un arco in base alla probabilità di esistenza di ogni singolo arco, sempre con gli archi indipendenti gli uni dagli altri. Invece di fissare il numero di archi, fisso la probabilità di esistenza degli archi.

+ In G(n, p) il **numero di archi** che in G(n, m) era ESATTAMENTE m è IN MEDIA: $p\times n(n-1)/2$

+ **Grado medio** lo ricavo considerando tutte le estremità degli archi e dividendo per il numero di nodi: $\frac{2\times [m]}{n}=(n-1)p$

>[!example] Differenza G(n, m) / G(n, p)
>Ad esempio un grafo G(n, m) = G(4, 2) non sarà mai connesso, mentre un grafo G(n, p) = G(4, 1/3) PUO' essere connesso.

**Numero di archi medio**: 
$$[m]=\frac{n(n-1)}{2}p=\binom{n}{2}p$$
**Distribuzione dei gradi** (stesso per G(n, p) e G(n, m)): 
+ Tutti i nodi sono uguali in questo grafo, senza privilegi, quindi sarà raro che un nodo possa ricevere maggiori archi o minori archi degli altri, rendendo la distribuzione simile alla **distribuzione di Poisson**, con la probabilità di avere un grado diverso da quello medio che si abbassa subitamente allontanandosi dal valore medio.
  Non si trovano cosiddetti hub, ovvero nodi con un alto numero di archi collegati. (intuitivamente aggiungendo archi a caso capita raramente di ri-aggiungere allo stesso nodo, soprattutto $n \rightarrow \infty$)
  Le distribuzioni reali però abbiamo visto avere una distribuzione a coda lunga, lontana da quella a campana dei grafi casuali.
+ Grado medio:
  $$[k]=\frac{2[m]}{n}=(n-1)p$$

**Coefficiente di clustering** (probabilità che i vicini di un nodo siano vicini tra loro):
+ Sarà molto basso, e sarà tendente a 0 più $n$ tende a infinito: $C=\frac{c}{n-1}$  con $c$ che rappresenta il grado medio

>[!tip] Pensiero fino ad ora
>Una prima conclusione è che queste reti non vadano bene per modellare reti reali ma hold on diamo fiducia ancora un po'.

>[!question] Grafo G(n, p) è connesso?
>In generale no. In genere ci sono diverse componenti connesse isolate.
>

Però questa non è la domanda giusta, in quanto:
>[!example]
>Se ad esempio ho 50 miliardi di nodi e sono tutti connessi tranne 1 la rete praticamente è connessa, quindi la domanda sulla connettività non è giusta.

La domanda giusta è:
>[!question] Grafo G(n, p) è connesso all'incirca/ più o meno/ in pratica?

Che equivale a:
>[!question] Esiste una componente gigante?
>Ovvero se esiste una componente che comprende quasi tutti i nodi, o almeno la maggior parte rispetto alle altre componenti.

Pensando a due casi estremi:
+ p=0, nessun arco viene generato e il grafo è disconnesso e la componente più grande sarà grande 1.
+ p=1, tutti gli archi vengono generati e il grafo è completo e connesso e la componente più grande sarà grande n.
Differenze tra i due casi:
+ Qualitativamente la dimensione della componente più grande nel primo è costante all'aumentare di n (rimane 1 anche se aumenta n), nel secondo no, aumenta con n (il numero aumenta più aumenta n)

>[!definition]
>Componente gigante (GC)
>>Definizione più precisa di componente gigante:
>>Una GC è una componente connessa, la più grande della rete.
>>GC ha una grandezza che cresce in proporzione a $n$ (si fa infatti il $lim$ $n \rightarrow \infty$)

Una rete ha una CG se ha una frazione finita di $n$ connessa (90%, 50%, ma anche ad esempio 10%, se tutte le altre componenti connettono un numero minore del 10% dei nodi. La GC deve rappresentare in pratica la frazione più grande).

>[!warning]
>Il grado medio dei nodi per avere una componente gigante è $c=1$.
>

$c=1$ è effettivamente un valore controintuitivo incredibilmente basso, ma in effetti se ogni nodo connesso presenta due archi che connettono altri due nodi, ci saranno anche nodi che non possiedono alcun arco, e quindi di media il grado sarà 1.
Equivalente ad un valore $c=1$ è la probabilità $p$ che $c$ sia 1: $p=c/(n-1)=1/(n-1)$           $\leftarrow$ (ricordare per sicurezza)

Quindi se $c \geq 1 \rightarrow$ componente gigante: grafo 'quasi connesso' 

**Transizione di fase:**
+ In reti reali c'è una transizione di fase (cambiamento brusco) in cui appare la GC. se $c < 1$ no GC, se $c\geq1$ la connettività aumenta velocemente

>[!tip] Attenzione
>E' $n$, che varia, per $c$ fissato:
>- Fisso $c\geq1$, faccio lim $n\rightarrow \infty$ e scopro che c'è GC.
>- Fisso $c<1$, faccio lim $n\rightarrow \infty$ e scopro che non c'è GC.

Riassuntino efficace dei GC nei grafi casuali:
+ Per $c<1$: Ci saranno cluster piccoli e isolati
+ Per $c=1$: Appare la Giant Component
+ Per $c>1$: Quasi tutti i nodi sono connessi
![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-10-24 225246.png|300]]

___
#### Diametro
Quando circa tutti i nodi sono raggiunti, il diametro sarà $l=\frac{ln(n)}{ln(c)}$ , quindi cresce con $n$ e cala al crescere di $c$. Nella rete reale se ad esempio tutti conoscono 100 persone il diametro è di 4,9; numero molto vicino a quello di milgram. 
Alla comparsa della componente gigante (c=1) si ha il picco del diametro, che forma una cuspide per poi riscendere con l'aumentare di c.

---

>[!question]
>E' possibile usare i grafi casuali per modellare le reti reali?

Non per il coefficiente di **clustering** (sottostimato) e la **degree distribution** (a campana e non a power law come nelle reali), in quanto non rappresentativo. 
Per rappresentare invece la **lunghezza media** dei cammini vanno bene.

___

## Small world (WSSW)

Una delle proprietà che mancano alle reti casuali è avere un coefficiente di clustering $c$ alto, diversamente dalle reti regolari.

L'idea è quindi di partire da delle reti regolari e da esse staccare un arco da un nodo e riattaccarlo in qualche altro nodo, con una probabilità $p$. Se $p=1$ la rete diventa casuale, quindi è interessante vedere come si comportano le reti con $0<p<1$.

>[!question]
>Cosa succede nella rete per valori di $p$ compresi tra 0 e 1?

##### Proprietà delle reti:
+ n = numero di nodi
+ c = numero medio di archi per vertice
	+ $nc/2$ è il numero di archi totale
+ Relazione tra n e c: $n >> c >> log(n) >> 1$.

##### Osservazione della variazione di due misure:
+ L = lunghezza media del cammino minimo fra 2 nodi della rete
  (Misura per quanti amici devo passare per raggiungere una persona)
>[!question] Come varia L al variare di p?
>- Per p=0, L è ragionevolmente grande
>- Per p=1, L è ragionevolmente piccolo

+ C = coefficiente di clustering
  (Misura quanto gli amici di una persona sono amici fra loro)
>[!question] Cosa succede al coefficiente di clustering al variare di $p$?
>- Per p=0, C alto
>- Per p=1, C basso

>[!tip]
>Sia L che C per $p$ basso sono alti e per $p$ alto sono bassi, tuttavia i valori intermedi formano due 'parabole' opposte.

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-11-02 193210.png|400]]

>[!example]
>+ Se $p=0,001$ (redirigo un arco su mille) le distanze rappresentate da L dimezzano, infatti L=0,5 circa, quindi L decresce molto velocemente. Questo perché se attacco un arco ad un gruppo lontano di nodi automaticamente avvicino i due gruppi di nodi diminuendo molto le loro distanze.
>+ C invece fino a $p=0,1$ non decresce di un valore oltre al 35% del suo  valore massimo. Questo perché se rompo dei triangoli solo quel triangolo viene separato e quindi il coefficiente rimane quasi intoccato per parecchi valori di $p$.

>[!tip]
>Reti regolari e casuali non vanno bene a rappresentare le reti reali:
>Prendendo in esame tutte le persone ($O(10^9)$) e i vicini per ogni nodo (c=$O(10^3)$):
>+ Regolare: $L(0) = O(10^6)$ (irrealistico); ma con C ci saremmo.
>+ Casuale: $L(1) = 9/3 = 3$ (andrebbe bene); ma C sarebbe quasi 0 che non va bene.

##### Distribuzione dei gradi
Nelle reti WSSW la distribuzione dei gradi è circa a campana ed è priva della coda lunga e di hub, no power-law. 
Formula della probabilità del grado di un nodo:
$$p\_k=e^{cp}\frac{(cp)^{k-c}}{(k-c)!}$$

>[!warning]
>Le reti WSSW sono quindi un interessante mix delle reti regolari e delle reti casuali:
>+ Spiegano il coefficiente di clustering alto
>+ Non spiegano la distribuzione dei gradi che si trova nelle reti naturali (no power-law, no coda lunga, no hub)

##### Riassunto delle prime tre reti
![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-11-03 111637.png]]

**Degree distribution**:
+ Reti regolari: di solito tutti i nodi hanno grado simile
+ Reti casuali: distribuzione di Poisson
+ Reti WSSW: distribuzione di Poisson circa
>[!warning]
>Nessuno di questi modelli crea reti uguali a quelle del mondo reale.

___

## Scale-free

Idea: 
+ 'rich-get-richer': i ricchi diventano più ricchi e i poveri restano poveri.
+ 'vantaggio cumulativo': a partire da un articolo con il passare del tempo ci saranno sempre più articoli che citano l'articolo iniziale, e un articolo più citato sarà sempre più citato rispetto ad un articolo citato pochissimo.

>[!question]
>+ Ci sono altre reti in natura oltre al web che hanno una distribuzione a power-law?
>+ Quale processo stocastico riesce a generare una rete con distribuzione power-law e piccolo mondo (distanze brevi)? in quanto tutte le reti che abbiamo visto finora non andavano bene

Due stronzi propongono un nuovo modello stocastico, detto '**Preferential attachment**':
+ Crescita della rete: la rete parte con pochi nodi e ad ogni istante temporale aggiungono un nodo
+ Probabilità non uniforme: la probabilità di connettersi a un nodo esistente è proporzionale al grado del nodo esistente.

___
#### Attaccamento preferenziale

+ Per il nuovo nodo $v$ collego $v$ ad un nodo casuale $v\_i$ con probabilità $P(v\_i)=\frac{d\_i}{\sum\_j{d\_j}}$ 

>[!tip]
>Con generazione di grafi ad attaccamento preferenziale possiamo simulare reti del mondo reale.

>[!example]
>![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-04 190719.png|400]]

**Simulazioni**:
![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-04 191326.png]]
+ Nel primo grafico si può vedere come la distribuzione dei gradi non dipende dalla grandezza della rete, avendo una power law.
  Invarianza rispetto alla scala, stazionario rispetto al tempo / dimensione.
+ Il secondo grafico invece fa vedere come la distribuzione cambia all'aumentare della scala.
  Varia a seconda del numero di archi a ogni passaggio; non c'è power law e neanche stazionarietà.
+ Nel terzo grafico si vede la distribuzione di due nodi che sembrano costanti ma in realtà all'aumentate del tempo aumenta molto di più il primo nodo (verso sinistra) rispetto al secondo (verso destra) (ricchi diventano sempre più ricchi).


**Reti scale-free**: reti che hanno una distribuzione dei gradi di tipo power-law: $f(k)=\frac{C}{k^\alpha}$
+ Molti nodi (la gran maggioranza) hanno grado k basso.
+ Ci sono nodi, pochi ma in percentuale non trascurabile, che hanno grado molto alto: gli **Hub**.
+ Grazie agli hub si ha un effetto small world (cammini brevi)
+ Alcune reti del mondo reale sono proprio così (aeroporti, Web,...)

>[!definition]
>Hub
>>Nodi con grado eccezionalmente alto, tramite loro i cammini diventano più brevi

___
Riassunto dei 4 modelli:
![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-03 151924.png]]

Scale-free ha finalmente la degree distribution corretta ma non il coefficiente di clustering.

Ricerca di una soluzione a questo, Rispetto alla formula originale della probabilità di collegare un nuovo nodo $v$ ad un vecchio nodo casuale $v\_i$ $P(v\_i)=\frac{d\_i}{\sum\_jd\_j}$:
+ **Attaccamento preferenziale non lineare**: $P(v\_i)=\frac{d\_i^\alpha}{\sum\_j{d\_j^\alpha}}$ 
	+ $\alpha$ = 1  $\rightarrow$ attaccamento preferenziale originale
	+ $\alpha<1   \rightarrow$no longtail, no hubs
	+ $\alpha>1   \rightarrow$ winner takes all, un singolo nodo connesso a tutti
+ **Attrattività: $P(v\_i)=\frac{A+d\_i}{\sum\_j{(A+d\_j)}}$ **
	+ A=0 $\rightarrow$ attaccamento preferenziale originale
	+ Definire la probabilità $P(v\_i)=\frac{A+d\_i}{\sum\_j{A+d\_j}}$ 
	+ Si ottiene sempre una power law con una pendenza che varia con A
+ **Fitness: $P(v\_i)=\frac{𝜂\_i\times d\_i}{\sum\_j{(𝜂\_i\times d\_j)}}$**
	+ $𝜂\_i$ rappresenta la fitness del nodo $i$
	+ Si ottiene sempre una power law
+ **Modello 'Random Walk**':
	+ Ad ogni passo si aggiunge un nuovo nodo $i$, con m>1 archi attaccati, di cui un arco è collegato ad un vecchio nodo $j$ scelto a caso, con probabilità uniforme.
	+ Ogni altro arco degli m-1 restanti viene collegato con probabilità $p$ a un vicino di $j$ scelto a caso, e con una probabilità 1-$p$ a un nodo vecchio qualsiasi scelto a caso. ($p$ probabilità che si formi un triangolo).
	+ Con nodi con tanti archi è più probabile privilegiare (attaccarsi) a nodi con un grado a loro volta maggiore (i ricchi diventano più ricchi).

Questo ultimo modello random walk finalmente funziona: prendendo a martellate il modello scale free trasformandolo in random walks si ha quindi una degree distribution con power law, cammini brevi e C alto (alta presenza di triangoli).

---
title: 10-Comunita
---
# Comunità

Le comunità possono essere:
+ Esplicite (gruppi Facebook, associazioni LinkedIn)
+ Implicite (Legami interni forti all'interno della comunità e legami esterni deboli fra comunità diverse)

>[!definition]
>Comunità
>>Gruppo di nodi connessi fra di loro e non connessi con gli altri.

>[!definition]
>Omofilia
>>Tendenza delle persone ad associarsi e formare legami con persone simili a loro

>[!example]
>+ Un conflitto in un club di karate ha separato in due gruppi e le persone del club che avevano più legami di amicizia con uno con l'altro hanno scelto il relativo schieramento.
>+ In una scuola di solito i bianchi sono amici di bianchi e i neri sono amici dei neri
>+ I repubblicani hanno amici dello stesso pensiero politico e così anche i democratici

Proviamo a dare una vera definizione utile a noi di comunità:
>[!definition]
>1-Definizione ideale di comunità
>>Dato un grafo G una comunità C è un sottografo di G tale che:
>+ C è connesso (o addirittura completo)
>+ $\forall$ nodo $v \notin C$, $v$ è sconnesso da C

Questa definizione è fatta per casi ideali, estremi e in realtà computazionalmente difficili, quindi non va bene (soprattutto il secondo punto della definizione).

>[!definition]
>2-Definizione di comunità
>>Dato un grafo G una comunità C è un sottografo di G tale che:
>>+ C è **connesso**
>>+ $\forall$ nodo $v \notin C$, $v$ è **poco connesso** a C


>[!question] Come individuare le comunità?
>Esistono vari algoritmi e noi vediamo il più importante (anche se non il più efficace):
>+ Edge betweenness centrality

### Edge betweenness centrality

##### Algoritmo di Girvan-Newman
**Idea**: rimuovere ricorsivamente i legami deboli, ovvero rimuovendo gli archi con alta centralità di betweenness (weak ties) e disconnettendo così via via la rete, rendendo le comunità delle componenti sconnesse e potendo così trovarle.

Viene quindi prodotto un albero detto dendogramma dove in ogni livello più lontano dalla radice ci sono componenti (comunità) sempre più piccole, essendo l'albero formato da comunità, sottocomunità e sopracomunità.


___

# Grafo di Facebook

### Lavoro 1: The Anatomy of the Facebook Social Graph
Grafo sociale di Facebook nel 2011:

Primo grafico rappresenta la degree distribution per gli utenti, il secondo rappresenta la CCDF della degree distribution:

![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-04 195601.png|500]]
+ Utenti: 721 milioni di nodi, 10% della popolazione mondiale
+ Archi: circa 69 miliardi, 190 amici a persona in media
+ La degree distribution non è proprio una power law, ma presenta un punto di flessione (sembrano due powerlaw fuse al punto di flessione). Si vede inoltre il limite imposto da Facebook stesso di 5000 amici. 
+ Complementary cumulative distribution funtion (CCDF).
  La CCDF al grado k misura la frazione di utenti che hanno grado k o minore in termini di degree distribution. Si vede bene come nella coda il rumore scompare.

___

Il seguente grafico mostra la distribuzione delle **componenti connesse**:

![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-04 195734.png|350]]
+ Distribuzione delle componenti connesse rappresentata da una power law, in cui si vede che con l'aumentare della grandezza della componente si abbassa il numero di componenti, quindi ci sono poche componenti grandi e molte più piccole. Curiosa la presenza di una componente connessa estremamente grande (100 milioni), che rappresenta praticamente tutto il grafo ed è di fatto la **giant component** della rete di Facebook, il che fa capire che la rete è praticamente connessa o quasi.
+ La dimensione media quando si parla di componenti connesse è un'informazione praticamente irrilevante: in questo grafico vediamo che la dimensione media è circa dell'ordine dei 100 nodi, ma non ci frega niente perché l'unica componente che ci interessa è l'outlier ovvero la giant component

___

Vennero studiate poi le distanze medie in un grafico rappresentante le distanze cumulativa.
![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-08 114513.png|350]]

+ Vediamo come il 92% delle coppie di nodi ha una distanza inferiore a 5. La distanza minore uguale a 6 ce l'hanno quasi il 100% delle coppie di nodi.

___

Venne analizzato anche il **coefficiente di clustering**:
![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-11-08 114702.png|350]]

+ Andamento monotono decrescente (più un nodo ha grado alto più il coefficiente del nodo sarà di grado basso e viceversa)
+ Appena prima dei 5000 c'è una decrescita ripida del coefficiente di clustering. Questo perché i profili con così tanti amici probabilmente non sono persone ma aziende o cose simili che chiedono quindi amicizia a tutti senza avere davvero rapporti con queste persone

___
#### Paradosso degli amici

"I tuoi amici hanno più amici di te"
>[!question] Cosa vuol dire?
>Se prendo un nodo a caso su una rete e conto quanti amici ha otterrò un certo valore, ma se prendo un nodo a  caso e seguo un link e conto quanti amici ha tenderà ad averne di più del nodo iniziale.

![[materie/anno_2025-2026/social_computing/assets/Screenshot 2026-01-18 113031.png|350]]

+ La linea tratteggiata è quello che ci aspetteremmo se non ci fosse il paradosso degli amici: i miei amici avrebbero esattamente gli amici che ho io
+ In realtà gli amici dei miei amici sono mediamente un numer più grande dei miei
+ Si vede però che circa oltre il grado 700 i miei amici hanno meno a mici di me, perché più amici ho io e più è difficile per i miei amici avere tanti amici quanti ne ho io.


#### Paese di appartenenza
In base all'IP si è potuto vedere come l'85% degli archi di un nodo sono all'interno del paese di appartenenza del nodo.

---

### Lavoro 2: Four Degrees of Separation
Grafo di Facebook nel 2012:

#### Osservazioni rispetto allo studio precedente
+ Aumento del numero di nodi e numero di archi aumentato in modo abbastanza costante.
+ Grado medio dei nodi è pure chiaramente in crescita con il passare del tempo.
+ La densità (numero di archi effettivo / numero di archi possibili) invece cala nel tempo. I legami dei nuovi utenti non riescono a sopperire la densità rispetto agli archi che ci potrebbero essere.
+ Distanza fra due nodi: Come si vede dal grafico la distanza media tra due nodi è di 4. Più precisamente in tutto facebook la distanza è uguale a 5. Se i nodi su cui si misura la distanza sono dello stesso paese allora si abbassa a 4.
![[materie/anno_2025-2026/social_computing/assets/distanza.png|400]]
+ Andamento della varianza della distanza: ha un convergenza rapida fino al 2008, in cui si stabilizza praticamente a 0.
+ La distanza media ha una sorta di convergenza fino al 2008 per poi stabilizzarsi ad una distanza media di 4-5. Questo nonostante la densità cali.

___
### Lavoro 3: 
2016

+ Si rianalizzò la distanza media e attennero un valore di 3.5, valore leggermente inferiore al precedente.

---
title: "11-12-13-14-Diffusione-Informazioni"
---
# Diffusione delle informazioni

le pubblicità non dipendono solo dalle possibilità economiche delle aziende.

>[!example]
>Oreo durante il blackout del Super Bowl di 30 minuti ha twittato "Rimasti senza luce, nessun problema potete anche inzupparlo al buio". Strategia questa che ha reso subito virale il tweet e di conseguenza l'azienda Oreo.

#### Esempi di diffusione di informazioni
+ Barzellette
+ Rumors (possono anche essere fake news)
+ Video virali
+ Meme

Mezzo principale delle fake news sono i social.

>[!definition]
>Diffusione delle informazioni
>>Processo per cui un'informazione si diffonde e raggiunge altri individui, ma anche un comportamento (come l'adozione di una tecnologia piuttosto che un'altra).
>>Ci sono metodi per studiare queste diffusioni: sociologia, epidemiologia, statistica,...

##### Temi comuni delle diffusioni:
+ **Mittente**: uno o pochi mittenti che iniziano il processo
+ **Destinatari**: Uno o molti destinatari che ricevono l'informazione (insieme dei destinatari di solito più grande dell'insieme dei mittenti)
+ **Mezzo**: mezzo tramite cui la diffusione avviene (ad esempio retweettare)
+ **Intervention**: processo di interferire col processo di diffusione delle informazioni in atto (ad esempio se voglio che un'informazione venga maggiormente diffusa, o bloccare la diffusione di un'informazione)

#### Modelli per la diffusione delle informazioni
+ Herd behaviour (comportamento del gregge)
+ Information cascade
+ Epidemics (e social contagion)
+ Modello dei benefici diretti (Morris)

## Herd behavior

Idea easy: "Si tende ad imitare quello che fanno gli altri"

>[!example]
>+ Ordino in un ristorante A, arrivato lì vedo che A è vuoto e invece dall'altra parte della strada il ristorante B è pieno nonostante abbiano lo stesso menù. Secondo questo modello sceglierei di andare nel ristorante B perché è quello che tutti gli altri hanno fatto.
>+ Ad un asta se vedo una persona offrire molto io sarò più tentato di offrire a mia volta di più pensando che il tipo sappia il valor elevato dell'oggetto venduto.
>

#### Caso di studio
+ C'è un'urna con tre palline dentro che possono essere rosse o blu. ogni persona deve estrarre una pallina e dire qual è il colore che sta in maggioranza dentro l'urna: o blu o rosso. 
  Il primo studente estrae blu e dice blu.
  Il secondo studente osserva blu e dice blu.
  Il terzo studente se osserva rosso, ma i due precedenti hanno detto blu, dirà blu.
  Il quarto studente qualsiasi cosa peschi dirà blu perché tutti precedentemente hanno detto blu.

+ Probabilità che sia blu =probabilità che sia rosso = 1/2
+ P(blue | maggioranza-blu) = P(red | maggioranza-red)= 2/3
+ Bayes: $p(C|I)=\frac{p(C)\times p(I|C)}{p(I)}$ 
+ Quindi P(maggioranza-blu | blu) = (2/3 x 1/2) / (1/2) = 2/3 > 1/2
+ Quindi il primo studente dovrebbe indovinare blu se pesca blu e anche il secondo studente. 
+ Quindi **razionalmente** il terzo studente dovrebbe indovinare blu anche se vede rosso, in quanto P(maggioranza-blu | blue, blue, red) = (4/27 x 1/2) / (1/9) = 2/3 > 1/2

>[!tip]
>Razionalmente non istintivamente. La scelta da fare è quella razionale.


#### Herding Intervention
Intervention nel modello di herding. L'herding può essere interventato ad esempio rilasciando informazioni private che non erano accessibili prima (ad esempio facendo vedere la pallina che si è estratto nell'esempio)
>[!tip]
>La prima persona che fa notare l'errore che il gruppo sta commettendo, interrompe l'herd behavior.


#### **Riassunto Herd behavior**
+ Basato sull'osservazione di azioni/comportamento
+ Razionale, non istintivo
+ è un risultato/effetto, non un'operazione di base
+ rete quasi completa: vedo i comportamenti di tutti (unidirezionale: vedo tutti e soli i "precedenti")
+ Poco realistico/interessante
+ Comportamento di gregge è abbastanza facile e si può rompere (intervention) in modo semplice.

___

## Information cascade

Tipicamente gli user repostano ciò che è stato postato da altri, e l'informazione diventa diffusa tra gli amici a cascata. 
Information cascade:
+ Ognuno vede ciò che fanno/decisioni dei vicini, localmente. 
+ Herd behavior invece vedeva globalmente.

>[!example]
>Hotmail ad esempio crebbe in iscritti molto velocemente grazie all'aggiunta in appendice in ogni mail mandata di un link per poter creare il proprio account Hotmail.


#### Assumpion per modelli cascade
+ Un nodo può influenzare solo i nodi a cui è connesso
+ Decisioni binarie
+ Singoli nodi possono essere:
	+ Attivi (aderiscono alla decisione adottata)
	+ Non attivi (non aderiscono alla decisione)
+ La rete è un grafo diretto. ("Follow" su X)
+ Non si torna indietro (Se aderisco a hotmail non posso disiscrivermi)

### Independent Cascade Model (ICM)
+ Basato sul mittente
+ Ogni nodo ha un'unica occasione di attivare i suoi vicini, subito dopo la sua attivazione
+ In ICM, i nodi che sono attivi sono mittenti e i nodi che vengono attivati sono riceventi.
##### Algoritmo ICM
>[!warning]
>+ Il nodo attivato al tempo $t$ ha **una sola** possibilità (in base ad una probabilità $p\_{vw}$) di attivare i suoi vicini al tempo $t+1$.
>+ $p\_{vw}$ può essere differente per paia di nodi differenti.
>+ L'attivazione può avvenire solo al tempo $t+1$

Questo modello cerca di rispondere a questa domanda:
>[!question] Come faccio a scegliere i nodi per massimizzare la mia cascata, ovvero la diffusione delle informazioni?
>
>

>[!example]
>Con un limite di budget per una pubblicità voglio sapere come raggiungere una grande fetta di persone.
>In base ai nodi che attacco, esse attivano a loro volta (con un certa probabilità) i loro vicini. Quindi i nodi da attivare inizialmente devono essere accurati e con un ampio numero di vicini che non intaccano con i vicini di altri nodi attivati in modo da massimizzare la crescita della cascata.

>[!problem]
>Si tratta quindi un problema di ottimizzazione.
>+ Dato un paramentro k (budget)
>+ Trovare un set iniziale S per cui |S|=k, che massimizza $f(S)$, con $f$ funzione di diffusione. 

>[!definition]
>Maximizing the Spread of Cascades
>>Problema di trovare un piccolo set di nodi in una rete sociale tali che la loro diffusione aggregata nella rete sia massimizzata.


#### Rendere il problema deterministico
+ Rendere randomiche le attivazioni
+ Generare i numeri random per tutti gli archi, all'inizio del processo ICM
+ Nondeterministic/random --> deterministic

##### Proprietà $f(S)$
+ Non negativa 
+ Monotona: $f(S+v)\geq f(S)$ 
+ Submodulare: Se N è un set finito, la funzione del set è submodulare solo e solo se $$f:2^N \rightarrow R,\forall S \subset T \subset N, \forall v \in N \setminus T, f(S+v)-f(S)\geq f(T+v)-f(T)$$ ovvero "S ci guadagna di più di T", "i sottoinsiemi ci guadagnano di più".

Possiamo usare un algoritmo greedy: 
+ iniziamo con un set vuoto S
+ per k interazioni ad ogni step aggiungiamo ad S il nodo $v$ che massimizza $f(S \cup {v}) - f(S)$ 
+ l'algoritmo greedy fornisce un'approssimazione di (1-1/$e$)
+ Il set S risultante attiva almeno (1-1/$e$)=63% del numero di nodi che ogni set S di grandezza k può attivare.

#### Intervention cascade
+ **Limitare (o increase)** numero di out-links (disconnettere nodi porta a non attivarne altri)
+ **Limitare (o increase)** numero di in-links (ridurre la possibilità di essere attivato da altri)
+ **Decrease (o increase)** la probabilità di attivazione $p\_{vw}$ (ridurre la possibilità di attivare altri)

___

## Epidemics models

>[!definition]
>Epidemics
>>Descrive il processo con il quale una malattia viene diffusa.

**Componenti:**
+ **Un elemento patogeno:** virus infettante, virus informatico, tweet che viene retweettato
+ **Una popolazione di host:** umani, animali, piante,...
+ **Un meccanismo di diffusione:** respirare, bere, sessare,...

>[!scopo]
>Provare a modellare la diffusione di malattie contagiose e trasferirle nel mondo digitale.

##### Differenza con Herd behavior:
+ In herd behavior tutti sono in contatti con tutti.
+ Nei modelli epidemici tutti potrebbero contattare tutti ma non si sa con chi si è stati in contatto.
+ Quindi diversamente dall'herding, le connessioni esistono ma sono sconosciute

### Metodi di analisi delle epidemics:
+ Metodo **Fully-mixed**
	+ analizza solo i gradi (i momenti) in cui ciascun host viene infettato e guarito, evita di considerare le informazioni della rete
+ Usando **Contact Network**
	+ Un grafo dove i nodi rappresentano gli host e gli archi rappresentano le interazioni tra questi host
>[!example]
>Per il covid-19 gli host che sono connessi vuol dire che respirano la stessa aria.

I metodi assumono che:
+ non ci sono informazioni dalla contact network
+ Il processo con il quale gli host vengono infettati è sconosciuto

### Modelli epidemici
+ **SI (susceptible/infected)**
	+ suscettibili possono venire infettati
	+ infettati non guariranno mai. Possono infettare i suscettibili
	+ S(t) numero di suscettibili al tempo t
	+ I(t) infettati al tempo t
	+ $s(t)=S(t)/N$
	+ $i(t) = I(t)/N$
	+ $\beta$ è la probabilità di contatto (ovvero infezione)
	+ $N=S(t)+I(t)$
	+ $1=s(t)+i(t)$
>[!tip]
>Al tempo t un infetto incontrerà $\beta N$ persone e infetterà $\beta S$ di loro. La variazione di individui che diventerà infetta è data dalla moltiplicazione $\beta I S$ nel time step successivo.

**Equazioni**:
+ Ad ogni time step la variazione del numero di individui in S e I è di $\beta IS$ :
  $$\frac{dS}{dt}= -\beta IS$$$$\frac{dI}{dt}=\beta IS$$ 
(S + I = N)  --->  $\frac{dI}{dt} = \beta I(N-I)$  --->  $I(t)=\frac{N\times I\_0\times e^{\beta tN}}{N+I\_0\times (e^{\beta tN}-1)}$   con $I\_0$ numero degli individui infettati al tempo 0. Questa è la curva di crescita logistica:

![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-12 143421.png|350]]

>[!warning]
>All'inizio gli individui sono tutto suscettibili, col passare di t gli infetti crescono sempre di più finché non raggiungono il 100% sempre, senza scampo.

___
+ **SIR (susceptible/infected/recovered)**    ---> variante del modello SI
	+ Gli infetti possono guarire o morire
	+ Una volta che un host è guarito (o rimosso):
		+ Non possono più infettare
		+ non possono più essere infettati e non sono più suscettibili (restano in R)

**Equazioni**

$$\frac{dS}{dt}= -\beta IS$$

$$\frac{dI}{dt}= \beta IS - \gamma I$$

$$\frac{dR}{dt}= \gamma I$$

>[!tip]
>$\gamma$ definisce la probabilità di recovery di un infetto individuale in un lasso di tempo

**Grafico del modello SIR**

![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-14 103024.png|400]]

+ All'inizio tutti tranne 1 sono suscettibili, poi calano a favore degli infetti, che però dopo un po' cominciano a calare essendo sopraffatti dai recovered che non possono riammalarsi
+ Alla fine non ci saranno più infetti e quasi tutti saranno recovered ($< 100$%) e con pochissimi suscettibili (> 0%) pioché quando non ci sono più I non resta nessuno a contagiare i rimanenti S.

>[!tip]
>Un buon dato per capire quanto l'epidemia è stata importante è vedere il numero finale di recovered, ma anche se la curva degli infetti non è molto pronunciata vuol dire che è più difficile prendere la malattia piuttosto che guarire da essa.

**Commenti**:
+ Gli S decrescono monotonicamente
+ Gli R crescono monotonicamente
+ Gli I crescono inizialmente, per poi decrescere man mano che gli individui guariscono e vanno a 0 per $t\rightarrow \infty$ 

#### $R\_0$: Basic reproduction number
+ $R\_0=\beta/\gamma$
+ $R\_0$ è il numero medio di individui che I contagia prima di guarire/morire e $\beta$ e $\gamma$ misurano quanto i due "rubinetti" sono aperti (da S a I e da I a R)
+ $R\_0=\beta / \gamma$  = 1 marca la **soglia epidemica**, ovvero c'è epidemia se $R\_0 \geq 1$ ovvero si forma una componente gigante e l'epidemia esplode.

>[!tip]
>$R\_0 = \beta / \gamma \leq 1$ Non abbiamo epidemia in quanto gli I guariscono più in fretta di quanto gli S si ammalino.
>Il numero di I parte basso e diminuisce.

### Transizione epidemica

>[!definition]
>Transizione epidemica
>>Transizione fra regime epidemia e regime non-epidemia alla soglia $\beta = \gamma$  --> $R\_0 = \beta/\gamma = 1$

Transizione di fase brusca, improvvisa

>[!tip]
>Fenomeno analogo alla comparsa della giant component in G(n, p) per c >1

$S=1-e^{-cS}$   =       $r(t) = 1-e^{-\beta/\gamma \times r(t)}$ 

___

+ **SIS (susceptible/infected/susceptible)**
	+ Gli infetti che guariscono diventano suscettibili nuovamente
	+ Il modello SI è sostanzialmente una variazione dello SIS in cui il valore $\gamma$ è molto basso, vicino a 0

**Equazioni**
$$\frac{dS}{dt}= \gamma I - \beta IS$$
$$\frac{dI}{dt}= \beta IS - \gamma I = I(\beta N -\gamma) - \beta I^2$$
+ $\beta$ passaggio da S a I
+ $\gamma$ passaggio da I a S


**Grafico del modello SIS**

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-11-14 105718.png|400]]

+ Il numero di infetti si alza così come il numero di suscettibili si abbassa, per poi stazionarsi ad un valore (<100% e >0%)

___
#### Confronto curve degli infetti in SI-SIR-SIS

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-11-14 110046.png|400]]

___

+ **SIRS (susceptible/infected/recovered/susceptible)**
	+ Suscettibili si infettano, guariscono, sono immuni per un po' e poi tornano suscettibili
	+ $\lambda$ la probabilità di passare da recovered a susceptible

**Equazioni**
$$\frac{dS}{dt}= \lambda R - \beta IS$$
$$\frac{dI}{dt}= \beta IS - \gamma I$$
$$\frac{dR}{dt}= \gamma I - \lambda R$$

**Grafico del modello SIRS**

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-11-14 110750.png|400]]

+ Grafico simile a SIR, ma i recovered non raggiungono mai la totalità, anzi dopo un po' tendono a diminuire e di conseguenza i suscettibili aumentano a loro volta, rendendo il grafico con una sorta di oscillazione dei valori all'aumentare del tempo, poiché l'epidemia è libera di continuare.

___

### Social contagion

**Idea**: Se un individuo vede un comportamento in un altro individuo, lo imita (adotta lo stesso comportamento), proprio come le epidemie.

Simile a guarire da una malattia può essere smettere di dire una barzelletta perché tutti dicono di saperla già.
+ Modello chiamato **ISR**
Da SIR a ISR --> 
+ Susceptible --> Ignorant (I)
	+ Individuo che non ha ancora ricevuto l'informazione (barzelletta)
+ Infected --> Spreder (S) (diffusore)
	+ Individuo che ha ricevuto l'informazione e la diffonde
+ Recovered --> Stifler (R) (soffocatore)
	+ Ha ricevuto l'informazione ma non la diffonde più (perché gli altri "la sanno già")

+ $\lambda$ tra I e S
+ $\alpha$ tra S e R

Anche se in realtà **Contagio fisiologico $\neq$ Contagio sociale**:
+ **Contagio fisiologico**:
	+ Contaminazione patogena
	+ Processo passivo (vengo contagiato)
	+ Basta un singolo I
	+ Transizione da I a R spontanea
+ **Contagio sociale**:
	+ Atto intenzionale
	+ Processo attivo (cerco l'informazione)
	+ Servono più di un individuo
	+ Transizione da S a R in seguito a interazione S+R o S+S

Diffusione dell'epidemia per i due modelli SIR e ISR:
+ SIR
	+ I+S $\rightarrow^\beta$ 2I
	+ I $\rightarrow^\gamma$ R
+ ISR
	+ I+S $\rightarrow^\lambda$ 2S
	+ S+R $\rightarrow^\alpha$ 2R
	+ S+S $\rightarrow^\alpha$ R+S  oppure  S+S $\rightarrow^\alpha$ 2R

**Equazioni**
+ Si adotta una approccio fully-mixed
$$\begin{aligned}
\frac{dI}{dt} &= -\gamma I S \\
\frac{dS}{dt} &= \gamma I S - \alpha S [S+R] \\
\frac{dR}{dt} &= \alpha S [S + R]
\end{aligned}$$

In un istante $t$:
$$I + S + R = 1$$ 

>[!tip]
>+ Passaggio da I a R in SIR è spontaneo e dipende solo dal numero di I e dal tasso/parametro $\gamma$ 
>+ Passaggio da S a R in ISR è non spontaneo e dipende sia dal numero di S e dal parametro $\alpha$ sia dal numero di R


Per ISR:
+ A tempo $+\infty$ non ci sono più spreader: $s_\infty = \lim_{t\rightarrow \infty}s(t) = 0$ 
+ Gli ignoranti saranno tanti di meno quanti di più saranno gli stifler: $i_\infty=e^{-(1+\lambda/\alpha)*r_\infty}$ 
+ Gli stifler saranno tutti gli altri: $r_\infty= 1-e^{-(1+\lambda/\alpha)r_\infty}$
+ $r_\infty$ è la misura della **diffusione** (frazione di stiflers: infettati e poi recovered): quanto si è diffusa la barzelletta (reliability)

>[!tip]
>Non è esattamente uguale alle epidemie, in quanto non esiste più la soglia epidemica, esiste sempre un'epidemia sociale qualsiasi siano i valori dei parametri.
>La diffusione nel modello ISR raggiunge sempre la componente gigante, quindi si diffonde sempre in una frazione macroscopica della popolazione ($r_\infty > 0$ sempre) 


___


>[!question] E le reti cosa c'entrano con le epidemie?

Questi modelli per epidemie si basano sull'assunzione:
+ Fully mixed
+ Tutti sono in contatto con tutti, rete completa
 Questo non è vero nelle reti reali
 >[!example]
 >Le piante non vanno in giro a contagiare altre piante lontane
 >Nella realtà ci sono gruppi sociale che rendono più probabile incontrare una persona piuttosto che un'altra.

#### Epidemie sulle reti

+ Necessita quindi un'assunzione più debole di prima: rete omogenea, non completa.
	+ Tutti i nodi hanno grado simile
	+ Ogni individuo viene a contatto con lo stesso numero di individui
+ Basic reproduction number $R\_0$ su rete omogenea (tutti i nodi hanno grado simile alla media):
	+ A inizio epidemia sono quasi tutti S
	+ Ogni I infetta un vicino S con probabilità $\beta$
	+ Ad ogni istante $t$ ogni I può transitare in R con probabilità $\gamma$ 
	+ Quindi:
		+ $\Delta I_{t+1} = \beta [k] I_t$    
		+ $\Delta R_{t+1} = \gamma I_t$ 
		+ Per avere epidemia deve essere $\Delta I_{t+1} > \Delta R_{t+1}$ ossia $\beta[k]I_t > \gamma I_t$
		+ Quindi $R_0 = [k] \beta/\gamma$


>[!question] Come diminuire $R_0=[k] \beta/\gamma$?
>+ Diminuire la contagiosità $\beta$ (mascherine, vaccino)
>+ Aumentare la velocità di guarigione $\gamma$ (cure)
>+ Diminuire il grado medio $[k]$ (lockdown, quarantene)

___

### Reti eterogenee
Nel mondo reale le reti sono eterogenee (Power law, Hub)

**Intuizione**: 
+ Gli hub si contagiano facilmente
+ E contagiano molti altri nodi
**Intervention**:
+ Vaccinazioni mirate
+ Paradosso degli amici

>[!example]
>Epidemia della mucca pazza.
>Si è distribuita molto grazie ai legami deboli, ad esempio tramite le persone come turisti che andavano a vedere le mucche perché il virus si diffondeva anche attraverso il terreno.
>In queto caso è critico restare sotto la soglia epidemica ()

>[!definition] 
>**Paradosso degli amici**:
>>Chiedere ad un nodo a caso di scegliere altri individui secondo loro più fragili e di vaccinarli.

>[!tip]
>Coefficiente di clustering alto per il modello ISR vuole dire incontrare spesso gente che "sa già la barzelletta".

Piccolo mondo si verifica tra 10^-1 e 10^-2 di probabilità nel grafico.
**Spiegazione:**
+ Per $p$ bassi:
	+ Rete molto clusterizzata, alto C, molti triangoli
	+ Spreaders diffondono sempre agli stessi
	+ Quindi passano in fretta fra gli stiflers, poca diffusione
+ Per $p$ alti:
	+ Rete con shortcut
	+ Spreaders diffondono anche in parti lontane
	+ Quindi il rumor si diffonde
+ Ovviamente di più per $[k]$ alti

$$\begin{cases} S+R \rightarrow^\alpha 2R \\ S+S \rightarrow^\alpha R+S \end{cases}$$

Su **reti eterogenee**?
Gli hub dovrebbero essere degli spreader efficientissimi perché infatti gli hub diffondono le malattie ed è facile che un rumor raggiunga uno hub e la diffusione diviene più alta.
>[!tip]
>Però dati sperimentali mostrano che $r\_\infty$ è più alto su reti omogenee che su reti eterogenee

>[!question] Perché questo?

Non è vero che l'informazione si diffonde meno su reti eterogenee
+ Per le malattie gli hub aiutano la diffusione
+ Per i rumor no
+ Perché?
	+ è facile che un rumor raggiunga uno hub, e a quel punto la diffusione è molto alta
	+ Ma se hub diventano spreader, allora ci saranno subito molte interazioni spreader-spreader, che porteranno a stifler, e poi molte interazioni spreader-stifler, idem
Gli hub passano da spreader a stifler prima di contagiare molti nodi:
A quel punto gli hub-stifler frammentano la rete --> isolano i nodi --> i nodi isolati restano ignorant.

è quindi possibile modellare la diffusione di rumors con modelli analoghi a quelli per le epidemie, ma ha senso separare **contagio sociale $\neq$ contagio fisiologico**:
+ Processo attivo vs. processo passivo
+ Atto intenzionale vs. contaminazione patogena
+ Decido io di adottare una moda vs. non decido io di ammalarmi
+ transizione da S a R in seguito a interazione S+R o S+S vs. transizione spontanea sa I a R

#### Riassunto sulle epidemie

Modelli: SI, SIR, SIS, SIRS
	Soglia epidemica $R\_0$
Contagio sociale IST
	No soglia epidemica

Reti
+ Epidemie
	+ Rete omogenea (G(n, p)): $R\_0=[k] \beta/\gamma$ 
	+ Rete eterogenea: hub, vaccinazione, paradosso degli amici
+ Contagio sociale
	+ Rete WSSW
	+ Rete eterogenea: ruolo "strani degli hub"

**Modelli sensati ma non perfetti   --> necessità di studiarne altri.**

___

### Modello di Morris (Direct benefit)

+ Basato su benefici diretti (che cosa ci guadagno)

>[!tip]
>Modelli basati su:
>+ Informazioni (faccio X perché vedo gli altri)
>+ Benefici diretti (faccio X perché mi conviene rispetto a non farlo)

>[!example]
>Uso Whatsapp al posto di Telegram perché tutti usano whatsapp e quindi **mi conviene** usare quello per poter comunicare.

Idea:
+ Quindi una decisione arriva ad un nodo ed il nodo stesso decide se adottarla o meno. Solitamente se i nodi vicini l'hanno adottata la adotta anche lui.
>[!tip]
>Per un nodo, il beneficio di adottare un comportamento cresce al crescere del numero di vicini che lo adottano

#### Teoria dei giochi
+ Ogni nodo sceglie fra 2 possibili comportamenti A e B
+ Se due nodi sono collegati da un arco sono incentivati ad adottare comportamenti uguali
	+ Se v e w adottano entrambi A --> payoff a>0
	+ Se v e w adottano entrambi B --> payoff b>0
	+ Se v adotta A e w adotta B --> payoff 0

Matrice dei payoff presente per ogni arco.

Il payoff totale di un nodo v sarà la somma di tutti i payoff in base alle scelte svolte per qualsiasi arco. Lo scopo di tale nodo è massimizzare tale payoff.

>[!question] Se alcuni vicini adottano A e altri adottano B, quale mi conviene adottare?
>Dipende da:
>+ payoff a
>+ payoff b
>+ numero (o %) vicini che scelgono A
>+ numero (o %) vicini che scelgono B

+ $p$ = % vicini che adottano A
+ $1-p$ = % vicini che adottano B
+ $d$ = numero di vicini
+ Regola di decisione:
	+ $v$ adotta A solo se: $p \geq \frac{b}{a+b}$

>[!definition]
>Regola
>> Se almeno una frazione q  ($q = \frac{b}{a+b}$) dei miei vicini adotta A, allora lo faccio anche io (dove q dipende dai payoff).

##### Equilibri
+ tutti adottano A
+ tutti adottano B

>[!question] Come si passa da un equilibrio all'altro?

>[!example]
>tutti stanno adottando B ma alcuni nodi per motivi extra-payoff adottano A (altri vantaggi magari) e possono poi convincere altri B a cambiare e poi altri ancora a cascata. Alla fine possono farlo per tutta la rete.

+ Il processo è **monotono**: dopo la scelta di cambiare il nodo non torna indietro
+ Il processo si ferma quando:
	+ o tutti passano ad A
	+ o nessuno più vuole passare ad A

>[!question] Quando l'equilibrio non viene ribaltato completamente cosa succede e perché?
>Si passa da B ad A se almeno 2/5 dei vicini scelgono A. Se questo non accade il cambiamento da B ad A si ferma.
>Ad esempio se sono presenti dei sottografi completi difficilmente verranno convinti avendo solo un collegamento con il corpo della rete.

+ Si può svolgere un'intervention per far ripartire lo switch del comportamento cercando di far adottare quel comportamento ad un nodo "strategico", che permetterebbe di far ripartire lo switch di tutta la rete.
+ **Cascata di adozioni di A**: molti nodi stanno passando ad A
+ **Cascata completa**: tutti i nodi sono passati ad A

Differenze con l'ICM (Independent Cascade Model):
+ ICM è stocastico
+ Questo invece è deterministico
+ l'Intervention è di natura diversa nei due modelli

#### Intervention
Strategie per far passare ad A:
+ Migliorare il payoff di A
+ Convincere alcuni nodi chiave per far ripartire la reazione a catena (tramite regali, omaggi,...)

#### Cluster di densità $p$
Se ogni nodo che vi appartiene ha almeno una frazione $p$ dei suoi vicini nel cluster
+ "comunità coesa"

>[!tip]
>I cluster fermano le cascate. Anzi una cascata si ferma **solo se** c'è un cluster.

#### Teorema di Morris
+ Soglia q per adottare A
+ (1) Se il resto della rete contiene un cluster di densità > 1-q, allora non ci sarà una cascata completa
	+ **Dimostrazione**: 
		+ Sia $v$ il primo nodo nel cluster che adotta A al tempo $t$
		+ Allora a $t-1$: 
			+ c'è almeno una frazione $q$ di vicini di $v$ adottanti A
			+ nessuno nel cluster adotta A
			+ $v$ aveva almeno una frazione $q$ di vicini fuori dal cluster
		+ Il cluster di densità > 1-q --> >1-q vicini di $v$ devono essere nel cluster --> è impossibile averne q fuori --> assurdo. --> niente $v$ --> no complete cascade.
+ (2) Se non c'è una cascata completa, allora c'è un cluster di densità > 1-q
	+ **Dimostrazione**:
		+ Massa cumplica, varda sue slaid.


#### Ancora Intervention
Quindi per far ripartire una cascade bloccata posso:
+ Aggiungere archi fra cluster diversi (rinforzo i legami deboli)
+ Togliere archi all'interno di un cluster (indebolisco la densità dei cluster bloccanti)
Per bloccare una cascade:
+ Togliere archi fra cluster diversi (indebolisco i legami deboli)
+ Aggiungere archi all'interno dei cluster (rinforzo i cluster bloccanti)

>[!tip]
>Cluster e cascade sono due facce dalle stessa medaglia.
>+ Cluster bloccano le cascade
>+ Se una cascade si blocca ---> c'è un cluster
>+ I cluster però non bloccano le malattie o il contagio sociale

#### Awareness, adoption, weak ties
+ Weak ties: legami deboli
	+ Conoscenze non intime (es. utili se devo trovare lavoro)
+ Utili per diffusione informazioni (o malattie)
	+ **Awareness**, semplice consapevolezza
+ Molto meno utili per diffusione mode, innovazioni
	+ **Adoption**, adozione di un comportamento
+ **Awareness $\neq$ Adoption** 
>[!example]
>È facile raccontare una barzelletta ad uno sconosciuto. È difficile convincerlo a fare la rivoluzione.

#### Diffusioni
+ Movimenti sociali
	+ Diffusione lenta e locale
	+ Adoption
	+ soglia alta (mi costa fare la rivoluzione)
	+ NON sfruttano weak ties
+ Barzellette, meme
	+ Diffusione rapida e planetaria
	+ Awareness
	+ soglia bassa (mi costa poco condividere un video)
	+ sfruttano weak ties

#### Riassunto modello di Morris
+ Basato su Benefici Diretti
+ Diverso dai modelli di contagio sociale e malattie
+ Un nodo **decide** di adottare un comportamento perché **gli conviene**, non perché pensa che sia giusto o per imitare
+ Cascade complete, legame con cluster

---
title: "15-Diffusione-Disinformazioni"
---
# Disinformazione

**Misinformation**: credere che una informazione sia vera anche se in realtà è falsa.
**Disinformation (fake news)**: Diffondere informazioni false essendone consapevole.

>[!tip]
>Non è sempre distinguibile tra le due.
>Alcuni potrebbero diffondere in buona fede notizie create per essere false.

>[!definition]
>Basic definition of misinformation
>>+ Notizie chiaramente false mascherate come cose vere?
>>+ Qualsiasi informazione vada contro il consenso della scienza?
>>+ Qualsiasi informazione che sia falsa? Non è l'unico criterio possibile
>>+ Neanche tra gli esperti c'è una definizione singola di misinformation, ma ci sono diversi tipi di misinformation (Menzogne, Deepfakes, Propaganda Cospirazioni, Rumors,...)

+ Titoli clickbait  fanno in modo che le persone clicchino sul link che farà poi capire ai motori di ricerca che è un sito che gli utenti vogliono vedere e lo posizionerà sempre più in alto nelle ricerche.

>[!tip]
>C'è anche una via di mezzo tra le notizie completamente vere e quelle false. Dipende dal punto di vista della persona che la legge.
>**TRUTHFULNESS: 6 livelli** da TRUE a PANTS ON FIRE (ridicolmente falsa).

+ Non solo ci sono più di due categorie ordinali, ma più di una dimensione, a volte più di due.
>[!tip]
>Si propongono 7 dimensioni in cui plottare le notizie in base alla loro veridicità o falsità.
>+ Correttezza
>+ Neutralità
>+ Comprensibilità
>+ Precisione
>+ Completezza
>+ Affidabilità/Credibilità del diffusore
>+ Informatività

>[!warning]
>Ognuno definisce la misinformation in modi diversi e l'importante è rendersene conto e non cercare una definizione comune per tutti.

#### Motivazioni
+ Importante socialmente
	+ Alto impatto
	+ "Infodemia"
+ Interessante scientificamente


>[!tip]
>Tre misperceptions comuni:
>+ alta esposizione  a contenuto problematico 
>+ Algoritmi sono largamente responsabili per questa esposizione
>+ Social media è la causa primari di problemi sociali come la polarizzazione.

+ Le AI aumentano inavvertitamente la disinformazione, creandola non solo tramite articoli falsi, ma anche multimedialmente: immagini e deepfake.

>[!warning]
>Le fake news sono un problema da combattere, anche se qualcuno sostiene che sia meno grave di quanto percepito.

___

### Modelli epidemici per disinformazione

+ Chi ha ricevuto fake news: **Suscettibile**
+ Chi l'ha ricevuta e la distribuisce: **Spreader**
+ Chi non la distribuisce più: **Recovered**


#### Confronto con SIR
![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-21 111453.png]]

#### "Vaccini" per disinformazione
+ Mostrare info falsa ma non pericolosa, solo leggermente falsa (mettere la candeggina spalmata sulla mano, al posto di iniettarsela per curarsi dal covid) per aumentare resistenza a fake news future.
+ **Inoculation**:
	+ Inoculare le persone contro specifici esempi di misinformazione
	+ Concentrarsi sulle strategie di manipolazione che sono spesso usate per convincere le persone


___

## Tre studi sperimentali
Tre studi sperimentali sulla diffusione delle disinformazioni (aka "fake news").

### Primo studio
Sono state classificate 126000 storie (rumors) twittate da circa 3 milioni di persone e sono state classificate come vere o false usando servizi di terze parti.
**Risultati**: 
+ Le cose false si diffondono più in lunghezza più velocemente e più in profondità rispetto alle notizie vere. 
+ Le emozioni ispirate dalle notizie false erano paura, disgusto, sorpresa
+ Le emozioni ispirate dalle notizie vere erano tristezza gioia e fiducia
+ Contrariamente  quanto si penserebbe i bot accelerano la diffusione di notizie vere e false allo stesso modo, questo perché loro semplicemente distribuiscono ciò che arriva a loro, sono gli utenti umani che favoriscono la diffusione di notizie false.
+ Misure analizzate: Profondità, dimensione, ampiezza max, viralità strutturale

>[!question] Si diffondono di più le notizie vere o quelle false (secondo le 4 misure)?
>+ Per tutte e quattro le misure si ripete la stessa cosa, ovvero che le notizie false hanno misure più ampie delle notizie vere.
>![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-30 125824.png]]

I pattern di diffusione comunque son molto simili tra notizie false e vere quindi **NON** si può trovare delle feature in base alle quali classificare le notizie false e dividerle da quelle vere, in quanto hanno curve molto simili (in base a questo studio).

___
 
### Secondo studio

Sono stati scaricati tutti i post dal 2010 al 2014 di Facebook, e tutte le user interactions (condivisioni, commenti, reactions).

Solitamente sia per le notizie scientifiche che per le notizie cospirazioniste c'è un picco nel corso di un paio d'ore della diffusione, per poi scemare in un pattern simile.
![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-11-30 125943.png|400]]

+ Avviene però una divisione delle due comunità (divento di una o dell'altra se metto like ad un post o all'altro): una scientifica e una cospirazionista, che non si parlano tra loro e condividono tra loro solo post del relativo argomento.
+ L'appartenenza ad una comunità è definita anche dal **valore di omogeneità** dei nodi rispetto agli altri: se l'omogeneità è circa 1, i due nodi analizzati appartengono alla stessa comunità.
+ **Echo chambers:** i contenuti tendono a circolare solo all'interno della rispettiva comunità, data l'omogeneità alta.

___

#### Terzo studio
Si basava sulla modalità di **debunking**, ovvero smontare le falsità a cui erano convinte le comunità cospirazioniste.
L'uomo però possiede il **pregiudizio di conferma**, che consta nel credere solo a ciò che è simile alle cose che già da per vere.

Il debunking sembra quindi inutile.

---
title: "16-17-Networkx-Pyvis"
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

---
title: "18-Crowdsourcing"
---
Il corso è sostanzialmente diviso in 2:
$$\frac{(Social Media)+(Crowdsourcing) =}{(Social Computing)}$$
+ **Social Media**: 
	+ Comportamento sociale viene supportato dai sistemi computazionali
	+ Persone comunicano sfruttando i sistemi computazionali
+ **Crowdsourcing:**
	+ Sistemi computazionali vengono supportati dal comportamento sociale
	+ Compiti che i calcolatori non riescono a svolgere vengono svolti da folle di persone tramite i sistemi computazionali

___
## Aspetti concettuali

Crowds = Folle

>[!definition]
>Folla
>>Tante persone.
>>Possono portare ad una isteria collettiva, ma anche ad un aiuto comune per svolgere qualcosa che il singolo non riuscirebbe.
>>(Due libri opposti: "Madness of the crowds" e "Wisdom of the crowds")


>[!example]
>+ Concorso a premi per vincere bisognava indovinare il peso di un bue. Ognuno scriveva il peso in un bigliettino. Tenendo la media dei pesi scritti si arrivava ad un valore molto vicino al valore corretto. A volte le decisioni prese da una folla di persone sono più corrette di quelle prese dal singolo.
>+ Caso OK della folla:
>	+ Uno shuttle è esploso, la collettività fece scendere in borsa le azioni della marca dello shuttle e in seguito si vide che la colpa era per l'appunto di questa azienda.
>+ Casi KO della folla:
>	+ Shuttle rientrato esploso al rientro, era danneggiato e il comitato decise che non si poteva far niente e lo fecero rientrare ed esplose.
>	+ C'erano delle informazioni su un possibile attacco l'11 settembre, che non vennero condivise tra i diversi enti di sicurezza e per questo non si fece niente

### Principi per cui può funzionare
Affinchè una folla funzioni bene servono questi 4 principi:
+ Diversità di opinioni (possono avere informazioni private)
+ Indipendenza (decisioni non determinate da chi sta intorno: no herding behavior, information cascade)
+ Decentralizzazione (Le varie persone devono essere in grado di specializzarsi in maniera diversa)
+ Aggregazione (deve essere possibile aggregare i dati)
+ Bonus:
	+ Fiducia nella folla (singoli individui devono credere che la folla funzioni)

### Motivi per cui non può funzionare
+ Omogeneità: deve esserci diversità
+ Centralizzazione: se c'è uno che comanda non va bene
+ Divisione: informazioni non accessibili agli altri
+ Imitazione: Formazione di information cascade o herding behavior
+ Emotività: Fatti emotivi possono portare a isteria.

>[!definition]
>Crowdsourcing 1
>>Crowd + outsourcing = Outsourcing to the Crowd ---> Una persona che devo svolgere un compito può svolgerlo in più modi, o dentro l'azienda svolto da pochi dipendenti o viene dato fuori alla folla

>[!definition]
>Crowdsourcing 2
>>Esternalizzare un compito, che tradizionalmente viene eseguito da un impiegato o contraente, a un gruppo di persone indefinito e ampio in forma di una chiamata aperta (chiunque può partecipare).

>[!example]
>Colgate aveva il problema di iniettare della polvere di fluoro dentro un tubetto di dentifricio, ha postato il compito su una piattaforma e un ingegnere a caso ha detto che bastava elettrizzare la polvere in modo da attrarli e si è guadagnato 25000 dollari nel chill easy per il poppin.

>[!tip]
>Piattaforma di crowdsourcing: Amazon Mechanical Turk

___
### Human computation

>[!definition]
>Human computation
>>Processo computazionale da in outsourcing alcuni passi a umani: ruoli tradizionali vengono invertiti, è il computer che chiede alla persona o un gruppo di risolvere il problema e poi raccoglie e interpreta le soluzioni.

Nasce così l'idea dei GWAP (Games with a Purpose), ad esempio:
+ ESP Game (Trovare etichette che descrivono l'immagine ed è da utilizzare la stessa etichetta di una seconda persona, si gioca in coppia) (intanto si etichettano immagini per le AI)
+ Duolingo (Imparare lingue)(intanto tradurre documenti)
+ ReCAPTCHA (test anti-bot)(intanto il calcolatore che sta dietro capisce cosa vuole dire il captcha quando l'utente lo traduce, chiedendo a più utenti e vedere se sono d'accordo)

Motivi per diventare questi "calcolatori umani":
+ Denaro
+ Divertimento
+ Fama
+ Altruismo

>[!tip]
>Il crowdsourcing è un caso particolare di human computation.
>Human computation sembra più efficace se i sistemi digitali sono usati nel processo.

>[!example]
>Ulteriori esempi:
>+ Ricercatore vuole dei dati per gli esperimenti può decidere di cercarli in crowdsourcing. 
>+ azienda che vende beni può fare indagini di mercato veloci e a poco prezzo in crowdsourcing
>+ Amministrazione comunale può chiedere di far foto alle buche in strada anche in maniera gratuita per vedere dove agire.

___
### Soylent: Find-Fix-Verify
>[!definition]
>Soylent
>>processore del mondo con una folla al suo interno.
>>Accorcia, Correzione bozze, human macros (trasforma al passato).

Flusso di lavoro di Soylent:
+ **Find**: identificare in un documento di testo dei pezzi che possono essere accorciati senza cambiare il significato del paragrafo
+ **Fix**: Modificare la parte selezionata per accorciarne la lunghezza senza cambiarne il significato
+ **Verify**: Scegliere almeno una riscrizione che ha errori di stile e almeno una riscrizione che cambia il significato del paragrafo

___
### Amazon Mechanical Turk
Rappresenta una piattaforma in un "mercato per lavoro che richiede intelligenza umana".
+ **Requester**: individuo con lavoro da far svolgere
+ **Worker**: Persona che vuole fare il lavoro
+ **HIT (Human Intelligence Task)**: unità di lavoro da svolgere. Ad ogni HIT è associato un pagamento (pochi centesimi)
+ **Batch**: insieme di HIT caricato da un Requester
Solitamente sono richieste che richiedono meno di un minuto e pagano circa 1-3 centesimi a task
>[!tip]
>Amazon Mechanical Turk rispetta i 4 principi di Surowiecki:
>+ Diversità delle opinioni
>+ Indipendenza
>+ Decentralizzazione
>+ Aggregazione


____

>[!warning]
>**Take home message:** In certe condizioni le folle sembrano essere utili per svolgere compiti di buona qualità.

### Critiche

+ **Critica principale al crowdsourcing**: Qualità messa in dubbio. Attività amatoriale vs. attività di esperti del settore, portano qualità bassa i principianti. Posizione estrema ma con un fondo di verità. Difficile da capire come è veramente.

>[!example]
>Vedendo gli errori che ci sono su wikipedia (fatta da amatori) e sull'enciclopedia britannica (fatta da esperti) si vede come più o meno il numero di errori è lo stesso. Esempio di come gli amatori abbiano fatto comunque un buon lavoro.

+  **Altro problema**:
Molti compiti da qui a 5 anni fa vengono subappaltati alle AI, sia da parte degli esperti che da parte degli amatori.
>[!tip]
>Molti dicono che le AI abbiano ucciso il crowdsourcing, anche se per il momento ad esempio i soldi messi in palio su amazon mechanical turk sono circa li stessi di anni fa. è comunque un fenomeno da tenere in conto.

+ **Ulteriore critica**: Etica del lavoro. Il worker non può essere un lavoro che rende indipendente una persona, la paga a task è minima (1-2 centesimi di solito). Rischio di cadere nello sfruttamento dei worker.

---
title: "19-Crowdsourcing-Tipologie-Classificazioni"
---
# Crowdsourcing

## Tipi di task
**Categorizzazione per Demartini**:
+ Task complesse (costruire sito web)
+ Progetti semplici (design di un logo)
+ Macro task (scrivere una recensione di un ristorante)
+ Micro task (verificare un indirizzo)

#### Tipi di task per Brabham
+ **Knowledge discovery and management**
	+ scoprire e organizzare conoscenze già disponibili ma disorganizzate
	+ tipo Wikipedia, ma con un'organizzazione che sponsorizza
+ **Broadcast search**
	+ Trovare uno specialista che svolga un compito e trovi la soluzione
	+ Tipo dispensa delle slide di Social Computing, uno che metta apposto le lezioni
+ **Peer-vetted creative production**
	+ Crowd produce e seleziona idee creative
	+ Creazione di video ads ad esempio al super bowl, problemi la cui soluzione dipende da gusti e mercato
+ **Distributed human-intelligence task**
	+ Grandi problemi di processione dei dati sono decomposti in piccole task che necessitano dell'intelligenza umana.
	+ Tipo ReCAPTCHA o amazon mechanical turk

#### Tipi di task per Grier
+ **Crowdcontest**
	+ Si da in outsourcing un compito. Solitamente non c'è scomposizione (tutto intero), oppure può essere in formato contest.
+ **Macrotasking**
	+ Dare in outsourcing a un consulente, libero professionista
	+ Spesso pagamento con tariffa oraria
+ **Microtasking**
	+ Compito suddiviso in piccole parti, poi aggregate
	+ "vero" crowdsourcing
+ **Self-organised crowds**
	+ Chiedo che venga svolto un lavoro ma gli individui del crowd interagiscono e si organizzano
	+ Esempio: in una challenge in cui erano da trovare 10 palloni nascosti negli stati uniti. vinse un gruppo MIT che promise ricompense a chi trovava o aveva invitato a trovare ecc...
+ **Crowdfunding**
	+ Non chiedo lavoro alle folle, ma chiedo soldi. Tante piccole donazioni per fare qualcosa.
	+ **Non è propriamente crowdsourcing**

___
### Tipi di pagamento
+ Pay-all: Tutti i worker che hanno svolto il lavoro vengono pagati
+ Pay-one: Nei contest; pago uno solo

___
### Tipi di mercato/crowd
+ **Indipendenti:** ognuno lavora per sé
+ **Collaborative**: cooperazione tra worker, si dividono la paga

>[!warning]
>I confini delle diverse tipologie di crowdsourcing sono molto sfocati e a volte possono prendere caratteristiche da più tipologie.

___
### Motivazioni e incentivi per i worker
+ Divertimento
+ Volontariato
+ Reputazione
+ Retribuzione
+ Nascosto: Non so che sto eseguendo un compito. Produco dati con il mio comportamento.

Motivazioni:
+ **Estrinseche**: Per convincere il worker a fare un compito considerato noioso, socialmente spiacevole, ecc..
+ **Intrinseche**: Se l'attività consegue all'interesse stesso del worker. ricompensa intrinseca allo svolgimento stesso del compito (tipo assaggiare le caramelle e dire se sono buone)

>[!question] Ma X è crowdsourcing?
>Risposta è "dipende".
>Anzi la risposta è spesso inutile.
>Confini labili, sfocati, non netti.

___
### Tipi di domande
+ **Domanda scelta singola:** Singola risposta fra alcune opzioni.
+ **Domanda a scelta multipla**: Una o più risposte fra alcune opzioni.
+ **Fill-in-the-blank**:
	+ Numerico: esempio il peso della mucca
	+ Testuale: email di qualcuno
+ **Collection**: Raccolta dati

___
### Real-world tasks
+ **Sentiment analysis**
	+ Domanda a scelta singola
+ **Search relevance**
	+ Domanda a scelta singola
+ **Moderazione dei contenuti**
	+ Domanda a scelta singola
+ **Raccolta dati**
	+ Collection task type
+ **Categorizzazione**
	+ Domanda a scelta multipla
+ **Trascrizione di audio/immagini**
	+ Fill-in-the-blank

___
### Matrice worker / task
+ Matrice con la quale rappresentare l'esito di un esperimento di crowdsourcing, con *n* tasks e *m* workers. Ogni $v\_{ij}$, che rappresenta i valori dati in risposta, sarà un numero / testo / scelta multipla / ecc..
+ La matrice è però sparsa: non tutti i worker fanno tutti i task e non tutti i task sono fatti da tutti i worker

---
title: 20-(Micro)task-Design
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

---
title: "21-Controlli-Ridondanza-Aggregazione"
---
## Tecniche per migliorare la qualità

+ Metodologiche (già viste): Pairwise, scale,...
+ Controlli in itinere
+ Ridondanza e aggregazione
+ Ex-post (dopo l'esecuzione dell'esperimento)

### Controlli in itinere
**Design del task**: scegliere la giusta modalità di presentazione (uso colori, paginazione, ecc...)
+ L'atteggiamento deve essere duplice: semplificare il task il più possibile, ma inserire anche dei controlli per tenere d'occhio i comportamenti dei worker

Per i controlli ci sono varie tecniche:
+ Test di qualificazione 
	+ prima del task il worker deve superare un test
	+ Obiettivo: selezionare worker effettivamente motivati che cercano di superare il qualification test
	+ Due possibilità: Da una piattaforma (mturk) oppure interno al task stesso
+ Controlli sintattici (parsing)
	+ Evitare risposte non date o campi vuoti (ad esempio un radio button che richiede una risposta obbligatoria)
	+ Conteggio dei caratteri/parole (mettere magari un minimo di parole)
	+ Verificare esistenza di URL inseriti dall'utente
	+ Blacklist di termini (per le bestemmie e cose così)
	+ Controllo copia-incolla (risposte uguali in più sezioni diverse)
	+ Controllo anti plagio
+ Test nascosti (gold questions)
	+ All'interno del task mettere delle domande per misurare la qualità del worker (solitamente domande estremamente semplici impossibili da sbagliare)
	+ Per i task di raccolta di opinioni è più complicata la faccenda. In questi casi si fanno magari due domande di cui si sa la risposta e vedere cosa risponde il worker (es. "più alto l'everest o il monte bianco?" e poi "più alto il monte bianco o l'everest?" e vedere se il worker risponde coerentemente a tutte e due)
+ Monitoraggio dei tempi
	+ Cutoff sul tempo totale (se il worker va troppo veloce non va bene)
	+ Anche per le soglie superiori (worker troppo lento, è distratto)
+ Monitoraggio azioni
	+ Verificare i spostamenti del mouse
	+ Scrolling (es. se per leggere un testo bisogna scrollare uno slider e l'utente non lo fa vuol dire che non sta leggendo quel testo)
	+ Monitorare l'ordine di inserimento dei dati

>[!question] Come usare i controlli in itinere?
>Se la qualità del worker è bassa, posso decidere di scartarlo (magari anche bloccarlo per il futuro o decidere di non pagarlo) o farlo pesare di meno in base alla qualità rilevata.

---
### Controlli ex-post

Posso anche valutare il worker alla fine dell'esecuzione del lavoro, analizzando in post quello che ha fatto (anche con analisi più sofisticate di quelle fatte online durante il task) e potendo quindi decidere di:
+ Non usare i dati
+ Non accettarli
+ Bloccarlo o non pagarlo
Le analisi più sofisticate che non posso inserire dentro a ciascun task ad esempio possono consistere in:
+ Usare le risposte degli altri worker allo stesso task
+ Usare le risposte di tutti i worker a tutte le task
+ Analisi manuale dei testi o delle risposte

>[!tip]
>L'attitudine del requester deve essere quella di massimizzare i dati buoni da utilizzare, quindi non limitarsi a dividere binariamente in perfetto/sbagliato. Porre un "tipping point", una soglia oltre la quale la qualità è considerata "abbastanza".

---

### Ridondanza & Aggregazione

+ Raccogliere più risposte alla stessa domanda per più volte
+ Aggregare le risposte in un unico valore con qualche funzione di aggregazione (media, mediana, moda, ...) 

**Qualità:**
+ Individuale: risposta del singolo worker
+ Aggregata: risposte ad un task
	+ Ridondanza: più worker fanno lo stesso task

>[!example]
>Per valutare la rilevanza di un documento si aggrega tutte le risposte dei worker e un oracolo ci dice quel è il valore corretto tramite il valore aggregato.

#### Notazione e funzioni di aggregazione

Leggiti le merdo-merda di slide dalla 36 alla 41


>[!example]
>Nell'esempio di prima sulla rilevanza dei documenti pongo 1 al posto di Relevant e 0 al posto di Not relevant. 
>+ Svolgo poi l'aggregazione attraverso la moda. Ottengo così dei valori ammissibili ma perdo informazione (se ad esempio in una colonna tutti dicono 1 ma in un'altra 51 dicono 1 e 49 dicono 0; il valore di aggregazione delle due colonne sarà però sempre 1)
>+ Provo allora ad aggregare utilizzando la media. Ottengo valori non ammissibili (diversi da solo 1 e solo 0) ma perdo meno informazione (tiene conto del numero di valori di 1 e 0).
>+ Non è così scontato capire cosa fare

---
title: 22-Misurazione-Ridondanza-Aggregazione
---
## Teoria della misurazione
+ Measurement
+ Scales (N, O, I, R)
+ Permissible transformations
+ Meaningful statements
+ Legit operations & statistics

### Measurement

>[!definition]
>Measurement - 1
>>Un processo con lo scopo di determinare una relazione tra una quantità fisica e un'unità di misura
>>$\omega:D\rightarrow R$
>>Un assegnamento $\omega$ è una funzione che assegna valori agli oggetti in un set $D$

>[!tip]
>Measurement = Assignment of a real number
>Si ma non solo...
>

>[!problem]
>Un po' di cose strane da capire
>Stessa misura vs. misura equivalente
>+ Numeri diversi per la stessa cosa (es. temperatura: gradi, celsius, kelvin, fahreneit)
>+ Confronti (es. 1-2-3    |     10-11-12)
>+ Numerare le categorie (es. cambio la numerazione di categorie da 1-2-3 a 1-3-5 oppure 3-2-1)
>+ Aggregazione (es. posizione media, colore medio riferito magari ad una temperatura)
>+ Aggettivi strani (tipo "doppio" può essere utilizzato con la temperatura? A è il doppio più caldo di B?)

>[!definition]
>Measurement - 2
>>Per essere una misura, un assegnamento deve essere un **omomorfismo** (esempio "agglomeration (+)", "heavier than (>)")
>
>Queste proprietà valgono in qualsiasi misura (es. un chilo di patate è ">" di 6 chili di patate)

___

### Measurement scale

>[!question]
>Che scale devo usare per una data misura?

**Standard set:**
+ Nominale
+ Ordinale
+ Intervallare
+ Ratio

#### Ratio scale
>[!example]
>"sono alto due volte lui"
>"lui è ricco due volte me"
>+ Parte da zero (Età, ricchezza, altezza)
>+ Non tutte le misure possono utilizzarla (es. oggi è caldo due volte ieri   -->   non va bene)

#### Interval scale
>[!example]
>"Negli ultimi giorni abbiamo avito un incremento di 5°C nella temperatura"
>Esempi sono temperatura e le date
>+ Stessa differenza (2019-2017 = 2006-1004)
>+ Non lo stesso ratio (2000 non è due volte 1000)

#### Ordinal scale
>[!example]
>la misura non è un ammontare ma un rank:
>+ "oggi è più caldo di ieri"   -->  oggi = prima posizione,     ieri = seconda posizione

#### Nominal scale
>[!example]
>Misure qualitative, categorie.
>+ Es. nomi, generi, nazionalità, colori...
>+ I numeri fungono da identificatori della classe

#### Trasformazioni permesse
Data una scala, la misura può essere trasformata per ottenere una misura equivalente?
+ Ovvero se tu **trasformi** la misura, stai ancora misurando la stessa cosa (es. nazionalità, rank, temperatura, soldi)

![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-12-20 174723.png]]

+ Alcuni frasi in una misurazione hanno senso, altre no. Es:
	+ Age: 40 anni = 20 anni $\times 2$    -->  tu hai il doppio dei miei anni
	+ Scala nominale della nazionalità:  Greek = 1; Italian = 2; ....
	  Non posso dire che l'italiano è il doppio del greco, non vorrebbe dire niente. 

>[!tip]
>Data una scala, solo alcune delle frasi hanno senso (sono meaningful), e la loro truthfulness (o falsehood) rimane anche dopo le permissible transformations.

Anche solo alcune operazioni (legit operations) avranno senso in base alla scala:
+ relazionali: =, >, <
+ aritmetiche: +, -, $\times $, /
+ statistiche: media, mediana, moda

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-12-20 180437.png]]

>[!warning]
>Non confondere **permissible transformations** e **legit operations**:
>+ Permissible operations: trasformazioni che posso applicare alla misurazione mantenendo la stessa misurazione (una equivalente)
>+ Legit operations: Cose che posso usare per definire la relazione tra le misurazioni

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-12-20 180500.png]]
___
## Aggregazione reloaded

>[!question] A cosa serve?
>A ragionare sull'aggregazione   (Relevance assessment binario)

Secondo la teoria della misurazione la scala utilizzata è nominale; scelta tra moda e media cambia poco nel caso dell'esempio slide 59.
A volte però è più complicato, per esempio possiamo dover utilizzare le **Categorie ordinali** (es. Pants on Fire, False, Half True, True,....).
Utilizzando nuovamente la moda con queste categorie
>[!example]
>Utilizzando nuovamenta la moda nell'esempio se ad esempio abbiamo 51 True e 49 Mostly True, sarà come avere 99 T e 1 MT.
>+ Gli errori piccoli saranno uguali agli errori grandi (49 F e 51 T, sarà considerato True)
>+ Si perdono informazioni

>[!soluzione]
>Potrei fare una trasformazione iniettiva non monotona alle categorie assegnando numeri crescenti in base alla veridicità della categoria alle categorie stesse. (False = 1, Barely True = 2, Half True = 3,....).
>Rendo la scala nominale una **scala ordinale**.
>Con questa soluzione ci sono comunque cose che possiamo dire con certezza ed altre che non possiamo dire.

>[!tip]
>La scala può essere scelta in base all'impatto anche psicologico che le sue etichette si presume abbiano verso i worker, ma possono avere anche problemi di "ridondanza".
>Ad esempio una scala a 100 valori può essere probabilmente semplificata in una scala a 10 valori.
>Più le scali sono grandi e più si avvicinano a una scala a intervalli, ma più la scala è grande e più i risultati appaiono vicini magari alle misurazioni degli esperti.

___

### Funzioni di aggregazione

+ Moda, a maggioranza, Majority Voting
+ Mediana
+ Media aritmetica, geometrica, armonica, pesata

>[!tip]
>Non è sempre semplice scegliere la funzione giusta.

#### Media aritmetica e geometrica
>[!example]
>Misurazione di gradimento di una fotografia in numeri compresi tra 0 e 1.
>Suppongo di avere due casi:
>+ Miglioro da 0.1 a 0.2 in questionari successivi
>+ Miglioro da 0.8 a 0.9 in questionari successivi
>Si potrebbero fare diversi ragionamenti come che il miglioramento è uguale oppure che il primo miglioramento in termini percentuali è del 100%, oppure meglio il secondo perché mi avvicino maggiormente alla perfezione.
>


Altro problema è quello degli outlier:
Gli outlier tendono a sfasare il dato reale della media, se ad esempio 9 persone mettono un valore simile a 1 e una persona sola mette 100, la media aritmetica porta un valore che non è molto rappresentativo di quello che dicono effettivamente i worker.
Con la mediana questo errore non succede.

#### Media armonica

>[!definition]
>Media armonica
>>Reciproco della media aritmetica dei reciproci.
>>Ha la proprietà di essere vicino al minimo.

Proprietà:
+ media armonica < media geometrica < media aritmetica

---
title: 23-Crowd-Frame--Accordo
---
# Crowd_Frame

Amazon Mechanical Turk presenta tre fasi per il design delle task:
+ Project definition
+ Task interface design
+ Customization and publication
Per sviluppare le interfacce del task bisogna comunque avere delle competenze informatiche non indifferenti, bisogna saper scrivere in HTML (di cui AMT fornisce dei superset per organizzare il body del task), CSS, Javascript.
Anche la customizzazione del task e la pubblicazione richiede competenze informatiche 

Idea di soluzione per queste difficoltà:
+ Utilizzare una piattaforma di crowdsourcing solo per reclutare i workers, ma usare un software esterno per creare il task a cui i worker avranno accesso (Crowd_Frame)
+ I worker fanno la task e tornano alla piattaforma per ricevere il pagamento

### Crowd_Frame

Crowd_Frame quindi permette di automatizzare il processo di backend della creazione di un task: permette di definire il task e, tramite script automatici, crea l'infrastruttura necessaria su AWS e pubblica il task su MTurk.
Permette di ricoprire punti dello sviluppo del task quali:
+ Configurazione (parametri di configurazione del task)
+ Sviluppo del task (interfaccia che vedrà l'utente)
+ Deploy (lancio su AWS per creare il bucket e una tabella DynamoDB per salvare i dati)
+ Pubblicazione (comunica con le API di MTurk per rendere il task visibile ai worker)
+ Raccolta dati (dati salvati su AWS)

Questo tramite lanci di script Python per i quali serve una conoscenza minima rispetto allo sviluppo standard del task su Amazon Mechanical Turk.
#### Limitazioni: 
+ Implementazione di allocazioni automatiche di elementi in HITs
+ Una interfaccia per monitorare internamente lo status della task
+ Crowd_Frame è comunque un tool di ricerca, non un prodotto
+ Le skill da developer sono comunque richieste, benché molte meno

___
# Accordo

Anche dopo avere pagato il worker e a lavoro finito, posso scegliere di dar un peso diverso ad un dato worker rispetto agli altri.

Due tipi di accordo:
+ **Accordo globale**: guardare quanto i worker sono in accordo fra loro:
	+ Se sono in accordo, i dati sono affidabili
	+ Se sono in disaccordo, dati non affidabili
+ **Accordo individuale**  (slide 65)
	+ Non guardo l'agreement generale di un worker ma considero ogni singolo worker e guardo quanto correla con l'aggregato degli altri worker (sullo stesso task): sostanzialmente se il worker è d'accordo con gli altri è un buon worker, se è in disaccordo con la maggioranza degli altri è un cattivo worker
	+ Posso quindi in seguito decidere di escludere una percentuale dei worker in base alla percentuale più piccola o  più grande

>[!question] Come misuro l'accordo (agreement)?
>Ovvero: quanto i vari worker che lavorano sullo stesso task danno la stessa risposta?
>+ NON si usano Aggregazione e Ground Truth
>+ Quello che si fa è guardare i singoli worker che stanno facendo la stessa task nella matrice con i worker come righe e i task come colonne
>+ Variabili che determinano il risultato:
>	+ numero di worker
>	+ Tipo di scala (nominale, binaria, ordinale, intervalli, rapporti)
>	+ Sparsità della matrice (non tutte le celle della matrice sono piene)

>[!tip]
>Accordo visto come un proxy/ un'approssimazione della qualità del lavoro
### Misure di accordo per scale nominali (non vediamo quelle ordinali)
+ 2 worker
	+ Percent(age) agreement
	+ Cohen's kappa
+ Più worker (n worker)
	+ Pairwise agreement
	+ Fleiss's kappa

#### Percent(age) agreement
Accordo percentuale
Si parte dalla solita matrice workers / tasks e la semplifichiamo
>[!example]
>Caso semplice: matrice di 2 workers non sparsa (tutti i task di tutti i worker hanno risposta) e con scala nominale binaria (Y/N):
>+ Trasformiamo la matrice in una matrice di confusione che contiene i dati su quante volte i worker hanno dato tutte le combinazioni possibili di risposte (W1_Y/W2_Y, W1_Y/W2_N, ecc...) 

>[!tip]
>Ad una matrice workers/tasks corrisponde una sola matrice di confusione, ad una matrice di confusione possono corrispondere più matrici workers/tasks.

Il Percent agreement quindi sostanzialmente somma tutte le volte in cui i workers hanno risposto allo stesso modo (diagonale della matrice di confusione) e divide per la totalità delle risposte (somma di tutti i valori della matrice di confusione).
![[materie/anno_2025-2026/social_computing/assets/Screenshot 2026-01-15 114151.png|400]]
Il risultato è la percentuale di accordo dei workers.
La misura è estendibile facilmente a più categorie (sempre scala nominale), basta aggiungere righe e colonne alla matrice di confusione
##### Svantaggi
+ Agreement by chance: se i worker rispondono a caso avranno comunque un accordo percentuale, che però non corrisponde al reale.
  Con l'aumento delle categorie l'accordo percentuale, se sparato a caso, viene comunque diminuito
+ Se i worker sanno che il 90% dei casi è N, faranno in modo di rispondere N al 90% delle domande, quindi l'accordo percentuale aumenta notevolmente
+ questa cosa funziona con 2 worker, altrimenti con più worker mi servirebbe una matrice di confusione a più dimensioni
+ Funziona solo con scale nominali

____
### Cohen's kappa
Restiamo sempre sul caso 2 workers, con scala nominale.
Corregge la formula del percent agreement inserendo anche il percent agreement atteso.
$$k = \frac{p\_0-p\_e}{1-p\_e}$$
+ $p\_0$ è il percent agreement osservato
+ $p\_e$ è il percent agreement atteso: è calcolato aggiungendo sulla matrice di confusione una riga e una colonna che contengano le somme dei valori delle colonne e delle righe corrispondenti ai valori delle task dati dai workers, e calcolando il percent agreement delle volte in cui entrambi hanno detto Y ed entrambi hanno detto N e il $p\_e$ sarà la somma di questi 2 agreement
>[!tip]
>$k$ può essere anche < 0 se il percent agreement atteso è maggiore del percent agreement ottenuto

____

### Fleiss's kappa
Sempre su scala nominale, ma estende ad $m$ workers e con $n$ categorie.
Invece di guardare tutti i worker insieme, applico il pairwise agreement, quindi guardo le coppie di worker e guardo quale frazioni di coppie è in accordo di più
>[!example]
>Ho $m$ worker, le coppie di worker saranno $m(m-1)/2$
>Ricerco quindi la % di coppie in accordo.
>Esempio: ho 5 task e 4 worker, con tre categorie A, B, C
>+ $4\times 3/2=6$ coppie
>+ Per ogni task guardo tutte le 6 coppie possibili e vedo la percentuale di coppie che ha risposto uguale (se ad esempio al primo task tutti hanno risposto A, il pairwise agreeement sarà 6/6)
>+ Infine si fa la somma di tutti i pairwise agreement (ad esempio $6/6+1/6+3/6+5/6+3/6 = 18/(6\times 5)$) e si trova il kappa di Fleiss

#### Definizione generale
$$k = \frac{\bar{P}-\bar{P\_e}}{1-\bar{P\_e}}$$
(godo si skippa fino a slide 62)
(si skippa ulteriormente perché boh fino a slide 73)
___
#### Schema sulla ricerca della qualità delle task
+ Qualità 1: **Pre raccolta dati**
	+ Design delle task
	+ Ridondanza & Aggregazione
+ Qualità 2: **Mentre si raccolgono i dati**
	+ Teoria della misurazione
	+ Aggregazione reloaded
+ Qualità 3: **In seguito alla raccolta di dati**
	+ Accordo

>[!warning]
>Non esiste una soluzione finale da usare in tutti i casi.
>

---
title: "24-Fine"
---
# Fake news

>[!question] Si riesce ad individuare le notizie vere da quelle false, magari utilizzando il Crowdsourcing?
>Si tenta lo sviluppo di una macchina della verità, che riceve in input la notizia e rilascia in output la sua veridicità o falsità.

In realtà queste macchine della verità sono dei fact-checker expert, ovvero delle persone che manualmente controllano le notizie. Tuttavia ci sono molte più notizie che fact-checker, che non sono scalabili

Altra possibilità è integrare AI tools con i crowd workers e con i fact-checkers, per aumentarne l'efficienza.
Però sorgono delle domande:
+ Ha senso chiedere al crowd di dire se una notizia è vera o falsa, crowd che è lo stesso che mette in giro tale notizia
+ Generalmente AI e fact-checkers si contrappongono negli stats: ad esempio i fact-checkers hanno un'accuratezza maggiore e un controllo del bias maggiore, mentre l'AI ha una scala maggiore e un costo maggiore. Potrebbe quindi avere senso usarli insieme, con i crowd workers che probabilmente si pongono nel mezzo tra i due.

>[!example]
>Community notes è un sistema di Twitter che permette al crowd di aggiungere note sulle notizie dicendo se sono vere o false, giudicate dalla community.

**Efficacia** delle singole componenti:
+ Esperti: 100%
+ Crowd: 80%
+ AI: 80%
Effettivamente potrebbe bastare un'efficacia inferiore al 100%

**Confidenza**:
+ Le confidenze delle AI non sono per nulla affidabili, sono molto brave ad essere estremamente sicure dei loro errori
+ Anche Per i crowd workers non è detto che se c'è un maggior accordo allora le notizie sono più vere

**Valutazione**:
+ Benchmark (dare in pasto alla macchina una serie di notizie etichettate come vere o false e vedere quante ne indovina)
	+ Problemi:
		+ **Data contamination**: Nelle AI spesso vengono date in allenamento delle notizie con relative risposte, quindi non sta facendo un vero ragionamento ma sta semplicemente incollando la risposta collegata a quella notizia

(siuuuuu si salta fino a slide 33)

___
### Esperimento

Sono stati presi vari statement già giudicati da esperti e vengono fatti giudicare ai worker

+ Distribuzione box-plot con sull'asse delle x i valori reali attribuiti da esperti e sull'asse delle y valori ad intervalli da 1 a 6 che corrispondono ai valori di verità partendo da 1=falso a 6=vero.
![[materie/anno_2025-2026/social_computing/assets/Screenshot 2026-01-15 125635.png|450]]
  Si vede come in alcune notizie il crowd non abbia fatto proprio un bel lavoro, soprattutto su quelle ritenute false dagli esperti, essendoci dei casi in cui alcune notizie sono state valutate intorno al 5, nonostante fossero completamente false.
  L'accuracy del crowd si attesta in questo caso intorno al 70%, che è più o meno alla pari all'epoca dei sistemi automatici, quindi non conveniva utilizzare il crowd che dava la stessa accuratezza dei sistemi AI.

Ci riprovarono successivamente negli scorsi anni e rivedendo i dati i crowd ebbero un'accuratezza dell'80%, maggiore delle AI (che però negli ultimi anni sono cresciute fino all'80% anche loro)

Riassunto di tutto è che praticamente lo studio non è ancora finito e quindi non si sa se il crowd e le AI vanno bene o no. Insomma in alcune cose si in altre no.

# FINE