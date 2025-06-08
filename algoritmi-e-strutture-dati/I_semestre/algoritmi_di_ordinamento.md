---
title: Algoritmi di Ordinamento
aliases:
  - Algoritmi di Ordinamento
tags:
  - algoritmi-e-strutture-dati
  - I-semestre
  - algoritmi-di-ordinamento
  - università
created: 2025-06-04
---
## Insertion Sort

```
INSERTION-SORT(A){
	for j = 2 to A.length{
		key = A[j]
		// Inserisce A[j] nella sequenza ordinata A[1...j-1].
		i = j-1
		while i>0 and A[i] > key{
			A[i+1] = A[i]
			i = i - 1
		}
		A[i+1] = key
	}
}
```

### Costo
$O(n^{2})$

### Correttezza
**Insertion Sort:** Per ogni vettore A, l'algoritmo Insertion Sort termina con A ordinato.

**Invariante di ciclo:** All'inizio dell’i-esima iterazione, $A[1...i-1]$ è ordinato.

**Dimostrazione per induzione sull'indice i:**

- **Caso base:** i = 2. All'inizio della seconda iterazione del ciclo for, $A[1...1]$ è ordinato, essendo un vettore con un solo elemento.
    
- **Passo induttivo:** Supponiamo che l'invariante sia vera fino all’inizio dell’i-esima iterazione compresa, quindi $A[1...i-1]$ è ordinato.
    

**Tesi:** L'invariante è vera all’inizio della (i+1)-esima iterazione e quindi $A[1...i]$ è ordinato.

## MergeSort

```
MERGESORT(A, p, q){
	if (p < q){
		r <- (p+q)/2
		MERGESORT(A, p, r)
		MERGESORT(A, r+1, q)
		MERGE(A, p, r, q)
	}
}

MERGE(A, p, q, r){
	n1 = q - p + 1
	n2 = r - q
	for (i = 1 to n1){
		L[i] = A[p+i-1]
	}
	for (j = 1 to n2){
		R[j] = A[q+j]
	}
	L[n1+1] = infinito
	R[n2+1] = infinito
	i=1
	j=1
	for (k = p to r){
		if (L[i] <= R[j]){
			A[k] = L[i]
			i = i + 1
		}else if (A[k] = R[j]){
			j = j + 1
		}
	}
}
```

### Correttezza

**Dimostrazione per induzione sul numero di chiamate ricorsive:**

- **Caso base:** $h = 0$ chiamate ricorsive. L'array $A[p...q]$ è già ordinato ($p = q$ o $p > q$).
    
- **Passo induttivo:** 
	- Ipotesi induttiva: MergeSort(A, p, q) termina con $A[p...q]$ ordinato se sono state effettuate $h - 1$ chiamate ricorsive.
    
- **Tesi:** MergeSort(A, p, q) termina con $A[p...q]$ ordinato se sono state effettuate $h$ chiamate ricorsive.
    

Alla h-esima chiamata ricorsiva $A[p...q]$

Alla (h - 1)-esima chiamata, gli array $A[p...\frac{p+q}{2}]$ e $A[\frac{p+q}{2}+1...q]$ sono ordinati.

Per effetto dell’azione di _Partition_ o della fase di merge, alla h-esima chiamata $A[p...q]$ sarà ordinato.

### Complessità
+ **MergeSort:** $O(n\log n)$ una chiamata a Merge e due ricorsioni con la metà degli elementi
+ **Merge:** $O(n)$ 2 for innestati
## HeapSort

