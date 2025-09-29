---
title: Inserimento
aliases:
  - Inserimento
tags:
  - RBT
  - modifiche
  - inserimento
created: 2025-06-09
---
# Inserimento in Red-Black Tree

Dato un albero [[red_black_tree|Red Black Tree]] `T` contenente `n` chiavi, e un nuovo nodo `x` con chiave `k`, si vuole **inserire** `x` in `T`.

---

## 🧠 Idea generale

- Si esegue **[[algoritmi-e-strutture-dati/II_semestre/BST/modifiche/Inserimento|inserimento standard da BST]]**: il nodo `x` viene inserito con due figli `NIL`.
- Si colora `x` di **rosso**.
- Se `x` ha un padre anch'esso rosso, la proprietà dei RBT viene violata.
- Il problema viene **risolto ricorsivamente salendo** verso la radice con rotazioni e/o ricolorazioni.

> In ogni istante o si risolvere il problema _`RED` figlio di `RED`_ o lo si sposta verso l'alto.
![[red_black_tree_schema#^frame=yU7gsk4ZCxI1W9g01cTYS|75%]]
### Esempio di inserimento
![[red_black_tree_schema#^frame=3swyF2lIDqCFRh4HVSaQq|100%]]


---

## Come si risolve il problema?
Spostando i nodi da un sottoalbero al fratello:
![[red_black_tree_schema#^frame=KfPaL02tUmdtp4uZRazEO|75%]]
### Risoluzione delle violazioni

> Quando il nodo `x` `RED` ha un padre `RED`, serve **"aiuto dello zio"** per mantenere le proprietà.

#### 🍀 Caso 1 — _Fortunato_
Sono fortunato se il "nonno" di `x` è `BLACK` e ha un figlio (_lo zio_) `BLACK`, (due nodi `BLACK` consecutivi, nel sottoalbero con più nodi) ^018bf9

Effettuo rotazioni verso lo zio, ricoloro:
##### Esempio
![[red_black_tree_schema#^frame=pCu2TTX5vXESOLFiw9TsD|100%]]
##### 📎 Controllo altezze nere
![[red_black_tree_schema#^frame=uQcg3IBRfoBaBv3D1loIF|100%]]


---
#### 😐 Caso 2 — _Quasi Fortunato_
Sono quasi fortunato se lo zio di `x` è `BLACK`ma dallo stesso lato di `x`.
Effettuo una rotazione opposta alla posizione dello zio di `x` e poi applico [[#^018bf9|Caso Fortunato]].
##### Esempio
![[red_black_tree_schema#^frame=XixrMuWdAL_A7gwUw9j6b|100%]]

---
#### 😣 Caso 3 — _Sfortunato_
Sono sfortunato se lo zio di `x` è `RED`.
Effettuo una ricolorazione del genitore, del nonno e dello zio di `x` e sposto il problema più in alto
##### Esempio
![[red_black_tree_schema#^frame=7dBTNNdjsR7CXbHg1XqWu|100%]]

---
## Pseudocodice

```c
RB-INSERT(T, z){
    x ← T.root
    y ← T.nil     // sentinella
    
    while x ≠ T.nil {
        y ← x
        if z.key < x.key
            x ← x.left
        else
            x ← x.right
    }
    
    z.parent ← y
    
    if y = T.nil
        T.root ← z        // l’albero era vuoto
    else if z.key < y.key
        y.left ← z
    else
        y.right ← z
    
    z.left ← T.nil
    z.right ← T.nil
    z.color ← RED
    
    RB-INSERT-FIXUP(T, z)
}

RB-INSERT-FIXUP(T, x){
    while (x.parent.color = RED){
        if x.parent = x.parent.parent.left       // x è figlio sinistro
            z ← x.parent.parent.right            // z è lo zio di x
            if z.color = RED                     // Caso 3
                x.parent.color ← BLACK
                z.color ← BLACK
                x.parent.parent.color ← RED
                x ← x.parent.parent
            else
                if x = x.parent.right            // Caso 2
                    x ← x.parent
                    LEFT-ROTATE(T, x)
                x.parent.color ← BLACK           // Caso 1
                x.parent.parent.color ← RED
                RIGHT-ROTATE(T, x.parent.parent)
        else                                     // x è figlio destro (simmetrico)
            z ← x.parent.parent.left
            if z.color = RED                     // Caso 3
                x.parent.color ← BLACK
                z.color ← BLACK
                x.parent.parent.color ← RED
                x ← x.parent.parent
            else
                if x = x.parent.left             // Caso 2
                    x ← x.parent
                    RIGHT-ROTATE(T, x)
                x.parent.color ← BLACK           // Caso 1
                x.parent.parent.color ← RED
                LEFT-ROTATE(T, x.parent.parent)
	}
    T.root.color ← BLACK
}
```

---
## Costo computazionale

- **Fase di discesa:** $\Theta(\log n)$ per trovare la posizione.
    
- **Fase di risalita (fix-up):** massimo $\Theta(\log n)$ rotazioni o ricolorazioni.
    

 Complessivamente: $\Theta(\log n)$

> Le proprietà fondamentali dei RBT vengono sempre mantenute dopo `RB-INSERT-FIXUP`.


---

## Esempio
![[red_black_tree_schema#^frame=R0xbObPNQS-SoEXvc4iPe|100%]]

