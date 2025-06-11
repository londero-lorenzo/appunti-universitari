---
title: Cancellazione
aliases:
  - Cancellazione
tags:
  - RBT
  - modifiche
  - cancellazione
created: 2025-06-10
---
# Cancellazione in Red-Black Tree

Dato un [[red_black_tree|Red Black Tree]] `T` e un nodo `z` appartenente a `T`, la procedura `RB-DELETE` elimina `z` preservando le [[algoritmi-e-strutture-dati/II_semestre/RBT/definizione|proprietà dei Red-Black Tree]].

---

##  🧠 Idea generale

- Si cancella `z` come in un normale [[algoritmi-e-strutture-dati/II_semestre/BST/modifiche/cancellazione|Binary Search Tree (BST)]]:
  ![[procedure_di_modifica_schema#^group=mv67uw71q9-hnCUzK1ygP]]

> ❗ Se il nodo `b` che viene eliminato è `BLACK`, potrebbe abbassarsi l’altezza nera dell’albero.

In particolare:
- `b` viene **sostituito** con un suo figlio `x`
- Se `x` è `RED` → si colora di `BLACK` e termina
- Se `x` è `BLACK` → si ha uno **sbilanciamento** → entra in gioco il concetto di **double BLACK**

Esempio:
![[red_black_tree_schema#^frame=McV1QsPXUG35QM64UPAU7|100%]]

---

## ⚫⚫ Double BLACK

Quando un nodo `BLACK` viene eliminato e sostituito da un altro `BLACK`, il nodo sostituto `x` si comporta come se avesse **due livelli di nero** → `double BLACK`.

> Violazione: compaiono tre stati di colore effettivi — `RED`, `BLACK`, `double BLACK` — che rompono le proprietà del Red-Black Tree.

###  🔧 Risoluzione
- Se il nodo `double BLACK` `x` era precedentemente `RED` → basta colorarlo `BLACK` e terminare
- Altrimenti → serve propagare o risolvere il problema tramite:
  - **Rotazioni**
  - **Ricolorazioni**

---

### ✏️ Esempio

![[red_black_tree_schema#^frame=o-ltRbMNWXkpaDv7E1JGB|100%]]


---
###  ⚖️ Sbilanciamento double BLACK
![[red_black_tree_schema#^frame=THLzv0PitJiVAM5Nu8bgj|100%]]

---

#### 🍀 Caso 1 — _Fortunato_
Il nodo `double BLACK` ha un **nipote `RED` opposto** rispetto al fratello → si può risolvere in un solo step.

![[red_black_tree_schema#^frame=H47a1H-GvcB3zcdMx0O7r|100%]]


#### 😐 Caso 2 — _Quasi Fortunato_
Il `double BLACK` ha un **nipote `RED` dallo stesso lato** del fratello → è necessario trasformarlo nel caso fortunato con una rotazione intermedia.

![[red_black_tree_schema#^frame=T9uQAm8vC5_nc0oJiSBfx|100%]]

#### 😣 Caso 3 — _Sfortunato_
Il fratello ed entrambi i nipoti del `double BLACK` sono `BLACK` → si ricolora e si propaga il `double BLACK` verso il padre.

![[red_black_tree_schema#^frame=0_cPh_Xsfrhqaxg14fApc|100%]]


#### 😠 Caso 4 — _Antipatico_
Il fratello del `double BLACK` è `RED`, ma i suoi figli sono `BLACK` → si ruota e si trasforma in uno dei casi precedenti.

![[red_black_tree_schema#^frame=jMx26dX_hUZqzJRIPMZpl|100%]]




## Pseudocodice

```
RB-DELETE(T, z)
    if z.left = T.nil or z.right = T.nil
        y ← z
    else
        y ← TREE-SUCCESSOR(z)
	
    if y.left ≠ T.nil
        x ← y.left
    else
        x ← y.right 
	
    if y.parent = T.nil
        T.root ← x
    else if y = y.parent.left 
        y.parent.left ← x
    else
        y.parent.right ← x
	
	if x != T.nil
		x.parent ← y.parent
	
    if y ≠ z
        z.key ← y.key
	
    if y.color = BLACK
        RB-DELETE-FIXUP(T, x)
	
    return y

```

```
RB-DELETE-FIXUP(T, z)
    while z ≠ T.root and z.color = BLACK do
        if z = z.parent.left then
            y ← z.parent.right   // fratello di z
			
            if y.color = RED then
                // Caso 4: y è rosso → scambio colori e ruoto a sinistra
                y.color ← BLACK
                z.parent.color ← RED
                LEFT-ROTATE(T, z.parent)
                y ← z.parent.right
				
            if y.left.color = BLACK and y.right.color = BLACK then
                // Caso 3: entrambi i figli di y sono neri → alzo il doppio nero
                y.color ← RED
                z ← z.parent
            else
                if y.right.color = BLACK then
                    // Caso 2: figlio destro nero → ruoto a destra su y
                    y.left.color ← BLACK
                    y.color ← RED
                    RIGHT-ROTATE(T, y)
                    y ← z.parent.right
				
                // Caso 1: figlio destro rosso → ruoto a sinistra su parent(z)
                y.color ← z.parent.color
                z.parent.color ← BLACK
                y.right.color ← BLACK
                LEFT-ROTATE(T, z.parent)
                z ← T.root
        else
            // stessa logica, ma con right e left invertiti
            y ← z.parent.left
			
            if y.color = RED then
                y.color ← BLACK
                z.parent.color ← RED
                RIGHT-ROTATE(T, z.parent)
                y ← z.parent.left
				
            if y.right.color = BLACK and y.left.color = BLACK then
                y.color ← RED
                z ← z.parent
            else
                if y.left.color = BLACK then
                    y.right.color ← BLACK
                    y.color ← RED
                    LEFT-ROTATE(T, y)
                    y ← z.parent.left
					
                y.color ← z.parent.color
                z.parent.color ← BLACK
                y.left.color ← BLACK
                RIGHT-ROTATE(T, z.parent)
                z ← T.root
	
    z.color ← BLACK

```



---



### 🎯 Obiettivo di `RB-DELETE-FIXUP`

Nel [[red_black_tree|Red-Black Tree]], la procedura `RB-DELETE-FIXUP` ha lo scopo di:

- **ristabilire tutte le proprietà dei red-black tree** dopo una cancellazione,
    
- in particolare, **correggere la violazione della proprietà [[algoritmi-e-strutture-dati/II_semestre/RBT/definizione#^434e76|3]]** 
    
- ciò accade quando viene **eliminato un nodo nero**, introducendo un "doppio nero" in `x`.


Non si occupa del caso `red-red` (violazione proprietà 4) che riguarda l’**inserimento**, non la cancellazione.

---
#### ⏱ Analisi della complessità

#####  Quante volte può entrare nel ciclo `while`?

`while x ≠ T.root and x.color = BLACK`

- `x` risale verso la radice a ogni iterazione.
    
- L’altezza di un red-black tree è **O(log n)** ⇒ il ciclo può ripetersi al massimo **O(log n)** volte.
    
- Alcuni casi (come il **caso 4**) portano all'uscita immediata.

✅ **Massimo numero di iterazioni: O(log n)**


---

#####  Cosa succede dentro il ciclo?

In ogni iterazione:

- viene eseguita **una singola rotazione** (`LEFT-ROTATE` o `RIGHT-ROTATE`) **al massimo**,
    
- vengono fatte **una manciata di confronti e assegnazioni di colori**,
    
- **nessuna ricorsione**, **nessuna visita dell'intero sottoalbero**.
    

✅ **Costo per iterazione: O(1)**

---

#### 📌 Conclusione

- **Caso peggiore:** si risale fino alla radice → **O(log n)** iterazioni da O(1) →  
    ✅ **Complessità totale: O(log n)**
    
- **Caso migliore:** il nodo cancellato era rosso → nessuna violazione →  
    ✅ **Complessità: O(1)**


---



### 🎯 Obiettivo di `RB-DELETE`

Come negli alberi binari di ricerca (BST), `RB-DELETE` deve:

1. **trovare** il nodo da eliminare;
    
2. **modificare** i puntatori dell'albero (sostituzione, rimozione);
    
3. **chiamare `RB-DELETE-FIXUP`** se serve ristabilire le proprietà del [[algoritmi-e-strutture-dati/II_semestre/RBT/definizione|Red Black Tree]].


---

#### ⏱ Analisi della complessità

##### 1. **Ricerca del successore `y`**

- Se `z` ha due figli, si cerca `y = SuccessorBST(z)`, che richiede **O(log n)** (si scende in un sottoalbero).
    
- Se `z` ha al massimo un figlio, si salta questo step.
    

✅ **Costo: O(log n)** nel caso peggiore.

---

##### 2. **Spostamento di puntatori**

- Tutte le assegnazioni (`x ← child`, `x.parent ← y.parent`, ecc.) sono a **costo costante**.
    

✅ **Costo: O(1)**.

---

##### 3. **Fix-up**

- Come analizzato prima, `RB-DELETE-FIXUP` ha costo **O(log n)** nel caso peggiore.
    

✅ **Costo: O(log n)**.

#### 📌 Conclusione

Il tempo dipende dalla **profondità dell’albero**, che è garantita essere **O(log n)** da una delle proprietà fondamentali degli alberi red-black.

Se il fixup non fosse limitato a O(log n), si perderebbe l’efficienza nei casi peggiori — ed è proprio questo che gli RBT garantiscono rispetto ai BST classici.