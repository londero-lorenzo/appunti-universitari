---
title: "Guida Query Sql"
aliases: ["Guida Query Sql"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "GuidaEsame", "guida-query-SQL"]
created: 2026-04-22
---
Certo. Ti preparo una guida pratica, costruita sui pattern che abbiamo usato negli esercizi, per capire **come riconoscere il tipo di query** e **come impostarla correttamente**. L’idea di fondo è sempre quella delle slide: partire da `SELECT`, `FROM`, `WHERE`, `GROUP BY`, `HAVING`, sapendo che logicamente una query si ragiona soprattutto come `FROM → WHERE → GROUP BY → HAVING → SELECT`. Inoltre, `WHERE` filtra righe, mentre `HAVING` filtra gruppi; `EXISTS` e `NOT EXISTS` servono per condizioni di esistenza o assenza; `ALL` è utile per massimi e minimi.

# Guida completa ai pattern delle query SQL

## 1. Il metodo generale: come iniziare sempre

Quando leggi un esercizio, non partire subito dal codice. Parti da queste 5 domande.

### 1. Che cosa devo restituire?

Devi capire qual è l’oggetto del risultato:

- studenti?
    
- reparti?
    
- gare?
    
- coppie di persone?
    
- un numero medio?
    
- un massimo?
    

Questo ti dice **cosa va nel `SELECT`**.

### 2. Da quali tabelle prendo i dati?

Devi capire quali relazioni contengono le informazioni che ti servono.

Questo ti dice **cosa va nel `FROM`** e quali join servono.

### 3. Sto filtrando righe o gruppi?

Questa è la domanda più importante:

- se stai scegliendo singole tuple, usi `WHERE`
    
- se stai scegliendo gruppi dopo un conteggio/media/somma, usi `HAVING`
    

### 4. La query chiede “esiste”, “non esiste”, “tutti”, “solo”, “almeno uno”?

Se sì, probabilmente devi ragionare con:

- `EXISTS`
    
- `NOT EXISTS`
    
- eventualmente doppio `NOT EXISTS`
    

### 5. La query chiede un numero massimo/minimo?

Allora spesso devi:

- contare per gruppo
    
- poi confrontare con:
    
    - `MAX(...)`
        
    - oppure `>= ALL (...)`
        
    - oppure `<= ALL (...)`
        

---

# 2. Pattern fondamentale: query semplici con SELECT-FROM-WHERE

Questo è il caso base.

## Quando si usa

Quando il testo ti chiede solo di:

- selezionare certi record
    
- unire tabelle
    
- filtrare su attributi
    
- calcolare espressioni semplici
    

## Struttura mentale

1. prendi le tabelle
    
2. fai i join
    
3. metti i filtri nel `WHERE`
    
4. scegli cosa mostrare nel `SELECT`
    

## Esempio di logica

“i turisti che hanno visitato una città polacca prima del 1979”:

- tabelle: `Turista`, `Ha_Visitato`, `Si_Trova_In`
    
- join sui campi chiave
    
- filtro su `Nazione = 'Polonia'`
    
- filtro su anno < 1979
    
- nel `SELECT` puoi anche mettere l’età calcolata
    

## Segnale tipico

Se non compaiono parole come:

- numero di
    
- media
    
- tutti
    
- nessuno
    
- unico
    
- massimo/minimo
    

allora spesso basta `SELECT-FROM-WHERE`.

---

# 3. Pattern con GROUP BY e HAVING

Questo è il pattern da usare quando devi **contare**, **fare medie**, **somma**, **massimo per gruppo**, ecc.

## Quando si usa

Quando il testo dice:

- il numero di ...
    
- la media di ...
    
- la somma di ...
    
- almeno 2
    
- esattamente 3
    
- più di 5
    
- per ogni reparto / per ogni studente / per ogni città
    

## Regola fondamentale

- `WHERE` filtra le righe prima del raggruppamento
    
