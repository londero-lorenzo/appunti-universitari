---
title: Albero Binario di Ricerca
aliases:
  - Albero Binario di Ricerca
tags:
  - II-semestre
  - BST
  - albero-binario-di-ricerca
created: 2025-06-01
---

Un **albero binario di ricerca** (BST) è una struttura dati binaria dove, per ogni nodo `x`, valgono le seguenti proprietà:

- `x.left.key ≤ x.key ≤ x.right.key`
- Entrambi i sottoalberi (sinistro e destro) sono anch’essi BST

[[algoritmi-e-strutture-dati/II_semestre/BST/definizione|→ Vedi definizione formale]]

---

## 🔍 Operazioni di ricerca

Queste operazioni sfruttano la struttura ordinata dell'albero:

- [[ricerca_di_una_chiave|Ricerca di una chiave specifica]]
- [[ricerca_del_massimo|Ricerca del massimo]]
- [[ricerca_del_minimo|Ricerca del minimo]]
- [[ricerca_del_successore|Successore In-Order]]
- [[ricerca_del_predecessore|Predecessore In-Order]]

---

## 🔄 Operazioni di modifica

Le seguenti procedure modificano la struttura del BST preservandone le proprietà:

- [[algoritmi-e-strutture-dati/II_semestre/BST/modifiche/Inserimento|Inserimento di una nuova chiave]]
- [[algoritmi-e-strutture-dati/II_semestre/BST/modifiche/cancellazione|Cancellazione di una chiave esistente]]

---

## 📚 Visite dell’albero

Utili per visualizzare i dati in vari ordini:

- [[visita_in-order|Visita In-Order]] (output ordinato)
- [[visita_pre-order|Visita Pre-Order]]
- [[visita_post-order|Visita Post-Order]]

---

## ⏱️ Complessità

- Altezza `h` dell’albero domina le operazioni: ricerca, inserimento, cancellazione
- Caso peggiore (degenere): `h = n` ⇒ ($\Theta(n)$)
- Caso ideale (bilanciato): `h = \log n` ⇒ ($\Theta(\log n)$)
