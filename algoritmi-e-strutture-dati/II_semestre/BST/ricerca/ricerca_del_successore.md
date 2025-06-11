---
title: Ricerca del Successore
aliases:
  - Ricerca del Successore
tags:
  - BST
  - ricerca
  - ricerca-del-successore
created: 2025-06-08
---
Dato un nodo `x` in un [[albero_binario_di_ricerca|Albero Binario di Ricerca]], il **successore** di `x` è il nodo con la chiave minima maggiore di `x.key`.

### Strategia

- Se `x` ha un sottoalbero destro, il successore è il nodo con la chiave minima in quel sottoalbero (cioè il minimo del sottoalbero destro).
    
- Se `x` non ha un sottoalbero destro, il successore è il primo antenato `y` di `x` per cui `x` è nel sottoalbero sinistro di `y`.

---
### Pseudocodice

```
TREE-SUCCESSOR(x){
	if(x.right != NIL){
		return BSTSearchMin(x.right)
	}else{
		y <- x.parent
		while(y != NIL && x = y.right){
			x <- y
			y <- x.parent
		}
		return y
	}
}
```

#### Spiegazione passo passo

- Se `x` ha un figlio destro, cerco il minimo di quel sottoalbero (funzione [[ricerca_del_minimo#Pseudocodice|SearchMinBST]]), ovvero scendo sempre a sinistra finché possibile.
	
- Altrimenti, risalgo verso i genitori:
    
    - Finché `x` è figlio destro di `y`, continuo a risalire (cioè `x` e `y` si spostano verso l’alto).
        
    - Quando incontro un nodo `y` per cui `x` è figlio sinistro, `y` è il successore di `x`.
        
- Se nessun antenato soddisfa questa condizione, allora `x` non ha successore (esempio: è il nodo con chiave massima).

---
## Complessità
La procedura [[#Pseudocodice|TREE-SUCCESSOR]] ha complessità O(h), dove h è l’[[altezza]] dell’albero `T`.