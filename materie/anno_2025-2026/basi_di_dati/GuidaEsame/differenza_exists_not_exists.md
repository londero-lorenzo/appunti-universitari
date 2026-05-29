---
title: "Differenza Exists Not Exists"
aliases: ["Differenza Exists Not Exists"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "GuidaEsame", "differenza-exists-not-exists"]
created: 2026-05-29
---
# Guida Completa a `EXISTS` e `NOT EXISTS` in SQL

## Concetto fondamentale

```text
EXISTS     = voglio che esista almeno una riga con quella proprietà
NOT EXISTS = voglio che non esista nessuna riga con quella proprietà
```

Quindi:

```sql
EXISTS (...)
```

risponde a:

> esiste almeno un caso?

mentre:

```sql
NOT EXISTS (...)
```

risponde a:

> non esiste alcun caso?

---

# 1. `EXISTS`: quando cerco almeno un caso buono

Usi `EXISTS` quando il testo dice, esplicitamente o implicitamente:

- almeno uno
    
- almeno una
    
- esiste
    
- ha partecipato ad almeno una...
    
- ha superato almeno un...
    
- ha vinto almeno un...
    
- c’è un caso in cui...
    

## Esempio: studenti unici a superare un esame nel 2023

Testo:

> gli studenti tali che esista almeno un insegnamento del quale sono stati gli unici a superare l’esame nel 2023

Qui vuoi trovare uno studente per cui **esiste almeno un esame buono**.

```sql
SELECT S.Matricola
FROM Studenti AS S
WHERE EXISTS (
    SELECT *
    FROM Esami AS E1
    WHERE E1.Studente = S.Matricola
      AND E1.Anno = 2023
      AND NOT EXISTS (
          SELECT *
          FROM Esami AS E2
          WHERE E2.Insegnamento = E1.Insegnamento
            AND E2.Anno = 2023
            AND E2.Studente <> S.Matricola
      )
);
```

Qui:

```sql
EXISTS (...)
```

significa:

> esiste almeno un esame dello studente nel 2023

che soddisfa la condizione di unicità.

---

# 2. `NOT EXISTS`: quando cerco assenza di casi vietati

Usi `NOT EXISTS` quando il testo dice:

- nessuno
    
- mai
    
- non esiste
    
- non ha fatto alcun...
    
- privo di...
    
- solo...
    
- tutti...
    

Però attenzione: con `NOT EXISTS` di solito non cerchi il caso buono, ma il **caso cattivo**.

## Esempio: club privi di atleti sul podio

Testo:

> i club privi di atleti che siano andati sul podio

Il caso vietato è:

> un atleta del club con posizione 1, 2 o 3

Quindi scrivo:

```sql
SELECT C.nome
FROM club AS C
WHERE NOT EXISTS (
    SELECT *
    FROM atleta AS A
    JOIN gareggia AS G ON A.codiceFiscale = G.atleta
    WHERE A.club = C.nome
      AND G.posizione IN (1, 2, 3)
);
```

Qui:

```sql
NOT EXISTS (...)
```

significa:

> non esiste un atleta del club andato sul podio

Se al posto di `NOT EXISTS` usassi `EXISTS`, otterresti il contrario:

> club con almeno un atleta sul podio

---

# 3. La regola più importante: cerca il “caso buono” o il “caso cattivo”?

Quando leggi una richiesta, chiediti:

## Sto cercando un caso buono?

Allora uso `EXISTS`.

Esempio:

> clienti che hanno almeno un conto in Veneto

```sql
WHERE EXISTS (
    conto del cliente in Veneto
)
```

## Sto vietando un caso cattivo?

Allora uso `NOT EXISTS`.

Esempio:

> clienti che hanno solo conti in Veneto

Il caso cattivo è:

> conto fuori dal Veneto

```sql
WHERE NOT EXISTS (
    conto del cliente fuori Veneto
)
```

---

# 4. `NOT EXISTS` con “solo”

La parola **solo** è una delle più importanti.

Quando il testo dice:

> solo in X

non devi cercare le righe in X.

Devi escludere le righe fuori da X.

## Esempio: attori che hanno recitato solo in film di Kurosawa

Sbagliato pensare:

```sql
WHERE Regista = 'Kurosawa'
```

Corretto:

```sql
SELECT A.CodiceAttore
FROM ATTORI AS A
WHERE NOT EXISTS (
    SELECT *
    FROM INTERPRETAZIONE AS I
    JOIN FILM AS F ON I.Film = F.CodiceFilm
    WHERE I.Attore = A.CodiceAttore
      AND F.Regista <> 'Kurosawa'
);
```

Si legge:

> non esiste un film non di Kurosawa in cui l’attore abbia recitato.

---

# 5. `NOT EXISTS` con “tutti”

Quando il testo dice:

> ha superato tutti gli esami del secondo anno

significa:

> non esiste un insegnamento del secondo anno che lo studente non abbia superato.

```sql
SELECT S.Matricola
FROM Studente AS S
WHERE NOT EXISTS (
    SELECT *
    FROM Insegnamento AS I
    WHERE I.AnnoDiCorso = 2
      AND NOT EXISTS (
          SELECT *
          FROM HaSostenutoEsame AS H
          WHERE H.Studente = S.Matricola
            AND H.Insegnamento = I.InsegnamentoId
      )
);
```