```
HEAPSORT(A){
	BUILDHEAP(A)
	for (i<-A.length down to 2){
		Scambia(A,1,i)
		A.heapsize<-A.heapsize-1
		HEAPIFY(A,1)   
	}
}

MAX-HEAPIFY(A, i){
	l = LEFT(i)
	r = RIGHT(i)
	if (l <= A.heapsize and A[l] > A[i]){
		massimo = l	
	}else{
		massimo = i
	}
	if (r <= A.heapsize and A[r] > A[massimo]){
		massimo = r
	}
	if (massimo != i){
		Scambia(A[i], A[massimo])
		MAX-HEAPIFY(A, massimo)
	}
}

MIN-HEAPIFY(A, i){
	l = LEFT(i)
	r = RIGHT(i)
	if (l <= A.heapsize and A[l] < A[i]){
		minimo = l	
	}else{
		minimo = i
	}
	if (r <= A.heapsize and A[r] < A[minimo]){
		minimo = r
	}
	if (minimo != i){
		Scambia(A[i], A[minimo])
		MAX-HEAPIFY(A, minimo)
	}
}

BUILDHEAP(A){
	A.heapsize = A.length
	for (i = floor(A.length/2) down to 1){
		HEAPIFY(A, i)
	}
}
```

### Correttezza
**Heapify:** Siano `H[LEFT(i)]` e `A[RIGHT(i)]` sono radici di MAX-HEAP, allora `HEAPIFY(H,i)` termina con `H[i]` radice di MAX-HEAP.

**Dimostrazione per induzione sul numero di chiamate ricorsive:**

- **Caso base:** h = 0 chiamate ricorsive  
    I figli non esistono oppure hanno chiavi minori o uguali rispetto al genitore.
    
- **Passo induttivo:**  
    Ipotesi: Heapify funziona correttamente con al massimo k chiamate ricorsive.  
    Tesi: Heapify funziona correttamente con k + 1 chiamate ricorsive.
    
Sono nel caso in cui $m\neq i$, supponiamo $m=l$, se $m=l$ allora $b>a$ e $b\geq c$. Il codice mi chiede quindi di scambiare $b$ e $a$ e svolgo $k$ chiamate ricorsive sotto. ![[Algoritmi/Esame/Untitled Diagram.svg]]
![[Algoritmi/Esame/Untitled Diagram 1.svg]]


Se il valore del nodo corrente non rispetta la proprietà di max-heap (ad esempio se il figlio b è maggiore del genitore a), allora scambio b e a e procedo con la chiamata ricorsiva su b. 


**HeapSort(A)** termina con A ordinato.

**Invariante del ciclo for:**  
All'inizio della i-esima iterazione del ciclo for:

- $A[1...i]$ è una max-heap;
    
- $A[i+1...length]$ è ordinato;
    
- Tutti gli elementi di $A[1...i]$ sono minori o uguali a tutti quelli di $A[i+1...length]$.
    

**Dimostrazione per induzione su i:**

- **Caso base:** i = A.length, vero per la correttezza della funzione BuildHeap.  
    Infatti, $∀ x ∈ A[1...i], ∀ y ∈ A[i+1...length], x ≤ y$.
    
- **Passo induttivo:**  
    Ipotesi: l'invariante è vera all'inizio della i-esima iterazione.  
    Tesi: è vera all'inizio della (i-1)-esima iterazione.
    

Durante il ciclo, l’elemento in prima posizione viene scambiato con l’ultimo elemento della max-heap A[1...i]. La heap diventa lunga i - 1 e viene svolto Heapify sulla radice della MaxHeap mettendo a posto l'elemento.
In questo modo, essendo la precedente radice della MaxHeap il valore più grande ed essendo $\forall x \in A[1...i], \forall y \in A[i+1,...A.length],  x \leq y$
$A[i+1,...A.length]$ sarà sempre ordinato anche dopo la i-1 esima iterazione.

### Complessità
+ **Heapify:** $O(\log n)\rightarrow$ chiamata ricorsiva ma sulla lunghezza della heap - 1
+ **BuildHeap:** $O(n)\rightarrow$ chiamata a Heapify dentro un ciclo for ma converge quindi rimane $O(n)$
+ **HeapSort:** $O(n \log n)\rightarrow$ Heapify dentro un for e un BuildHeap all'inizio
+ **ExtractMax:** $O(\log n)\rightarrow$ svolgo Heapify
+ **InsertMax:** $O(\log n)\rightarrow$ ciclo while sulla lunghezza della heap

## Code di priorità

