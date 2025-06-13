---
title: Cancellazione
aliases:
  - Cancellazione
tags:
  - B-Tree
  - modifiche
  - cancellazione
created: 2025-06-12
---
# ❌ Cancellazione in B-Tree

Data una chiave `k` da rimuovere da un [[b-tree|B-Tree]] `T` di grado `t`, la procedura `BTREE-DELETE(T, k)` elimina `k` preservando tutte le proprietà strutturali del B-Tree.

📌 A differenza dell'inserimento, **non si conosce a priori il nodo** contenente `k`: è necessario **cercarlo** partendo dalla radice.

---
## 🔢 Casi principali

### ✅ Caso 1 — `k` si trova in una **foglia**

- Spostare a sinistra tutte le chiavi successive a `k`
    
- Decrementare `x.n` di 1
    

📷 _Schema di supporto:_  
![[algoritmi-e-strutture-dati/II_semestre/B-Tree/b-tree_schema.md#^frame=LrHS50gbzt3oB84P-_PT4|80%]]

---

### ✅ Caso 2 — `k` si trova in un **nodo interno**

#### 🔁 Idea generale:

Sostituire `k` con il **suo predecessore** o **successore** e cancellare ricorsivamente quest’ultimo da un sottoalbero foglia (o comunque più basso).

#### 🔨 Tre sotto-casi:

- Se il **figlio sinistro `z`** ha almeno `t` chiavi:
    
    - Trova il **predecessore** di `k` in `z`
        
    - Sostituisci `k` con il predecessore
        
    - Cancella ricorsivamente il predecessore in `z`
        
- Se il **figlio destro `w`** ha almeno `t` chiavi:
    
    - Trova il **successore** di `k` in `w`
        
    - Sostituisci `k` con il successore
        
    - Cancella ricorsivamente il successore in `w`
        
- Se **entrambi** hanno solo `t-1` chiavi:
    
    - Esegui `B-MERGE(z, k, w)`
        
    - Scendi ricorsivamente nel nodo fuso (che ora contiene `2t - 1` chiavi) per cancellare `k`
        

📷 _Schema di supporto:_  
![[algoritmi-e-strutture-dati/II_semestre/B-Tree/b-tree_schema.md#^frame=NpatL0t_qUI3Jdo6BFH9e|80%]]

---

### ✅ Caso 3 — `k` non si trova in `x`, e `x` non è foglia

Occorre decidere **in quale figlio `y` scendere** per continuare la ricerca.

#### ⚠️ Prima di scendere:

Verificare se `y` ha **almeno `t` chiavi**. Se non le ha, **bisogna "aggiungerle" usando le tecniche di** [[aggiungere_chiavi#Come aggiungere chiavi ad un nodo?|aggiunta chiavi]].

#### 🔨 Tre sotto-casi:

- Se `y` ha almeno `t` chiavi → si scende direttamente
    
- Se `y` ha solo `t-1` chiavi:
    
    - Se un fratello ha ≥ `t` chiavi, **si ribilancia** (vedi: "Aggiungere chiavi")
        
    - Se entrambi i fratelli hanno `t-1` chiavi → si esegue `B-MERGE`
        

📷 _Schema di supporto:_  
![[algoritmi-e-strutture-dati/II_semestre/B-Tree/b-tree_esempi.md#^frame=FeoNCVdQIPgu_8XaYl6Cd|100%]]

---

## 🔗 Collegamenti utili

- 📄 [[aggiungere_chiavi|Aggiungere chiavi ad un nodo prima di scenderci]]
    
- 📄 [[b-tree|B-Tree: definizione e proprietà]]


---

## 🧮 Complessità

### 🧠 Tempo computazionale

O(t⋅log⁡tn)\mathcal{O}(t \cdot \log_t n)O(t⋅logt​n)

- Profondità: $\log_t n$
    
- In ogni nodo si scandiscono fino a $2t - 1$ chiavi
    

### 💾 Complessità I/O

O(log⁡tn)\mathcal{O}(\log_t n)O(logt​n)

- Una lettura per ogni livello dell’albero