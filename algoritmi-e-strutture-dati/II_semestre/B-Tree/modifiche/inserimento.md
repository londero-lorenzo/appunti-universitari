---
title: Inserimento
aliases:
  - Inserimento
tags:
  - B-Tree
  - modifiche
  - inserimento
created: 2025-06-12
---
---
## 📌 Inserimento in un B-Tree

Dato un [[b-tree|B-Tree]] `T` con `n` chiavi e un valore `k` da inserire, l’obiettivo è **inserire `k` in una foglia esistente** senza violare le [[algoritmi-e-strutture-dati/II_semestre/B-Tree/definizione#🧱 Campi di un nodo `x`|proprietà del B-Tree]].

> **Nota:** Le foglie devono trovarsi **tutte allo stesso livello**. Inserire una nuova foglia romperebbe questa proprietà.  
> ⟶ Quindi `k` deve essere inserita in una foglia già esistente.
> ![[algoritmi-e-strutture-dati/II_semestre/B-Tree/b-tree_schema.md#^frame=UfgTACxc77cuGNQJWHxtO|100%]]

---

## 🧱 Strategia generale

Durante la discesa dalla **radice alle foglie**, ogni volta che si incontra un **nodo pieno**                         (`n == 2t - 1`), lo si **splitta**.

La procedura `BTREE-SPLIT(x, y, i, t)`:

- Divide il figlio `y` pieno in due nodi.
    
- Fa salire la chiave centrale in `x`.
    
- Si assicura che nessun nodo sia pieno **prima** di inserirvi qualcosa.
    

⟶ Questo garantisce che, quando si arriva alla foglia dove inserire `k`, essa **non sarà piena**.

---

## 🔁 Processo d’inserimento

Il procedimento avviene in due fasi:

### 1. `BTREE-INSERT(T, t, k)`

- Se la **radice è piena**, crea un nuovo nodo `s`, che diventa la nuova radice.
    
- Fa uno split della vecchia radice.
    
- Poi chiama `BTREE-INSERT-NOTFULL(s, k, t)`.

#### Codice

```c
BTREE-INSERT(T, t, k){ // k non è già in T
	r = T.root
	if (r.n == 2*t - 1){
		// la radice è piena, split
		s = ALLOCATE-NODE(t)
		// s nuova radice temporanea
		s.n = 0
		s.leaf = false
		s.c[1] = r // figli indicizzati da 1
		T.root = s
		BTREE-SPLIT(s, r, 1, t)
		// s nuova radice splittata
		BTREE-INSERT-NOTFULL(s, k, t)
	}else{
		BTREE-INSERT-NOTFULL(r, k, t)
	}
}
```

---

### 2. `BTREE-INSERT-NOTFULL(x, k, t)`

- Inserisce `k` nel nodo `x` o nei suoi discendenti, assumendo che `x` **non sia pieno**.
    
- Se `x` è foglia, inserisce direttamente `k`.
    
- Se `x` non è foglia:
    
    - individua il figlio `x.c[i]` dove dovrebbe andare `k`;
        
    - se `x.c[i]` è pieno, fa uno `split`;
        
    - poi prosegue la discesa nel figlio giusto (quello rimasto o quello nuovo, a seconda della chiave centrale salita).

#### Codice

```c
BTREE-INSERT-NOTFULL(x, k, t){ // k va in una delle foglie di x                                                   // x.n < 2t-1 (x non è pieno)                                                      // x è già in RAM
	if (x.leaf){
		i = x.n
		while (i >= 1 && x.key[i] > k){
			x.key[i+1] = x.key[i]
			i = i-1
		}
		// i è fermo sull'ultima chiave più piccola di k
		x.key[i+1] = k
		x.n = x.n + 1
		DISK-WRITE(x)
	}else{
		i = x.n
		while (i >= 1 && x.key[i]> k){ // i >= 0 perchè può succedere che tutte le                                        // chiavi siano più grandi di k
			i = i - 1
		}
		// i è fermo sull'ultima chiave più piccola di k
		y = DISK-READ(x.c[i+1])
		if (y.n < 2*t-1)
			// il figlio non è pieno
			BTREE-INSERT-NOTFULL(y, k, t)
		else{
			BTREE-SPLIT(x, y, i+1, t)
			// devo decidere su quale ramo scendere dopo il split
			if (k < x.key[i+1]){
				// scendo a sinistra
				y = DISK-READ(x.c[i+1])
				BTREE-INSERT-NOTFULL(y, k, t)
			}else{
				// scendo a destra
				z = DISK-READ(x.c[i+2])
				BTREE-INSERT-NOTFULL(z, k, t)
			}
		}
	}
}
```


---


## ❓ Gestione dello split e degli indici

Quando si fa uno **split** mentre si scende:

- La chiave centrale di un nodo pieno **sale** al padre.
    
- Bisogna aggiornare l’indice di discesa: dopo lo split, la chiave `k` potrebbe dover andare a destra della chiave salita.
    

> 👀 Vedi lo schema di aggiornamento degli indici  
> ![[b-tree_schema.md#^frame=5DyZTDwKCKka8krFj_EFj|100%]]
### Esempio
![[algoritmi-e-strutture-dati/II_semestre/B-Tree/b-tree_esempi.md#^frame=IJcl4dYi8iy86Ekg9ruEa|100%]]

## 📝 Note importanti

- 🔄 **L'altezza del B-Tree aumenta solo in `BTREE-INSERT`**, mai in `BTREE-INSERT-NOTFULL`.
    

> 💬 _Domanda:_ "`BTREE-INSERT-NOTFULL` può aumentare l'altezza del B-Tree?"  
> _Risposta:_ No. L’altezza cresce solo quando si splitta la radice, ed è gestito da `BTREE-INSERT`.

- 💾 **Scritture su disco:**
    
    - Non servono in `BTREE-INSERT-NOTFULL` se non si fa uno split.
        
    - Le scritture sono gestite direttamente da `BTREE-SPLIT`.
        

> 💬 _Domanda:_ "È corretto non avere `DISK-WRITE` in `BTREE-INSERT-NOTFULL`?"  
> _Risposta:_ Sì. Perché `BTREE-SPLIT` si occupa delle scritture, ed è l’unico punto in cui si modifica la struttura.

---

## 🧮 Complessità

### 📌 Tempo (CPU)

$\mathcal{O}(t \cdot \log_t n)$

- Profondità dell’albero: $\log_t n$
    
- Per ogni nodo si scandiscono fino a $2t - 1$ chiavi
    

### 📌 I/O (letture/scritture su disco)

$\Theta(\log_t n)$

- Fino a **2 letture** per nodo visitato
    
- Fino a **3 scritture** ogni volta che si fa uno split