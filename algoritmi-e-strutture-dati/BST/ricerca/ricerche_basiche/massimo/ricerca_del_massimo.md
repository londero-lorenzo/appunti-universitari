---
title: "Ricerca del Massimo"
aliases: ["Ricerca del Massimo"]
tags: [università, "algoritmi-e-strutture-dati", "BST", "ricerca", "ricerche-basiche", "massimo", "ricerca-del-massimo"]
created: 2025-06-04
---
```
BSTSearchMax(T){
	x <- T.root
	while(x.right != NIL){
		x <- x.right
	}
	return x
}
```

### Vedi anche:
- [[BST/ricerca/ricerche_basiche/Costo|Costo ricerche basiche]]