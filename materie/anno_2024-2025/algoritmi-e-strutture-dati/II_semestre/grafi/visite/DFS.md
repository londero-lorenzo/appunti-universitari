---
title: Dfs
aliases:
  - Dfs
tags:
  - grafi
  - visite
  - DFS
created: 2025-06-14
---
# Visita Depth-First Search (_in ampiezza_)


Percorro un cammino fino a quando mi permette di trovare qualcosa di nuovo, faccio backtracking quando necessario.

Strutture dati usate:
- Colori
- la visita riparte se sono rimasti nodi bianchi
- $\Pi$ albero di visita DFS
- tempi inizio e fine visita

Esempio:
![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=7lx48Ebgosev-KdUaEQ2K|100%]]

>Utilizzeremo delle pile ricorsive.


## DFS
```c
DFS(G){
	for (each v in V){
		color[v] = B
		pi[v] = NIL
	}
	TIME = 1
	for (each v in V){
		if (color[v] == B){
			TIME = DFS_visit(G, v, TIME)
		}
	}
}
```


### DFS_visit
```c
DFS_visit(G, v, TIME){
	color[v] = G
	i[v] = TIME
	TIME = TIME + 1
	for (each u in Adj[v]){
		if (color[u] == B){
			pi[u] = v // ho scoperto u tramite v
			TIME = DFS_visit(G, u, TIME)
		}
	}
	f[v] = TIME
	TIME = TIME + 1
	color[v] = N
	return TIME
}
```

---

## Complessità
devo ragionare complessivamente su tutto il grafo.
Se tengo conto del numero di visite su ogni nodo, ogni nodo passerà da un colore bianco a uno non bianco. Dato che il for principale itererà su tutti i nodo, alla fine tutti i nodi avranno cambiato colore.

for iniziale + operazioni $\Theta(1)$ + i for interni a dfs sui vertici adiacenti:
$$
\Theta(|v|) + \Theta(|V|) + \Theta(\sum_{v\in V}|Adj[v]|)
$$

### Liste
for iniziale + operazioni $\Theta(1)$ + scansione della lista di adiacenza ($\Theta(|V|)$):
$$
\Theta(|V|) + \Theta(\sum_{v\in V}|L_G[v]|) = \Theta(|V| + |E|)
$$


### Matrici
for iniziale + operazioni $\Theta(1)$ + la scansione di una riga ($\Theta(|V|)$)
$$
\Theta(|V|) + \Theta(\sum_{v\in V}|V|)= \Theta({|V|}^2)
$$



## Come sarà fatto $\Pi$ alla fine della visita?

I nodi i cui $\Pi$ è `NIL`  alla fine della visita `DFS` rappresentano i nodi la cui chiamata la è partita dalla procedura principale.

I `NIL` alla fine rappresentano i nodi sui quali DFS_visit è stata richiamata da DFS.


Alla fine della procedura $\Pi$ rappresenta una foresta di alberi:

![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=OhnJyOfzBA8dRMbgZBl63|100%]]

Nel caso di Grafi non orientati ho un unico albero di visita se e solo se G è connesso.

---

## Analisi di time

Analizzando i tempi di inizio e fine visita

![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=E4-cKaobpfoQwNgF9J-to|100%]]

### Teorema delle parentesi

Per ogni $a,b \in V$:
$$
[i[a], f[a]] \cap [i[b], f[b]] = \emptyset
$$ oppure
$$
[i[a], f[a]] \subseteq [i[b], f[b]]
$$
oppure
$$
[i[b], f[b]] \subseteq [i[a], f[a]]
$$

Domanda: _Quali sono nella foresta di alberi DFS i discendenti di un nodo `v`?_

![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=1TMZHrfq6DmmKDcus0JCj|100%]]

#### Teorema
$u$ è discendente di $v$ nella foresta `DFS` se e solo se $[i[u], f[u]] \subseteq [i[v], f[v]]$

---

Domanda: _Quali sono nella foresta di alberi DFS i discendenti di un nodo `v` usando i colori?_

Dobbiamo guardare i colori durante l'esecuzione della visita in quanto alla fine della DFS tutti i nodi avranno colore nero.

Supponiamo di trovarci all'istante `i[v]`, in questo istante `v` è grigio. E' presente un nodo `B` che è bianco e raggiungibile da `v` attraversi altri nodi.

![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=sV_w586cjC1oCsD8V9zq7|100%]]

B diventerà sicuramente successore di `v`?
No, controesempio:
![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=YcacIIPeWTwAdemF1ucGO|100%]]


come possiamo quindi determinare i discendenti di un nodo basandoci solo sul colore?
tramite il Teorema dei cammini bianchi.

### Teorema dei cammini bianchi

>Un nodo `u` sarà discendente di `v` se e solo se esiste un cammino di nodi bianchi da `v` ad `a` nel tempo `i[v]`
>Esempio:
>![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=nKoP54HkEFEQT8U42p07z|100%]]


#TODO completare con i vari tipo di archi. [Video lezione 30 aprile 2021; minuto 00:00](https://uniudamce.sharepoint.com/sites/117802-ALGORITMIESTRUTTUREDATIELABORATORIO/_layouts/15/stream.aspx?id=%2Fsites%2F117802%2DALGORITMIESTRUTTUREDATIELABORATORIO%2FDocumenti%20condivisi%2FGeneral%2FRecordings%2FASD%20lezione%2046%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ef24c08ff%2D25ae%2D4221%2Dadd5%2Dde1938c2cc16)