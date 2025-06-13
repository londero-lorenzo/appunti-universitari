---
title: Esercizi
aliases:
  - Esercizi
tags:
  - RBT
  - esercizi
created: 2025-06-11
---

# Costruzione

## Es.1


Come costruire un [[red_black_tree|Red Black Tree]] contenente `n` chiavi che si trovano in un vettore `A`,

### Complessità
 $\to\mathcal{O}(n\log n)$ 

### Nota
Non si può in $\Theta(n)$ nel caso migliore, altrimenti avremmo trovato una procedura di ordinamento lineare.

Commenti:
 >_Se riuscissi a costruire sempre in tempo lineare un RBT a partire da un vettore generico, poi siccome la [[visita_in-order|Visita In-Order]] restituisce un vettore ordinato avrei ottenuto un algoritmo lineare per l'ordinamento. Abbiamo dimostrato che usando solo scambi e confronti senza ipotesi sull'input non è possibile ordinare in tempo lineare **sempre.
> Carla Piazza

## Es.2
Come costruire un [[red_black_tree|Red Black Tree]] contenente `n` chiavi che si trovano in un vettore `A` ordinato.
### Idea
![[esercizi_schizzi#^frame=65v8RgJ-t7uc8sPGLteG9|75%]]
### Complessità
$\to T(n) = 2T(\frac{n}2) + \mathcal{O}(\log n)$


## Es.3

Passare da Vettore Ordinato a [[red_black_tree|Red Black Tree]] e viceversa.
Quali operazioni sono più efficaci su Vettori Ordinati e RBT?

Assumiamo:
MinHeap vs RBT
Mi interessano:
- inserimenti
- cancellazioni
- cancellazioni del minimo

Operazioni a confronto:

| Operazioni           | MinHeap               | RBT                   |
| -------------------- | --------------------- | --------------------- |
| Inserimento          | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ |
| Cancellazione        | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ |
| Cancellazione minimo | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ |
Stessa complessità per entrambe le strutture dati.

Quindi:
### Quando conviene usare MinHeap o RBT?
> _Gli RBT vengono utilizzati nei sistemi operativi_
> 

### Da Vettore Ordinato a [[red_black_tree|Red Black Tree]]


### Da [[red_black_tree|Red Black Tree]] a Vettore Ordinato


# Compitino di ASD del 17-06-19
## Es.1
Sia T un RB-tree contenente n chiavi intere e sia k una chiave intera che non occorre in T. Si consideri il problema di determinare la più piccola chiave di T maggiore di k (successore di k in T), se esiste.
1. Si fornisca lo pseudocodice di un algoritmo efficiente per risolvere il problema enunciato senza modificare l’albero T.
2. Si determini la complessità e si dimostri la correttezza della soluzione proposta.

### Codice

```c
NEXT-KEY(T, k){
	x = T.root
	y = x
	while(x != T.nil){
		y = x
		if (k < y.key){
			x = y.left
		}else{
			x = y.right
		}
		
	}
	if (y == T.nil)
		return T.nil
		
	if (y.key < k)
		return TREE-SUCCESSOR(T, y)
	else
		return y
}
```

---

### Complessità
 1 discesa e 1 possibile risalita: $\mathcal{O}(h) = \mathcal{O}(\log_{2}{n})$
 
 ---

### ✅ Correttezza della procedura `NEXT-KEY(T, k)`

**Ipotesi**:

- `k` è una chiave intera che **non appartiene** all'albero `T`
    
- `T` è un **Red-Black Tree**, quindi un **Binary Search Tree (BST)** che soddisfa anche proprietà di bilanciamento
    
- La procedura `TREE-SUCCESSOR(T, y)` è **corretta**


**Tesi**:  
La procedura `NEXT-KEY(T, k)` termina e restituisce la **chiave più piccola maggiore di `k`**, se esiste (cioè il **successore** di `k` in `T`).


---

### 🧩 Passo base

Se `T` è vuoto (`n = 0`), allora `T.root = T.nil`.  
Il ciclo `while` non viene mai eseguito, e `y = x = T.nil`.

→ La funzione restituisce `T.nil`, correttamente: **non esiste alcun successore**.


---

### 🔁 Invariante del ciclo

Durante l'esecuzione del ciclo `while`, si mantiene:

> `y` è sempre l’**ultimo nodo non nullo** visitato nella discesa a partire dalla radice.

Essendo `T` un BST e `k` non presente, il confronto `k < y.key` guida sempre la discesa in un sottoalbero **che potrebbe contenere il successore**, fino ad arrivare a un nodo foglia (cioè a `T.nil`).


---

### 🔚 Uscita dal ciclo

Alla fine del ciclo `while`, `x = T.nil` e `y` è l’ultimo nodo visitato con chiave `y.key`.

Si verificano due casi:

#### Caso 1: `y == T.nil`

L’albero era vuoto → restituisco `T.nil`.

#### Caso 2: `y != T.nil`

Analizzo la relazione tra `k` e `y.key`:

- **Se `y.key > k`**:  
    Durante la discesa, l’algoritmo ha preso un ramo sinistro → `y` è la **prima chiave incontrata maggiore di `k`**.  
    Quindi `y` è **il successore corretto di `k`**, e viene restituito.
    
- **Se `y.key < k`**:  
    Tutte le chiavi visitate erano < `k`, quindi siamo discesi sempre a destra.  
    `y` è l’ultima chiave < `k`, ma non è il successore.  
    → In questo caso, invocare `TREE-SUCCESSOR(T, y)` restituisce correttamente il **minimo nodo antenato (o discendente a destra)** con chiave maggiore di `k`.


---


### ✔ Conclusione

In entrambi i casi:

- Se il successore **esiste**, viene restituito
    
- Se il successore **non esiste**, la funzione restituisce `T.nil`
    

La funzione `NEXT-KEY` è **corretta**.


----
