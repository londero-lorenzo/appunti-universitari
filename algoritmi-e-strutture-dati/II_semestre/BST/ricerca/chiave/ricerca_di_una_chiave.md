---
title: Ricerca di Una Chiave
aliases:
  - Ricerca di Una Chiave
tags:
  - BST
  - ricerca
  - chiave
  - ricerca-di-una-chiave
created: 2025-06-04
---
# Ricerca in Albero Binario di Ricerca (BST)

Dato un [[albero_binario_di_ricerca|Albero Binario di Ricerca]] `T` e una chiave `k`, si vuole determinare se esiste un nodo `x` in `T` tale che `x.key = k`.

## Descrizione

La **ricerca** sfrutta la [[algoritmi-e-strutture-dati/II_semestre/BST/definizione|proprietà fondamentale]] del BST:

> Per ogni nodo `x`, tutte le chiavi nel sottoalbero sinistro sono minori di `x.key`, tutte quelle nel sottoalbero destro sono maggiori.

---

## Pseudocodice

```c
BSTSearch(T, k){
    return BSTSearchNode(T.root, k)
}

BSTSearchNode(x, k){
    if (x == NIL || x.key == k){
        return x
    } else if (k < x.key){
        return BSTSearchNode(x.left, k)
    } else {
        return BSTSearchNode(x.right, k)
    }
}
```

## Note

- L’algoritmo è **ricorsivo**, ma può essere riscritto in versione **iterativa** per ridurre il consumo di memoria (stack).
    
- In caso di successo, restituisce il **puntatore al nodo** contenente la chiave `k`.
    
- In caso contrario, restituisce `NIL`.

---
### Complessità
Questa proprietà permette di eseguire la ricerca in tempo proporzionale all'altezza dell'albero `h`:

- `O(h)` nel caso generale
- `O(log n)` se l'albero è bilanciato