---
title: Inserimento
aliases:
  - Inserimento
tags:
  - BST
  - modifiche
  - inserimento
created: 2025-06-13
---
Dato un [[albero_binario_di_ricerca|albero binario di ricerca]] `T` e un nodo `z` tale che `z.key = v`, `z.left = NIL` e `z.right = NIL`, la procedura `InsertBST` modifica `T` e alcuni attributi di `z` per inserirlo in una posizione coerente con la [[albero_binario_di_ricerca#Definizione|proprietà del BST]].

## Pseudocodice

```c
InsertBST(T, z){
	y <- NIL
	x <- T.root
	while (x != NIL){
		if (x.key > z.key){
			y <- x
			x <- x.left
		}else{
			x <- x.right
		}
	}
	z.parent <- y
	if (y = NIL){
		T.root <- z
	}else if (y.key > z.key){
		y.left <- z
	}else{
		y.right <- z
	}
}
```

## Descrizione

- `InsertBST` parte dalla radice e percorre l'albero verso il basso, seguendo la proprietà dell’ordinamento.
    
- Il puntatore `x` individua la posizione corrente nel percorso, mentre `y` tiene traccia del **padre** di `x`.
    
- Il ciclo `while` cerca un puntatore `x` uguale a `NIL`, cioè il punto in cui inserire `z`.
    
- Alla fine della ricerca, `y` punterà al nodo genitore corretto per `z`. A quel punto:
    
    - Se `T` è vuoto (`y = NIL`), `z` diventa la nuova radice.
        
    - Altrimenti, `z` viene collegato come figlio sinistro o destro di `y`, in base al confronto tra le chiavi.
        

## Note

- La procedura **non** gestisce casi di chiavi duplicate: se `z.key = x.key`, `z` verrà inserito nel sottoalbero destro.
	
- Il nuovo nodo viene aggiunto in una foglia 


## Complessità
La procedura [[#Pseudocodice]] ha complessità O(h), dove h è l’altezza dell’albero `T`.