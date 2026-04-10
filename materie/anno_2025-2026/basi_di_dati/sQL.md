---
title: "Sql"
aliases: ["Sql"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "sql"]
created: 2026-03-31
---
1. Risultati di proiezioni sono **multistes** più che set (di default i duplicati non sono rimossi)
2. **Valori** vs relazioni (risultato di una funziona aggregata può, in un certo contesto, essere trattata come un valore e non come una relazione)

- SELECT ⟨ list of attributes ⟩ (target list)
- FROM ⟨ list of tables ⟩
- WHERE ⟨ condition ⟩
- GROUP BY ⟨ list of attributes (grouping) ⟩
- HAVING ⟨ condition (grouping) ⟩
- ORDER BY ⟨ list of attributes ⟩

**Ordine di esecuzione:** FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY

>[!definition]
>SELECT
>>specifica gli attributi e/o le funzioni i cui valori sono ritornati dalla query

>[!definition]
>FROM
>>specifica le relazioni a cui si deve accedere per recuperare l'informazione richiesta dalla query

>[!definition]
>WHERE
>>specifica le condizioni per la selezione di tuple dalle relazioni indicate nella clausola del FROM

>[!example] Find the salary of employees whose last name is Bianco

```sql
SELECT SALARY AS SALARYBIANCO
FROM EMPLOYEE
WHERE LNAME = 'BIANCO'
```

>[!example] Retrieve all information related to employees whose last name is Bianco.

```sql
SELECT *
FROM EMPLOYEE
WHERE LNAME='BIANCO'
```

>[!example] Find the monthly salary of employees whose last name is Bianco.

```sql
SELECT SALARY / 12 AS MONTHLYSALARY
FROM EMPLOYEE
WHERE LNAME = 'BIANCO'
```

>[!example] Per ogni impiegato, ricavare il nome del dipartimento per cui lavorano.

```sql
SELECT SSN, DNAME
FROM EMPLOYEE, DEPARTMENT
WHERE DNO = DNUMBER
```

## SELECT-FROM sottoblocco e uso di DISTINCT

>[!definition]
>DISTINCT
>>applicata dopo SELECT, esclude tutte le righe duplicate, ritorna solo valori diversi nel set

>[!example] Ricavare il salario per ogni impiegato

```sql
SELECT SSN, SALARY
FROM EMPLOYEE
```

>[!example] Determinare l'ammontare dei salari dei dipendenti nell'azienda.

```sql
SELECT DISTINCT SALARY
FROM EMPLOYEE
```

## Dot notation e nomi di attributi un po' sus

>[!example] Per ogni impiegato, identificarli per nome e cognome, recuperare i numeri di progetti a cui lavorano.

```sql
SELECT EMPLOYEE, SSN, EMPLOYEE.FNAME, EMPLOYEE.LNAME, W.PNUMBER
FROM EMPLOYEE, WORKS_ON AS W
WHERE SSN = ESSN
```

>[!example] Recuperare il nome e data di nascita dei dipendenti per ogni impiegato

```sql
SELECT SSN, D.DEPENDENT_NAME, D.BDATE
FROM EMPLOYEE, DEPENDENT D
WHERE SSN = ESSN
```

## Alias e operazioni per rinominare

>[!example] Recuperare il nome e cognome dei supervisori dei dipendenti del dipartimento 10

```sql
SELECT S.FNAME, S.LNAME
FROM EMPLOYEE AS E S
WHERE E.DNO = 10 AND E.SUPER_SSN = S.SSN
```

>[!example] Trovare dipartimenti che hanno almeno una locazione in comune

```sql
SELECT DISTINCT L1.DNUMBER, L2.DNUMBER
FROM DEPT_LOCATIONS L1 L2
WHERE L1.DLOCATION = L2.DLOCATION AND L1.DNUMBER < L2.DNUMBER
```

>[!example] Ricavare il nome e cognome degli impiegati maschi che guadagnano più di 40000 euro

