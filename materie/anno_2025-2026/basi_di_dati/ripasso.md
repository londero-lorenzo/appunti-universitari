---
title: "Ripasso"
aliases: ["Ripasso"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "ripasso"]
created: 2026-03-03
---
# Conceptual Design
- Visione astratta del contenuto della base di dati
- schema + annotazioni scritte

Modello entità relazione descrive:
- Entity sets
- Relationship sets
- Attributes
## Entity sets
- oggetti distinguibili
- Attributi: proprietà di ogni membro dell'entity set
- sono insiemi quindi non posso avere elementi ripetuti

## Relationship sets
- relazione = associazione tra varie entità
	- Professore --- Insegna --->Corsi
- $R\subseteq E x $

### Notazioni per relazioni ternarie
- cardinalità ci dice come ogni entità partecipa
	- un professore può insegnare più corsi
	- un corso può usare più libri
- se un professore insegna usando solo un libro in un determinato corso l'istanza di libro sarà 1
- se professore e corso hanno N vuol dire che possono usare anche dei libri usati da altri professori/corsi
- per le relazioni ricorsive se non sono simmetriche è utile aggiungere i **ruoli**

## Entità deboli
>[!example]
>- ci possono essere hotel con lo stesso nome in diverse città
>- per tenere traccia degli hotel il nome non basta
>- per identificarlo usiamo nome hotel + nome città in cui si trova

>[!definition]
>Reificazione
>> Possiamo rimpiazzare una relazione ternaria con un entity set e 3 relationship sets

## Specializzazione
- Veicolo si specializza in macchina/camion
### Totale
- tutti i genitori devono essere mappati in uno o più figli sotto
- no entità generiche
### Parziale
- Alcune entità possono rimanere generiche
### Disgiunto
- Al più posso far parte di uno solo dei figli
### Overlap
- puoi far parte di più di uno dei figli
- es. Person può essere persona con diploma/ persona con degree ma anche nessuno dei due 
# Design patterns
## Instance of construct
>[!example]
>- Libro: un libro virtuale con ISBN
>- Volume: la copia fisica del libro 

>[!warning]
>Instance of è diverso da part of
>- Instance of è usato di solito per relazioni 1 a molti
>- non dovremmo usare entità deboli se l'entità ha un esistenza autonoma:
>	- una sala del cinema è parte di un'entità cinema

### Relazioni multiple tra entità
- nell'esempio studente/esame dobbiamo usare la reificazione per fare in modo che lo studente possa dare più di una volta l'esame per un corso
## Managing history - Entities
- Validità iniziale < Validità finale
- un cliente deve apparire una volta come Customer (current)
- un cliente deve apparire più volte come Customer (history)

# Documentazione degli E-R
- Se c'è un ciclo devo verificare non sia un problema
## Business rules
- **Assertions**
	- nella forma: *concept* must / must not *expression over the concepts*
- **Derivations**
- **Enforcement**
