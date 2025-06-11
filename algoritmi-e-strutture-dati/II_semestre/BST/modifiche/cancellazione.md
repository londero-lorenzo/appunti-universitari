---
title: Cancellazione
aliases:
  - Cancellazione
tags:
  - BST
  - modifiche
  - cancellazione
created: 2025-06-08
---
Dato un [[albero_binario_di_ricerca|albero binario di ricerca]] `T` e un nodo `z` che appartiene a `T`, la procedura `DeleteBST` elimina `z` in modo da preservare la [[albero_binario_di_ricerca#Definizione|proprietà del BST]].

## Pseudo codice

```
DeleteBST(T, z){
	if(z.left = NIL || z.right = NIL){
		x <- z
	}else{
		x <- TREE-SUCCESSOR(z)
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

### Funzionamento
### 1. Identificazione del nodo da rimuovere (`x`)

Due casi:

- **`z` ha al massimo un figlio:**  
    Possiamo rimuoverlo direttamente, quindi poniamo `x = z`.
    
- **`z` ha due figli:**  
    Non può essere rimosso direttamente senza rompere la struttura dell'albero.  
    Viene scelto il **successore in-order** di `z`, che è il **minimo del sottoalbero destro**.  
    Per costruzione, questo nodo ha [[procedure_di_modifica_schema#^L715l5hJ|al massimo un figlio destro]], quindi rimuoverlo è più semplice.
![[procedure_di_modifica_schema#^frame=DFhT4R1nIz4qA76LWO2Ot|100%]]
---

### 2. Identificazione del figlio `v` di `x` (se esiste)

Una volta determinato `x` (il nodo effettivo da rimuovere), dobbiamo trovare il suo **unico figlio**, se presente.

- Se `x.left ≠ NIL`, allora `v = x.left`
- Altrimenti, `v = x.right`

**Perché uno solo dei due sarà diverso da NIL?**
- Per costruzione: `x` è stato scelto in modo che abbia **al massimo un figlio**
  - Questo è sempre vero se `x = z` con ≤ 1 figlio
  - È vero anche se `x = BSTSuccessor(z)`, perché il successore in-order **non può avere figlio sinistro**
![[procedure_di_modifica_schema#^frame=Kjs5qIOTBCEz56rdposyp|100%]]

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
![[procedure_di_modifica_schema#^frame=dcJN4CezPfs4oBgfPu51n|100%]]

---

### 4. Ricollegamento di `v` al padre di `x`

Se `v ≠ NIL` (cioè se `x` aveva un figlio), bisogna aggiornare anche il **campo `parent` di `v`**, perché ora `v` è collegato al posto di `x`.

- Quindi: `v.parent = x.parent`
![[procedure_di_modifica_schema#^frame=SK0kSuAIk-TeLjGnWzgbw|100%]]
---

### 5. Sostituzione della chiave (se necessario)

Questo passo avviene **solo se `x ≠ z`**, cioè quando abbiamo sostituito `z` col suo successore.

- In quel caso:
  - Abbiamo rimosso `x` (il successore di `z`)
  - Ora copiamo la sua chiave in `z`, così `z` **contiene il valore corretto** e la struttura BST rimane intatta

Quindi: `z.key = x.key`

![[procedure_di_modifica_schema#^frame=-jtM02Mov59grxczPAsxu|100%]]

### Costo Inserimento e Cancellazione
+ $O(h)\rightarrow O(n)$
+ $\Theta(n)$
