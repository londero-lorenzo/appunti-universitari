---
title: "Dag"
aliases: ["Dag"]
tags: [università, "algoritmi-e-strutture-dati", "II-semestre", "grafi", "dag"]
created: 2025-06-15
---


# Grafi Orientati Aciclici

simi ad alberi ma ad uno stesso modo posso arrivare con cammini diversi
> grafo orientato aciclico

Sono "stratificati"

## Topological Sort
**Definizione:**
>ordinamento dei nodi di un DAG t.c. se $(u, v) \in E$ allora nell'ordinamento il nodo $u$ viene prima del nodo $v$

Un Topological Sort è un qualsiasi ordinamento dei nodi di un dag che soddisfa questa richiesta

Esempio:
![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=sUroNSfu_7Vsx-uJe_v7P]]
In questo esempio $a<b<c<d$ è un Topological Sort?
No perché $(d, a) \not\implies d < a$ 

Esempi di Topological Sort:
1. $d < a < c$
2. $d < b < c$


Ogni grafo aciclico ha almeno un nodo senza archi uscenti e almeno un nodo senza archi entranti.

---

### Costruzione di un Topological Sort in grafi orientati aciclici

Prima procedura con cancellazione dell'ultimo nodo nel topological sort

Seconda procedura utilizzando [[DFS]] con l'aggiunta di una lista per aggiungere in testa gli ultimi nodi neri.

---

### Posso creare un Topological sort in grafi orientati ciclici?
Raggruppando i nodi nei cicli ottengo dei cluster di nodi i quali formano un DAG
Esempio
![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=g3y089tOqPa4ogKaayXMQ|100%]]

Come determino:
- i cluster?
- il DAG?
 
---

