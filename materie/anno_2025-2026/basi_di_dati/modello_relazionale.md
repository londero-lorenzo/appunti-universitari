---
title: "Modello Relazionale"
aliases: ["Modello Relazionale"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "modello-relazionale"]
created: 2026-03-04
---
**References** tra dati in relazioni diverse sono rappresentate dalla media dei valori del dominio


| RegNum | Surname | FirstName | BirthDate  |
| ------ | ------- | --------- | ---------- |
| 6554   | Rossi   | Mario     | 5/12/1978  |
| 8765   | Neri    | Paolo     | 3/11/1976  |
| 9283   | Verdi   | Luisa     | 12/11/1979 |
| 3456   | Rossi   | Marisa    | 1/2/1978   |

| Student | Grade | Course |
| ------- | ----- | ------ |
| 3456    | 30    | 04     |
| 3456    | 24    | 02     |
| 9283    | 28    | 01     |
| 6554    | 26    | 01     |

| Code | Title   | Tutor |
| ---- | ------- | ----- |
| 01   | Analisi | Neri  |
| 02   | Chimica | Bruni |
| 04   | Chimica | Verdi |

## Definizioni
### Schema della relazione
Un nome di una relazione $R$ con un set di attributi $A\_1,...,A\_n$
$$
R(A\_1,...,A\_n)
$$
### Schema del database
Set di schemi di relazione con nomi differenti:
$$
R=\{R(X\_1),...R(X\_n)\}
$$

### Relazione su uno schema della relazione
set $r$ di tuple su $X$

### Database su uno schema del database
$$
R=\{R(X\_1),...R(X\_n)\}:
$$
set di relazioni $r=\{r\_1,...,r\_n\}$ (con $r\_i$ relazioni su $R\_i$)

# Inormazioni incomplete
## Soluzioni
**Non** si usano valori di dominio (zero, 99, stringa vuota) per rappresentare la mancanza di informazioni

Tecnica usata:
- **null value**: valore speciale che denota l'assenza di un valore del dominio
- una tupla su $X$ è una funzione che associa a ogni $A\in X$ un valore dal dominio $dom(A)$ o NULL

**Tipi di valore nullo:**
- **unknown value:** c'è un valore del dominio ma non è conosciuto
- **valore non esistente:** l'attributo non è applicabile per la tupla
- **no-information value:** non sappiamo se un valore esiste o no
	- questa è la disgiunzione degli altri due 
>[!warning]
>DBMSs non distinguono fra i tipi: adottano implicitamente la **no-information value**.

# Come prevenire istanze senza significato ?

| RegNum | Name  | Course | Grade | Honours |
| ------ | ----- | ------ | ----- | ------- |
| 6554   | Rossi | B01    | K     |         |
| 8765   | Neri  | B03    | C     |         |
| 3456   | Verdi | B04    | B     | honours |
| 3456   | Rossi | B03    | A     | honours |


- Scala di valutazione sono compresi tra A e F
- lode può essere presa solo con il voto A
- vari studenti devono avere diversi numeri di registrazione
- esami devono riferirsi a corsi esistenti

## Integrity constraints

- Per preservare la consistenza e la qualità dell'informazione memorizzata nel database si definisce **vincoli di integrità**: limitando i dati che possono essere memorizzati nelle tabelle
- **Intra-relational** constraints:
	- Not-null constraint
	- Uniqueness constraint
	- Primary key
	- General tuple-level constraints
- **Inter-relational** constraints:
	- Foreign key
- Alcuni vincoli sono **impliciti** dal modello dei dati
### Vincoli di tuple
- Esprimono **condizioni sui valori di ogni tupla**
- **Vincoli di dominio**: vincolo di tuple che coinvolge un singolo attributo
	- (Grade $\geq$ "A") AND (Grade $\leq$ "F")
- Vincolo di tuple
	- (NOT (Honours = "honours")) OR (Grade = "A")

#### Not-null constraint

- definito su **una colonna**: **proibisce** valori **null**
>[!example]
>Prendiamo una colonna di una tabella e poniamo il vincolo VNN: {column}: le righe con valore **null** nella suddetta colonna non verranno rifiutate
#### Uniqueness constraint
- vincolo di unicità può essere definita su **una o più colonne**
- obbliga i valori di una colonna o gruppi di colonne ad **essere unico tra le righe della tabella**
	- example: in una tabella con le informazioni su degli hotel possiamo impedire la presenza di più hotel che sono nella stessa città che abbiano lo stesso nome
	- definiamo un vincolo di unicità sul gruppo di colonne UNIQUE: {(Nome_albergo, Città)}
	- diverso da definire due vincoli di unicità su Nome_albergo e su Città: UNIQUE: {(Nome_albergo), (Città)}

#### Primary Key contraint
- Alcuni attributi giocano un ruolo fondamentale
- conoscendo il loro valore è possibile **identificare unicamente una tupla dentro una tabella**

**Definizione:**
- Dato $R(X)$ $K\subseteq X$
- $K$ è una **superkey** di $R$ se i valori per $K$ sono sufficienti per identificare in un unico modo qualsiasi tupla
- Superchiave $K$ è una chiave candidata se $K$ è minimale
	- **Minimale**: se rimuoviamo un attributo da $K$ allora non è più una superchiave
- Una delle chiavi candidate è scelta come **chiave primaria**
	- di solito la più piccola
	- nello schema la sottolineiamo

**Esistenza e importanza delle chiavi**
- relazioni sono set
