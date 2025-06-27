---
title: Apsp
aliases:
  - Apsp
tags:
  - cammini-minimi
  - apsp
  - grafi
created: 2025-06-15
---
# All Pairs Shortest Paths
$\forall s \forall v$ determinare un cammino di peso minimo da $s$ a $v$

```c
APSP(G){
	for(each s in V){
		DIJKSTRA(G, s)
	}
}
```

complessità:
$\mathcal{O}(|V|\cdot |E|\log{|V|})$

nel caso peggiore se $|E|= \Theta(|V|^2)$:
$\mathcal{O}(|V|^3\log{|V|})$

senza heap senza matrici: $\Theta(|V|^3)$

---

Ultimo algoritmo:
## Floyd-Warshall
- usa matrici:
	- in $D[i,j]$ = peso di un cammino minimo da $i$ a $j$
- programmazione Dinamica
	- algoritmo suddiviso in sottoproblemi una volta risolti memorizzo i risultato per ripescarli quando mi servono

### Idea

suppongo di aver 