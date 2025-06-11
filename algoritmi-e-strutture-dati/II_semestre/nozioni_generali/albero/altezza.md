---
title: Altezza
aliases:
  - Altezza
tags:
  - BST
  - altezza
created: 2025-06-08
---
## 🌲 Altezza di un albero

Sia `T` un albero binario con `n` nodi (chiavi).  
L’**altezza** `h(T)` è il **numero massimo di archi** nel cammino dalla **radice a una foglia**.

---

### 🔹 Caso ideale – Albero bilanciato

Se `T` è ben bilanciato, allora:

- $h(T) = \mathcal{O}(\log n)$
    
- le operazioni su `T` (inserimento, ricerca, cancellazione) hanno **costo logaritmico**
    

📉 Esempio:


<pre>
	   8
     /   \
    4     12
   / \   /  \
  2   6 10  14
  </pre>

---

### 🔸 Caso peggiore – Albero degenerato

Se `T` è sbilanciato (es. inserimento di chiavi in ordine crescente), si degrada in una **lista**:

- $h(T) = \mathcal{O}(n)$
    
- le operazioni diventano **lineari**
    

📈 Esempio:

<pre>
	8
	 \
	  12
	    \
	     14
	       \
	        16

</pre>

---

## 🧠 Implicazioni

- L’altezza `h` è la misura **critica** per la **complessità** di un albero.
    
- Alberi **bilanciati** mantengono `h = \mathcal{O}(\log n)` anche nei casi peggiori.
    
- Le strutture come [[red_black_tree|Red Black Tree]], [[b_tree|BTree]] sono progettate per **controllare l’altezza**.
    

---

## 🔁 Collegamento

🔗 Vedi anche: [[albero_bilanciato]] per come mantenere bassa l’altezza.