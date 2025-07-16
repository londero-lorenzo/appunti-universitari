---
title: Hash Table
aliases:
  - Hash Table
tags:
  - I-semestre
  - hash-table
created: 2025-07-12
---
>[!abstract]
>Questa sezione esplora le problematiche di mantenere una porzione di elementi appartenenti ad un universo molto più grande. Verranno definite delle procedure per effettuare operazioni di inserimento ricerca e cancellazione su una popolazione  dinamica.

>[!definition]
>Universo
>>Universo $U$, insieme di oggetti identificati attraverso una chiave unica e distinta per ogni oggetto.

In ogni istante sono interessato a gestire (mantenere in memoria) un sottoinsieme k:
- $|K| = n << |U| = M$
- $k$ varia dinamicamente nel tempo

Voglio effettuare operazioni di ricerca inserimento cancellazione sull'insieme $k$ cercando di bilanciare i costi in tempo e spazio.

Esempio:
U universo di studenti dell'università di Udine
k universo di studenti che frequentano il costo di algoritmi e strutture dati

k << U

usiamo come chiave il numero di matricola

---
### Modo, uso vettore sovradimensionato (60 milioni) \[indirizzamento diretto\]

- uso NIL per le matricole che non seguono il corso
- uso la matricola per le matricole che seguono il corso
- Costi:
	- Ricerca: $\Theta(1)$
	- Inserimento: $\Theta(1)$
	- Cancellazione: $\Theta(1)$
	- Spazio: $\Theta(|U|) = \Theta(M)$

Cosa vorrei:
	Vorrei utilizzare Spazio $\Theta(|K|) = \Theta(n)$

---
### Proviamo a utilizzare Liste concatenate:
- Costi:
	- Spazio: $\Theta(|k|) = \Theta(n)$
	- Ricerca: $\Theta(|K|)$
	- Inserimento: $\Theta(1)$
	- Cancellazione: $\Theta(|K|)$

Entrambi i casi implicano troppo tempo.

Soluzione:
Usate le tabelle di HASH

Esistono due tipo:
- Hash con chaining
- Hash con Oper Addressing
