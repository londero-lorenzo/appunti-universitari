---
title: "15 1 Livelli di Isolamento"
aliases: ["15 1 Livelli di Isolamento"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "15-1-livelli-di-isolamento"]
created: 2026-05-18
---
Questi appunti seguono la slide caricata sui **livelli di isolamento**, le anomalie ammesse/non ammesse dallo standard SQL e alcune note pratiche su PostgreSQL / Snapshot Isolation.

````markdown
# Livelli di isolamento delle transazioni

#basi-di-dati #transazioni #concorrenza #isolamento #SQL

## 1. Contesto generale

In un DBMS, più transazioni possono essere eseguite contemporaneamente.

Il problema è che l’esecuzione concorrente può produrre risultati anomali se una transazione legge dati modificati da altre transazioni non ancora concluse, oppure se durante la sua esecuzione il contenuto del database cambia.

Il livello di isolamento stabilisce **quanto una transazione è protetta dagli effetti delle altre transazioni concorrenti**.

Più il livello di isolamento è alto:

- maggiore è la correttezza percepita;
- minore è il rischio di anomalie;
- maggiore può essere il costo in termini di blocchi, attese e riduzione della concorrenza.

---

## 2. Le principali anomalie di isolamento

Lo standard SQL classifica i livelli di isolamento in base a tre anomalie principali:

1. **Dirty Read**, o lettura sporca;
2. **Non-Repeatable Read**, o lettura non ripetibile / lettura inconsistente;
3. **Phantom Read**, o inserimento fantasma.

---

## 3. Dirty Read

Una **Dirty Read** avviene quando una transazione legge un dato scritto da un’altra transazione che non ha ancora fatto `COMMIT`.

Il problema è che la transazione che ha scritto quel dato potrebbe poi fare `ROLLBACK`.

### Esempio

