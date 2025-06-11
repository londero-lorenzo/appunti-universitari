---
title: Esercizi
aliases:
  - Esercizi
tags:
  - RBT
  - esercizi
created: 2025-06-11
---

# Costruzione

## Es.1
Come costruire un [[red_black_tree|Red Black Tree]] contenente `n` chiavi che si trovano in un vettore `A`,

### Complessità
 $\to\mathcal{O}(n\log n)$ 

### Nota
Non si può in $\Theta(n)$ nel caso migliore, altrimenti avremmo trovato una procedura di ordinamento lineare.

Commenti:
 >_Se riuscissi a costruire sempre in tempo lineare un RBT a partire da un vettore generico, poi siccome la [[visita_in-order|Visita In-Order]] restituisce un vettore ordinato avrei ottenuto un algoritmo lineare per l'ordinamento. Abbiamo dimostrato che usando solo scambi e confronti senza ipotesi sull'input non è possibile ordinare in tempo lineare **sempre.
> Carla Piazza

## Es.2
Come costruire un [[red_black_tree|Red Black Tree]] contenente `n` chiavi che si trovano in un vettore `A` ordinato.
### Idea
![[esercizi_schizzi#^frame=65v8RgJ-t7uc8sPGLteG9|75%]]
### Complessità
$\to T(n) = 2T(\frac{n}2) + \mathcal{O}(\log n)$


## Es.3

Passare da Vettore Ordinato a [[red_black_tree|Red Black Tree]] e viceversa.
Quali operazioni sono più efficaci su Vettori Ordinati e RBT?

Assumiamo:
MinHeap vs RBT
Mi interessano:
- inserimenti
- cancellazioni
- cancellazioni del minimo

Operazioni a confronto:

| Operazioni           | MinHeap               | RBT                   |
| -------------------- | --------------------- | --------------------- |
| Inserimento          | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ |
| Cancellazione        | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ |
| Cancellazione minimo | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ |
Stessa complessità per entrambe le strutture dati.

Quindi:
### Quando conviene usare MinHeap o RBT?
> _Gli RBT vengono utilizzati nei sistemi operativi_
> 

### Da Vettore Ordinato a [[red_black_tree|Red Black Tree]]


### Da [[red_black_tree|Red Black Tree]] a Vettore Ordinato
