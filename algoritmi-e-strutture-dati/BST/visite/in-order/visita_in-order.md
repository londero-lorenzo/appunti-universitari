---
title: "Visita In-Order"
aliases: ["Visita In-Order"]
tags: [università, "algoritmi-e-strutture-dati", "BST", "visite", "in-order", "visita-in-order"]
created: 2025-06-04
---
La [[visita_in-order]] attraversa i nodi di un [[albero_binario_di_ricerca|Albero binario di ricerca]] in ordine crescente.

```
InOrder(x){
	if(x != NIL){
		InOrder(x.left)
		Print(x.key)
		InOrder(x.right)
	}
}
```

### Vedi anche
* [[algoritmi-e-strutture-dati/BST/visite/in-order/correttezza|Correttezza In-Order]]
- [[algoritmi-e-strutture-dati/BST/visite/in-order/costo|Costo  In-Order]]