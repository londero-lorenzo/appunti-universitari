---
title: Creazione
aliases:
  - Creazione
tags:
  - B-Tree
  - modifiche
  - creazione
created: 2025-06-12
---
### Creare albero vuoto

![[algoritmi-e-strutture-dati/II_semestre/B-Tree/b-tree_schema.md#^frame=lvBl90RMmcmM4EELdHvzB]]

```
BTREE-CREATE(T, t){
	x = ALLOCATE-NEW-NODE(t) // procedura che deve allora tutto ciò che serve ad                                // un B-Tree (vettore chiavi di lunghezza 2t-1,                                    //vettore figli di lunghezza 2t)
	x.leaf = true
	x.n = 0
	T.root = DiskWrite(x) // il nodo viene scritto in memoria secondaria, viene                              // restituito l'indirizzo che viene memorizzato nel                                // campo T.root
	return T
}
```