- `GROUP BY` costruisce i gruppi
    
- `HAVING` tiene solo i gruppi che soddisfano una condizione aggregata
    

## Esempi tipici

### “studenti con insufficienza in due materie”

- filtri prima: `voto <= 5`
    
- gruppi: per studente
    
- condizione sul gruppo: `COUNT(*) = 2`
    

### “ispettori che nel 2013 hanno controllato una o due aziende”

- filtri prima: `Anno = 2013`
    
- gruppi: per ispettore
    
- condizione: `COUNT(*) = 1 OR COUNT(*) = 2`
    

### “aziende controllate da un unico ispettore”

Attenzione: qui non conti i controlli, ma gli **ispettori distinti**.

- gruppi: per azienda
    
- condizione: `COUNT(DISTINCT Ispettore) = 1`
    

## Errore tipico

Mettere `COUNT(*) > 2` nel `WHERE`.  
È sbagliato, perché i gruppi ancora non esistono. Le aggregazioni vanno in `HAVING`.

---

# 4. Pattern EXISTS

`EXISTS` si usa quando il testo dice:

- esiste almeno uno
    
- almeno una materia
    
- almeno una conferenza
    
- almeno una gara
    
- almeno un medico
    
- almeno una riga con una certa proprietà
    

## Traduzione mentale

“Esiste almeno uno ...”  
→ `EXISTS (SELECT * FROM ... WHERE ...)`

## Esempi tipici

### “studenti tali che esiste almeno un esame in cui sono stati gli unici a superarlo”

- `EXISTS` un esame dello studente
    
- tale che `NOT EXISTS` un altro studente sullo stesso esame
    

### “afferenti tali che esiste almeno una conferenza del 2011 in cui sono stati gli unici del dipartimento”

- `EXISTS` una partecipazione del 2011
    
- con `NOT EXISTS` altri partecipanti del dipartimento
    

## Formula mentale

Quando leggi:

> almeno uno / almeno una / esiste

pensa subito:

```sql
WHERE EXISTS ( ... )
```

---

# 5. Pattern NOT EXISTS

`NOT EXISTS` si usa quando il testo dice:

- nessuno
    
- non esiste
    
- mai
    
- non ha fatto alcun ...
    
- privo di ...
    
- non ha partecipato ad alcuna ...
    
- tutti gli elementi devono soddisfare una proprietà
    

## Traduzione mentale

“Non esiste una riga con una certa proprietà”  
→ `NOT EXISTS (SELECT * FROM ... WHERE ...)`

## Esempi tipici

### “studenti che nel 2014 non hanno superato alcun esame”

- `NOT EXISTS` un esame con anno 2014
    

### “medici ortopedici che nel maggio 2013 non hanno visitato pazienti di Verona”

- `NOT EXISTS` una visita di quel medico a un paziente di Verona nel periodo indicato
    

### “musicisti che non hanno mai suonato in sale >500 posti o in Germania”

- `NOT EXISTS` un concerto “proibito”
    

## Errore tipico

Pensare che `NOT EXISTS` “restituisca dati”.  
Non restituisce righe da mostrare: restituisce **vero/falso** nella `WHERE`.

---

# 6. Pattern “tutti”, “ogni”, “solo”: doppio NOT EXISTS

Questo è uno dei pattern più importanti.

## Quando si usa

Quando il testo dice:

- tutti gli esami ...
    
- ogni anno ...
    
- tutte le edizioni ...
    
- ha partecipato solo a ...
    
- ha superato un sottoinsieme ...
    
- ha un soprainsieme ...
    
- stesso insieme
    

## Idea chiave

Le frasi con “tutti” si traducono meglio così:

> **non esiste** un elemento del primo insieme  
> per cui **non esiste** una corrispondenza nel secondo insieme

Questa è la struttura:

