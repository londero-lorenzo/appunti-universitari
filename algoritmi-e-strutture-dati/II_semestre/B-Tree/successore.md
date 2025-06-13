---
title: Successore
aliases:
  - Successore
tags:
  - B-Tree
  - successore
created: 2025-06-13
---

## B-SUCCESSOR

```c
B-SUCCESSOR(T, t, k){  /// k sta in t
	x = DISK-READ(T.root)
	k_1 = inf
	if (not x.leaf){
		i = 1
		while (i <= x.n && x.key[i] < k){ // cerco la prima chiave maggiore di k
			i = i + 1
		}
		if (i <= x.n && x.key[i] == k){
			// ho trovato k in x quindi cerco il suo successore nel valore minimo              // dell'albero radicato nell'i-esaima posizione di x
			y = DISK-READ(x.c[i])
			return B-MIN(y, t)
		}
		if (i <= x.n){
			// tengo traccia della prima chiave più grande di k in x
			k_i = x.key[i]
		}
		// scendo nel nodo i-esimo di x
		x = DISK-READ(x.c[i])
	}
	i = 1
	while (i <= x.n && x.key[i] < k){
		i = i + 1
	}
	if (i < x.n){
		// sono fermo alla prima chiave più
		return x.key[i]
	}else{
		return k_1
	}
}
```


## Costo

- CPU: $\mathcal{O}(t\cdot\log_{t}{n})$, `t` è riferito ai costi dei while
- R/W: $\Theta(\log_{t}{n})$, un albero per forza lo devo leggere tutto