```sql
-- T1
START TRANSACTION;
UPDATE Conti SET saldo = saldo - 100 WHERE id = 1;

-- T2
START TRANSACTION;
SELECT saldo FROM Conti WHERE id = 1;
````

Se `T2` legge il saldo modificato da `T1`, ma `T1` non ha ancora fatto `COMMIT`, allora `T2` sta leggendo un dato provvisorio.

Se poi `T1` fa:

```sql
ROLLBACK;
```

il dato letto da `T2` non è mai esistito realmente nello stato finale del database.

### Intuizione

La Dirty Read è l’anomalia più grave tra quelle considerate dallo standard, perché permette di leggere dati non confermati.

---

## 4. Non-Repeatable Read

Una **Non-Repeatable Read** avviene quando una transazione legge due volte lo stesso dato e ottiene due risultati diversi, perché nel frattempo un’altra transazione ha modificato e confermato quel dato.

### Esempio

```sql
-- T1
START TRANSACTION;
SELECT saldo FROM Conti WHERE id = 1;
-- risultato: 1000
```

Nel frattempo:

```sql
-- T2
START TRANSACTION;
UPDATE Conti SET saldo = 500 WHERE id = 1;
COMMIT;
```

Poi `T1` rilegge lo stesso dato:

```sql
-- T1
SELECT saldo FROM Conti WHERE id = 1;
-- risultato: 500
```

La stessa transazione `T1`, leggendo lo stesso oggetto, ha ottenuto due valori diversi.

### Intuizione

Il problema non è leggere un dato non confermato, ma leggere dati confermati che cambiano durante la vita della transazione.

---

## 5. Phantom Read

Una **Phantom Read** avviene quando una transazione esegue due volte la stessa query con una condizione, ma la seconda volta compaiono nuove tuple che prima non c’erano.

È detta “phantom” perché appaiono nuovi record che soddisfano il predicato della query.

### Esempio

```sql
-- T1
START TRANSACTION;
SELECT * FROM Prenotazioni WHERE data = '2026-05-20';
-- risultato: 3 prenotazioni
```

Nel frattempo:

```sql
-- T2
START TRANSACTION;
INSERT INTO Prenotazioni VALUES (..., '2026-05-20', ...);
COMMIT;
```

Poi `T1` ripete la stessa query:

```sql
-- T1
SELECT * FROM Prenotazioni WHERE data = '2026-05-20';
-- risultato: 4 prenotazioni
```

La query è la stessa, ma il risultato cambia perché è stata inserita una nuova tupla che soddisfa il predicato.

### Differenza rispetto alla Non-Repeatable Read

- **Non-Repeatable Read**: cambia il valore di una tupla già letta.
    
- **Phantom Read**: compaiono nuove tuple che prima non facevano parte del risultato.
    

---

# 6. Livelli di isolamento secondo lo standard SQL

Lo standard SQL definisce quattro livelli di isolamento:

1. `READ UNCOMMITTED`
    
2. `READ COMMITTED`
    
3. `REPEATABLE READ`
    
4. `SERIALIZABLE`
    

Ogni livello vieta alcune anomalie, ma ne può ammettere altre.

---

## 7. Tabella riassuntiva delle anomalie

|Livello di isolamento|Dirty Read|Non-Repeatable Read|Phantom Read|
|---|--:|--:|--:|
|`READ UNCOMMITTED`|Ammessa|Ammessa|Ammessa|
|`READ COMMITTED`|Non ammessa|Ammessa|Ammessa|
|`REPEATABLE READ`|Non ammessa|Non ammessa|Ammessa|
|`SERIALIZABLE`|Non ammessa|Non ammessa|Non ammessa|

---

## 8. READ UNCOMMITTED

`READ UNCOMMITTED` è il livello di isolamento più debole.

Una transazione può leggere modifiche effettuate da altre transazioni anche se queste non hanno ancora fatto `COMMIT`.

### Anomalie

|Anomalia|Ammessa?|
|---|--:|
|Dirty Read|Sì|
|Non-Repeatable Read|Sì|
|Phantom Read|Sì|

### Significato

Questo livello permette la massima concorrenza, ma offre pochissime garanzie.

È pericoloso perché una transazione può basare i propri calcoli su dati che potrebbero essere annullati.

---

## 9. READ COMMITTED

`READ COMMITTED` impedisce le Dirty Read.

Una transazione può leggere solo dati già confermati da transazioni che hanno fatto `COMMIT`.

Tuttavia, se durante la transazione un’altra transazione modifica e conferma un dato, la prima transazione può vedere il nuovo valore in una lettura successiva.

### Anomalie

|Anomalia|Ammessa?|
|---|--:|
|Dirty Read|No|
|Non-Repeatable Read|Sì|
|Phantom Read|Sì|

### Esempio intuitivo

Se una transazione legge il saldo di un conto, poi un’altra transazione modifica quel saldo e fa `COMMIT`, la prima transazione può leggere un valore diverso se ripete la `SELECT`.

---

## 10. REPEATABLE READ

`REPEATABLE READ` impedisce sia le Dirty Read sia le Non-Repeatable Read.

Questo significa che, se una transazione legge un dato, letture successive dello stesso dato dovrebbero restituire lo stesso valore.

Tuttavia, secondo lo standard SQL, possono ancora comparire tuple fantasma.

### Anomalie

|Anomalia|Ammessa?|
|---|--:|
|Dirty Read|No|
|Non-Repeatable Read|No|
|Phantom Read|Sì|

### Intuizione

Il DBMS garantisce stabilità sulle tuple già lette, ma non necessariamente sull’intero insieme di tuple che soddisfano un certo predicato.

Per evitare anche i fantasmi servirebbe bloccare non solo i record letti, ma anche il predicato della query.

---

## 11. SERIALIZABLE

`SERIALIZABLE` è il livello di isolamento più forte.

L’obiettivo è fare in modo che l’esecuzione concorrente delle transazioni sia equivalente a una qualche esecuzione seriale, cioè una transazione dopo l’altra.

### Anomalie

|Anomalia|Ammessa?|
|---|--:|
|Dirty Read|No|
|Non-Repeatable Read|No|
|Phantom Read|No|

### Significato

Una transazione eseguita a livello `SERIALIZABLE` dovrebbe comportarsi come se non ci fossero altre transazioni concorrenti.

Naturalmente, questo può ridurre la concorrenza e aumentare il rischio di attese o abort.

---

# 12. Limite importante dello standard SQL

Lo standard SQL dice quali anomalie **non devono accadere** a ciascun livello di isolamento.

Tuttavia, non dice che le anomalie ammesse **debbano per forza accadere**.

Quindi:

> Se un livello ammette una certa anomalia, significa solo che il DBMS non è obbligato a impedirla.

Per esempio, secondo lo standard, `REPEATABLE READ` ammette i Phantom Read, ma un DBMS concreto potrebbe comunque evitarli.

---

# 13. Meccanismi di controllo della concorrenza

I livelli di isolamento possono essere implementati tramite diversi meccanismi.

Uno dei meccanismi classici è il locking, cioè l’uso di lock sulle letture e sulle scritture.

---

## 14. Lock sulle letture e sulle scritture

Nella slide vengono distinti i meccanismi applicati:

- sulle letture;
    
- sulle scritture.
    

Le scritture sono in genere più delicate, perché modificano lo stato del database.

---

## 15. Possibile implementazione con lock

|Livello|Letture|Scritture|
|---|---|---|
|`READ UNCOMMITTED`|Nessun lock|2PL stretto|
|`READ COMMITTED`|Lock acquisito e rilasciato subito|2PL stretto|
|`REPEATABLE READ`|2PL stretto|2PL stretto|
|`SERIALIZABLE`|2PL stretto + lock di predicato|2PL stretto + lock di predicato|

---

# 16. 2PL: Two-Phase Locking

Il **Two-Phase Locking**, abbreviato `2PL`, è un protocollo di controllo della concorrenza basato sui lock.

Una transazione ha due fasi:

1. **Fase di crescita**  
    La transazione può acquisire nuovi lock.
    
2. **Fase di rilascio**  
    La transazione rilascia lock, ma non può più acquisirne di nuovi.
    

### Idea

Il 2PL serve a garantire la serializzabilità dei conflitti.

Se tutte le transazioni rispettano il 2PL, l’esecuzione risultante è conflict-serializable.

---

## 17. 2PL stretto

Il **2PL stretto** è una variante del 2PL in cui i lock, soprattutto quelli di scrittura, vengono mantenuti fino al `COMMIT` o al `ROLLBACK`.

Questo evita che altre transazioni leggano dati non ancora confermati.

### Perché è utile?

Il 2PL stretto impedisce le Dirty Read, perché una transazione non può leggere un dato scritto da un’altra transazione finché quest’ultima non ha concluso.

---

## 18. Lock di predicato

Il **lock di predicato** serve a impedire i Phantom Read.

Invece di bloccare solo le tuple già esistenti, il DBMS blocca l’intero predicato della query.

### Esempio

Se una transazione esegue:

```sql
SELECT * 
FROM Prenotazioni 
WHERE data = '2026-05-20';
```

un lock di predicato dovrebbe impedire a un’altra transazione di inserire nuove prenotazioni con quella stessa data finché la prima transazione non termina.

### Perché serve?

Senza lock di predicato, il DBMS può bloccare solo le tuple già lette.

Ma il problema del Phantom Read riguarda tuple che ancora non esistono nel risultato della prima lettura.

---

# 19. Snapshot Isolation

Nella pratica, alcuni DBMS non implementano i livelli di isolamento esattamente con i lock descritti in modo teorico.

Un esempio importante è la **Snapshot Isolation**, usata da DBMS basati su multiversione.

## Idea di base

Con la Snapshot Isolation, quando una transazione inizia, ottiene una “fotografia” dello stato del database.

La transazione continua a leggere da quella fotografia, anche se nel frattempo altre transazioni modificano il database.

Per questo motivo, durante la sua esecuzione, la transazione vede uno stato coerente e stabile.

---

## 20. Snapshot Isolation e multiversioni

La Snapshot Isolation si basa sul concetto di **multiversione**.

Invece di avere un solo valore corrente per ogni dato, il DBMS mantiene più versioni dello stesso dato.

Ogni transazione legge la versione coerente con il proprio snapshot.

### Esempio intuitivo

Se `T1` inizia quando il saldo è 1000, continuerà a vedere 1000 anche se `T2` modifica il saldo a 500 e fa `COMMIT`.

Questo evita letture inconsistenti all’interno della stessa transazione.

---

## 21. Snapshot Isolation e PostgreSQL

In PostgreSQL, il livello `REPEATABLE READ` è implementato in modo simile alla Snapshot Isolation.

Questo significa che, in pratica, PostgreSQL può evitare anche alcuni casi di Phantom Read che secondo lo standard SQL sarebbero ammessi a livello `REPEATABLE READ`.

Quindi bisogna distinguere tra:

- definizione teorica dello standard SQL;
    
- comportamento concreto del DBMS.
    

---

# 22. Snapshot Isolation non è uguale a Serializable

Anche se la Snapshot Isolation evita molte anomalie, non coincide automaticamente con la serializzabilità.

Infatti possono esistere anomalie che non sono Dirty Read, Non-Repeatable Read o Phantom Read, ma che rendono comunque l’esecuzione non equivalente a una seriale.

Un caso classico è il cosiddetto **write skew**.

---

## 23. Esempio intuitivo di Write Skew

Supponiamo che in ospedale debba esserci sempre almeno un medico di turno.

Tabella:

```sql
Medici(nome, in_turno)
```

Situazione iniziale:

|nome|in_turno|
|---|---|
|Anna|true|
|Bruno|true|

Due transazioni partono contemporaneamente.

### Transazione T1

Anna controlla che ci sia almeno un altro medico di turno:

```sql
SELECT COUNT(*) 
FROM Medici 
WHERE in_turno = true;
```

Vede 2 medici, quindi decide di togliersi dal turno:

```sql
UPDATE Medici 
SET in_turno = false 
WHERE nome = 'Anna';
```

### Transazione T2

Bruno fa la stessa cosa nello stesso momento:

```sql
SELECT COUNT(*) 
FROM Medici 
WHERE in_turno = true;
```

Anche lui vede 2 medici, quindi decide di togliersi dal turno:

```sql
UPDATE Medici 
SET in_turno = false 
WHERE nome = 'Bruno';
```

Se entrambe le transazioni fanno `COMMIT`, il risultato finale è:

|nome|in_turno|
|---|---|
|Anna|false|
|Bruno|false|

La regola “deve esserci almeno un medico di turno” viene violata.

### Perché può succedere?

Perché entrambe le transazioni hanno letto lo stesso snapshot iniziale, ma hanno modificato righe diverse.

Non c’è un conflitto diretto sulla stessa tupla, ma il risultato globale è scorretto.

---

# 24. Serializable Snapshot Isolation

Per ottenere un vero livello `SERIALIZABLE`, alcuni DBMS usano meccanismi più avanzati.

Nel caso di PostgreSQL, il livello `SERIALIZABLE` usa una tecnica chiamata **Serializable Snapshot Isolation**, spesso abbreviata `SSI`.

L’idea è partire dalla Snapshot Isolation, ma aggiungere controlli per rilevare situazioni che potrebbero produrre esecuzioni non serializzabili.

Quando il DBMS rileva un possibile conflitto pericoloso, può abortire una delle transazioni.

---

# 25. Riassunto per l’esame

## Tabella fondamentale

|Livello|Dirty Read|Non-Repeatable Read|Phantom Read|
|---|--:|--:|--:|
|`READ UNCOMMITTED`|Sì|Sì|Sì|
|`READ COMMITTED`|No|Sì|Sì|
|`REPEATABLE READ`|No|No|Sì|
|`SERIALIZABLE`|No|No|No|

---

## Da ricordare

- `READ UNCOMMITTED` è il livello più debole.
    
- `READ COMMITTED` impedisce le Dirty Read.
    
- `REPEATABLE READ` impedisce Dirty Read e Non-Repeatable Read.
    
- `SERIALIZABLE` impedisce anche i Phantom Read.
    
- I Phantom Read richiedono attenzione ai predicati, non solo alle singole tuple.
    
- Lo standard dice quali anomalie devono essere impedite, ma non obbliga il DBMS a far comparire quelle ammesse.
    
- PostgreSQL può avere comportamenti pratici più forti rispetto alla definizione minima dello standard.
    
- Snapshot Isolation dà a ogni transazione una fotografia coerente del database.
    
- Snapshot Isolation non equivale sempre a Serializable.
    

---

# 26. Domande tipiche da esame

## Domanda 1

Quali sono i quattro livelli di isolamento previsti dallo standard SQL?

### Risposta

I quattro livelli sono:

1. `READ UNCOMMITTED`
    
2. `READ COMMITTED`
    
3. `REPEATABLE READ`
    
4. `SERIALIZABLE`
    

---

## Domanda 2

Quali anomalie sono ammesse a livello `READ COMMITTED`?

### Risposta

A livello `READ COMMITTED`:

- le Dirty Read non sono ammesse;
    
- le Non-Repeatable Read sono ammesse;
    
- i Phantom Read sono ammessi.
    

---

## Domanda 3

Qual è la differenza tra Non-Repeatable Read e Phantom Read?

### Risposta

La Non-Repeatable Read riguarda la rilettura di una stessa tupla che ha cambiato valore.

Il Phantom Read riguarda invece la comparsa di nuove tuple che soddisfano una certa condizione di ricerca.

---

## Domanda 4

Perché per evitare i Phantom Read non basta bloccare le tuple lette?

### Risposta

Perché i Phantom Read riguardano tuple che al momento della prima lettura non esistono ancora nel risultato.

Bisogna quindi bloccare il predicato della query, non solo le tuple già presenti.

---

## Domanda 5

Snapshot Isolation è uguale a Serializable?

### Risposta

No.

Snapshot Isolation garantisce che ogni transazione lavori su uno snapshot coerente del database, evitando molte anomalie.

Tuttavia, può ancora permettere anomalie come il write skew, quindi non coincide necessariamente con la serializzabilità.

---

# 27. Schema mentale finale

```text
READ UNCOMMITTED
    ↓ impedisce Dirty Read
READ COMMITTED
    ↓ impedisce Non-Repeatable Read
REPEATABLE READ
    ↓ impedisce Phantom Read
SERIALIZABLE
```

Più si scende nello schema, più il livello di isolamento è forte.