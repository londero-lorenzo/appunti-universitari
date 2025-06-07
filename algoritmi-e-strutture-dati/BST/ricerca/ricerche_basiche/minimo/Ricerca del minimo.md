---
title: "Ricerca del Minimo"
aliases: ["Ricerca del Minimo"]
tags: [università, "algoritmi-e-strutture-dati", "BST", "ricerca", "ricerche-basiche", "minimo", "Ricerca del minimo"]
created: 2025-06-04
---
```
BSTSearchMin(T){
	x <- T.root
	while(x.left != NIL){
		x <- x.left
	}
	return x
}
```

### Vedi anche:
- [[BST/ricerca/ricerche_basiche/Costo|Costo ricerche basiche]]