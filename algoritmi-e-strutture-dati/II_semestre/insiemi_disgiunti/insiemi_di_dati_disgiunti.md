---
title: "Insiemi di Dati Disgiunti"
aliases: ["Insiemi di Dati Disgiunti"]
tags: [università, "algoritmi-e-strutture-dati", "II-semestre", "insiemi-disgiunti", "insiemi-di-dati-disgiunti"]
created: 2025-06-13
---
Abbiamo un insieme `S`

$S = \{S_1, ..., S_m\}$
$S_i$ insieme di oggetti
$S_i = \{x_{i1}, x_{i2}, ..., x_{ij_i}\}$
caratteristiche:
$S_i \cap S_j = \emptyset$ se $i \neq j$ 
$S_i \neq \emptyset$

## Operazioni possibili:
- `MAKE(x)` costruire $\{x\}$
- `FIND(x)` restituire $S_i \quad\text{t.c.}\quad x\notin S_i$
- `UNION(x, y)` se $x\in S_i$ e $y \in S_j$ con $i \neq j$ sostituire $S_i$ e $S_j$ con $S_i \cup S_j$


![[algoritmi-e-strutture-dati/II_semestre/insiemi_disgiunti/insiemi_di_dati_disgiunti_schema.md#^frame=cjpapDzUHvnO6ACaTXfvV|100%]]


---

### Esempio
$G = (V, E)$
Componenti connesse
![[algoritmi-e-strutture-dati/II_semestre/insiemi_disgiunti/insiemi_di_dati_disgiunti_schema.md#^frame=4DCd30JoZ4PwYChoFEUby|70%]]

Costruisco $\{x\}$ per ogni $x \in V$
per ogni $\{x, y\}\in E$ faccio `Union(x,y)`
Alla fine ho un insieme di nodi per ogni componente connessa.

Faccio:
- $\Theta(|V|)$ `MAKE`
- $\mathcal{O}(|E|)$ `UNION` e `FIND` (_Big-O, perché potrei aver già unito quei nodi in modo diretto)

Il costo effettivo dipende da come saranno implementati gli insiemi disgiunti

Nota:
> _Analizzeremo il costo di `m` operazione complessive (`MAKE`, `UNION`, `FIND`) di cui `n` operazioni `MAKE`_

Esempio:
$m = n + u + f \quad\quad m\geq n;\quad u\leq n-1$


---

## Implementazioni

- Liste concatenate
- Alberi
## Ottimizzazioni
- Weighted Union
- Union by Rank

## Applicazione
- Minimum Spanning Tree

---