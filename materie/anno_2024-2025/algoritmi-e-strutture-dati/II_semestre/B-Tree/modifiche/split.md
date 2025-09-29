---
title: Split
aliases:
  - Split
tags:
  - B-Tree
  - modifiche
  - split
created: 2025-06-12
---
## ✂️ Procedura BTREE-SPLIT

Siano `x`, `y` due nodi di un [[b-tree|B-Tree]] di grado `t`, con:
- `x`: **nodo interno non pieno**
- `y`: **i-esimo figlio di `x`**, **pieno** (`y.n = 2t - 1`)

Allora la procedura `BTREE-SPLIT(x, y, i, t)`:

1. 🆕 **Crea un nuovo nodo** `z`
2. 🔁 Copia `z.leaf ← y.leaf`
3. 🧩 Imposta `z.n ← t - 1`
4. 🗝️ Copia in `z.key[1..t-1]` le **ultime `t-1` chiavi** di `y`
5. 🌿 Se `y` **non è foglia**, copia in `z.c[1..t]` gli **ultimi `t` figli** di `y`
6. ✂️ Riduce `y.n ← t - 1`
7. 🔄 Sposta verso destra le chiavi `x.key[i..x.n]` e i figli `x.c[i+1..x.n+1]` di una posizione
8. ⬆️ Inserisce `y.key[t]` in `x.key[i]`
9. ➕ Inserisce `z` in `x.c[i+1]`
10. 🔼 Incrementa `x.n ← x.n + 1`
11. 💾 Scrive `x`, `y`, `z` su memoria secondaria (disco)

📌 Rappresentazione grafica:  
![[algoritmi-e-strutture-dati/II_semestre/B-Tree/b-tree_schema.md#^frame=keTxvWyiMTS8bQQlZVcB5|100%]]

---


### BTREE-SPLIT
```c
BTREE-SPLIT(x, y, i, t) {
    // y è l’i-esimo figlio di x (x.c[i] = y)
    // y è pieno (y.n == 2t - 1)
    // x non è pieno

    // 1. Alloca nuovo nodo z
    z = ALLOCATE-NEW-NODE(t)
    z.leaf = y.leaf
    z.n = t - 1

    // 2. Copia ultime t-1 chiavi di y in z
    for (j = 1; j <= t - 1; j++) {
        z.key[j] = y.key[j + t]
    }

    // 3. Se y non è foglia, copia gli ultimi t figli
    if (!y.leaf) {
        for (j = 1; j <= t; j++) {
            z.c[j] = y.c[j + t]
        }
    }

    // 4. Riduci il numero di chiavi in y
    y.n = t - 1

    // 5. Sposta le chiavi di x per fare spazio a y.key[t]
    for (j = x.n; j >= i; j--) {
        x.key[j + 1] = x.key[j]
    }
    x.key[i] = y.key[t] // chiave centrale che sale in x

    // 6. Sposta i puntatori ai figli di x
    for (j = x.n + 1; j >= i + 1; j--) {
        x.c[j + 1] = x.c[j]
    }
    x.c[i + 1] = z

    // 7. Aggiorna numero di chiavi in x
    x.n = x.n + 1

    // 8. Salva i nodi su disco
    DISK-WRITE(x)
    DISK-WRITE(y)
    DISK-WRITE(z)
}

```

## 📊 Complessità

- 🧠 CPU: $\mathcal{O}(t)$  
  (*Copia di vettori di chiavi e figli*)
- 💾 R/W: $\mathcal{O}(1)$  
  (*Numero fisso di operazioni di lettura/scrittura: 3 nodi → `x`, `y`, `z`*)

📚 Riferimento: *Introduction to Algorithms*, 4th ed., Cormen et al., p. 504
