---
title: Altezza
aliases:
  - Altezza
tags:
  - BST
  - altezza
created: 2025-06-08
---
## Altezza di un albero binario di ricerca (BST)

Sia `T` un [[albero_binario_di_ricerca|Albero Binario di Ricerca]] con `n` nodi (chiavi).

- L’**altezza** `h` di `T` è definita come il numero massimo di archi nel cammino dalla radice a una foglia più distante.
    
- Nel **caso ideale**, quando l’albero è bilanciato, l’altezza è proporzionale a `log₂(n)`.  
    Questo significa che la profondità media delle operazioni (inserimento, ricerca, cancellazione) è `O(log n)`.
    
- Nel **caso peggiore**, se l’albero è fortemente sbilanciato (ad esempio, una struttura simile a una lista collegata), l’altezza può diventare `h = n`, con conseguente complessità `O(n)` per le operazioni.