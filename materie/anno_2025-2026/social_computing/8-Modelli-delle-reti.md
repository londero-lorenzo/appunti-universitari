---
title: 8-Modelli-Delle-Reti
aliases:
  - 8-Modelli-Delle-Reti
tags:
  - università
  - materie
  - anno-2025-2026
  - social-computing
  - 8-Modelli-delle-reti
created: 2025-10-24
description: (INCLUDE SLIDE 8-9)
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

+ In G(n, p) il **numero di archi** che in G(n, m) era ESATTAMENTE m è IN MEDIA: $p\*n(n-1)/2$

+ **Grado medio** lo ricavo considerando tutte le estremità degli archi e dividendo per il numero di nodi: $\frac{2\*[m]}{n}=(n-1)p$

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
+ **Fitness: $P(v\_i)=\frac{𝜂\_i\*d\_i}{\sum\_j{(𝜂\_i\*d\_j)}}$**
	+ $𝜂\_i$ rappresenta la fitness del nodo $i$
	+ Si ottiene sempre una power law
+ **Modello 'Random Walk**':
	+ Ad ogni passo si aggiunge un nuovo nodo $i$, con m>1 archi attaccati, di cui un arco è collegato ad un vecchio nodo $j$ scelto a caso, con probabilità uniforme.
	+ Ogni altro arco degli m-1 restanti viene collegato con probabilità $p$ a un vicino di $j$ scelto a caso, e con una probabilità 1-$p$ a un nodo vecchio qualsiasi scelto a caso. ($p$ probabilità che si formi un triangolo).
	+ Con nodi con tanti archi è più probabile privilegiare (attaccarsi) a nodi con un grado a loro volta maggiore (i ricchi diventano più ricchi).

Questo ultimo modello random walk finalmente funziona: prendendo a martellate il modello scale free trasformandolo in random walks si ha quindi una degree distribution con power law, cammini brevi e C alto (alta presenza di triangoli).