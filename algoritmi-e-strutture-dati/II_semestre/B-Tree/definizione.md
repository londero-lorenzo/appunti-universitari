---
title: Definizione
aliases:
  - Definizione
tags:
  - B-Tree
  - definizione
created: 2025-06-12
---
---
# 🌳 B-Tree di grado $t \geq 2$

Un **B-Tree** $T$ di grado $t \geq 2$ è una struttura dati ad albero bilanciato utilizzata per gestire grandi quantità di dati ordinati. Ogni nodo `x` contiene:

## 🧱 Campi di un nodo `x`


- `x.n` — numero di chiavi memorizzate nel nodo.
- `x.key[1...x.n]` — array ordinato di chiavi.
- `x.c[1...x.n+1]` — array di puntatori ai figli (lungh. $2t$ al massimo).
- `x.leaf` — booleano, `true` se `x` è una foglia, `false` altrimenti.

> **Nota**: le chiavi sono memorizzate in ordine strettamente crescente:
$$
x.key[1] < x.key[2] < \dots < x.key[x.n]
$$


### ⚠️ Attenzione
> Non ho il  puntatore `x.parent`

Da `x` posso solo scendere verso i figli.
##### Perché?
> _Stiamo cercando di rendere minimo il numero di camminate `radice-foglia` che facciamo, in tutte le procedure che faremo cercheremo di utilizzare una chiamata `radice-foglia` e quindi non abbiamo bisogno di risalire verso il padre._


---

### ⚠️ Vincoli sui nodi

- Se `x` è **radice**, allora:
  $$
  1 \leq x.n \leq 2t - 1
  $$

- Se `x` **non** è radice:
  $$
  t - 1 \leq x.n \leq 2t - 1
  $$

---

## 🔗 Relazioni tra chiavi e sottoalberi

Per ogni nodo interno `x` e per ogni indice $i$ tale che $1 \leq i \leq x.n$:
- Tutte le chiavi nel sottoalbero radicato in `x.c[i]` sono **strettamente maggiori** di `x.key[i-1]` e **strettamente minori** di `x.key[i]`.

---

## 🧬 Proprietà strutturali del B-Tree

- Tutte le **foglie si trovano allo stesso livello** (profondità uniforme). ^c40b63
- L'altezza dell'albero è $O(\log_t n)$, dove $n$ è il numero totale di chiavi memorizzate.

---

## 🖼️ Riferimento visuale
![[algoritmi-e-strutture-dati/II_semestre/B-Tree/b-tree_schema.md#^frame=eOT-U4wqS5absuZtg7-1i|100%]]


---

