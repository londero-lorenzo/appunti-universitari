---
title: Operazioni di Input-Output
aliases:
  - Operazioni di Input-Output
tags:
  - B-Tree
  - osservazioni
  - operazioni-di-input-output
created: 2025-06-12
---
## 💾 Operazioni di Input/Output nei B-Tree

Poiché la struttura dati [[b-tree|B-Tree]] risiede tipicamente nella **memoria secondaria** (es. disco), ogni operazione coinvolge due fasi:

- 📤 **Operazioni di I/O**: lettura e scrittura di nodi dalla/alla memoria secondaria.
- 🧠 **Operazioni di CPU**: manipolazione dei dati nella memoria principale (RAM).

---

## 🧮 Due tipi di costo asintotico

Poiché i due tipi di operazioni possono avere costi molto diversi, si distinguono due **ordini di grandezza**:

- 💾 **Costo di I/O** (lettura/scrittura):  
  $\mathcal{O}(\text{funzione legata a accessi su disco})$

- 🧠 **Costo CPU** (in memoria centrale):  
  $\mathcal{O}(\text{funzione legata a operazioni logiche})$

> ⚠️ **Osservazione importante**:  
> In architetture moderne, **le operazioni di I/O sono molto più costose** di quelle CPU.  
> **Obiettivo principale** → **minimizzare le operazioni di I/O**.

---

## 🧪 Esempio di confronto tra due procedure

Supponiamo di avere due procedure:

- ### 🅰️ Procedura A
  - 💾 I/O: $\mathcal{O}(f(t,n))$
  - 🧠 CPU: $\mathcal{O}(g(t,n))$

- ### 🅱️ Procedura B
  - 💾 I/O: $\mathcal{O}(k(t,n))$
  - 🧠 CPU: $\mathcal{O}(r(t,n))$

Se:
- $f(t,n), g(t,n), k(t,n), r(t,n) \in \Theta(\log_t n)$  
- Le differenze stanno solo nelle **costanti moltiplicative**, allora...

### ✅ Scelta ottimale
Si preferisce la procedura con **minor costo di I/O**, anche se ha un leggero costo CPU superiore:

$$
\text{(meglio) }f(t, n) = 6\log_t n \quad\quad\quad\quad\quad\quad\quad\quad\quad \\
k(t, n) = 10\log_t n
$$

---

## 🎯 Conclusione

- Minimizzare le **operazioni di I/O** è **fondamentale** per efficienza nei B-Tree.
- Il numero di accessi a disco domina il tempo totale.
- Le **analisi devono sempre separare** i costi di I/O da quelli CPU.
