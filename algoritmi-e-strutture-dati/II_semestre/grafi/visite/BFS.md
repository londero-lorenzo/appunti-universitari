---
title: BFS
aliases:
  - BFS
tags:
  - grafi
  - visite
  - BFS
created: 2025-06-14
---
# Visita Breadth-First Search (_in ampiezza_)


## Idea
Scandire tutti i nodi di $G$
Procedendo a distanza crescente da s (_nodo_)
- distanza: numero di archi su un cammino minimo

Non devo visitare più volte lo stesso nodo

Devo tenere traccia di ciò che ho scoperto e di ciò che ho già visitato.
> _Con visitato si intende che di quel nodo ho già scandito la sua lista di Adiacenza_

Esempio con i relativi problemi
![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=80zi7fDowvx2zE90y-n59|100%]]

Per tenere traccia di ciò che ho già scoperto coloro i nodi:
- Bianco (nodo non scoperto scoperto)
- Grigio (nodo scoperto)
- Nero (nodo la cui lista di adiacenza è scandita)

Esempio:
![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=gaRtbOiR3LrTKWURVrdCQ|100%]]


---

### Come memorizzare colori, albero di visita distanze?

- colore vettore di lunghezza $|V|$
	- `color[i]`, indica il colore del nodo `i`
- `d` vettore di lunghezza $|V|$
	- `d[i]` alla fine della visita contiene la distanza da `i` a `s`
	- distanza: numero di archi cammino più corto da `s` a `i`
- $\Pi$ vettore di lunghezza $|V|$
	- vettore dei predecessori di lunghezza minima


---


## BFS
```c
BFS(G, s){
	for (each u in V){
		color[u] = B
		d[u] = inf
		pi[u] = NIL
	}
	Q = []
	color[s] = G
	d[s] = 0
	Enqueue(Q, s)
	while(Q != []){
		u = Q.peek()
		for (each v in Adj[u]){
			if (color[v] == B){
				color[v] = G
				d[v] = d[u] + 1
				pi[v] = u
				Enqueue(Q, v)
			}
		}
		color[u] = N
		Dequeue(Q)
	}
}
```


---

## Problema del BFS
Non è garantito che tutti i nodi vengano visitati, vengono scoperti solo i nodi raggiungibili da `s`
Esempio
![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=sqwQitc9flaUlKUm_Uc9d|100%]]


---

## Complessità

Domanda: _Quante volte passo per il `while`?_
$\mathcal{O}(|V|)$

Domanda: _Quante volte passo per il `for`?_
$\mathcal{O}(|V|)$


Risultato, sovradimensionato: $\mathcal{O}({|V|}^2)$

---

## Analisi con le matrici e liste di adiacenza

Con matrici: $\mathcal{O}({|V|}^2)$

Con liste: $\mathcal{O}(|V| + |E|)$

#TODO aggiungere descrizioni aggiuntive per i costi e aggiungere dimostrazioni. [Video lezione (23 aprile 2021, minuto 13:20)](https://uniudamce.sharepoint.com/sites/117802-ALGORITMIESTRUTTUREDATIELABORATORIO/_layouts/15/stream.aspx?id=%2Fsites%2F117802%2DALGORITMIESTRUTTUREDATIELABORATORIO%2FDocumenti%20condivisi%2FGeneral%2FRecordings%2FASD%20lezione%2042%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E356eff62%2D34d3%2D4333%2D9738%2D7168a0fb7cb5)



---

Al termine di `BFS(G, s)` $d[v] \geq \delta(s,v)$

devo dimostrare che `d[v]` rappresenti la distanza di un cammino minimo

Per farlo devo dimostrare alcune proprietà della coda `Q` durante BFS.

### Proprietà
Durante l'esecuzione di BFS(G, s) se $Q=[u_1, u_2, ..., u_k]$
- $u_1, ..., u_k$ sono Grigi
- $pi[u_i] = NIL$ se $u_i \neq s$
- $d[u_1]\leq d[u_2]\leq ... \leq d[u_k]\leq d[u_1]+1$


![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=5wycVQqpkc4qM3EQfKB9t|100%]]


---

#### Dimostrazione
#TODO [Video lezione (23 aprile 2021, minuto 53:30)](https://uniudamce.sharepoint.com/sites/117802-ALGORITMIESTRUTTUREDATIELABORATORIO/_layouts/15/stream.aspx?id=%2Fsites%2F117802%2DALGORITMIESTRUTTUREDATIELABORATORIO%2FDocumenti%20condivisi%2FGeneral%2FRecordings%2FASD%20lezione%2042%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E356eff62%2D34d3%2D4333%2D9738%2D7168a0fb7cb5)



---

## BFS-tree

$G = (V, E)$ con $s\in V$

al termine della visita BFS ottengo:

$G_\Pi = (V_\Pi, E_\Pi)$  con:
- $V_\Pi = \{v\quad| \text{ al termine di } BFS(G, 1)\quad color[v] = Nero\}$
	> Questo funziona perché alla fine non mi resta nulla nella coda
- $E_\Pi = \{\quad(\Pi[v], v)\quad|\quad v\in V_\Pi\textbackslash\{s\}\}$


---

> _calcolare il percorso minimo tra `s` e `t` equivale a fare tutta la visita di `G`, questo perché non sappiamo in che direzione andare_