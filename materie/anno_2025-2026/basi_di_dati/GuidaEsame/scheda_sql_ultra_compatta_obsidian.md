# SQL — Scheda riassuntiva ultra compatta per l’esame

## 1. Prima domanda: cosa chiede il testo?

### Se chiede...
- **elenco di entità** → `SELECT ... FROM ... WHERE ...`
- **numero / media / somma** → `GROUP BY` + funzione aggregata
- **almeno uno / esiste** → `EXISTS`
- **nessuno / mai / non esiste / privo di** → `NOT EXISTS`
- **tutti / ogni / solo** → spesso doppio `NOT EXISTS`
- **massimo / minimo / maggior numero / minor numero** → `ALL`, `MAX`, `MIN`
- **sottoinsieme / soprainsieme / stesso insieme** → contenimento tra insiemi

---

## 2. Regola d’oro: WHERE vs HAVING

### `WHERE`
Filtra le **righe** prima del raggruppamento.

Esempi:
- `Anno = 2013`
- `Voto <= 5`
- `Nazione = 'Germania'`

### `HAVING`
Filtra i **gruppi** dopo il `GROUP BY`.

Esempi:
- `HAVING COUNT(*) = 2`
- `HAVING COUNT(*) >= 3`
- `HAVING COUNT(DISTINCT Torneo) <= 2`

### Formula mentale
- condizione su **una riga** → `WHERE`
- condizione su **un conteggio/media/somma** → `HAVING`

---

## 3. Pattern base

## A. Query semplice
Quando non ci sono conteggi o “tutti/nessuno”.

```sql
SELECT ...
FROM ...
WHERE ...
```

---

## B. Conteggi, media, somma
Quando il testo dice:
- numero di
- media di
- somma di
- almeno 2 / esattamente 3 / più di 5

```sql
SELECT X
FROM ...
WHERE ...
GROUP BY X
HAVING COUNT(*) ...
```

### Attenzione
- **“diversi”** → spesso serve `COUNT(DISTINCT ...)`

---

## 4. Pattern EXISTS / NOT EXISTS

## A. “Esiste almeno uno”
```sql
WHERE EXISTS (
    SELECT *
    FROM ...
    WHERE ...
)
```

### Parole chiave
- almeno uno
- almeno una
- esiste

---

## B. “Non esiste nessuno”
```sql
WHERE NOT EXISTS (
    SELECT *
    FROM ...
    WHERE ...
)
```

### Parole chiave
- nessuno
- mai
- non esiste
- non ha fatto alcun
- privo di

---

## 5. Pattern “tutti”, “ogni”, “solo”

Quando il testo dice:
- tutti
- ogni
- solo
- ha partecipato a tutte le ...
- ha superato tutti gli ...

### Schema standard
```sql
WHERE NOT EXISTS (
    elemento del primo insieme
    AND NOT EXISTS (
        elemento corrispondente del secondo insieme
    )
)
```

### Traduzione mentale
> non esiste un elemento che manca dall’altra parte

---

## 6. Pattern insiemi

## A. Sottoinsieme
**I miei elementi stanno tutti nei suoi**

```sql
NOT EXISTS (
    elemento mio
    AND NOT EXISTS (
        stesso elemento suo
    )
)
```

### Formula mentale
> non esiste un mio elemento fuori dal suo insieme

---

## B. Soprainsieme
**I suoi elementi stanno tutti nei miei**

```sql
NOT EXISTS (
    elemento suo
    AND NOT EXISTS (
        stesso elemento mio
    )
)
```

### Formula mentale
> non esiste un suo elemento fuori dal mio insieme

---

## C. Stesso insieme
Due inclusioni insieme:

- mio sottoinsieme del suo
- suo sottoinsieme del mio

Quindi servono **due blocchi**.

---

## D. Sottoinsieme proprio
- contenimento
- e almeno un elemento suo che manca in me

```sql
contenimento
AND EXISTS (
    elemento suo
    che manca in me
)
```

---

## E. Soprainsieme proprio
- contenimento
- e almeno un elemento mio che manca in lui

```sql
contenimento
AND EXISTS (
    elemento mio
    che manca in lui
)
```

---

## 7. Pattern “unico / gli unici / nessun altro”

Quando il testo dice:
- unico
- gli unici
- nessun altro
- l’unico a superare / partecipare / vincere

### Schema standard
```sql
WHERE EXISTS (
    mio elemento
    AND NOT EXISTS (
        elemento di un altro
        con la stessa proprietà
    )
)
```

### Formula mentale
> esiste un caso in cui ci sono io e non esiste nessun altro

---

## 8. Massimo e minimo

## A. Con `ALL`
### Massimo
```sql
HAVING COUNT(*) >= ALL (
    SELECT COUNT(*)
    FROM ...
    GROUP BY ...
)
```

### Minimo
```sql
HAVING COUNT(*) <= ALL (
    SELECT COUNT(*)
    FROM ...
    GROUP BY ...
)
```

---

## B. Con `MAX` / `MIN`
Alternativa equivalente.

### Esempio logico
- prima calcolo tutti i conteggi
- poi prendo `MAX` o `MIN`
- poi confronto

