---
title: Visita Post-Order
aliases:
  - Visita Post-Order
tags:
  - BST
  - visite
  - visita-post-order
created: 2025-06-08
---
La procedura `PostOrder` attraversa i nodi di un [[albero_binario_di_ricerca|Albero binario di ricerca]] visitando prima il sottoalbero sinistro, poi il sottoalbero destro e infine il nodo stesso.

```c
PostOrder(x){
	if(x != NIL){
		PostOrder(x.left)
		PostOrder(x.right)
		Print(x.key)
	}
}
```

Se $x$ è la radice di un sottoalbero di $n$ nodi, la chiamata `InOrder(x)`richiede $\Theta(n)$.
