---
title: Ricerca del Minimo
aliases:
  - Ricerca del Minimo
tags:
  - BST
  - ricerca
  - ricerca-del-minimo
created: 2025-06-04
---
## Pseudocodice

```c
SearchMinBST(T){
	x <- T.root
	while(x.left != NIL){
		x <- x.left
	}
	return x
}
```


---
## Complessità
La procedura [[#Pseudocodice|SearchMinBST]] ha complessità O(h), dove h è l’[[altezza]] dell’albero `T`.