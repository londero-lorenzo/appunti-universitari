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
>Possiamo stimare quanto un grafo sia sia vicino ad essere completo misurandone la transitività?
>
>Non del tutto, grafo completo e alta transitività sono disuguali: aggiungendo archi a caso in un grafo già denso non aumento molto la transitività.




