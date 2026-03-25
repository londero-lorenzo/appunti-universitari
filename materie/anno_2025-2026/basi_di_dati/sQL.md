---
title: "Sql"
aliases: ["Sql"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "sQL"]
created: 2026-03-24
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
>SELECT SALARY AS SALARYBIANCO
>FROM EMPLOYEE
>WHERE LNAME = 'BIANCO'

>[!example] Retrieve all information related to employees whose last name is Bianco.
>SELECT *
>FROM EMPLOYEE
>WHERE LNAME='BIANCO'

>[!example] Find the monthly salary of employees whose last name is Bianco.
>SELECT SALARY / 12 AS MONTHLYSALARY
>FROM EMPLOYEE
>WHERE LNAME = 'BIANCO'

>[!example] Per ogni impiegato, ricavare il nome del dipartimento per cui lavorano.
>SELECT SSN, DNAME
>FROM EMPLOYEE, DEPARTMENT
>WHERE DNO = DNUMBER

## SELECT-FROM sottoblocco e uso di DISTINCT

>[!definition]
>DISTINCT
>>applicata dopo SELECT, esclude tutte le righe duplicate, ritorna solo valori diversi nel set

>[!example] Ricavare il salario per ogni impiegato
>SELECT SSN, SALARY
>FROM EMPLOYEE

>[!example] Determinare l'ammontare dei salari dei dipendenti nell'azienda.
>SELECT DISTINCT SALARY
>FROM EMPLOYEE

## Dot notation e nomi di attributi un po' sus

>[!example] Per ogni impiegato, identificarli per nome e cognome, recuperare i numeri di progetti a cui lavorano.
>SELECT EMPLOYEE, SSN, EMPLOYEE.FNAME, EMPLOYEE.LNAME, W.PNUMBER
>FROM EMPLOYEE, WORKS_ON AS W
>WHERE SSN = ESSN

>[!example] Recuperare il nome e data di nascita dei dipendenti per ogni impiegato
>SELECT SSN, D.DEPENDENT_NAME, D.BDATE
>FROM EMPLOYEE, DEPENDENT D
>WHERE SSN = ESSN

## Alias e operazioni per rinominare

>[!example] Recuperare il nome e cognome dei supervisori dei dipendenti del dipartimento 10
>SELECT S.FNAME, S.LNAME
>FROM EMPLOYEE AS E S
>WHERE E.DNO = 10 AND E.SUPER_SSN = S.SSN

>[!example] Trovare dipartimenti che hanno almeno una locazione in comune
>SELECT DISTINCT L1.DNUMBER, L2.DNUMBER
>FROM DEPT_LOCATIONS L1 L2
>WHERE L1.DLOCATION = L2.DLOCATION AND L1.DNUMBER < L2.DNUMBER

>[!example] Ricavare il nome e cognome degli impiegati maschi che guadagnano più di 40000 euro 
>SELECT FNAME, LNAME
>FROM EMPLOYEE
>WHERE SEX = 'M' AND SALARY > 40000

>[!example] Determinare gli impiegati con il cognome BIANCO che lavorano per il dipartimento 2 o 3
>SELECT SSN
>FROM EMPLOYEE
>WHERE LNAME = 'BIANCO' AND (DNO = 2 OR DNO = 3)

## SET operations
### 1
- UNION
- EXCEPT
- INTERSECT
Duplicati sono rimossi a meno che non sia richiesto di mantenerli (con la keyword ALL)

>[!example] Selezionare la data di nascita di tutti gli impiegati e dei loro dipendenti
>SELECT BDATE
>FROM EMPLOYEE
>UNION
>SELECT BDATE
>FROM DEPENDENT

### 2
Se gli attributi hanno nomi diversi, una union può essere usata comunque e il risultato avrà i nomi del primo operatore.
>[!example] Selezionare i nomi e cognomi dei tutti gli impiegati
>SELECT FNAME
>FROM EMPLOYEE
>UNION
>SELECT LNAME
>FROM EMPLOYEE

# NESTED QUERIES
Nella clausola WHERE: SQL permette di comparare un valore con il risultato di una query annidata, usando operatori di comparazione standard

>[!question] Come comparare un singolo valore con un set di valori ?
>Si usa la keyword **ANY**

## ANY

>[!example] Selezionare gli impiegati che appartengono a un dipartimento con una location a Pordenone.
>SELECT *
>FROM EMPLOYEE
>WHERE DNO = ANY (      SELECT DNUMBER
>					FROM DEPT_LOCATIONS
>					WHERE DLOCATION = 'PORDENONE')

>[!example] Selezionare il SSN degli impiegati che hanno lo stesso cognome di un impiegato che sta lavorando per il dipartimento 10
>SELECT SSN
>FROM EMPLOYEE
>WHERE LNAME = ANY ( SELECT LNAME
>						FROM EMPLOYEE
>						WHERE DNO = 10)