```sql
SELECT FNAME, LNAME
FROM EMPLOYEE
WHERE SEX = 'M' AND SALARY > 40000
```

>[!example] Determinare gli impiegati con il cognome BIANCO che lavorano per il dipartimento 2 o 3

```sql
SELECT SSN
FROM EMPLOYEE
WHERE LNAME = 'BIANCO' AND (DNO = 2 OR DNO = 3)
```

## SET operations
### 1
- UNION
- EXCEPT
- INTERSECT
Duplicati sono rimossi a meno che non sia richiesto di mantenerli (con la keyword ALL)

>[!example] Selezionare la data di nascita di tutti gli impiegati e dei loro dipendenti

```sql
SELECT BDATE
FROM EMPLOYEE
UNION
SELECT BDATE
FROM DEPENDENT
```

### 2
Se gli attributi hanno nomi diversi, una union può essere usata comunque e il risultato avrà i nomi del primo operatore.
>[!example] Selezionare i nomi e cognomi dei tutti gli impiegati

```sql
SELECT FNAME
FROM EMPLOYEE
UNION
SELECT LNAME
FROM EMPLOYEE
```

# NESTED QUERIES
Nella clausola WHERE: SQL permette di comparare un valore con il risultato di una query annidata, usando operatori di comparazione standard

>[!question] Come comparare un singolo valore con un set di valori ?
>Si usa la keyword **ANY**

## ANY

>[!example] Selezionare gli impiegati che appartengono a un dipartimento con una location a Pordenone.

```sql
SELECT *
FROM EMPLOYEE
WHERE DNO = ANY (      SELECT DNUMBER
					FROM DEPT_LOCATIONS
					WHERE DLOCATION = 'PORDENONE')
```

>[!example] Selezionare il SSN degli impiegati che hanno lo stesso cognome di un impiegato che sta lavorando per il dipartimento 10

```sql
SELECT SSN
FROM EMPLOYEE
WHERE LNAME = ANY ( SELECT LNAME
						FROM EMPLOYEE
						WHERE DNO = 10)
```

## ALL

>[!example] Selezionare tutti i dipartimenti dove nessun impiegato guadagna più di 80.000 euro

```sql
SELECT DNUMBER
FROM DEPARTMENT
WHERE DNUMBER <> ALL (SELECT DNO
						FROM EMPLOYEE
						WHERE SALARY > 80000)
```

Soluzione alternativa:
```sql
SELECT DNUMBER
FROM DEPARTMENT
EXCEPT
SELECT DNO
FROM EMPLOYEE
WHERE SALARY > 80000
```

>[!example] Selezionare gli impiegati con salario più alto

```sql
SELECT SSN
FROM EMPLOYEE
WHERE SALARY >= ALL (SELECT SALARY
					FROM EMPLOYEE)
```

Soluzione alternativa
```sql
SELECT SSN
FROM EMPLOYEE
EXCEPT
SELECT E1.SSN
FROM EMPLOYEE AS E1 E2
WHERE E1.SALARY < E2.SALARY
```

## IN

Per controllare l'inclusione o l'esclusione di un elemento/valore in un set di elementi/valori restituiti da una query.
- IN equivalente e ANY
- NOT IN equivalente a ALL

>[!example] Selezionare gli impiegati appartenenti a un dipartimento con una locazione a Pordenone.

```sql
SELECT *
FROM EMPLOYEE
WHERE DNO IN ( SELECT DNUMBER
				FROM DEPT_LOCATIONS
				WHERE DLOCATION = 'PORDENONE')
```

## Nested queries correlate e non correlate
Le nested queries sono eseguite solo una volta: il risultato non dipende dalle specifiche tuple esaminate dalla query esterna.

A volte le nested queries devono essere in grado di riferirsi a tuple delle tabelle dichiarate nell'external query: il risultato dipende dalle tuple specifiche esaminate dall query esterna.


