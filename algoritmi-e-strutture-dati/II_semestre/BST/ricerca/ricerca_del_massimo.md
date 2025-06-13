---
title: Ricerca del Massimo
aliases:
  - Ricerca del Massimo
tags:
  - BST
  - ricerca
  - ricerca-del-massimo
created: 2025-06-04
---
## Pseudocodice

```c
SearchMaxBST(T){
	x <- T.root
	while(x.right != NIL){
		x <- x.right
	}
	return x
}
```


---
## Complessità
La procedura [[#Pseudocodice|SearchMaxBST]] ha complessità O(h), dove h è l’[[altezza]] dell’albero `T`.