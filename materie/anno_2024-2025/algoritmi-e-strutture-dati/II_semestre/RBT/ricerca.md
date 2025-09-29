---
title: Ricerca
aliases:
  - Ricerca
tags:
  - RBT
  - ricerca
created: 2025-06-09
---
# Ricerca in un Red-Black Tree 🔍

Dato un albero `T` di tipo [[red_black_tree|Red-Black Tree]] contenente `n` chiavi, e un intero `k`, si vuole cercare `k` in `T`.

## 📌 Metodo

La [[ricerca_di_una_chiave|procedura]] è **identica** a quella utilizzata nei [[ricerca_di_una_chiave|BST]]:  
si confronta `k` con la chiave del nodo corrente e si decide se scendere a sinistra o a destra, ricorsivamente o iterativamente.

## ⏱️ Complessità

- In un generico **BST**, il tempo di ricerca è $\mathcal{O}(h)$, dove `h` è l'altezza dell'albero.
    
- In un **Red-Black Tree**, grazie al bilanciamento garantito, vale:
    

$$
h = \Theta(\log n)
$$

Quindi:
$$
\text{Tempo di ricerca} = \mathcal{O}(\log n)
$$
## 🧠 Osservazioni

- Il bilanciamento dei RBT assicura che non esistano rami degenerati (es. linee verticali).
    
- Le operazioni di inserimento/cancellazione mantengono il bilanciamento, quindi **le ricerche rimangono efficienti nel tempo**.