```sql
NOT EXISTS (
    elemento del primo insieme
    AND NOT EXISTS (
        elemento corrispondente del secondo insieme
    )
)
```

Le slide mostrano proprio questa trasformazione per il contenimento tra insiemi e per il “contains”.

## Esempi tipici

### “studenti che hanno superato tutti gli esami di un altro studente”

- non esiste un esame dell’altro
    
- che non esiste anche nello studente candidato
    

### “afferenti che dal 2001 hanno partecipato ogni anno ad almeno una conferenza”

- non esiste un anno globale
    
- che non esiste tra gli anni dell’afferente
    

### “registi che hanno partecipato a tutte le edizioni di un festival”

- non esiste un’edizione del festival
    
- a cui il regista non ha partecipato
    

---

# 7. Pattern “sottoinsieme”, “soprainsieme”, “stesso insieme”, “proprio”

Questo è il cuore di molti esercizi.

## 7.1 Sottoinsieme

“X ha un sottoinsieme delle cose di Y” significa:

```text
X ⊆ Y
```

Traduzione:

- non esiste un elemento di X che non sia in Y
    

Schema:

```sql
NOT EXISTS (
    elemento di X
    AND NOT EXISTS (
        stesso elemento in Y
    )
)
```

## 7.2 Soprainsieme

“X ha un soprainsieme delle cose di Y” significa:

```text
Y ⊆ X
```

Traduzione:

- non esiste un elemento di Y che non sia in X
    

Schema:

```sql
NOT EXISTS (
    elemento di Y
    AND NOT EXISTS (
        stesso elemento in X
    )
)
```

## 7.3 Stesso insieme

“X ha lo stesso insieme di Y” significa:

```text
X = Y
```

cioè due inclusioni:

- `X ⊆ Y`
    
- `Y ⊆ X`
    

Quindi servono **due blocchi**.

## 7.4 Sottoinsieme proprio

“X ha un sottoinsieme proprio di Y” significa:

- `X ⊆ Y`
    
- e `X ≠ Y`
    

quindi:

- primo blocco: contenimento
    
- secondo blocco: esiste un elemento di Y che manca in X
    

## 7.5 Soprainsieme proprio

“X ha un soprainsieme proprio di Y” significa:

- `Y ⊆ X`
    
- e `X ≠ Y`
    

quindi:

- primo blocco: contenimento inverso
    
- secondo blocco: esiste un elemento di X che manca in Y
    

## Formula pratica

- **sottoinsieme** → “non esiste elemento mio fuori da lui”
    
- **soprainsieme** → “non esiste elemento suo fuori da me”
    
- **stesso insieme** → entrambe
    
- **proprio** → aggiungi anche l’esistenza di un elemento che sta solo da una parte
    

---

# 8. Pattern “unico”, “gli unici”, “nessun altro”

Questo pattern compare spesso.

## Quando si usa

Quando il testo dice:

- è l’unico
    
- sono gli unici
    
- nessun altro
    
- nessun altro studente/medico/afferente/tennista
    

## Struttura tipica

```sql
EXISTS (
    mia partecipazione / mio esame / mia riga
    AND NOT EXISTS (
        riga di un altro
        con la stessa proprietà rilevante
    )
)
```

## Esempi

### “studenti che nel 2015 sono stati gli unici a superare almeno un esame”

- `EXISTS` un esame dello studente nel 2015
    
- `NOT EXISTS` altro studente sullo stesso insegnamento nel 2015
    

### “afferenti che nel 2011 sono stati gli unici del dipartimento a una conferenza”

- `EXISTS` una partecipazione
    
- `NOT EXISTS` altra partecipazione alla stessa conferenza/anno
    

### “musicisti che nel 2014 hanno suonato solo in sale in cui erano gli unici”

- per ogni sala del 2014 dello stesso musicista
    
- non deve esistere un altro musicista in quella sala nel 2014
    

---

# 9. Pattern con ALL per massimo e minimo

