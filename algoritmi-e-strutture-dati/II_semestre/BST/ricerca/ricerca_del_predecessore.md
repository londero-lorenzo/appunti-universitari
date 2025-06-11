---
title: Ricerca del Predecessore
aliases:
  - Ricerca del Predecessore
tags:
  - BST
  - ricerca
  - ricerca-del-predecessore
created: 2025-06-08
---
Dato un nodo `x` in un albero binario di ricerca, il **predecessore** di `x` è il nodo con la chiave massima minore di `x.key`.

### Strategia

- Se `x` ha un sottoalbero sinistro, il predecessore è il nodo con la chiave massima in quel sottoalbero (cioè il massimo del sottoalbero sinistro).
    
- Se `x` non ha un sottoalbero sinistro, il predecessore è il primo antenato `y` di `x` per cui `x` è nel sottoalbero destro di `y`.  

---
### Pseudocodice

```
TREE-PREDECESSOR(x){
	if(x.left != NIL){
		return BSTSearchMax(x.left)
	}else{
		y <- x.parent
		while(y != NIL && x = y.left){
			x <- y
			y <- x.parent
		}
		return y
	}
}
```

### Spiegazione passo passo

- Se `x` ha un figlio sinistro, cerco il massimo di quel sottoalbero (funzione [[ricerca_del_massimo#Pseudocodice|SearchMaxBST]]), ovvero scendo sempre a destra finché possibile.
    
- Altrimenti, risalgo verso i genitori:
    
    - Finché `x` è figlio sinistro di `y`, continuo a risalire (cioè `x` e `y` si spostano verso l’alto).
        
    - Quando incontro un nodo `y` per cui `x` è figlio destro, `y` è il predecessore di `x`.
        
- Se nessun antenato soddisfa questa condizione, allora `x` non ha predecessore (esempio: è il nodo con chiave minima).

---
## Complessità
La procedura [[#Pseudocodice|TREE-PREDECESSOR]] ha complessità O(h), dove h è l’[[altezza]] dell’albero `T`.