---
title: "16 1 Organizzazione Fisica"
aliases: ["16 1 Organizzazione Fisica"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "16-1-organizzazione-fisica"]
created: 2026-05-18
---
Fonte: slide **16_1_OrganizzazioneFisica.pdf – Organizzazione Fisica dei Dati, Parte I**.

````markdown
# Organizzazione fisica dei dati - Parte I

#basi-di-dati #modello-fisico #file #record #hashing

## 1. Idea generale

Nel modello fisico dei dati ci si occupa di **come i dati vengono effettivamente memorizzati su memoria secondaria**, cioè su disco.

A livello logico noi vediamo relazioni, tuple e attributi.  
A livello fisico, invece, i dati sono organizzati in:

- **file**
- **record**
- **campi**
- **blocchi**
- eventuali **strutture di accesso**, come indici o strutture hash

Una tupla relazionale può essere vista fisicamente come un **record**, e il valore di ciascun attributo può essere memorizzato in un **campo** del record.

---

## 2. File di record

Un **file di record** è una collezione di record memorizzati su disco.

Ogni record rappresenta una collezione di dati riferiti a entità, attributi o relazioni.

Esempio:

```text
IMPIEGATO(CF, nome, cognome, stipendio)
````

può essere memorizzato come un record con campi:

```text
CF | nome | cognome | stipendio
```

---

## 3. Tecniche principali di organizzazione dei file

Le slide distinguono tre tecni­che principali di memorizzazione fisica dei record:

|Tecnica|Descrizione|Idea principale|
|---|---|---|
|**Heap file**|File non ordinato|I record sono inseriti senza un ordine particolare|
|**Sorted file**|File ordinato/sequenziale|I record sono ordinati rispetto a uno o più campi|
|**Hashed file**|File hash|La posizione del record dipende da una funzione hash|

---

## 4. Modalità di accesso alla base di dati

Molte applicazioni non devono leggere l’intera base di dati, ma solo una sua piccola parte.

Quando un’applicazione richiede certi dati, il DBMS deve:

1. **localizzare** i dati all’interno della base di dati;
    
2. **copiarli in memoria principale**, perché la CPU lavora sui dati in RAM;
    
3. se i dati sono stati modificati, **riscriverli su memoria secondaria**.
    

Quindi il costo di accesso ai dati dipende molto da:

- come i record sono organizzati;
    
- quanti blocchi bisogna leggere;
    
- se esistono strutture di accesso efficienti.
    

> Punto importante per l’esame: il costo delle operazioni fisiche viene spesso misurato in numero di **accessi a blocco**, non in numero di record.

---

# Record

## 5. Record di lunghezza fissa e variabile

Un file è una sequenza di record, solitamente dello stesso tipo.

### Record di lunghezza fissa

Un file ha **record di lunghezza fissa** quando tutti i record hanno la stessa dimensione in byte.

Esempio:

```text
Studente(matricola CHAR(10), età INT, anno INT)
```

Se tutti i campi hanno lunghezza fissa, ogni record occupa sempre lo stesso spazio.

### Record di lunghezza variabile

Un file ha **record di lunghezza variabile** quando non tutti i record hanno la stessa dimensione.

Le cause principali possono essere:

1. **Campi di lunghezza variabile**
    
    Esempio:
    
    ```text
    nome VARCHAR(50)
    ```
    
    Un nome come `Luca` occupa meno spazio di un nome più lungo.
    
2. **Campi ripetuti**
    
    Un campo può avere più valori per lo stesso record.
    
    Esempio:
    
    ```text
    Studente(nome, telefoni)
    ```
    
    dove uno studente può avere uno o più numeri di telefono.
    
3. **Campi opzionali**
    
    Alcuni record hanno un certo campo valorizzato, altri no.
    
    Esempio:
    
    ```sql
    Dipendente(nome, secondo_nome?)
    ```
    
4. **File mixed**
    
    Il file contiene record di tipi diversi e quindi di dimensioni diverse.
    
    Esempio storico: nel modello gerarchico, i record `ESAME` di uno studente potevano essere posizionati subito dopo il record `STUDENTE`.
    

---

# Blocchi

## 6. Organizzazione dei record in blocchi

I record devono essere allocati in **blocchi**, perché il blocco è l’unità di trasferimento tra disco e memoria principale.

Questo significa che il DBMS non legge normalmente un singolo record isolato, ma legge un intero blocco che può contenere più record.

Siano:

- `B` = dimensione del blocco in byte;
    
- `R` = dimensione del record in byte;
    
- `B >= R`.
    

Il numero massimo di record che possono stare in un blocco è detto:

## Blocking factor

$$  
bfr = \left\lfloor \frac{B}{R} \right\rfloor  
$$

dove:

- `bfr` = blocking factor;
    
- `B` = dimensione del blocco;
    
- `R` = dimensione del record.
    

### Esempio

Se:

```text
B = 120 byte
R = 15 byte
```

allora:

$$  
bfr = \left\lfloor \frac{120}{15} \right\rfloor = 8  
$$

Quindi ogni blocco può contenere 8 record.

---

## 7. Record spanned e unspanned

I record possono essere organizzati nei blocchi secondo due modalità.

## Organizzazione unspanned

Nell’organizzazione **unspanned**, un record non può essere diviso tra due blocchi.

Quindi ogni record deve stare interamente dentro un singolo blocco.

### Conseguenza

Se in un blocco rimane spazio libero ma non sufficiente per contenere un intero record, quello spazio resta inutilizzato.

Esempio concettuale:

```text
Blocco i:     [Record 1][Record 2][Record 3][spazio vuoto]
Blocco i+1:   [Record 4][Record 5][Record 6][spazio vuoto]
```

## Organizzazione spanned

Nell’organizzazione **spanned**, un record può essere diviso tra due blocchi.

Una parte del record si trova in un blocco, mentre la parte rimanente si trova nel blocco successivo.

Esempio concettuale:

```text
Blocco i:     [Record 1][Record 2][inizio Record 3]
Blocco i+1:   [fine Record 3][Record 4][Record 5]
```

Per collegare le due parti del record servono puntatori o informazioni aggiuntive.

---

## 8. Confronto tra spanned e unspanned

|Aspetto|Unspanned|Spanned|
|---|---|---|
|Record diviso tra blocchi?|No|Sì|
|Semplicità|Maggiore|Minore|
|Spreco di spazio|Possibile|Minore|
|Gestione|Più semplice|Più complessa|
|Utile per record molto grandi?|No|Sì|

### Da ricordare

- **Unspanned**: più semplice, ma può sprecare spazio.
    
- **Spanned**: più efficiente nello spazio, ma più complesso da gestire.
    

---

# Dimensionamento dei file

## 9. Numero di blocchi necessari

Se conosciamo:

- `r` = numero di record del file;
    
- `bfr` = blocking factor;
    

allora, assumendo organizzazione **unspanned**, il numero di blocchi necessari è:

$$  
nb = \left\lceil \frac{r}{bfr} \right\rceil  
$$

dove `nb` è il numero di blocchi.

### Perché si usa il soffitto?

Perché se rimane anche solo un record in più, serve comunque un altro blocco.

### Esempio

Supponiamo:

```text
r = 100 record
bfr = 8 record per blocco
```

Allora:

$$  
nb = \left\lceil \frac{100}{8} \right\rceil = \left\lceil 12.5 \right\rceil = 13  
$$

Servono quindi 13 blocchi.

---

# File header

## 10. File header

Il **file header**, o **descrittore del file**, contiene informazioni necessarie per gestire il file fisico.

In particolare, contiene informazioni per determinare gli indirizzi dei blocchi del file su disco.

Può contenere anche informazioni sul formato dei record.

### Per record di lunghezza fissa

Il file header può contenere:

- lunghezza dei campi;
    
- ordine dei campi nel record;
    
- informazioni sulla struttura dei blocchi.
    

### Per record di lunghezza variabile

Il file header può contenere:

- codici tipo dei campi;
    
- caratteri separatori;
    
- codici tipo dei record.
    

### Perché è importante?

Perché quando un blocco viene letto in memoria, il DBMS deve sapere come interpretare i byte contenuti nel blocco.

Senza il file header, il sistema non saprebbe dove iniziano e finiscono i campi o i record.

---

# Ricerca e operazioni sui file

## 11. Ricerca di record su disco

Per cercare un record su disco, il sistema deve copiare uno o più blocchi nel buffer della memoria principale.

Poi il programma di ricerca analizza i record contenuti nei buffer.

Se l’indirizzo del blocco che contiene il record non è noto, bisogna effettuare una:

## Ricerca lineare

La ricerca lineare consiste nel controllare i blocchi uno alla volta:

```text
leggi blocco 1
controlla i record
se non trovi il record, leggi blocco 2
controlla i record
...
```

La ricerca termina quando:

- il record viene trovato;
    
- oppure sono stati controllati tutti i blocchi del file.
    

### Costo

La ricerca lineare è molto costosa per file grandi, perché può richiedere la lettura di molti blocchi.

---

## 12. Operazioni sui file

Le operazioni sui file si dividono in due grandi categorie.

## Operazioni di recupero

Sono operazioni che non modificano i dati.

Esempi:

- ricerca di record;
    
- lettura di record;
    
- selezione di record che soddisfano una certa condizione.
    

## Operazioni di aggiornamento

Sono operazioni che modificano il file.

Esempi:

- inserimento di un record;
    
- cancellazione di un record;
    
- modifica del valore di uno o più campi.
    

In entrambi i casi bisogna spesso selezionare uno o più record tramite una condizione di selezione.

---

# Organizzazione dei file e metodi di accesso

## 13. Organizzazione dei file

L’**organizzazione dei file** riguarda il modo in cui i dati sono memorizzati fisicamente in:

- record;
    
- blocchi;
    
- collegamenti tra blocchi;
    
- eventuali strutture di accesso.
    

Esempi di organizzazione:

- heap file;
    
- file ordinato;
    
- file hash;
    
- file con indice.
    

## 14. Metodo di accesso

Un **metodo di accesso** è l’insieme dei programmi che permettono di effettuare operazioni sui file.

Ogni metodo di accesso funziona solo se il file è organizzato in modo adatto.

Esempio:

Un metodo di accesso basato su indice può essere applicato solo se il file possiede un indice.

---

# Heap file

## 15. File di record non ordinati

Un **heap file** è un file in cui i record sono memorizzati senza un ordine particolare.

Nel caso più semplice, i record sono inseriti nell’ordine in cui arrivano.

Ogni nuovo record viene aggiunto alla fine del file.

```text
Record 1
Record 2
Record 3
Record 4
nuovo record → aggiunto in fondo
```

---

## 16. Inserimento in un heap file

L’inserimento in un heap file è molto efficiente.

Passaggi:

1. si copia l’ultimo blocco del file in un buffer;
    
2. si aggiunge il nuovo record nel blocco;
    
3. si riscrive il blocco aggiornato su disco.
    

L’indirizzo dell’ultimo blocco viene mantenuto nel file header.

### Costo intuitivo

L’inserimento è veloce perché non bisogna mantenere nessun ordinamento.

---

## 17. Ricerca in un heap file

La ricerca in un heap file richiede una ricerca lineare blocco per blocco.

Se il file ha `nb` blocchi:

- se un solo record soddisfa la condizione di ricerca, in media si controllano:
    

$$  
\frac{nb}{2}  
$$

blocchi;

- se nessun record soddisfa la condizione, bisogna controllare:
    

$$  
nb  
$$

blocchi.

### Perché?

Perché non essendoci ordine, non abbiamo nessuna informazione per saltare direttamente al record desiderato.

---

## 18. Cancellazione in un heap file

Per cancellare un record da un heap file bisogna:

1. cercare il record;
    
2. copiare in un buffer il blocco che lo contiene;
    
3. cancellare il record dal buffer;
    
4. riscrivere il blocco su disco.
    

### Problema dello spazio inutilizzato

Ogni cancellazione può lasciare spazio vuoto nel blocco.

Con molte cancellazioni si crea molto **wasted space**, cioè spazio sprecato.

---

## 19. Deletion marker

Una tecnica alternativa è usare un **deletion marker**.

Si aggiunge a ogni record un bit o byte extra che indica se il record è valido o cancellato.

Esempio:

```text
deletion_marker = 0 → record valido
deletion_marker = 1 → record cancellato logicamente
```

In questo modo il record non viene rimosso fisicamente subito, ma solo marcato come cancellato.

### Vantaggio

La cancellazione è più semplice e veloce.

### Svantaggio

Lo spazio non viene recuperato immediatamente.

Serve una riorganizzazione periodica del file per recuperare spazio.

---

## 20. Lettura ordinata in un heap file

Se vogliamo leggere tutti i record di un heap file secondo un certo ordine, dobbiamo creare una copia ordinata del file.

Questo ordinamento può essere costoso per file grandi.

Le slide descrivono un procedimento simile al merge sort esterno:

1. i record contenuti in ciascun blocco vengono ordinati;
    
2. coppie di blocchi ordinati vengono unite per creare run ordinate di 2 blocchi;
    
3. le run di 2 blocchi vengono unite per creare run di 4 blocchi;
    
4. il processo continua fino a ottenere un unico file ordinato.
    

---

## 21. Riassunto heap file

|Operazione|Efficienza|Motivo|
|---|---|---|
|Inserimento|Alta|Si inserisce in fondo al file|
|Ricerca|Bassa|Serve ricerca lineare|
|Cancellazione|Dipende dalla ricerca|Prima bisogna trovare il record|
|Lettura ordinata|Bassa|Serve ordinare il file|

### Quando conviene?

Un heap file conviene quando:

- gli inserimenti sono molto frequenti;
    
- non è richiesto spesso l’accesso ordinato;
    
- non ci sono molte ricerche puntuali senza indice.
    

---

# File ordinati

## 22. File di record ordinati

Un **file ordinato** è un file in cui i record sono fisicamente ordinati su disco rispetto al valore di uno o più campi.

Il campo usato per ordinare viene detto:

```text
campo ordinante
```

Se il campo è anche una chiave, si parla di:

```text
chiave ordinante
```

Esempio:

```text
IMPIEGATO ordinato per NAME
```

I record vengono disposti in ordine alfabetico rispetto al nome.

---

## 23. Vantaggi dei file ordinati

I file ordinati hanno diversi vantaggi.

### 1. Lettura ordinata efficiente

Se vogliamo leggere tutti i record secondo l’ordine del campo ordinante, il file è già ordinato.

Non serve creare una copia ordinata.

### 2. Record successivo efficiente

Trovato un record, leggere il successivo è efficiente.

Spesso il record successivo si trova nello stesso blocco.

Solo se il record corrente è l’ultimo del blocco sarà necessario leggere il blocco successivo.

### 3. Ricerca efficiente sul campo ordinante

Se la ricerca è basata sul campo ordinante, si può usare la **ricerca binaria** invece della ricerca lineare.

---

## 24. Ricerca binaria nei file ordinati

La ricerca binaria viene fatta a livello di blocchi, non di singoli record.

Supponiamo:

- file con `nb` blocchi;
    
- blocchi numerati da `1` a `nb`;
    
- record ordinati in modo crescente rispetto alla chiave ordinante;
    
- si cerca un record con valore della chiave uguale a `k`.
    

La ricerca binaria accede circa a:

$$  
\log_2(nb)  
$$

blocchi.

### Confronto con ricerca lineare

|Caso|Ricerca lineare|Ricerca binaria|
|---|--:|--:|
|Record presente|`nb / 2` blocchi in media|`log₂(nb)` blocchi|
|Record assente|`nb` blocchi|`log₂(nb)` blocchi|

### Esempio

Se un file ha:

```text
nb = 1024 blocchi
```

ricerca lineare media:

$$  
\frac{1024}{2} = 512  
$$

accessi a blocco.

ricerca binaria:

$$  
\log_2(1024) = 10  
$$

accessi a blocco.

La differenza è enorme.

---

## 25. Ricerche con operatori di confronto

I file ordinati sono efficienti anche per condizioni del tipo:

```text
>
<
>=
<=
```

sul campo ordinante.

Esempio:

```sql
NAME < 'F'
```

Se il file è ordinato alfabeticamente per `NAME`, tutti i record con nome precedente a `F` si trovano contigui dall’inizio del file fino al primo nome che inizia con `F`.

Quindi le query di intervallo sono efficienti quando usano il campo ordinante.

---

## 26. Inserimento in un file ordinato

L’inserimento è costoso perché bisogna preservare l’ordinamento fisico.

Per inserire un nuovo record bisogna:

1. trovare la posizione corretta;
    
2. creare spazio per il nuovo record;
    
3. spostare altri record se necessario.
    

In media può essere necessario spostare metà dei record del file, cioè leggere e riscrivere metà dei blocchi.

---

## 27. Soluzioni al costo di inserimento

Le slide indicano due possibili soluzioni.

### 1. Spazio libero nei blocchi

Si lascia spazio libero in ogni blocco per eventuali inserimenti futuri.

Vantaggio:

- riduce la necessità di spostare molti record.
    

Svantaggio:

- spreca spazio se gli inserimenti non avvengono.
    

### 2. File di overflow

Si crea un file temporaneo non ordinato, detto:

```text
file di overflow
```

o:

```text
transaction file
```

I nuovi record vengono inseriti alla fine del file di overflow.

Periodicamente, il file di overflow viene unito al file principale tramite una riorganizzazione.

---

## 28. Modifica in un file ordinato

La modifica dipende da due fattori:

1. la condizione usata per trovare il record;
    
2. il campo che viene modificato.
    

### Caso 1: ricerca sul campo ordinante

Se la condizione di ricerca usa il campo ordinante, il record può essere localizzato con ricerca binaria.

### Caso 2: ricerca su campo non ordinante

Se la condizione usa un campo diverso dal campo ordinante, serve una ricerca lineare, a meno che non esista un indice.

### Caso 3: modifica del campo ordinante

Se si modifica proprio il campo ordinante, il record potrebbe non trovarsi più nella posizione corretta.

Quindi può essere necessario riposizionarlo.

---

## 29. Limite pratico dei file ordinati

Le slide concludono che i file ordinati sono raramente usati da soli nelle basi di dati reali.

Sono più utili quando esiste una struttura di indicizzazione, come un **indice primario**, che permette un accesso efficiente ai dati.

---

## 30. Riassunto file ordinati

|Operazione|Efficienza|Motivo|
|---|---|---|
|Lettura ordinata|Alta|Il file è già ordinato|
|Ricerca su campo ordinante|Alta|Si usa ricerca binaria|
|Query di intervallo sul campo ordinante|Alta|I record sono contigui|
|Inserimento|Bassa|Bisogna mantenere l’ordine|
|Modifica campo ordinante|Bassa|Può richiedere riposizionamento|
|Ricerca su campo non ordinante|Bassa|Serve ricerca lineare senza indice|

---

# Hashing

## 31. Tecniche di hashing

L’hashing è un’altra tecnica di organizzazione primaria dei file.

Un file organizzato tramite hashing è detto anche:

```text
hash file
```

o:

```text
direct file
```

L’obiettivo è permettere un accesso molto veloce ai record rispetto a certe condizioni di ricerca.

La condizione tipica è una condizione di uguaglianza su un singolo campo.

Esempio:

```sql
WHERE matricola = '12345'
```

Il campo usato per calcolare la funzione hash è detto:

```text
hash field
```

Se questo campo è una chiave, viene detto:

```text
hash key
```

---

## 32. Funzionamento generale dell’hashing

Si usa una funzione hash:

$$  
h(k)  
$$

dove `k` è il valore del campo hash.

La funzione restituisce l’indirizzo della posizione in cui il record deve essere memorizzato.

Nel caso di hashing esterno, restituisce l’indirizzo del blocco o della cella su disco.

Idea:

```text
valore chiave → funzione hash → indirizzo fisico
```

Esempio:

```text
matricola 12345 → h(12345) → blocco 7
```

---

# Hashing interno

## 33. Hashing interno

L’**hashing interno** viene usato per file temporanei o strutture in memoria principale.

È implementato tramite array di record.

Supponiamo che l’array abbia `m` posizioni:

```text
0, 1, 2, ..., m-1
```

La funzione hash trasforma il valore del campo hash in un numero intero compreso tra `0` e `m - 1`.

---

## 34. Funzione MOD

Se il campo hash è intero, una funzione hash semplice è:

$$  
h(k) = k \ MOD \ m  
$$

dove:

- `k` è il valore del campo hash;
    
- `m` è il numero di slot;
    
- il risultato è il resto della divisione di `k` per `m`.
    

### Esempio

Se:

```text
m = 10
k = 27
```

allora:

$$  
h(27) = 27 \ MOD \ 10 = 7  
$$

Il record viene posizionato nello slot 7.

---

## 35. Hashing su valori non interi

Se il campo hash non è intero, può essere trasformato in un numero intero.

Per esempio, una stringa può essere trasformata usando i codici numerici dei caratteri.

Esempio intuitivo:

```text
"ABC" → codice numerico → funzione hash
```

Attenzione: alcune trasformazioni possono produrre lo stesso valore per stringhe diverse o permutazioni degli stessi caratteri, aumentando il rischio di collisioni.

---

# Collisioni

## 36. Problema delle collisioni

La maggior parte delle funzioni hash non garantisce che valori diversi producano indirizzi diversi.

Questo perché lo spazio dei possibili valori del campo hash è solitamente molto più grande dello spazio degli indirizzi disponibili.

Quando due valori diversi producono lo stesso indirizzo, si ha una:

```text
collisione
```

Esempio:

```text
h(27) = 7
h(37) = 7
```

I due record vorrebbero occupare la stessa posizione.

Serve quindi una tecnica di:

```text
risoluzione delle collisioni
```

---

## 37. Tecniche di risoluzione delle collisioni

Le slide presentano tre tecniche principali:

1. open addressing;
    
2. multiple hashing;
    
3. chaining.
    

---

## 38. Open addressing

Nell’**open addressing**, se la posizione calcolata dalla funzione hash è occupata, si cercano posizioni successive finché se ne trova una libera.

Schema:

```text
i := hash_address