`ALL` è molto utile quando il testo chiede:

- il massimo
    
- il minimo
    
- il maggior numero
    
- il minor numero
    
- il voto più alto
    
- il maggior numero di partecipazioni
    

## Regola pratica

- massimo → `>= ALL (...)`
    
- minimo → `<= ALL (...)`
    

## Esempi

### “l’afferente che nel biennio ha partecipato al maggior numero di conferenze”

- conti per afferente
    
- `HAVING COUNT(*) >= ALL (...)`
    

### “reparti col minor numero di medici femminili”

- conti le mediche per reparto
    
- `HAVING COUNT(*) <= ALL (...)`
    

Le slide presentano `ALL` proprio come confronto di un valore con tutti i valori prodotti da una sottoquery.

---

# 10. Pattern con MIN e MAX

A volte, invece di `ALL`, puoi usare:

- `MAX(...)`
    
- `MIN(...)`
    

## Quando si usa

Quando vuoi confrontare un conteggio o un valore con:

- il massimo dei conteggi
    
- il minimo dei conteggi
    
- il massimo dei voti su una stessa prova/materia
    

## Esempi

### “studenti che hanno ottenuto il voto più alto in almeno una materia”

- per una riga `R`, confronti `R.voto` con:
    

```sql
SELECT MAX(voto) ...
```

### “reparti col minor numero di medici femminili”

- puoi prima calcolare tutti i conteggi per reparto
    
- poi applicare `MIN` a quei conteggi
    

## Nota pratica

- `ALL` è spesso più elegante
    
- `MAX/MIN` a volte è più intuitivo
    

---

# 11. Pattern con EXCEPT

`EXCEPT` è molto utile per esprimere differenza tra insiemi.

## Idea chiave

Se vuoi dire:

- “X è contenuto in Y”
    

puoi scrivere:

```text
X − Y = ∅
```

In SQL:

```sql
NOT EXISTS (
    SELECT ...
    FROM X
    EXCEPT
    SELECT ...
    FROM Y
)
```

Le slide mostrano proprio il legame tra contenimento e differenza insiemistica vuota.

## Quando conviene

Quando il testo parla di:

- sottoinsieme
    
- soprainsieme
    
- stesso insieme
    
- tutte le edizioni
    
- tutti gli esami
    
- tutte le conferenze
    

## Esempio mentale

“le edizioni di LICS dell’afferente A sono sottoinsieme di quelle di B”:

```sql
NOT EXISTS (
   edizioni di A
   EXCEPT
   edizioni di B
)
```

---

# 12. Quando usare condizioni separate e quando annidate

Questa è una domanda chiave.

## Usa condizioni separate quando il testo chiede proprietà indipendenti

Esempio:

- tutti i medici in Piemonte
    
- almeno uno a Torino
    

Qui hai due test distinti:

```sql
WHERE NOT EXISTS(...)
  AND EXISTS(...)
```

## Usa annidate quando una condizione dipende da un elemento trovato dalla prima

Esempio:

- per ogni materia di Matteo, deve esistere la stessa materia nello studente
    
- esiste un esame tale che non esiste nessun altro studente sullo stesso esame
    

Qui la seconda query dipende dalla riga trovata dalla prima.

## Regola pratica

Chiediti:

> la seconda condizione dipende dalla riga della prima?

- se no → spesso separate
    
- se sì → spesso annidate
    

---

# 13. Errori tipici da evitare

## 13.1 Mettere aggregazioni nel WHERE

Sbagliato:

```sql
WHERE COUNT(*) > 2
```

Corretto:

```sql
HAVING COUNT(*) > 2
```

## 13.2 Usare `COUNT(*)` quando serve `COUNT(DISTINCT ...)`

Se il testo dice:

- tornei diversi
    
- aziende diverse
    
- materie diverse
    

devi quasi sempre valutare `DISTINCT`.

## 13.3 Confondere “esiste almeno uno” con “tutti”