### Massimo
```
HeapExtractMax(A){
	if (A.heap-size < 1){
		error "underflow dell'heap"
	}
	max = A[1]
	A[1] = A[A.heap-size]
	A.heap-size = A.heap-size - 1
	MaxHeapify(A, 1)
	return max
}

HeapIncreaseKey(A, i, key){
	if key < A[i]{
		error "la nuov chiave è più piccola di quella corrente"
		A[i] = key
		while (i > 1 && A[Parent(i)] < A[i]){
			Scambia(A[i], A[Parent(i)])
			i = Parent(i)
		}
	}
}

MaxHeapInsert(A, key){
	A.heap-size = A.heap-size + 1
	A[A.heap-size] = -inf
	HeapIncreaseKey(A, A.heap-size, key)
}

```

### Minimo
```
HeapExtractMin(A){
	if (A.heap-size < 1){
		error "underflow dell'heap"
	}
	min = A[1]
	A[1] = A[A.heap-size]
	A.heap-size = A.heap-size - 1
	MinHeapify(A, 1)
	return min
}

HeapDecreaseKey(A, i, key)
    if (key > A[i]){
        error "la nuova chiave è più grande di quella corrente"
    }
    A[i] = key
    while (i > 1 and A[PARENT(i)] > A[i]){
        scambia A[i] con A[PARENT(i)]
        i = PARENT(i)
    }
    
MinHeapInsert(A, key)
    A.heap_size = A.heap_size + 1
    A[A.heap_size] = +∞      # o un numero molto grande
    HEAP-DECREASE-KEY(A, A.heap_size, key)

```

#### Costo:
Il costo di tutte queste procedure è di $O(\log n)$

## QuickSort

```
QUICKSORT(A,p,q){
	if (p < q){
		r <- Partition(A,p,q)
		QUICKSORT(A, p, r)
		QUICKSORT(A, r+1, q)
	}
}

PARTITION(A, p, q){
	x <- A[q]
	i <- p - 1
	for (j <- p to q){
		if (A[j] <= x){
			i <- i + 1
			Scambia(A, i, j)
		}
	}
	return i
}
```
### Correttezza
**QuickSort(A, p, q)** termina con A ordinato.

**Dimostrazione sul numero di chiamate ricorsive:**

- **Caso base:** $p ≥ q$, cioè l’array $A[p...q]$ ha 0 o 1 elemento, quindi è già ordinato.
    
- **Passo induttivo:**  
    Ipotesi: QuickSort ordina correttamente con n chiamate ricorsive.  
    Tesi: QuickSort ordina correttamente con n + 2 chiamate ricorsive.

**Dimostrazione di correttezza:** durante la chiamata n+2-esima, gli array $A[p...r]$ e $A[r+1...q]$ sono ordinati (per ipotesi induttiva), e per la correttezza di Partition, l’intero $A[p...q]$ risulta ordinato.

**Partition(A, p, q)** termina con tutti i valori $\leq$ pivot prima del pivot e tutti i valori $\geq$ del pivot dopo il pivot.

**Dimostrazione per induzione su j:**

**Invariante del ciclo for:**  
All’inizio della j-esima iterazione, gli elementi in $A[p...j-1]$ ≤ pivot stanno a sinistra del pivot.
![[Algoritmi/Esame/Untitled Diagram 2.svg]]

- **Caso base:** j = p.  
    Se A[p] è minore o uguale al pivot, incremento j e lo scambio è corretto.
    
- **Passo induttivo:**  
    Ipotesi: l'invariante è vera all’inizio della j-esima iterazione.  
    Tesi: l'invariante è vera all’inizio della (j+1)-esima iterazione.
    
**Dim correttezza:** `Partition(A, p, q)` termina all'inizio dell'iterazione in cui $i$ vale $q+1$. Per l'invariante quindi Partition è corretto.

### Complessità
+ **QuickSort:** $O(n\log n)$ una chiamata a Partition e due ricorsioni con la metà degli elementi
+ **Partition:** $O(n)$ ciclo for