- **First**: la nested query è valutata
- **Then:** la condizione della clausola WHERE della query più esterna è valutata

### Regole di visibilità
Gli attributi di una tabella può essere usata solo con le query in cui la tabella è dichiarata o in una nested query (ad ogni livello).

**Utilizzo di alias:** potrebbero esserci ambiguità quando ci sono più attributi con lo stesso nome, uno che appare in una tabella dichiarata nella query esterna, una che appare in una tabella dichiarata nella nested query.

**Regola di disambiguazione**: un attributo non qualificato che si riferisce alla tabella dichiarata nella **query più interna**. Per riferirsi agli attributi con lo stesso nome delle tabelle dichiarate nelle query più esterne, l'uso degli alias è necessario.

>[!example] Selezionare gli impiegati che appartengono al dipartimento di ricerca o a un dipartimento che è locato in almeno una città dove il dipartimento di ricerca è locato.

```sql
SELECT SSN
FROM EMPLOYEE
WHERE DNO IN (SELECT D1.DNUMBER
				FROM DEPARTMENT AS D1, DEPT_LOCATIONS AS L1
				WHERE D1.DNUMBER = L1.DNUMBER AND D1.DNAME = 'RESEARCH') R
	DNO IN (SELECT D2.DNUMBER
			FROM DEPT_LOCATIONS AS D2
			WHERE L1.DLOCATION = D2.DLOCATION)
```

>[!warning] Questa soluzione è sbagliata perché la tupla L1 non è visibile nella seconda nested query.


>[!example] Determinare il nome e cognome di tutti gli impiegati che hanno un dipendente del loro genere con lo stesso nome

```sql
SELECT FNAME, LNAME
FROM EMPLOYEE E
WHERE SSN IN( SELECT ESSN
			FROM DEPENDENT
			WHERE E.FNAME=DEPENDANT_NAME AND E.GENDER = GENDER)

```
>[!example] Selezionare gli impiegati che guadagnano un salario diverso da ogni altro impiegato nel dipartimento.

```sql
SELECT SSN
FROM EMPLOYEE AS E
WHERE SALARY NOT IN (SELECT SALARY
					FROM EMPLOYEE
					WHERE SSN <> E.SSN AND DNO=E.DNO)
```

### EXISTS

- Relazione non vuota: EXISTS
- Relazione vuota: NOT EXISTS

>[!example] Selezionare impiegati che non hanno dipendenti

```sql
SELECT SSN
FROM EMPLOYEE
WHERE NOT EXISTS(SELECT *
				FROM DEPENDENT
				WHERE SSN = ESSN)

```
>[!example] Ritorna il nome e cognome dei manager che hanno almeno un dipendente.


```sql
SELECT FNAME, LNAME
FROM EMPLOYEE
WHERE EXISTS (SELECT *
			FROM DEPARTMENT
			WHERE SSN = MGR_SSN) AND
		EXISTS( SELECT *
				FROM DEPENDENT
				WHERE SSN = ESSN)
```

#### INTERSEZIONE E EXCEPT tramite EXISTS
Date due relazioni R(A,B) e S(C,D)

intersezione (R S)
```sql
SELECT A, B
FROM R
INTERSECT
SELECT C, D
FROM S
```

Differenza (R-S)
```sql
SELECT A, B
FROM R
EXCEPT
SELECT C, D
FROM S
```

Intersezione con EXISTS
```sql
SELECT A, B
FROM R
WHERE EXISTS (SELECT * 
			FROM S
			WHERE C=A AND D = B)
```
Differenza:
```SQL
SELECT A, B
FROM R
WHERE NOT EXISTS( SELECT *
				FROM S
				WHERE C = A AND D = B)
```

### CONTAINS
Permette di determinare se un set è contenuto in un altro.

>[!example] Trovare tutti gli impiegati che lavorano al progetto controllato dal dipartimento 10

