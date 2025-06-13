---
title: Visita Pre-Order
aliases:
  - Visita Pre-Order
tags:
  - BST
  - visite
  - visita-pre-order
created: 2025-06-04
---
La procedura `PreOrder` attraversa i nodi di un [[albero_binario_di_ricerca]] partendo dalla radice, per poi visitare il sottoalbero sinistro e infine il sottoalbero destro

```c
PreOrder(x){
	if(x != NIL){
		Print(x.key)
		PreOrder(x.left)
		PreOrder(x.right)
	}
}

PreOrder(T.root)
```

Se $x$ è la radice di un sottoalbero di $n$ nodi, la chiamata `PreOrder(x)`richiede $\Theta(n)$.