---
title: "Sssp"
aliases: ["Sssp"]
tags: [università, "algoritmi-e-strutture-dati", "II-semestre", "cammini-minimi", "sssp"]
created: 2025-06-15
---
# Single Source Shortest Paths
Fissato $s$ determinare $\forall v \in V$ un cammino di peso minimo da $s$ a $v$


Se tutti gli archi hanno lo stesso peso, il problema si trasforma nel determinare il cammino minimo.
> Il peso del cammino è uguale alla lunghezza

---

Domanda: _Che differenza c'è tra MST e SSSP?_
> Uno cerca di connettere tutti i nodi utilizzando i pesi minimi, l'altro determina i cammini di peso minimo.
> Esempio:
> ![[peso_di_un_cammino_schema#^frame=XQs-T_D6J0GHHV9sKCtP_]]


Ricicliamo l'algoritmo di `PRIM`

```c
DIJKTRA(G = (V, E, W), s){
	for (each v in V){
		PI[v] = NIL
		d[v] = inf
	}
	d[s] = 0
	Q = V
	BuildMinHeap(Q, key)
	while (Q != []){
		u = ExtractMin(Q) // attenzione, questo modifica la heap, l'ultima                                   // posizione diventa la PRIMA
		for (each v in Adj[u]){
			if (v in Q && d[v]>d[u] + W({u, v})){
				d[v] = d[u] + W({u, v})
				PI[v] = u
				DecreaseKey(Q, v)
			}
		}
	}
}
```

![[peso_di_un_cammino_schema#^frame=lBYhIYazhgB7pOeLJIHP_|100%]]
Quindi devo controllare che il peso vecchia sia maggiore di questo appena trovato, se lo è allora cambio.


