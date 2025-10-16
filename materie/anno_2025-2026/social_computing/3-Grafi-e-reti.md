---
title: 3-Grafi-e-reti
aliases:
  - 3-Grafi-e-reti
tags:
  - università
  - materie
  - anno-2025-2026
  - social-computing
  - 6-10-25
created: 2025-10-07
---
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

Grafi diretti:
 $$D=\frac{2|E|}{|V|(|V|-1)}$$
Grafi indiretti:
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

>[!tip]
>Non bisogna scambiare le reale rete sociale con il modello utilizzato per rappresentarla.
>"Confondere il modello con la realtà è come andare al ristorante e mangiare il menù" diceva un frocio
