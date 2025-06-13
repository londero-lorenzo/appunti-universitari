---
title: Rotazione
aliases:
  - Rotazione
tags:
  - BST
  - modifiche
  - rotazione
created: 2025-06-09
---
## Rotazioni negli Alberi Binari Di Ricerca

Le rotazioni modificano la struttura locale di un albero **[[albero_binario_di_ricerca]]**, preservandone l’invariante d’ordine.

### Proposizione

> Se `T` è un [[albero_binario_di_ricerca|BST]], allora dopo `LEFT-ROTATE(T, x)` oppure `RIGHT-ROTATE(T, x)`, l’albero risultante è ancora un BST.
## Pseudocodici
### LEFT-ROTATE
```c
LEFT-ROTATE(T, x):
    y ← x.right                          // y è il figlio destro di x
    x.right ← y.left                     // il sottoalbero sinistro di y diventa il destro di x

    if y.left ≠ T.nil then              // se esiste un sottoalbero sinistro di y
        y.left.parent ← x                // allora x diventa il suo genitore

    y.parent ← x.parent                 // il genitore di y diventa il genitore di x

    if x.parent = T.nil then            // se x era la radice
        T.root ← y                       // y diventa la nuova radice
    else if x = x.parent.left then      // se x era figlio sinistro
        x.parent.left ← y
    else
        x.parent.right ← y              // altrimenti x era figlio destro

    y.left ← x                          // x diventa figlio sinistro di y
    x.parent ← y
```


### RIGHT-ROTATE
```c
RIGHT-ROTATE(T, x):
    y ← x.left                           // y è il figlio sinistro di x
    x.left ← y.right                     // il sottoalbero destro di y diventa il sinistro di x

    if y.right ≠ T.nil then             // se esiste un sottoalbero destro di y
        y.right.parent ← x              // allora x diventa il suo genitore

    y.parent ← x.parent                 // il genitore di y diventa il genitore di x

    if x.parent = T.nil then            // se x era la radice
        T.root ← y
    else if x = x.parent.right then     // se x era figlio destro
        x.parent.right ← y
    else
        x.parent.left ← y               // altrimenti x era figlio sinistro

    y.right ← x                         // x diventa figlio destro di y
    x.parent ← y

```
### Complessità

| Operazione   | Costo | Motivo                               |
| ------------ | ----- | ------------------------------------ |
| LEFT-ROTATE  | Θ(1)  | Massimo 7 aggiornamenti di puntatori |
| RIGHT-ROTATE | Θ(1)  | Simmetrica, stesso costo             |

Le rotazioni sono operazioni **costanti**, fondamentali per mantenere l’albero bilanciato con efficienza logaritmica globale.

![[red_black_tree_schema#^frame=x6mii0dMO9lwJgxwroBbB|100%]]


Esempio LeftRotate:
![[red_black_tree_schema#^frame=79QhkgoQAaOoYcTP5DnqU|100%]]