```SQL
SELECT SSN
FROM EMPLOYEE
WHERE (SELECT PNO
			FROM WORKS_ON
			WHERE SSN = ESSN)
			CONTAINS
			(SELECT PNUMBER
			FROM PROJECT
			WHERE DNUM = 10)
```

#### Come esprimo l'operatore CONTAINS
Date due relazioni R(A, B) e S(C, D) determiniamo se S $\subseteq$ R
Osserviamo che S $\subseteq$ R <-> S - R = vuoto
- usiamo NOT EXISTS per controllare se sia vuoto
- e EXCEPT per fare la differenza

```SQL
SELECT *
FROM ...
WHERE NOT EXISTS ( SELECT C, D
				FROM S
				EXCEPT
				SELECT A, B
				FROM R)
```

>[!example] Trovare impiegati che lavorano su tutti i progetti controllati dal dipartimento 10


```SQL
SELECT SSN
FROM EMPLOYEE AS E
WHERE NOT EXISTS( SELECT PNUMBER
				FROM PROJECT AS P
				WHERE DNUM = 10
				EXCEPT
				SELECT PNO
				FROM WORKS_ON
				WHERE E.SSN = ESSN)
```

##### Usando NOT EXISTS annidati
Date due relazioni R(A, B) e S(C, D) determiniamo se S $\subseteq$ R
Osserviamo che S $\subseteq$ R <-> S - R = vuoto
- usiamo NOT EXISTS per controllare se sia vuoto
- un altro NOT EXISTS per fare la differenza
```SQL
SELECT ∗
FROM . . .
WHERE NOT EXISTS ( SELECT ∗
					FROM S
					WHERE NOT EXISTS ( SELECT ∗
										FROM R
										WHERE C = A AND D = B))
```

>[!example] Trovare impiegati che lavorano su tutti i progetti controllati dal dipartimento 10

```SQL
SELECT SSN
FROM EMPLOYEE AS E
WHERE NOT EXISTS( SELECT PNUMBER
				FROM PROJECT AS P
				WHERE DNUM = 10 AND NOT EXISTS(
									SELECT *
									FROM WORKS_ON
									WHERE E.SSN = ESSN AND P.PNUMBER = PNO))
```

### Query universali e valori NULL
Query in linguaggio naturale: trovare tutte le entità (E) che sono associate con tutti i valori (V) associati all'entità ROSSI

T(ID, E, V)

| ID  | E       | V    |
| --- | ------- | ---- |
| 1   | ROSSI   | P1   |
| 2   | ROSSI   | NULL |
| 3   | BIANCHI | P1   |
| 4   | BIANCHI | NULL |
| 5   | VERDI   | P1   |

#### Tramite NOT EXISTS annidati
```SQL
SELECT DISTINCT H.E
FROM T AS H
WHERE NOT EXISTS ( SELECT ∗
					FROM T AS R
					WHERE R.E = ’ROSSI’ AND
					NOT EXISTS ( SELECT ∗
								FROM T AS X
								WHERE X.E = H.E AND X.V = R.V))
```
							

**Cosa c'è che non va?**
Per la tupla R(2, ROSSI, NULL) la condizione interna diventa: X.V = NULL che non è mai vera. Anche e il NOT EXISTS interno è TRUE quindi (2, ROSSI, NULL) è trattato come un controesempio per ogni candidato.
**Conseguenza:** anche BIANCHI è rifiutato, sebbene contenga entrambi valori visibili di ROSSI.
**Punto critico:** con l'uguaglianza ordinaria, un valore NULL nell'insieme quantificato universalmente si comporta come un requisito non soddisfacibile.
**Risultato di questa istanza:** non è restituita nessuna tupla.

