---
title: Definizione
aliases:
  - Definizione
tags:
  - RBT
  - definizione
created: 2025-06-09
---
# 📌 Definizione

Un [[red_black_tree|Red Black Tree]] è un [[albero_binario_di_ricerca|Albero Binario di Ricerca]] in cui **ogni nodo** ha un campo `color ∈ {RED, BLACK}`, e valgono le seguenti proprietà:

1. Le **foglie** (`NIL`) sono sempre di colore **Black**
    
2. Nessun nodo **Red** ha figli di colore **Red** ^27dda8  
    (ovvero, ogni nodo Red ha **due figli Black**)
    
3. Per ogni nodo `x`, **ogni cammino da `x` a una foglia** (`NIL`) contiene **lo stesso numero di nodi Black** ^434e76
    
4. La **radice** è **Black**  
    _(proprietà opzionale, può essere derivata dalle altre)_


---

# 📌 Implicazioni

## 🔍 Proprietà (3) solo sulla radice?

Domanda: _Cosa accadrebbe se la proprietà 3 valesse solo per la radice?_

### Risposta:

**Nulla cambia.**

Perché se un qualunque nodo `x` avesse due cammini `x → foglia` con numero diverso di nodi Black (`a ≠ b`), allora:

- Il cammino `radice → x` contiene `c` nodi Black
    
- Allora:
    
    - Cammino `radice → foglia₁`: contiene `c + a` nodi Black
        
    - Cammino `radice → foglia₂`: contiene `c + b` nodi Black
        
- Ma `c + a ≠ c + b` ⇒ **violazione della proprietà dalla radice**
    

✅ **Conclusione**: è sufficiente **verificare la proprietà 3 solo sulla radice**.


---

# 📐 Bilanciamento implicito

Le proprietà precedenti **impongono vincoli strutturali** che garantiscono:

- **Assenza di squilibri estremi**
    
- **Altezza dell’albero**: `O(log n)` rispetto al numero di nodi
    

➡️ Il Red Black Tree **rimane [[albero_bilanciato|bilanciato]]** automaticamente, senza necessità di bilanciamenti espliciti costosi.