se la posizione i è occupata:
    i := (i + 1) MOD m
    continua finché:
        - trovi una posizione libera
        - oppure torni alla posizione iniziale
```

Se si torna alla posizione iniziale, significa che tutte le posizioni sono occupate.

### Esempio

Supponiamo:

```text
m = 10
h(k) = 4
```

ma lo slot 4 è occupato.

Si prova:

```text
5, 6, 7, ...
```

fino a trovare uno slot libero.

---

## 39. Multiple hashing

Nel **multiple hashing**, se la prima funzione hash produce una collisione, si usa una seconda funzione hash.

Se anche la seconda produce una collisione, si può:

- usare una terza funzione;
    
- oppure passare a open addressing.
    

Idea:

```text
h1(k) → collisione
h2(k) → nuova posizione
h3(k) → eventualmente altra posizione
```

---

## 40. Chaining

Nel **chaining**, si usano posizioni di overflow e puntatori.

Ogni posizione dell’array contiene:

- i dati;
    
- un puntatore alla prossima posizione della catena.
    

Quando c’è una collisione:

1. il nuovo record viene inserito in una locazione di overflow;
    
2. il puntatore dell’ultimo record nella catena viene aggiornato;
    
3. i record con lo stesso indirizzo hash formano una lista collegata.
    

Esempio:

```text
slot 4 → record A → record B → record C
```

dove `A`, `B` e `C` hanno prodotto lo stesso indirizzo hash.

---

## 41. Soluzione ottimale per una hash table

L’obiettivo di una buona funzione hash è distribuire i record in modo uniforme.

Questo permette di:

- minimizzare le collisioni;
    
- evitare troppe locazioni inutilizzate.
    

Le slide indicano che una buona situazione si ha quando la tabella hash è piena circa tra il:

```text
70% e 90%
```

Se dobbiamo memorizzare `r` record in una tabella con `m` locazioni, il rapporto:

$$  
\frac{r}{m}  
$$

dovrebbe stare tra:

$$  
0.7 \leq \frac{r}{m} \leq 0.9  
$$

Questo rapporto misura il grado di riempimento della tabella.

### Interpretazione

- Se `r/m` è troppo basso, si spreca spazio.
    
- Se `r/m` è troppo alto, aumentano le collisioni.
    

---

# Hashing esterno

## 42. External hashing

L’**external hashing** è l’hashing usato per file che risiedono su disco.

Rispetto all’hashing interno, cambia l’unità di indirizzamento.

Non si parla più di singoli slot in memoria, ma di:

```text
bucket
```

o celle.

Una cella può essere:

- un singolo blocco;
    
- un insieme di blocchi contigui.
    

Ogni bucket può contenere più record.

---

## 43. Bucket

Nel contesto dell’external hashing, un **bucket** è una cella dello spazio degli indirizzi.

La funzione hash restituisce il numero del bucket.

Poi una tabella nel file header converte il numero del bucket nell’indirizzo fisico del blocco su disco.

Schema:

```text
valore chiave
    ↓