#### Tramite NOT EXISTS and set difference
```SQL
SELECT DISTINCT H.E
FROM T AS H
WHERE NOT EXISTS ( SELECT R.V
				FROM T AS R
				WHERE R.E = 'ROSSI'
				EXCEPT
				SELECT X.V
				FROM T AS X
				WHERE X.E = H.E)
```
**Che succede?** per BIANCHI, la differenza tra set è: {P1, NULL} - {P1, NULL} = vuoto
quindi BIANCHI è restituito.
Per VERDI, la differenza tra set è: {P1, NULL} - {P1} = {NULL}
Quindi VERDI è rifiutato.

**Punto critico:** nell'EXCEPT, NULL è comparato in modo teorico: un NULL sulla sinistra è rimosso se un matching NULL è presente anche sulla destra.

**Risultato dell'istanza:** solo BIANCHI è restituito

#### Uso di NOT IN invece del NOT EXISTS annidato
```SQL
SELECT DISTINCT H.E
FROM T AS H
WHERE NOT EXISTS ( SELECT ∗
				FROM T AS R
				WHERE R.E = ’ROSSI’ AND
				R.V NOT IN ( SELECT X.V
							FROM T AS X
							WHERE X.E = H.E))
```

**Perché è pericoloso:**
- se a sinistra è NULL, allora NOT IN non restituisce TRUE: NULL NOT IN ('P1') = UNKNOWN
- se a destra contiene un NULL, allora potrebbe essere ignorato un missing value: 'P2' NOT IN ('P1', NULL) = UNKNOWN

Per il candidato BIANCHI quando si controlla R.V = P2, otteniamo: 'P2' NOT IN ('P1', NULL) questo non è TRUE; è UNKNOWN. Quindi il valore mancante P2 non è identificato come controesempio.

**Punto critico:** con NOT IN, entrambi i NULL a destra e sinistra potrebbero cambiare il predicato in UNKNOWN invece che TRUE.

## The UNIQUE Boolean Function
La funzione booleana UNIQUE permette di verificare che non ci siano duplicati nel risultato della query annidata.

>[!example] Trovare gli impiegati che non hanno 2 o più persone a carico dello stesso genere.


```SQL
SELECT SSN
FROM EMPLOYEE
WHERE UNIQUE ( SELECT GENDER
				FROM DEPENDENT
				WHERE SSN = ESSN)
```

## JOIN
-  INNER JOIN (or simply JOIN)
- LEFT OUTER JOIN, RIGHT OUTER JOIN, FULL OUTER JOIN (the word OUTER can be omitted)
- NATURAL JOIN
- NATURAL LEFT/RIGHT/FULL OUTER JOIN

### INNER JOIN

>[!example] Ricavare il nome, cognome e indirizzo degli impiegati appartenenti al dipartimento di ricerca.

```SQL
SELECT FNAME, LNAME, ADDRESS
FROM (EMPLOYEE JOIN DEPARTMENT
		ON DNO = DNUMBER)
WHERE DNAME = 'RESEARCH'
```

>[!example] Per ogni progetto situato a Tolmezzo, restituire il numero del progetto, il dipartimento che lo controlla e il cognome del manager di quel dipartimento.

```SQL
SELECT PNUMBER, DNUMBER, LNAME
FROM ((PROJECT JOIN DEPARTMENT ON DNUM = DNUMBER)
		JOIN EMPLOYEE ON MGR_SSN = SSN)
WHERE PLOCATION = 'TOLMEZZO' 
```

### OUTER JOIN
>[!example] Restituire il nome e cognome per ogni impiegato e il loro supervisore.

```SQL
SELECT E.FNAME AS EMPFIRSTNAME, E.LNAME AS EMPLASTNAME,
        S.FNAME AS SUPFIRSTNAME, S.LNAME AS SUPLASTNAME
FROM (EMPLOYEE AS E LEFT OUTER JOIN
		EMPLOYEE AS S ON E.SUPERVISOR = S.SSN)
```

>[!example] Restituire tutti i dipartimenti con qualsiasi progetto che controllano.

```SQL
SELECT PNUMBER, DNUMBER
FROM (PROJECT RIGHT OUTER JOIN DEPARTMENT ON DNUM = DNUMBER)
```

