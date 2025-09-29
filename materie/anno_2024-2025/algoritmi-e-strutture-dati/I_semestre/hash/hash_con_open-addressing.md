---
title: "Hash con Open-Addressing"
aliases: ["Hash con Open-Addressing"]
tags: [università, "algoritmi-e-strutture-dati", "I-semestre", "hash", "hash-con-open-addressing"]
created: 2025-07-14
---
>[!abstract]
>Questa sezione si occupa di definire l'hash gestito con Open Addressing

>[!note] Con Chaining:
>Non so a priori quanto spazio occuperò

>[!note] Con Open-Addressing
>- Fisso a priori lo spazio che dedicherò alla tabella
>- Non utilizzo nessuna struttura dati esterna alla tabella
>- Dato $x$ calcolo $h(x.key)$ e memorizzo $x$ in $T[h(x.key)]$



>[!question] Cosa faccio se è già occupata?
>C'è il problema della sovrascrittura, quindi serve una sequenza di scansione

## Funzione di Hash con sequenza di scansione

![[algoritmi-e-strutture-dati/I_semestre/hash/hash.excalidraw.md#^frame=I_ImWLqu09HAbnDqDkTWZ|100%]]

>[!question] Che proprietà ha la sequenza generata?
>- non deve contenere ripetizioni
>- deve essere una permutazione degli indici [^1]
>
[^1]: compaiono tutti i numeri compresi tra $0.. m-1$

## Operazioni

Sia $|T| = m$ e $h$ funzione di hash con scansione lineare:
### Cancellazione:

Per cancellare devo scrivere `DEL` 
 - `DEL`è come `NIL` se devo inserire.
 - `DEL` è come una cella occupata per la ricerca

### Ricerca:
La ricerca di $x$ prosegue fino a che:
- trovo $x$ -> $x\in T$  _oppure_
- trovo `NIL` -> $x\not\in T$

## Funzioni di Hash

### Lineare
$$
h(key, i) = (h_1(key) + i)\mod m
$$
Questa funzione genera $\Theta(m)$ sequenze di scansione.
Se vale l'Ipotesi di Hashing Uniforme il **costo nel caso medio** per inserimento, ricerca e cancellazione vale $\Theta(1)$

## Double Hashing
$$
h(key, i) = (h_1(key) + i\cdot h_2(key)) \mod m
$$
Considerazioni:
- $h_1(key)$ -> posizione iniziale
- $h_2(key)$ -> offset dei tentativi, si raccomanda coprimo con $m$

### Casi
- primo caso:
	 - $m = 2^n \text{ con } n \in \mathbb{N}$
	 - $h_2(key) \in 2\mathbb{N} + 1$
- secondo caso:
	- $m$ primo
	- $h_2(x)\in \{n\in\mathbb{N}: n \lt m\}$

In questi due casi vengono prodotte $\Theta(m^2)$ sequenze di scansione

### Scansione quadratica
$$
h(key, i) = (h_1(key) + c_1{i} + c_2{i^2})\mod m
$$

