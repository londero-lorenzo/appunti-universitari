---
title: Kruskal
aliases:
  - Kruskal
tags:
  - MST
  - kruskal
  - grafi
created: 2025-06-15
---

Algoritmo per determinare MST

1. ordiniamo gli archi in ordine crescente
2. li scandisco in ordine di peso crescente
3. arrivati all'arco ${x, y}$ dobbiamo decidere se aggiungerlo ad $A$
	-  Devo valutare rapidamente se $\{x, y\}$ sono già connessi in $A$


```c
KRUSKAL(G = (V, E, W)){
	Sort(E, W)
	A = {}
	for (each v in V){
		MAKE(v)
	}
	for (each {x, y} in E){
		if (FIND(x) != FIND(y)){
			A = A.update({{u, v}})
			UNION(u, v)
		}
	}
	return A
}
```


Costo:

- ordinamento edges $O(|E| \log{|E|}1)$
- operazione muf
	- |V| make
	- |E| Find
	- |V|-1 Union

Usiamo Liste concatenate:
n = make = $O|V|$
m = make + union + find = |V| + |E| + |V|-1 = $\mathcal O(|E|)$

$O(n^2 + m)$ = $\Theta(|E|)$ + $O({|V|}^2)$ = $O(|V|^2 + |E|)$

potevo far finire per seconda la lista più lunga -> errore quadratico

Liste concatenate con wenghted union
n = make = $\mathcal{O}(|V|)$
m = make + find + union = $|V|+|E| +|V| - 1 = \mathcal{O}(|E|)$  
$O(m + n\log{n})$ = $\mathcal{O}(|E| + |V|\cdot \log{|V|})$

Alberi con `UNION-BY-RANK` e pathcompression
$\mathcal{O}(m \cdot \alpha(n, m)) = \mathcal{O}(|E| \cdot \alpha(|V|, |E|))$

Totale (con Alberi con `UNION-BY-RANK` e pathcompression):
$\mathcal{O}(|E| \log{|E|}) + \mathcal{O}(|E| \cdot \alpha(|V|, |E|)) = \mathcal{O}(|E| \log{|E|})$

Totale (con Liste concatenate con wenghted union):
$\mathcal{O}(|E| \log{|E|}) + \mathcal{O}(|E| + |V|\cdot \log{|V|}) = \mathcal{O}(|E| \log{|E|})$

Dato che $|E| \leq {|V|}^2$
$\mathcal{O}(|E| \log{|V|^2}) = \mathcal{O}(|E|\log{|V|})$ 
Questo peché il costo viene assorbito dall'ordinamento degli archi

**Correttezza segue dal corollario.**