## Aggregate Functions in SQL
- COUNT
- SUM
- AVG
- MAX
- MIN

>[!example] Determinare la somma totale dei salari pagati dall'azienda ai suoi impiegati, salario medio, salario più alto e quello più basso.

```SQL
SELECT SUM(SALARY), AVG(SALARY), MAX(SALARY), MIN(SALARY)
FROM EMPLOYEE
```

>[!warning] Vengono considerati tutti i valori tranne i NULL di SALARY

### COUNT
Permette di contare il numero di righe in una tabella, il numero di non-NULL 

>[!example] Determinare il numero degli impiegati nel dipartimento 3

```SQL
SELECT COUNT(\*)
FROM EMPLOYEE
WHERE DNO = 3
```

>[!example] Determinare il numero diverso dell'ammontare di salari nell'azienda.

```SQL
SELECT COUNT (DISTINCT SALARY)
FROM EMPLOYEE

```
### Queries inconsistenti
>[!EXAMPLE]

```SQL
SELECT FNAME, LNAME, MAX(SALARY)
FROM EMPLOYEE, DEPT_LOCATIONS
WHERE DNO = DNUMBER AND DLOCATION = 'TRIESTE'
```

### Queries con Grouping

GROUP BY permette di partizionare le tuple di una relazione

>[!example] Per ogni dipartimento, determinare la somma dei salari dei suoi membri.

```SQL
SELECT DNO, SUM(SALARY)
FROM EMPLOYEE
GROUP BY DNO

```
Con GROUP BY il SELECT può contenere solo funzioni di aggregazione e un subset degli attributi raggruppati

### Queries sintatticamente scorrette
>[!example] Per ogni dipartimento, restituire il numero di membri e il manager.

**Soluzione scorretta:**
```SQL
SELECT DNO, COUNT(\*), MGR_SSN
FROM EMPLOYEE, DEPARTMENT
WHERE DNO = DNUMBER
GROUP BY DNO
```

**Soluzione giusta:**
```SQL
SELECT DNO, COUNT(\*), MGR_SSN
FROM EMPLOYEE, DEPARTMENT
WHERE DNO = DNUMBER
GROUP BY DNO, MGR_SSN
```

### Predicati sui Gruppi
La clausola HAVING è usata per restringere il campo alle sole classi della partizione che rispondono a una certa condizione.

>[!example] Seleziona solo quei dipartimenti che spendono più di 1.000.000 di euro in salari per i loro membri.

```SQL
SELECT DNO, SUM(SALARY) AS TOTALSALARY
FROM EMPLOYEE
GROUP BY DNO
HAVING SUM(SALARY) > 1000000
```

### WHERE VS HAVING

>[!example] Per ogni dipartimento con più di 5 membri , trovare il numero di membri che guadagnano più di 60.000 euro.

**soluzione sbagliata:**

```SQL
SELECT DNO, COUNT(\*)
FROM EMPLOYEE
WHERE SALARY > 60000
GROUP BY DNO
HAVING COUNT (\*) > 5
```
**Soluzione giusta:**
```sql
	SELECT DNO, COUNT(∗)
	FROM EMPLOYEE
	WHERE SALARY > 60000 AND
			DNO IN ( SELECT DNO
					FROM EMPLOYEE
					GROUP BY DNO
					HAVING COUNT(∗) > 5)
	GROUP BY DNO
```

### Relazioni come valori
Una subquery che restituisce esattamente una riga e una colonna che può essere trattata come un singolo valore.

>[!example] Determinare il cognome e il nome degli impiegati che hanno due o più dipendenti.

```sql
SELECT LNAME, FNAME
FROM EMPLOYEE
WHERE (SELECT COUNT(*)
		FROM DEPENDENT
		WHERE SSN = ESSN ) >= 2
```

### Miscellanea
In comparazione con il risultato delle query annidate, tuple di attributi o valori possono essere usate come singoli attributi o valori.
#### 1

