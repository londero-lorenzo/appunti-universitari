---
title: "Logical Design"
aliases: ["Logical Design"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "logical-design"]
created: 2026-03-10
---
# Analisi delle ridondanze
- Informazione che può essere derivata da altri dati.
- Schema ER può contenere varie forme di ridondanza
- decisione di mantenere o cancellare la ridondanza si fa comparando il costo delle operazioni che coinvolge l'informazione ridondante e la memoria richiesta

# Rimozione generalizzazioni/specializzazioni
- Si deve trasformare in relazioni tra entità
## Totale
1.
- rimuovo i figli e metto tuti gli attributi al genitore
- uso un attributo tipo (un per figlio)
- info dei figli diventano opzionali
2.
- rimuovere il genitore e spostare le info tutte ai figli
- con overlap potremmo avere inconsistenza
3.
- tengo sia genitori che figli

# Partizionare entità e relazioni

# Rimozione degli attributi composti

# Selezione chiavi primarie
- no attributi con valori nulli
- uno o più attributi
- identificatore interno con qualche attributo è preferibile ad uno esterno
- un identificatore che è usato da molte operazioni 


# Traduzione in uno schema logico

## Entità
- entità sono tradotte in relazioni singole
- dobbiamo inserire not-null e unique constraints quando è necessario

## Mappare relazioni 1-1
Distinguiamo 3 casi:
1. Caso (1,1) - (0, 1)
		E1(PK1, A1) - (1,1) - R(A) - (0,1) - E2(PK2, A2)
		E1(PK1,A1)
		E2(PK2, A2, PK1)
	- (,1)ogni entità di E1 deve essere coinvolta almeno una volta 
	- PK1 deve essere UNIQUE
	- (,1)e2 può essere coinvolta al massimo una volta
	- (0,)non è obbligatorio che tutte le istanze di E2 partecipino
		- devo garantire che PK1 possa essere NULL
	- (1,)ogni istanza di E1 deve essere coinvolta nella relazione
	E1(PK1, A1, PK2)
	E2(PK2, A2)
	- (,1) su E1: PK1 è la primary key
	- (,1) su E2: E2 può essere coinvolta al più una volta nella relazione
		- vincolo UNIQUE
	- ogni tupla di E1 deve essere coinvolta nella relazione
		- NOT NULL su PK2
	- se ho istanze di PK2 non coinvolte il vincolo rimane soddisfatto

2. Caso (0,1) - (0,1)
	E1(PK1, A1, PK2)
	E2(PK2, A2)
	- (,1) su E1: 
	- (,1) su E2: PK2 è UNIQUE in E1
	- (0,) su E1: allora l'attributo chiave esterna PK2 avrà NULL

Definisco 3 relazioni:
- E1(PK1, A1)
- E2(PK2, A2)
- R(<u>PK1</u>, <u>PK2</u>) non devo mettere entrambi gli attributi come chiave basta uno

## Uno - molti
1. (0,1) - (0,N)
	E1(<u>PK1</u>, A1, PK2)
	E2(PK2, A2)
	- (,1) su E1: PK1 è unique
	- (,N) su E2: PK2 non è UNIQUE (ci sono due istanze differenti di E1 che si riferiscono entrambe alla stessa istanza di E2)
	- (0,) su E1: PK2 potrebbe essere NULL
	- (0,) su E2: possono esistere delle entità di E2 che non sono coinvolte
2. (1,1) - (0,N)
	E1(PK1, A1, PK2)
	E2(PK2, A2)
	- (,1) su E1: PK1 UNIQUE
	- (,N) su E2: PK2 non è UNIQUE
	- (1,) su E1: PK2 è NOT NULL
	- (0,) su E2: possono esistere delle entità di E2 che non sono coinvolte
3. (0,1) - (1,N)
	E1(PK1, A1, PK2)
	E2(PK2, A2)
	- (,1) su E1: PK1 UNIQUE
	- (,N) su E2: PK2 non è UNIQUE
	- (0,) su E1: PK2 può essere NULL
	- (1,) su E2: NON ESPRIMIBILE
4. (1,1) - (1,N)
	E1(PK1, A1, PK2)
	E2(PK2, A2)
	- (,1) su E1: PK1 UNIQUE
	- (,N) su E2: PK2 non è UNIQUE
	- (1,) su E1: PK2 è NOT NULL
	- (1,) su E2: NON ESPRIMIBILE
## Molti a molti
1. (0,N) - (0,N)
	E1(PK1, A1)
	E2(PK2, A2)
	R(PK1, PK2)
	- gia tutto giusto
2. (0,N) - (1,N)
	E1(PK1, A1)
	E2(PK2, A2)
	R(PK1, PK2)
	- 1 è problematico
3. (1,N) - (1,N)
	E1(PK1, A1)
	E2(PK2, A2)
	R(PK1, PK2)
	- tutti gli 1 sono problematici

# Categoria
![[materie/anno_2025-2026/basi_di_dati/basi_dei_dati.excalidraw.md#^frame=66YVukM3|100%]]
