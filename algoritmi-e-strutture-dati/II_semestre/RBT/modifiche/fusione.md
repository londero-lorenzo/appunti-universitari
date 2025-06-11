---
title: Fusione
aliases:
  - Fusione
tags:
  - RBT
  - modifiche
  - fusione
created: 2025-06-11
---
## Fusione di due Red-Black Tree con chiave intermedia `k`

### 🧠 Obiettivo

Fondere due **Red-Black Tree** `T₁` e `T₂` utilizzando una chiave `k`, **tale che**:

- `∀ x ∈ T₁, x < k`
    
- `∀ y ∈ T₂, k < y`

### ⚠️ Vincoli

`k` deve essere una **chiave intermedia** tra tutti i nodi di `T₁` e `T₂`.

### Situazione
![[red_black_tree_schema#^group=pF_XIstADRrea-iE3Lxlp|100%]]

---
## Casi possibili

### 🍀Caso 1 — _Fortunato_

> `bh(T₁) = bh(T₂)` (altezza nera uguale)

![[red_black_tree_schema#^group=X6g_bKsmkSbga-aDtRPoV|75%]]

Si crea un nuovo nodo `k`:

- `k.left ← root(T₁)`
    
- `k.right ← root(T₂)`
    
- `k.color ← RED` o `BLACK` secondo necessità
    

In questo caso, non è necessario alcun fix se `k` è colorato correttamente.

**Costo**: Θ(1)


### 🔁 Caso 2 — _Quasi Fortunato_

> `bh(T₁) > bh(T₂)` (oppure simmetricamente `bh(T₂) > bh(T₁)`)

#### Strategia

- Si **scende** in `T₁` lungo il **figlio destro**, mantenendo traccia dei nodi attraversati
    
- Si **trova il primo nodo `x`** tale che `bh(x) = bh(T₂)`
    
- Si crea il nodo `k` come:
    
    - `k.left ← x`
        
    - `k.right ← root(T₂)`
        
    - `k.color ← RED`
        
- Si **rimpiazza `x` con `k`** nel sottoalbero di `T₁`
    
- Si applica `RB-INSERT-FIXUP` (o simile) per mantenere le proprietà RB
    

📌 **Costo**:

- **Discesa** fino a `x`: `O(log n)`
    
- **Fix-up** verso la radice: `O(log n)`
    

➡️ **Totale**: **`O(log n)`**