>[!example] Selezionare gli impiegati che dedicano lo stesso numero di ore a un progetto come l'impiegato MNTGVN89S14J324Q

```sql
SELECT DISTINCT ESSN
FROM WORKS_ON
WHERE (PNO, HOURS) IN
			(SELECT PNO, HOURS
			FROM WORKS_ON
			WHERE ESSN = 'MNTGVN89S14J324Q')
```

#### 2
 Nella clausola WHERE, i set di valori possono essere introdotti esplicitamente.
>[!example] selezionare impiegati che lavorano al progetto 1, 2 o 3


```sql
SELECT DISTINCT ESSN
FROM WORKS_ON
WHERE PNO IN{1,2,3}

```

#### 3

Corrispondenza di pattern di stringhe: operatore **LIKE**

Vengono utilizzati due caratteri riservati: % che sostituisce un numero qualsiasi (0 o più) di caratteri e che sostituisce ogni singolo carattere.

>[!example] Selezionare gli impiegati che risiedono in una città con codice postale 33210.

```sql
SELECT FNAME, LNAME
FROM EMPLOYEE
WHERE ADDRESS LIKE '%33210%'
```

>[!EXAMPLE] Selezionare impiegati nati negli anni con il 6 (BDATE format yyyy/mm/dd)

```sql
SELECT FNAME, LNAME
FROM EMPLOYEE
WHERE BDATE LIKE '__6_______'
```

#### 4
Se % o _ devono essere usati come elementi di una stringa, ogni occorrenza deve essere preceduta da un **escape character** che è specificato alla fine della stringa usando ESCAPE

L'operatore di concatenazione **||** può essere usato per concatenare due stringhe.

**BETWEEN**: per esprimere condizioni in modo più compatto

>[!example] Selezionare gli impiegati del dipartimento 3 che guadagnano tra i 30.000 e i 40.000 euro

```sql
SELECT *
FROM EMPLOYEE
WHERE (SALARY BETWEEN 30000 AND 40000) AND DNO = 3
```

#### 5
**ORDER BY:** Tuple risultanti da una query possono essere ordinate in ordine crescente o decrescente, basato su uno o più attributi

>[!EXAMPLE] Restituisce la lista degli impiegati e dei progetti a cui lavorano, ordinati per dipartimento (ordine decrescente) e per ogni dipartimento in ordine alfabetico per cognome e nome.

```sql
SELECT DNAME, LNAME, FNAME, PNAME
FROM EMPLOYEE, DEPARTMENT, PROJECT, WORKS_ON
WHERE DNO = DNUMBER AND SSN=ESSN AND PNO=PNUMBER
ORDER BY DNAME DESC, LNAME ASC, FNAME ASC
```

#### 6
**IS NULL (IS NOT NULL)**: per selezionare tuple che hanno (o non hanno) un valore NULL in un certo attributo. Restituiscono TRUE se e solo se l'attributo ha un valore nullo (o no).

>[!example] Seleziona tutti gli impiegati che hanno un salario che non si conosce.

```sql
SELECT *
FROM EMPLOYEE
WHERE SALARY IS NULL
```

# Linguaggio

## Tipi di dato
### Stringhe
`character(n)` oppure `char(n)`
- stringhe di esattamente n caratteri
- stringhe più corte sono aggiunti spazi di coda
`varchar(n)`

### Booleani
- tre valori: vero, falso e indeterminato
- valore indeterminato = **null**
- 't', 'f'
- true, false
- 'yes', 'no'
- 'y', 'n'
- '1', '0'

### Numerici
- smallint: 2byte
- int: 4 byte
- real
- double precision
#### A precisione arbitraria
- numeric(prec, scala)
- decimal(prec, scala)

### Temporali
- timestamp(prec)
- date
- interval(prec)
	- intervalli di tempo relativi
	- prec: indica il numero di cifre frazionarie dopo i secondi

