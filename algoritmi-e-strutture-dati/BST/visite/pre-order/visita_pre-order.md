---
title: "Visita Pre-Order"
aliases: ["Visita Pre-Order"]
tags: [università, "algoritmi-e-strutture-dati", "BST", "visite", "pre-order", "visita-pre-order"]
created: 2025-06-04
---
La [[visita_pre-order]] attraversa i nodi di un [[albero_binario_di_ricerca]] in ordine decrescente.

```
PreOrder(x){
	if(x != NIL){
		Print(x.key)
		PreOrder(x.left)
		PreOrder(x.right)
	}
}

PreOrder(T.root)
```

### Vedi anche
* [[algoritmi-e-strutture-dati/BST/visite/pre-order/correttezza|Correttezza Pre-Order]]
- [[algoritmi-e-strutture-dati/BST/visite/pre-order/costo|Costo Pre-Order]]