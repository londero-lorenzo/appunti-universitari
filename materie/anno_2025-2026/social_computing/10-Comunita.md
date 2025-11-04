---
title: 10-Comunita
aliases:
  - 10-Comunita
tags:
  - università
  - materie
  - anno-2025-2026
  - social-computing
created: 2025-11-03
description: INCLUDE ANALISI GRAFO DI FACEBOOK
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
>+ Un conflitto in un club di karate ha separato in due gruppi le persone dl club che avevano più legami di amicizia con uno con l'altro
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
  La CCDF al grado k misura la frazione di utenti che hanno grado k o maggiore in termini di degree distribution. Si vede bene come nella coda il rumore scompare.
+ 
___

Il seguente grafico mostra la distribuzione delle componenti connesse:

![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-04 195734.png|350]]
+ Distribuzione delle componenti connesse rappresentata da una power law, in cui si vede che con l'aumentare della grandezza della componente si abbassa il numero di componenti, quindi ci sono poche componenti grandi e molte più piccole. Curiosa la presenza di una componente connessa estremamente grande (100 milioni), che rappresenta praticamente tutto il grafo ed è di fatto la **giant component** della rete di Facebook, il che fa capire che la rete è praticamente connessa o quasi.