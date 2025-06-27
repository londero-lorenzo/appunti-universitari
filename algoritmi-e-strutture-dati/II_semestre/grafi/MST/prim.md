---
title: Prim
aliases:
  - Prim
tags:
  - MST
  - prim
  - grafi
created: 2025-06-15
---
Voglio sfruttare [IL TEOREMA (video lezione 19 maggio 2021; ora 1:10:30)](https://uniudamce.sharepoint.com/sites/117802-ALGORITMIESTRUTTUREDATIELABORATORIO/_layouts/15/stream.aspx?id=%2Fsites%2F117802%2DALGORITMIESTRUTTUREDATIELABORATORIO%2FDocumenti%20condivisi%2FGeneral%2FRecordings%2FASD%20lezione%2050%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E294ce901%2Db18c%2D4a20%2D9ec8%2Db36760bf3f74)

# Idea
crea un albero partendo da un nodo che diventerà la radice e si espanderà
parto da un nodo e faccio cresce $A$ inglobando archi di attraversamento

Quali strutture dati usiamo?
In ogni istante devo valutare rapidamente:
- quali archi attraverseranno $A$
- quale è di peso minimo

Idea:
per ogni nodo $v$ in ogni istante memorizzo quale è l'arco di peso minimo che lo connette ad $A$

```c
PRIM(G = (V, E, W), s){
	for (each v in V){
		PI[v] = NIL
		key[v] = inf
	}
	key[s] = 0
	Q = V
	BuildMinHeap(Q, W)
	while (Q != []){
		u = ExtractMin(Q) // attenzione, questo modifica la heap, l'ultima                                   // posizione diventa la PRIMA
		for (each v in Adj[u]){
			if (v in Q && key[v]>W({u, v})){
				key[v] = W({u, v})
				PI[v] = u
				DecreaseKey(Q, v)
			}
		}
	}
}
```


il MST è memorizzato in PI

il nodo che nel dato istante viene aggiunto è $\{\Pi[u], u\}$

---

## Costo
inizializzazione +inizializzazione min heap + ciclo while-> viene eseguito per v volte + estrazione(logn) + descresekey (logn) * quanti sono i nodi adiacenti
$\Theta(|V|) + \Theta(|V|) + \displaystyle\sum_{u\in V}{(\mathcal{O}(\log{|V|})} + \mathcal{O}(|Adj[u]|)\cdot\mathcal{O}(\log{|V|})) = \Theta(|V|) + \mathcal{O}(|E|\log|V|) = \mathcal{O}(|E|\log{|V|})$

