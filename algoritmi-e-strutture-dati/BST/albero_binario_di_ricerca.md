---
title: "Albero Binario di Ricerca"
aliases: ["Albero Binario di Ricerca"]
tags: [università, "algoritmi-e-strutture-dati", "BST", "albero-binario-di-ricerca"]
created: 2025-06-04
---
## Definizione
Un albero binario di ricerca è un albero binario in cui ogni nodo ha una chiave intera tale che $\forall x \in T(\forall\ y \in x.left\ y.key<x.key\ \wedge\ \forall\ y \in x.right\ y.key>x.key)$
[[ALGORITMI]]

## Visite di alberi binari
- [[visita_pre-order]]
- [[visita_in-order]]


## Ricerche
- [[ricerca_di_una_chiave]]
- [[ricerca_del_massimo]]
- [[Ricerca del minimo]]
- [[Ricerca del predecessore]]
- [[Ricerca del successore]]
## Inserimento
## Cancellazione
```
BSTDelete(T, z){
	if(z.left = NIL || z.right = NIL){
		x <- z
	}else{
		x <- BSTSuccessor(z)
	}
	if (x.left != NIL){
		v <- x.left
	}else{
		v <- x.right
	}
	if (x.parent = NIL){
		T.root <- v
	}else if(x.parent.left = x){
		x.parent.left <- v
	}else{
		x.parent.right <- v
	}
	if (v != NIL){
		v.parent <- x.parent
	}
	if (x != z){
		z.key <- x.key
	}
}
```
Dato un nodo `z` nell’albero BST `T`, la procedura elimina `z` in modo da preservare la **proprietà dell’albero binario di ricerca (BST)**:

> Per ogni nodo `n`, tutte le chiavi nel sottoalbero sinistro di `n` sono **minori** di `n.key`,  
> e tutte le chiavi nel sottoalbero destro sono **maggiori** di `n.key`.

### 1. Selezione del nodo da rimuovere (`x`)

L'algoritmo distingue tra due casi principali:

- **Caso 1: `z` ha al massimo un figlio**  
  In questo caso `z` può essere rimosso direttamente perché la sua eliminazione non rompe la struttura dell'albero. Si imposta `x = z`, cioè il nodo da rimuovere è proprio `z`.

- **Caso 2: `z` ha due figli (sia sinistro che destro ≠ NIL)**  
  In questo caso, non possiamo eliminare `z` direttamente perché ha due rami da mantenere.  
  Soluzione:
  - Troviamo il **successore in-order** di `z`, cioè il **nodo con la chiave più piccola nel sottoalbero destro** di `z`
  - Questo successore, per costruzione dell’albero, **ha al massimo un figlio** (destro)
  - Impostiamo `x = BSTSuccessor(z)`, e ci occuperemo di rimuovere `x` al posto di `z`

---

### 2. Identificazione del figlio `v` di `x` (se esiste)

Una volta determinato `x` (il nodo effettivo da rimuovere), dobbiamo trovare il suo **unico figlio**, se presente.

- Se `x.left ≠ NIL`, allora `v = x.left`
- Altrimenti, `v = x.right`

**Perché uno solo dei due sarà diverso da NIL?**
- Per costruzione: `x` è stato scelto in modo che abbia **al massimo un figlio**
  - Questo è sempre vero se `x = z` con ≤ 1 figlio
  - È vero anche se `x = BSTSuccessor(z)`, perché il successore in-order **non può avere figlio sinistro**

---

### 3. Scollegamento di `x` dal suo genitore

Ora dobbiamo **rimuovere `x` dalla sua posizione nell'albero**, collegando il figlio `v` al posto suo.

- Se `x` è la **radice** dell'albero:
  - `T.root = v`, perché stiamo cambiando il nodo radice

- Altrimenti:
  - Se `x` è figlio sinistro del suo genitore:
    - `x.parent.left = v`
  - Se `x` è figlio destro:
    - `x.parent.right = v`

Questo ricollega correttamente l'albero rimuovendo `x`.

---

### 4. Ricollegamento di `v` al padre di `x`

Se `v ≠ NIL` (cioè se `x` aveva un figlio), bisogna aggiornare anche il **campo `parent` di `v`**, perché ora `v` è collegato al posto di `x`.

- Quindi: `v.parent = x.parent`

---

### 5. Sostituzione della chiave (se necessario)

Questo passo avviene **solo se `x ≠ z`**, cioè quando abbiamo sostituito `z` col suo successore.

- In quel caso:
  - Abbiamo rimosso `x` (il successore di `z`)
  - Ora copiamo la sua chiave in `z`, così `z` **contiene il valore corretto** e la struttura BST rimane intatta

Quindi: `z.key = x.key`

#### Costo Inserimento e Cancellazione
+ $O(h)\rightarrow O(n)$
+ $\Theta(n)$