## ALL

>[!example] Selezionare tutti i dipartimenti dove nessun impiegato guadagna più di 80.000 euro
>SELECT DNUMBER
>FROM DEPARTMENT
>WHERE DNUMBER <> ALL (SELECT DNO
>						FROM EMPLOYEE
>						WHERE SALARY > 80000)

Soluzione alternativa:
SELECT DNUMBER
FROM DEPARTMENT
EXCEPT
SELECT DNO
FROM EMPLOYEE
WHERE SALARY > 80000

>[!example] Selezionare gli impiegati con salario più alto
>SELECT SSN
>FROM EMPLOYEE
>WHERE SALARY >= ALL (SELECT SALARY
>					FROM EMPLOYEE)

Soluzione alternativa
SELECT SSN
FROM EMPLOYEE
EXCEPT
SELECT E1.SSN
FROM EMPLOYEE AS E1 E2
WHERE E1.SALARY < E2.SALARY

## IN

Per controllare l'inclusione o l'esclusione di un elemento/valore in un set di elementi/valori restituiti da una query.
- IN equivalente e ANY
- NOT IN equivalente a ALL

>[!example] Selezionare gli impiegati appartenenti a un dipartimento con una locazione a Pordenone.
>SELECT *
>FROM EMPLOYEE
>WHERE DNO IN ( SELECT DNUMBER
>				FROM DEPT_LOCATIONS
>				WHERE DLOCATION = 'PORDENONE')

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
>SELECT SSN
>FROM EMPLOYEE
>WHERE DNO IN (SELECT D1.DNUMBER
>				FROM DEPARTMENT AS D1, DEPT_LOCATIONS AS L1
>				WHERE D1.DNUMBER = L1.DNUMBER AND D1.DNAME = 'RESEARCH') OR
>	DNO IN (SELECT D2.DNUMBER
>			FROM DEPT_LOCATIONS AS D2
>			WHERE L1.DLOCATION = D2.DLOCATION)

>[!warning] Questa soluzione è sbagliata perché la tupla L1 non è visibile nella seconda nested query.


>[!example] Determinare il nome e cognome di tutti gli impiegati che hanno un dipendente del loro genere con lo stesso nome
>SELECT FNAME, LNAME
>FROM EMPLOYEE E
>WHERE SSN IN( SELECT ESSN
>			FROM DEPENDENT
>			WHERE E.FNAME=DEPENDANT_NAME AND E.GENDER = GENDER)

>[!example] Selezionare gli impiegati che guadagnano un salario diverso da ogni altro impiegato nel dipartimento.
>SELECT SSN
>FROM EMPLOYEE AS E
>WHERE SALARY NOT IN (SELECT SALARY
>					FROM EMPLOYEE
>					WHERE SSN <> E.SSN AND DNO=E.DNO)

### EXISTS

- Relazione non vuota: EXISTS
- Relazione vuota: NOT EXISTS

>[!example] Selezionare impiegati che non hanno dipendenti
>SELECT SSN
>FROM EMPLOYEE
>WHERE NOT EXISTS(SELECT *
>				FROM DEPENDENT
>				WHERE SSN = ESSN)

>[!example] Ritorna il nome e cognome dei manager che hanno almeno un dipendente.
>SELECT FNAME, LNAME
>FROM EMPLOYEE
>WHERE EXISTS (SELECT *
>			FROM DEPARTMENT
>			WHERE SSN = MGR_SSN) AND
>		EXISTS( SELECT *
>				FROM DEPENDENT
>				WHERE SSN = ESSN)

#### INTERSEZIONE E EXCEPT tramite EXISTS
Date due relazioni R(A,B) e S(C,D)

intersezione (R S)
SELECT A, B
FROM R
INTERSECT
SELECT C, D
FROM S

Differenza (R-S)
SELECT A, B
FROM R
EXCEPT
SELECT C, D
FROM S

Intersezione con EXISTS
SELECT A, B
FROM R
WHERE EXISTS (SELECT * 
			FROM S
			WHERE C=A AND D = B)
Differenza:
SELECT A, B
FROM R
WHERE NOT EXISTS( SELECT *
				FROM S
				WHERE C = A AND D = B)

### CONTAINS
Permette di determinare se un set è contenuto in un altro.

>[!example] Trovare tutti gli impiegati che lavorano al progetto controllato dal dipartimento 10
>SELECT SSN
>EMPLOYEE
>WHERE (SELECT PNO
>			FROM WORKS_ON
>			WHERE SSN = ESSN)
>			CONTAINS
>			(SELECT PNUMBER
>			FROM PROJECT
>			WHERE DNUM = 10)