- “esiste almeno uno” → `EXISTS`
    
- “tutti” → spesso `NOT EXISTS` su controesempio
    

## 13.4 Filtrare righe buone invece di escludere i casi cattivi

Esempio sbagliato:

- per “solo in Piemonte” mettere `WHERE Regione = 'Piemonte'`
    

Questo non basta, perché uno stesso soggetto può avere anche righe fuori Piemonte.

Devi invece fare:

- `NOT EXISTS` una riga fuori Piemonte
    

## 13.5 Dimenticare che “più alto di tutti” è stretto

Se il testo dice:

- più alto di tutti gli altri
    

allora il controesempio è:

- un altro con voto `>=`  
    non solo `>`.
    

## 13.6 Dimenticare la differenza tra “sottoinsieme” e “sottoinsieme proprio”

- sottoinsieme → basta il contenimento
    
- sottoinsieme proprio → serve anche dimostrare che non c’è uguaglianza
    

---

# 14. Schema operativo da usare all’esame

Quando leggi un esercizio, fai sempre questo mini-schema.

## Caso A: chiede numeri, media, somma, massimo/minimo per gruppo

Pensa a:

- `GROUP BY`
    
- `HAVING`
    
- eventualmente `ALL`, `MIN`, `MAX`
    

## Caso B: chiede “almeno uno”

Pensa a:

- `EXISTS`
    

## Caso C: chiede “nessuno”, “mai”, “privo di”

Pensa a:

- `NOT EXISTS`
    

## Caso D: chiede “tutti”, “ogni”, “solo”

Pensa a:

- controesempio
    
- doppio `NOT EXISTS`
    

## Caso E: chiede confronto di insiemi

Pensa a:

- sottoinsieme / soprainsieme / stesso insieme
    
- doppio `NOT EXISTS`
    
- oppure `EXCEPT`
    

## Caso F: chiede “massimo” o “minimo”

Pensa a:

- conteggio per gruppo
    
- confronto con `>= ALL (...)` o `<= ALL (...)`
    

---

# 15. Tabella mentale super sintetica

## “almeno uno”

```sql
EXISTS (...)
```

## “nessuno / mai”

```sql
NOT EXISTS (...)
```

## “tutti / ogni”

```sql
NOT EXISTS (
   elemento
   che NOT EXISTS (...)
)
```

## “sottoinsieme”

```sql
NOT EXISTS (
   mio elemento
   che manca nell’altro
)
```

## “soprainsieme”

```sql
NOT EXISTS (
   suo elemento
   che manca in me
)
```

## “stesso insieme”

due inclusioni

## “proprio”

contenimento + esistenza di un elemento in più o in meno

## “numero / media / somma”

`GROUP BY` + funzione aggregata

## “massimo / minimo”

`>= ALL (...)` / `<= ALL (...)`

---

# 16. Metodo finale di scrittura

Quando hai capito il pattern, scrivi la query sempre in questo ordine mentale:

### Step 1

Scrivi la query esterna:

- chi vuoi restituire?
    

### Step 2

Scrivi il blocco base:

- tabelle e join necessari
    

### Step 3

Aggiungi i filtri semplici:

- anno, luogo, città, specialità, voto, ecc.
    

### Step 4

Capisci se ti serve:

- `GROUP BY/HAVING`
    
- `EXISTS`
    
- `NOT EXISTS`
    
- doppio `NOT EXISTS`
    
- `ALL`
    
- `EXCEPT`
    

### Step 5

Controlla sempre:

- sto contando le righe giuste?
    
- serviva `DISTINCT`?
    
- la condizione è su righe o su gruppi?
    
- il testo dice “proprio” o no?
    
- il testo chiede “almeno uno” o “tutti”?
    

---

Se vuoi, posso trasformare questa guida in una **scheda riassuntiva ultra compatta da ripassare prima dell’esame**.