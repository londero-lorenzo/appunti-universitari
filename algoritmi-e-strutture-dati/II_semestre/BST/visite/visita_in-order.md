---
title: Visita In-Order
aliases:
  - Visita In-Order
tags:
  - BST
  - visite
  - visita-in-order
created: 2025-06-04
---
La procedura `InOrder` attraversa i nodi di un [[albero_binario_di_ricerca|Albero binario di ricerca]] in ordine crescente.

```
InOrder(x){
	if(x != NIL){
		InOrder(x.left)
		Print(x.key)
		InOrder(x.right)
	}
}
```

Se $x$ è la radice di un sottoalbero di $n$ nodi, la chiamata `InOrder(x)`richiede $\Theta(n)$.


## Correttezza

Per induzione su $n$ numero di chiavi memorizzate in $T$
+ **Ipotesi:** $T$ è BST
+ **Tesi:** `InOrder` stampa in ordine crescente
+ **BASE:** $n=0$ `InOrder` non stampa niente
+ **TESI:** se $T$ è un BST con $n$ chiavi `InOrder(T)` 