#### Come esprimo l'operatore CONTAINS
Date due relazioni R(A, B) e S(C, D) determiniamo se S $\subseteq$ R
Osserviamo che S $\subseteq$ R <-> S - R = vuoto
- usiamo NOT EXISTS per controllare se sia vuoto
- e EXCEPT per fare la differenza

SELECT *
FROM ...
WHERE NOT EXISTS ( SELECT C, D
				FROM S
				EXCEPT
				SELECT A, B
				FROM R)

>[!example] Trovare impiegati che lavorano su tutti i progetti controllati dal dipartimento 10
>SELECT SSN
>FROM EMPLOYEE AS E
>WHERE NOT EXISTS( SELECT PNUMBER
>				FROM PROJECT AS P
>				WHERE DNUM = 10
>				EXCEPT
>				SELECT PNO
>				FROM WORKS_ON
>				WHERE E.SSN = ESSN)

##### Usando NOT EXISTS annidati
Date due relazioni R(A, B) e S(C, D) determiniamo se S $\subseteq$ R
Osserviamo che S $\subseteq$ R <-> S - R = vuoto
- usiamo NOT EXISTS per controllare se sia vuoto
- un altro NOT EXISTS per fare la differenza
SELECT ∗
FROM . . .
WHERE NOT EXISTS ( SELECT ∗
					FROM S
					WHERE NOT EXISTS ( SELECT ∗
										FROM R
										WHERE C = A AND D = B))

>[!example] Trovare impiegati che lavorano su tutti i progetti controllati dal dipartimento 10
>SELECT SSN
>FROM EMPLOYEE AS E
>WHERE NOT EXISTS( SELECT PNUMBER
>				FROM PROJECT AS P
>				WHERE DNUM = 10 AND NOT EXISTS(
>									SELECT *
>									FROM WORKS_ON
>									WHERE E.SSN = ESSN AND P.PNUMBER = PNO))

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
SELECT DISTINCT H.E
FROM T AS H
WHERE NOT EXISTS ( SELECT ∗
					FROM T AS R
					WHERE R.E = ’ROSSI’ AND
					NOT EXISTS ( SELECT ∗
								FROM T AS X
								WHERE X.E = H.E AND X.V = R.V))
							

**Cosa c'è che non va?**
Per la tupla R(2, ROSSI, NULL) la condizione interna diventa: X.V = NULL che non è mai vera. Anche e il NOT EXISTS interno è TRUE quindi (2, ROSSI, NULL) è trattato come un controesempio per ogni candidato.
**Conseguenza:** anche BIANCHI è rifiutato, sebbene contenga entrambi valori visibili di ROSSI.
**Punto critico:** con l'uguaglianza ordinaria, un valore NULL nell'insieme quantificato universalmente si comporta come un requisito non soddisfacibile.
**Risultato di questa istanza:** non è restituita nessuna tupla.

#### Tramite NOT EXISTS and set difference
SELECT DISTINCT H.E
FROM T AS H
WHERE NOT EXISTS ( SELECT R.V
				FROM T AS R
				WHERE R.E = 'ROSSI'
				EXCEPT
				SELECT X.V
				FROM T AS X
				WHERE X.E = H.E)
**Che succede?** per BIANCHI, la differenza tra set è: {P1, NULL} - {P1, NULL} = vuoto
quindi BIANCHI è restituito.
Per VERDI, la differenza tra set è: {P1, NULL} - {P1} = {NULL}
Quindi VERDI è rifiutato.

**Punto critico:** nell'EXCEPT, NULL è comparato in modo teorico: un NULL sulla sinistra è rimosso se un matching NULL è presente anche sulla destra.

**Risultato dell'istanza:** solo BIANCHI è restituito

#### Uso di NOT IN invece del NOT EXISTS annidato
SELECT DISTINCT H.E
FROM T AS H
WHERE NOT EXISTS ( SELECT ∗
				FROM T AS R
				WHERE R.E = ’ROSSI’ AND
				R.V NOT IN ( SELECT X.V
							FROM T AS X
							WHERE X.E = H.E))

**Perché è pericoloso:**
- se a sinistra è NULL, allora NOT IN non restituisce TRUE: NULL NOT IN ('P1') = UNKNOWN
- se a destra contiene un NULL, allora potrebbe essere ignorato un missing value: 'P2' NOT IN ('P1', NULL) = UNKNOWN

Per il candidato BIANCHI quando si controlla R.V = P2, otteniamo: 'P2' NOT IN ('P1', NULL) questo non è TRUE; è UNKNOWN. Quindi il valore mancante P2 non è identificato come controesempio.

**Punto critico:** con NOT IN, entrambi i NULL a destra e sinistra potrebbero cambiare il predicato in UNKNOWN invece che TRUE.