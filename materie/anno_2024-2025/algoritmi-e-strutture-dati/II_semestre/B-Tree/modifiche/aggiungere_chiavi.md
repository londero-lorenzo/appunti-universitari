---
title: Aggiungere Chiavi
aliases:
  - Aggiungere Chiavi
tags:
  - B-Tree
  - modifiche
  - aggiungere-chiavi
created: 2025-06-13
---
# Aggiungere Chiavi a un Nodo in B-Tree

Durante la cancellazione in un B-Tree, è necessario assicurarsi che ogni nodo visitato **non abbia meno di `t` chiavi** prima di scenderci. Questa operazione evita violazioni delle proprietà del B-Tree ed è progettata per **minimizzare il numero di operazioni I/O** (letture/scritture disco).

## 🎯 Obiettivo

> Garantire che ogni nodo su cui si scende contenga **almeno `t` chiavi**, effettuando **una sola camminata (accesso disco) per nodo**.
> 
## 📌 Contesto

- Siamo in una fase in cui stiamo per visitare un nodo `y` con **solo `t-1` chiavi**, il che non è accettabile per procedere in sicurezza con la cancellazione.
    
- Il nodo padre `x` contiene almeno `t` chiavi, quindi può essere usato come ponte per ribilanciare.
    
- Gli altri figli di `x`, adiacenti a `y`, sono:
    
    - `z` = fratello sinistro di `y` (`x.c[i-1]`)
        
    - `w` = fratello destro di `y` (`x.c[i+1]`)

---

## ⚙️ Strategie di Ribilanciamento

> **Obiettivo comune**: portare `y` ad avere **almeno `t` chiavi** prima di scenderci.

### ✅ Caso 1 — Il fratello sinistro `z` ha più di `t-1` chiavi

- **Azione:**
    
    - Sposta la chiave `b = x.key[i-1]` da `x` a `y`
        
    - Sposta la chiave `a = z.key[z.n]` da `z` a `x`
        
    - Se esistono figli (i nodi non sono foglie):
        
        - Sposta il figlio destro di `z` (`z.c[z.n + 1]`) come primo figlio di `y`
	 ![[algoritmi-e-strutture-dati/II_semestre/B-Tree/b-tree_schema.md#^frame=UaQ8CQbHa72XU93G6enYn|100%]]
### ✅ Caso 2 — Il fratello destro `w` ha più di `t-1` chiavi

- **Azione:**
    
    - Sposta la chiave `d = x.key[i]` da `x` a `y`
        
    - Sposta la chiave `c = w.key[1]` da `w` a `x`
        
    - Se esistono figli:
        
        - Sposta il figlio sinistro di `w` (`w.c[1]`) come ultimo figlio di `y`
	![[algoritmi-e-strutture-dati/II_semestre/B-Tree/b-tree_schema.md#^frame=2UrygGefYtxrEa8blep7V|100%]]
### 🔁 Caso 3 — Entrambi `z` e `w` hanno esattamente `t-1` chiavi

- **Azione:**
    
    - Esegui `B-MERGE(x, i)` unendo `y`, `x.key[i]` e `w`
        
    - Risultato: `y` contiene tutte le chiavi/figli di `y`, `x.key[i]`, `w`
        
    - `x` perde una chiave e un figlio
	 ![[algoritmi-e-strutture-dati/II_semestre/B-Tree/b-tree_schema.md#^frame=gjdYw41Mq3HCZhMXYV__B|100%]]
## 📚 Considerazioni Finali

- Queste operazioni assicurano che, **prima di entrare in un nodo durante la cancellazione**, esso **non avrà mai meno di `t` chiavi**.
    
- Si evita il caso in cui ci si ritrova in fondo all’albero con un nodo troppo piccolo e si debba risalire o eseguire ribilanciamenti complessi.
    
- L’ordine di preferenza è:
    
    1. Prendere da un fratello ricco (`z` o `w`)
        
    2. Fondere con un fratello povero (`B-MERGE`)