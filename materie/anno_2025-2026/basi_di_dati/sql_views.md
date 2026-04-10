---
title: "Sql Views"
aliases: ["Sql Views"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "sql-views"]
created: 2026-04-08
---
Relazioni virtuali
- ha uno schema ma non un'stanza: ogni volta che si usa una view viene ricalcolata, aggiorna sempre le informazioni
- utilizzabile con le query come le tabelle base: abilita query annidate nel FROM

Materializzare una vista:
- salviamo il contenuto informativo
- vantaggio: l'uso della view diventa estremamente leggero
- problema: mantenere allineamento con la tabella base

## Sintassi
```sql
CREATE VIEW ViewName [(AttributeList)] AS
SELECT-SQL
[WITH [LOCAL | CASCADED] CHECK OPTION]
```

la query deve restituire un set di attributi compatibile con gli attributi dichiarati nello schema della view

>[!example] Definire una view EMPLOYEES5 che contenga solo gli employees del dipartimento 5 che guadagnano più di 10,000 euro

```sql
CREATE VIEW EMPLOYEES5(ID5, NAME5, SURNAME5, SALARY5) AS
SELECT SSN, Fname, Lname, Salary
FROM EMPLOYEE
WHERE Dno = 5 AND Salary > 10000
```

ora dalla view EMPLOYEES5 costruisco un'altra view con impiegati del dipartimento 5 che hanno un salario compreso tra 10.000 e 25.000

```sql
CREATE VIEW EMPLOYEES5POOR AS
SELECT *
FROM EMPLOYEES5
WHERE SALARY5 < 25000
WITH CHECK OPTION
```

## Queries e View
### Usare funzioni aggregate a cascata

>[!EXAMPLE] Trovare dipartimento caratterizzato dal salario massimo pagato ai suoi membri

```sql
CREATE VIEW DEPTTOTALSAL(DEPT, TOTALSALARY) AS
	SELECT Dno, SUM(Salary)
	FROM EMPLOYEE
	GROUP BY Dno
	
SELECT DEPT
FROM DEPTTOTALSAL
WHERE TOTALSALARY >= ALL ( SELECT TOTALSALARY
							FROM DEPTTOTALSAL)
```

>[!example] Considerare gli impiegati che hanno almeno un dipendente , determinare il numero massimo e medio dei dipendenti 

```sql
CREATE VIEW DEPENDENTEMP(EMP, DEPENDENT) AS
	SELECT ESSN, COUNT(*)
	FROM DEPENDENT
	GROUP BY ESSN

SELECT AVG(DEPENDENT), MAX(DEPENDENT)
FROM DEPENDENTEMP
```

Soluzione sbagliata:
```sql
SELECT AVG(COUNT(*)), MAX(COUNT(*))
FROM DEPENDENT
GROUP BY ESSN
```


## View ricorsive
>[!example] Trovare il diretto o indiretto supervisore di Giovanni Rossi

```sql
CREATE RECURSIVE VIEW HASSUPERIOR(EMPLOYEE, SUPERIOR) AS
	((SELECT SSN, Super_SSN
		FROM EMPLOYEE
		WHERE Super_SSN IS NOT NULL)
		UNION
	(SELECT E2.EMPLOYEE, E1.Super_SSN
	FROM EMPLOYEE E1, HASSUPERIOR E2
	WHERE E2.SUPERIOR = E1.SSN AND E1.Sper_SSN IS NOT NULL))

SELECT SSN, SUPERIOR
FROM (EMPLOYEE JOIN HASSUPERIOR on
		EMPLOYEE.SSN = HASSUPERIOR.EMPLOYEE)
WHERE Fname = 'GIOVANNI' AND Lname = 'ROSSI'
```

- La view ricorsiva HASSUPERIOR contiene gli impiegati e il loro diretto o indiretto supervisore
- Potrebbero esserci diversi supervisori per ogni impiegato, quindi il SSN da solo non identifica le tuple di HASSUPERIOR
- il concetto di una chiave non è definito per le view
- la definizione ricorsiva di HASSUPERIOR specifica il caso base (il supervisore diretto) e un caso ricorsivo (supervisore indiretto) dove HASSUPERIOR è riutilizzato
- alla fine il bersaglio è risolto selezionando il supervisore degli impiegati con il nome del coglione 

## View e operazioni di update

Alcune view permettono operazioni di aggiornamento che sono trasformate nell'operazione corrispondente sulla base delle tabelle da cui dipendono tali view

```sql
CREATE VIEW WORKS ON PROJECT AS
	SELECT Fname, Lname, Pname, Hours
	FROM EMPLOYEE, PROJECT, WORKS ON
	WHERE SSN = ESSN AND Pnumber = Pno
UPDATE WORKS ON PROJECT
SET Pname = ’PROJECTB’
WHERE Lname = ’ROSSI’ AND Fname = ’MARIO’ AND Pname = ’PROJECTA’
```

**Problemi con questo esempio:**
- assumiamo che il DB dichiara che Mario Rossi lavora a (15, PROJECTA). Il risultato dell'aggiornamento sulla view potrebbe voler dire (15, PROJECTA) --> (15, PROJECTB)
- assumiamo che DB dichiara che Mario Rossi lavora a (15, PROJECTA) e contiene anche (18, PROJECTB). Il risultato dell'aggiornamento sulla view potrebbe voler dire che Mario Rossi ora lavora a (18, PROJECTB)
- **Impossibile determinare la coerenza semantica**

### Quando può essere modificata una View?
- **Standard SQL**
- **Commercial systems**

### LOCAL
Il controllo sul mantenere le tuple nella view è fatto solo sull'ultimo livello (la modifica non deve causare violazioni delle condizioni definendo la view più esterna)

### CASCADED
Il controllo sul mantenere le tuple nella view è fatto ad alto livello (è controllato che le tuple che sono state modificate non spariscano dalla view come risultato di violazione di qualche condizione che coinvolge le view)

>[!example] Un assignment del valore di 8.000 euro a una delle tuple della view EMPLOYEES5POOR è accettata con LOCAL, ma è rifiutata con CASCADED. Una modifica che assegna un valore di 40.000 euro a una tuple della view è rifiutata con entrambe le opzioni.


## Un approccio parziale simile alle view: CTE e WITH
**Common Table Expression (CTE)**: query introdotta con WITH
