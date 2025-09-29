---
title: Esercizi
aliases:
  - Esercizi
tags:
  - insiemi-disgiunti
  - esercizi
  - esercizi
created: 2025-06-14
---
# Es 21/06/2016 -- Somma

Usiamo liste o alberi?

## Liste con W.U con l'aggiunta della somma + somma aggiornata solo nel rappresentante

costo find + costo delle union  $O(m + n\cdot\log{n})$ 

## Alberi con Union by Rank e PC

+ campo somma aggiornato solo per il rappresentante

costo: $O(m\cdot\alpha(n, m))$ conveniente quando m non è tanto più grande di n.

m = $\Theta(n)$ -> costo: $\Theta(n) \cdot \text{qualcosa simile ad una costante}$



#todo aggiungere le operazioni modificate quindi `make` `union`