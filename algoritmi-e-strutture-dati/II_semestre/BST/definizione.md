---
title: Definizione
aliases:
  - Definizione
tags:
  - BST
  - definizione
created: 2025-06-07
---
# Definizione
Un albero binario di ricerca è un albero binario in cui ogni nodo ha una chiave intera tale che $\forall x \in T(\forall\ y \in x.left\ y.key<x.key\ \wedge\ \forall\ y \in x.right\ y.key>x.key)$

Quindi, un Albero Binario di Ricerca (BST) garantisce che, per ogni nodo `x`:

- tutte le chiavi nel sottoalbero sinistro sono **minori** di `x.key`
- tutte le chiavi nel sottoalbero destro sono **maggiori** di `x.key`

---
## Implicazioni

- Una visita **in-order** produce le chiavi in **ordine crescente**
- Le operazioni di **ricerca, inserimento e cancellazione** sfruttano questa proprietà per eseguire confronti e scegliere quale ramo esplorare
- Se l’albero è bilanciato, si ottiene:
  - **Ricerca, Inserimento, Cancellazione** in tempo `O(log n)`
- Se è degenerato (es. simile a una lista), i tempi peggiorano a `O(n)`

## Vedi anche

- [[visita_in-order|Visita In-Order]]
- [[ricerca_di_una_chiave|Ricerca di Una Chiave]]