funzione hash
    ↓
numero bucket
    ↓
tabella nel file header
    ↓
indirizzo blocco su disco
```

---

## 44. Collisioni nell’external hashing

Il problema delle collisioni è meno grave rispetto all’hashing interno, perché un bucket può contenere molti record.

Una collisione diventa problematica solo quando il bucket è pieno e bisogna inserire un nuovo record nello stesso bucket.

In quel caso si usa una variante del chaining.

Ogni bucket mantiene un puntatore a una lista di overflow.

---

## 45. Overflow bucket

Quando un bucket principale è pieno, i nuovi record vengono inseriti in bucket di overflow.

Esempio:

```text
bucket principale 1:
    record 321
    record 761
    record 91
    puntatore → overflow bucket

overflow bucket:
    record 981
    record 182
```

---

## 46. Record pointer

Le slide specificano che un **record pointer** include due informazioni:

1. l’indirizzo del blocco;
    
2. la posizione relativa del record all’interno del blocco.
    

Quindi un puntatore a record non indica solo il blocco, ma anche dove si trova il record dentro quel blocco.

---

# Limiti dell’hashing

## 47. Limite dello spazio fisso

Un limite importante delle tecniche di hashing è che lo spazio allocato per il file è spesso fisso.

Supponiamo:

- `M` = numero di celle/bucket;
    
- `m` = numero massimo di record per cella.
    

Il numero massimo di record memorizzabili è:

$$  
m \cdot M  
$$

### Problema 1: pochi record

Se il numero di record è molto minore di:

$$  
m \cdot M  
$$

allora si spreca molto spazio.

### Problema 2: troppi record

Se il numero di record è molto maggiore di:

$$  
m \cdot M  
$$

allora ci saranno molte collisioni e molte aree di overflow.

Di conseguenza, le operazioni di ricerca rallenteranno.

---

## 48. Soluzione: espansione dinamica

Per risolvere il problema dello spazio fisso, bisogna poter cambiare dinamicamente il numero di bucket.

Questo implica:

1. modificare il numero di blocchi allocati;
    
2. usare una diversa funzione hash;
    
3. ridistribuire i record nelle nuove celle.
    

Le slide citano tre tecniche di hashing con espansione dinamica:

- **dynamic hashing**
    
- **extendible hashing**
    
- **linear hashing**
    

---

# Confronto finale tra le organizzazioni

## 49. Heap file vs file ordinato vs file hash

|Caratteristica|Heap file|File ordinato|File hash|
|---|---|---|---|
|Ordine fisico|Nessuno|Sì, su campo ordinante|Dipende dalla funzione hash|
|Inserimento|Molto efficiente|Costoso|Efficiente se poche collisioni|
|Ricerca per uguaglianza|Costosa senza indice|Efficiente solo su campo ordinante|Molto efficiente su hash field|
|Ricerca per intervallo|Costosa|Molto efficiente su campo ordinante|Poco adatta|
|Lettura ordinata|Richiede ordinamento|Efficiente|Non efficiente|
|Cancellazione|Può creare wasted space|Costosa|Dipende dalla gestione overflow|
|Problema principale|Ricerca lenta|Aggiornamenti costosi|Collisioni e dimensione fissa|

---

# 50. Quando usare quale organizzazione?

## Heap file

Conviene quando:

- servono inserimenti veloci;
    
- l’ordine non è importante;
    
- le ricerche sono supportate da indici oppure non sono frequenti.
    

## File ordinato

Conviene quando:

- si leggono spesso i dati in ordine;
    
- si fanno molte query su intervalli;
    
- la chiave di ricerca coincide spesso con il campo ordinante.
    

Svantaggio principale:

- inserimenti e modifiche possono essere costosi.
    

## File hash

Conviene quando:

- si fanno molte ricerche per uguaglianza;
    
- la ricerca avviene spesso su un campo specifico;
    
- non interessano query ordinate o per intervallo.
    

Svantaggio principale:

- non è adatto per range query;
    
- bisogna gestire collisioni e overflow.
    

---

# Formule da ricordare

## Blocking factor

$$  
bfr = \left\lfloor \frac{B}{R} \right\rfloor  
$$

dove:

- `B` = dimensione del blocco;
    
- `R` = dimensione del record.
    

---

## Numero di blocchi

$$  
nb = \left\lceil \frac{r}{bfr} \right\rceil  
$$

dove:

- `r` = numero di record;
    
- `bfr` = blocking factor.
    

---

## Ricerca lineare in heap file

Caso medio, se il record esiste:

$$  
\frac{nb}{2}  
$$

Caso peggiore o record assente:

$$  
nb  
$$

---

## Ricerca binaria in file ordinato

$$  
\log_2(nb)  
$$

accessi a blocco.

---

## Funzione hash MOD

$$  
h(k) = k \ MOD \ m  
$$

dove:

- `k` = valore del campo hash;
    
- `m` = numero di posizioni o bucket.
    

---

## Grado di riempimento hash table

$$  
0.7 \leq \frac{r}{m} \leq 0.9  
$$

dove:

- `r` = numero di record;
    
- `m` = numero di locazioni.
    

---

# Domande tipiche d’esame

## 1. Che cos’è il blocking factor?

Il blocking factor è il numero massimo di record che possono essere inseriti in un blocco.

Si calcola con:

$$  
bfr = \left\lfloor \frac{B}{R} \right\rfloor  
$$

---

## 2. Differenza tra record spanned e unspanned

Nei record **unspanned**, un record deve stare interamente in un solo blocco.

Nei record **spanned**, un record può essere diviso tra più blocchi.

---

## 3. Perché la ricerca in un heap file è costosa?

Perché i record non sono ordinati e non esiste una posizione prevedibile.

Quindi, se non esistono indici, bisogna fare una ricerca lineare sui blocchi.

---

## 4. Qual è il vantaggio principale di un file ordinato?

Permette ricerche efficienti sul campo ordinante tramite ricerca binaria e rende efficienti le query di intervallo.

---

## 5. Perché l’inserimento in un file ordinato è costoso?

Perché bisogna mantenere l’ordine fisico dei record.

Il nuovo record deve essere inserito nella posizione corretta e può essere necessario spostare molti record.

---

## 6. Qual è il vantaggio principale dell’hashing?

Permette accessi molto veloci per condizioni di uguaglianza sul campo hash.

Esempio:

```sql
WHERE matricola = 12345
```

---

## 7. Che cos’è una collisione?

Una collisione si verifica quando due valori diversi del campo hash producono lo stesso indirizzo.

---

## 8. Tecniche di risoluzione delle collisioni

Le tecniche principali sono:

- open addressing;
    
- multiple hashing;
    
- chaining.
    

---

## 9. Perché l’hashing non è adatto alle query di intervallo?

Perché la funzione hash distribuisce i record in modo apparentemente casuale.

Quindi record con valori vicini non sono necessariamente memorizzati vicini.

Esempio:

```sql
WHERE matricola BETWEEN 1000 AND 2000
```

non è efficiente con hashing.

---

## 10. Qual è il limite dello spazio fisso nell’hashing?

Se si allocano troppi bucket si spreca spazio.

Se se ne allocano troppo pochi si generano molte collisioni e overflow.

Per questo servono tecniche di espansione dinamica.

---

# Mini-schema mentale

```text
Organizzazione fisica dei dati
│
├── Record
│   ├── lunghezza fissa
│   └── lunghezza variabile
│
├── Blocchi
│   ├── blocking factor
│   ├── spanned
│   └── unspanned
│
├── File
│   ├── heap file
│   │   ├── inserimento veloce
│   │   └── ricerca lenta
│   │
│   ├── file ordinato
│   │   ├── ricerca efficiente sul campo ordinante
│   │   ├── range query efficienti
│   │   └── inserimento costoso
│   │
│   └── file hash
│       ├── uguaglianza efficiente
│       ├── collisioni
│       ├── overflow
│       └── espansione dinamica
```

---

# Cose da non confondere

## Organizzazione dei file vs metodo di accesso

- **Organizzazione del file**: come i dati sono fisicamente disposti.
    
- **Metodo di accesso**: programma/strategia usata per leggere o modificare i dati.
    

## Heap file vs file ordinato

- Heap file: inserimento veloce, ricerca lenta.
    
- File ordinato: ricerca ordinata veloce, inserimento costoso.
    

## Hashing interno vs external hashing

- Hashing interno: usato in memoria principale, con array.
    
- External hashing: usato su disco, con bucket e blocchi.
    

## Collisione vs overflow

- Collisione: due record producono lo stesso indirizzo hash.
    
- Overflow: spazio aggiuntivo usato quando la posizione/bucket principale è pieno.
    

---

# Sintesi finale

L’organizzazione fisica dei dati studia il modo in cui i record sono collocati nei blocchi e nei file su disco.

Le tre organizzazioni principali viste sono:

1. **Heap file**
    
    - semplice;
        
    - inserimenti veloci;
        
    - ricerche lente.
        
2. **File ordinato**
    
    - efficiente per letture ordinate e ricerche sul campo ordinante;
        
    - costoso per inserimenti e modifiche.
        
3. **File hash**
    
    - molto efficiente per ricerche di uguaglianza sul campo hash;
        
    - richiede gestione delle collisioni;
        
    - poco adatto a query di intervallo o lettura ordinata.
        

Il punto centrale è che ogni organizzazione ottimizza alcune operazioni ma ne penalizza altre. Per questo, nei DBMS reali, la scelta dell’organizzazione fisica dipende dal tipo di operazioni più frequenti.