---

## 9. Pattern EXCEPT

Molto utile per sottoinsiemi / soprainsiemi / stesso insieme.

### Sottoinsieme
```sql
NOT EXISTS (
    SELECT ...
    FROM X
    EXCEPT
    SELECT ...
    FROM Y
)
```

### Traduzione
> X − Y = ∅

---

## 10. Quando usare condizioni separate e quando annidate

## Usa condizioni separate se...
il testo chiede **due proprietà indipendenti**.

### Esempio
- tutti in Piemonte
- almeno uno a Torino

```sql
WHERE NOT EXISTS (...)
  AND EXISTS (...)
```

---

## Usa condizioni annidate se...
una condizione dipende da una riga trovata dalla prima.

### Esempio
- per ogni esame di Marco deve esistere lo stesso esame nello studente
- esiste una conferenza per cui non esiste nessun altro

```sql
NOT EXISTS (
   elemento
   AND NOT EXISTS (...)
)
```

### Domanda guida
> la seconda condizione dipende dalla riga della prima?

- **no** → spesso separate
- **sì** → spesso annidate

---

## 11. Errori tipici da evitare

### 1. `COUNT(*)` nel `WHERE`
❌ Sbagliato

```sql
WHERE COUNT(*) > 2
```

✅ Corretto

```sql
HAVING COUNT(*) > 2
```

---

### 2. Dimenticare `DISTINCT`
Se il testo dice:
- diversi
- tornei diversi
- aziende diverse
- materie diverse

valuta `COUNT(DISTINCT ...)`

---

### 3. Confondere “almeno uno” con “tutti”
- almeno uno → `EXISTS`
- tutti → spesso doppio `NOT EXISTS`

---

### 4. Filtrare le righe buone invece di escludere i casi cattivi
Se il testo dice “solo in Piemonte”, non basta:

```sql
WHERE Regione = 'Piemonte'
```

Perché uno stesso soggetto può avere anche righe fuori Piemonte.

Devi pensare:
```sql
NOT EXISTS (riga fuori Piemonte)
```

---

### 5. Dimenticare che “più alto di tutti” è stretto
Se il testo dice:
- più alto di tutti gli altri

il controesempio è:
```sql
altro con voto >=
```

non solo `>`.

---

### 6. Dimenticare la parola “proprio”
- sottoinsieme → contenimento
- sottoinsieme proprio → contenimento + differenza
- soprainsieme proprio → contenimento + differenza

---

## 12. Mini-tabella finale da memorizzare

| Testo dell’esercizio | Pattern |
|---|---|
| almeno uno | `EXISTS` |
| nessuno / mai | `NOT EXISTS` |
| tutti / ogni | doppio `NOT EXISTS` |
| numero / media / somma | `GROUP BY` + aggregazione |
| almeno 2 / esattamente 3 | `HAVING COUNT(*) ...` |
| diversi | `DISTINCT` |
| massimo | `>= ALL (...)` oppure `MAX` |
| minimo | `<= ALL (...)` oppure `MIN` |
| sottoinsieme | `NOT EXISTS (mio elemento fuori dal suo insieme)` |
| soprainsieme | `NOT EXISTS (suo elemento fuori dal mio insieme)` |
| stesso insieme | doppia inclusione |
| unico | `EXISTS (... AND NOT EXISTS altro ...)` |

---

## 13. Procedura pratica da usare sempre

### Step 1
Chiediti: **che cosa devo restituire?**
- una persona?
- una coppia?
- una città?
- un numero?

### Step 2
Individua le **tabelle necessarie**.

### Step 3
Capisci se il testo chiede:
- filtro semplice
- conteggio
- esistenza
- assenza
- contenimento tra insiemi
- massimo/minimo

### Step 4
Scegli il pattern:
- `WHERE`
- `GROUP BY/HAVING`
- `EXISTS`
- `NOT EXISTS`
- doppio `NOT EXISTS`
- `ALL`
- `EXCEPT`

### Step 5
Controlla sempre:
- sto contando le righe giuste?
- serve `DISTINCT`?
- devo usare `HAVING` invece di `WHERE`?
- il testo dice “proprio” oppure no?
- sto confrontando singole righe o insiemi?

---

## 14. Schema mentale lampo

- **se conta** → `GROUP BY`
- **se cerca almeno uno** → `EXISTS`
- **se vieta qualcosa** → `NOT EXISTS`
- **se dice tutti/ogni** → controesempio + doppio `NOT EXISTS`
- **se confronta insiemi** → contenimento
- **se cerca massimo/minimo** → `ALL` / `MAX` / `MIN`

---

## 15. Frasi da riconoscere subito

### “solo”
> nessuna riga fuori dall’insieme ammesso

### “tutti”
> non esiste un elemento che manca

### “almeno uno”
> esiste una riga buona

### “mai”
> non esiste riga cattiva

### “stesso insieme”
> doppia inclusione

### “sottoinsieme proprio”
> contenimento + elemento mancante dall’altra parte

### “soprainsieme proprio”
> contenimento + elemento in più dalla mia parte
