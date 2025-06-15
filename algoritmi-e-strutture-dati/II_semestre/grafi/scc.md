---
title: "Scc"
aliases: ["Scc"]
tags: [università, "algoritmi-e-strutture-dati", "II-semestre", "grafi", "scc"]
created: 2025-06-15
---
# Definizione di componente fortemente connessa (strongly connected component)
In $G$ orientato una componente fortemente connessa è un insieme massimale di nodi mutuamente raggiungibili

$C \subseteq V \land \forall u,v \in C \quad \exists u\to v$ 

##### Osservazioni
Le componenti fortemente connesse di un grafo $G$ $$C_1, C_2, C_3, ..., C_m$$ costituiscono una partizione di $v$

$$
C_1\cup C_2\cup C_3, ..., \cup \text{ }C_m = V
$$

$C_i \neq \emptyset$ 
$C_i \cap C_j = \emptyset$ con $i\neq j$


 ---
## Definizione $G_{scc}$

$G_{scc}= (V_{scc}, E_{scc})$
- $V_{scc}$ = $\{C_1, ..., C_m\}$ tutte e sole le s.c.c. di G
- $E_{scc} = {(C_i, C_j) \quad|\quad i\neq j \land \exists u \in C_i, v \in C_j \land (u, v) \in E}$

---

## Osservazione
$G_{scc}$ è sempre un `DAG` $\implies$ su $G_{scc}$ posso usare topological sort

---

## Come calcolare s.c.c su archi orientati

### Idea

Usare `DFS(G)`

che produce questa foresta di visita DFS:
![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=aUHeTBAEiCNmfwxR5j7Iq|100%]]


**Consideriamo $u_3$**
Domanda: _Dove si trovano i nodi della `s.c.c.` di $u_3$?_
> **Devono stare in $T_3$**
> Spiegazione:
> Quando ho iniziato $u_3$ tutti gli altri nodi in  $T_1$ e $T_2$  erano già neri quindi i nodi in $T_1$ e $T_2$ non possono raggiungere $T_3$.
> Se ci fosse stato un nodo $T_1$ che raggiunge $u_3$, significa che ci sarebbe stato un cammino bianco verso $u_3$ da un nodo a partire da $T_1$ e che quindi $u_3$ doveva stare in $T_1$


Domanda: La `s.c.c` di $u_3$ è tutta $T_3$?
> **NO**
> Spiegazione:
> ci possono essere dei `cross edge` verso un altro albero

Domanda: _Che differenze c'è alla fine ella visita tra $u_3$ e gli altri nodi di $T_3$?_
>$\Pi[u_3]=NIL$ 
>$f[u_3] > f[v]\forall v \in T_3$
>$f[u_3] = 2\cdot|V|$

Cosa sappiemo:
- $u_3$ quindi raggiunge i nodi che stanno in $T_3$ 
- tra i nodi di $T_3$ devono trovare quelli che raggiungono $u_3$
	- fare questo calcolo è parecchio costoso, dovrei far partire una `DFS_visit(G, v)`

Soluzione:
un nodo `v` appartenente a $T_3$ fa parte della `s.c.c` sss $u_3$ raggiunge $v$ in $G^{-1}$

---


### Soluzione
Per calcolare $s.c.c.(u_3)$ eseguirò $DFS(G^{-1}, u_3)$

---

Facendo partire una dfs su G, il nodo con tempo di fine visita maggiore (la radice dell'ultimo albero generato da DFS) si trova in una s.c.c senza archi entranti (in $G_{scc}$)

esempio:
![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=2bqpKSkhXzsNKENHzK5o1|100%]]

Domanda: _Cosa succede se parto da $G^{-1}$?_
- $G_{-1}$ ha le stesse s.c.c. di $G$
- la s.c.c. senza archi entranti ora in $G_{-1}$ è una s.c.c senza archi uscenti verso altre s.c.c

Quindi
Se faccio partire $DFS(G^{-1}, x)$ con $x$ nodo della s.c.c senza archi uscenti ottengo -> $T_1$ albero di visita  $DFS(G^{-1}, x)$ è esattamente la s.c.c. di x

x è il nodo che aveva tempo di fine visita massima in DFS(G, x)

Posso iterare nella visita di $G^{-1}$

---

### Ricapitolando 
Procedura:
- Uso una prima $DFS$ su $G$ per capire quali sono le $s.c.c.$ sorgenti in $G$
- Uso una seconda $DFS$ su $G^{-1}$ (in un ciclo for di DFS) procedendo in ordine decrescente rispetto al vettore dei tempi fine visita nella precedente $DFS$
	- Ora ogni albero è una $s.c.c.$ di $G$

### Complessità 
Liste di $Adj$
tempo 1° dfs+ tempo creazione $G^{-1}$ + tempo 2° dfs
$\Theta(|V| + |E|) + \Theta(|V| + |E|) + \Theta(|V| + |E|)$

Quali sono gli archi di $G_{scc}$
Sono gli archi  di attraversamento della seconda visita


---

Esempio
![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=ND0oXtjQMWquXrbiNFFsG|100%]]



---

![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=SatEQU4FPTcURP9GMlyoI|100%]]


---


## Calcolare s.c.c su grafi non orientati
> Basta una dfs, gli alberi di visita sono le componenti fortemente connesse


---

## Calcolare s.c.c su alberi
> ha una sola componente fortemente connessa