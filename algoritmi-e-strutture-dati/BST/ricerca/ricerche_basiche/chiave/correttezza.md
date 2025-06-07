---
title: "Correttezza"
aliases: ["Correttezza"]
tags: [università, "algoritmi-e-strutture-dati", "BST", "ricerca", "ricerche-basiche", "chiave", "Correttezza"]
created: 2025-06-04
---
L'algoritmo `BSTSearchNode(x, k)` restituisce il nodo contenente la chiave `k` se esiste nel sottoalbero radicato in `x`, altrimenti restituisce `NIL`.

**Struttura della dimostrazione**

- **Base dell'induzione**: albero di profondità 0 (cioè solo il nodo `x`, o `x = NIL`)
    
- **Passo induttivo**: assumiamo che l'algoritmo sia corretto per alberi di profondità ≤ `h`, e dimostriamo che è corretto per profondità `h+1`.
    


**Base dell’induzione**: profondità 0

**Due casi:**

1. `x = NIL`:
    
    - `BSTSearchNode(x, k)` → entra nella condizione `if (x = NIL || x.key = k)` → restituisce `x` = `NIL`
        
    - Corretto: la chiave non esiste, restituisce `NIL`.
        
2. `x ≠ NIL` e `x.key = k`:
    
    - L’algoritmo ritorna `x`.
        
    - Corretto: ha trovato la chiave desiderata.
        

Quindi l’algoritmo funziona correttamente per alberi di profondità 0.


**Passo induttivo**: ipotesi per profondità ≤ `h`, dimostrazione per `h+1`

**Ipotesi induttiva:**

Supponiamo che per ogni nodo `x` che radica un albero di profondità **≤ h**, `BSTSearchNode(x, k)` funzioni correttamente.

**Caso: albero con radice `x` e profondità `h+1`**

Tre casi possibili:



**Caso 1:** `x = NIL`

- Restituisce `NIL`.
    
- Corretto: sottoalbero vuoto ⇒ chiave non presente.
    


**Caso 2:** `x.key = k`

- L’algoritmo restituisce `x`.
    
- Corretto: ha trovato il nodo desiderato.
    


**Caso 3:** `x.key ≠ k`

- Se `k < x.key`, per proprietà del BST, **se `k` esiste, deve essere nel sottoalbero sinistro**.
    
    - L’algoritmo chiama `BSTSearchNode(x.left, k)`
        
    - `x.left` ha profondità ≤ `h` → per ipotesi induttiva, la chiamata funziona correttamente.
        
- Se `k > x.key`, analogamente cerca nel sottoalbero destro.
    

Quindi, in entrambi i casi l’algoritmo chiama ricorsivamente una versione corretta della funzione, e restituisce il valore corretto.