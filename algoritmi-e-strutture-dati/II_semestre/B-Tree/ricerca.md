---
title: Ricerca
aliases:
  - Ricerca
tags:
  - B-Tree
  - ricerca
created: 2025-06-12
---
# Ricerca in un B-Tree

Dati:

- un [[b-tree|B-Tree]] `T` di grado `t`
    
- una chiave `k`


Obiettivo: **trovare** `k` all'interno di `T`.


---

## Idea

Si cerca la chiave `k` in un nodo `x` (che si trova in RAM), confrontandola con le chiavi presenti nel nodo.

Se non la si trova, si **segue il puntatore al figlio corretto**, caricandolo da disco (I/O), e si ripete la procedura **ricorsivamente**.

 ![[algoritmi-e-strutture-dati/II_semestre/B-Tree/b-tree_schema.md#^frame=rhs_8cguZVainAcvA5X-x|100%]]



## BTREE-SEARCH

```c
BTREE-SEARCH(T, t, x, k){ // sono in un albero T che è di grado t, sono arrivata                             // al nodo x e sto cercando la chiave k                                            // x è in RAM
    i = 1
    while( i <= x.n && x.key[i] < k ){
        i = i + 1
    }
	// 3 casi:
	// 1. sono arrivato sulla chaive k
	// 2. sono arrivato su una chiave maggiore di k
	// 3. sono arrivato fuori dalle chiavi di x

    if (i <= x.n && x.key[i] == k) // caso 1: trovata
        return (x, i)
    else if (x.leaf)              // caso 2: non trovata, e sono a foglia
        return NIL
    else {
        // caso 3: non trovata, scendo nel figlio corretto
        y = DiskRead(x.c[i])     // caricamento da memoria secondaria
        return BTREE-SEARCH(T, t, y, k)
    }
}

```

## Perché `x.c[i]` esiste sempre?

- L’indice `i` esce dal `while` con valore al massimo `x.n + 1`
    
- Ogni nodo ha **esattamente `x.n + 1` figli**
    
- Quindi `x.c[i]` è **sempre definito** e valido

---
## Complessità

### Computazionale (in RAM)

- Per ogni nodo:
    
    - loop `while`: al più `x.n = 2t - 1 ⇒ O(t)` confronti
        
- Numero di nodi visitati: **altezza `h`** dell’albero
    
- Totale:
    
    $\mathcal{O}(h \cdot t) = \mathcal{O}(t \cdot \log_t{n})$

### Input/Output (memoria secondaria)

- Ogni accesso al figlio comporta un `DiskRead`:
    
    - Numero massimo di accessi: **una per livello** ⇒ $\mathcal{O}(h)$
        
    - Quindi:
        
        $\mathcal{O}(\log_t{n})$


---

## Osservazioni

- La **dipendenza da `t` è forte**: più `t` è grande, meno profondi saranno gli alberi, quindi meno accessi a disco.
    
- Questo è **il motivo principale** per cui i B-Tree sono usati in ambienti con accesso lento alla memoria secondaria (DBMS, filesystem, ecc.).