---

# 6. Perché con “tutti” non basta `EXISTS`?

Se scrivessi:

```sql
WHERE EXISTS (
    esame del secondo anno superato dallo studente
)
```

staresti dicendo:

> lo studente ha superato almeno un esame del secondo anno

Ma il testo chiede:

> lo studente ha superato tutti gli esami del secondo anno

Quindi `EXISTS` è troppo debole.

---

# 7. Differenza tra uno e due `NOT EXISTS`

## Un solo `NOT EXISTS`

Lo usi quando il caso vietato si vede direttamente su una riga o su un join.

Esempio:

> attori che non hanno recitato in alcun film di Ken Loach

```sql
WHERE NOT EXISTS (
    SELECT *
    FROM INTERPRETAZIONE I
    JOIN FILM F ON I.Film = F.CodiceFilm
    WHERE I.Attore = A.CodiceAttore
      AND F.Regista = 'Loach'
)
```

## Due `NOT EXISTS`

Li usi quando devi esprimere:

```text
per ogni X deve esistere Y
```

oppure un contenimento tra insiemi.

Esempio:

> studenti che hanno superato tutti gli esami del secondo anno

```text
per ogni insegnamento del secondo anno
esiste un esame dello studente
```

In SQL:

```sql
NOT EXISTS (
    insegnamento del secondo anno
    che NOT EXISTS tra gli esami dello studente
)
```

---

# 8. Pattern “per ogni X esiste Y”

Questo è il pattern più importante:

```text
PER OGNI X, ESISTE Y
```

diventa:

```sql
NOT EXISTS (
    X
    AND NOT EXISTS (
        Y corrispondente
    )
)
```

Perché:

```text
per ogni X esiste Y
```

equivale a:

```text
non esiste un X senza Y
```

---

# 9. Esempio: ricercatori e musei

Testo:

> i ricercatori tali che esiste almeno un reperto da loro scoperto in ogni museo in cui si trova almeno un reperto scoperto da R2324

Significa:

```text
per ogni museo di R2324
esiste un reperto del ricercatore corrente in quel museo
```

```sql
SELECT R.CodRicercatore
FROM Ricercatore AS R
WHERE NOT EXISTS (
    SELECT *
    FROM Reperto AS Rep1
    WHERE Rep1.Ricercatore = 'R2324'
      AND NOT EXISTS (
          SELECT *
          FROM Reperto AS Rep2
          WHERE Rep2.Ricercatore = R.CodRicercatore
            AND Rep2.Museo = Rep1.Museo
      )
);
```

---

# 10. Pattern “unico”

Quando il testo dice:

> è l’unico

di solito usi:

```sql
EXISTS (
    mio caso
    AND NOT EXISTS (
        caso di un altro
    )
)
```

---

# 11. Pattern “non in tutti”

Quando il testo dice:

> ha fatto almeno uno, ma non tutti

usi spesso:

```sql
EXISTS (almeno uno fatto)
AND EXISTS (uno mancante)
```

---

# 12. Pattern “tutti e soli”

Quando il testo dice:

> tutti e soli

significa:

```text
A = B
```

Servono due contenimenti:

```text
A ⊆ B
AND
B ⊆ A
```

In SQL:

```sql
WHERE NOT EXISTS (
    film di Kurosawa che manca all’attore
)
AND NOT EXISTS (
    film dell’attore che non è di Kurosawa
)
```

---

# 13. Quando `EXISTS` dà il contrario di `NOT EXISTS`

Richiesta:

> club privi di atleti sul podio

Corretto:

```sql
WHERE NOT EXISTS (
    atleta del club con posizione IN (1,2,3)
)
```

Se scrivi:

```sql
WHERE EXISTS (
    atleta del club con posizione IN (1,2,3)
)
```

ottieni:

> club con almeno un atleta sul podio

cioè il contrario.

---

# 14. Attenzione: anche cambiare la condizione dentro cambia tutto

Corretto:

```sql
NOT EXISTS (
    posizione IN (1,2,3)
)
```

oppure:

```sql
NOT EXISTS (
    posizione <= 3
)
```

Se scrivi:

```sql
NOT EXISTS (
    posizione > 3
)
```

stai dicendo:

> non esistono atleti fuori dal podio

che è una richiesta completamente diversa.

---

# 15. Riassunto secco

## Usa `EXISTS` quando vuoi dire:

```text
esiste almeno una riga buona
```

Esempi:

- almeno un esame
    
- almeno una conferenza
    
- almeno un film
    
- almeno un conto
    
- almeno un caso in cui è unico
    

## Usa `NOT EXISTS` quando vuoi dire:

```text
non esiste nessuna riga cattiva
```

Esempi:

- nessun esame nel 2014
    
- nessun film non di Kurosawa
    
- nessun atleta sul podio
    
- nessun conto fuori Veneto
    
- nessun insegnamento mancante
    

---

# 16. Formula finale da ricordare

```text
EXISTS = almeno uno
NOT EXISTS = nessuno
```

Ma il vero trucco è:

```text
EXISTS cerca il caso buono
NOT EXISTS esclude il caso cattivo
```

E per “tutti”:

```text
Tutti X hanno Y
=
Non esiste X senza Y
```

quindi:

```sql
NOT EXISTS (
    X
    AND NOT EXISTS (Y)
)
```