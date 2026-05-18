---
title: "16 2 Indici"
aliases: ["16 2 Indici"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "16-2-indici"]
created: 2026-05-18
---
Appunti basati sulle slide **16_2_Indici.pdf** su indici, indici multilivello, alberi di ricerca, B-alberi e B+-alberi.

# Indici nei DBMS

## 1. Perché servono gli indici

Gli **indici** sono strutture di accesso ai dati usate per rendere più veloce il recupero dei record quando si cercano dati tramite una certa condizione.

Esempio:

```sql
SELECT *
FROM Studenti
WHERE matricola = 12345;
```

Senza indice, il DBMS potrebbe dover fare una **scansione lineare** del file, cioè controllare molti record uno per uno.

Con un indice, invece, può seguire un percorso di ricerca più breve per arrivare rapidamente al blocco che contiene il record cercato.

Gli indici sono quindi dei **cammini di accesso alternativi** ai dati.

---

## 2. Campo indice

Un indice viene costruito su uno o più campi del file.

Il campo su cui è costruito l’indice si chiama:

> **indexing field**

Ad esempio, in una tabella:

```text
Studente(matricola, nome, cognome, corso)
```

possiamo creare un indice su:

```text
matricola
```

oppure su:

```text
cognome
```

L’indice contiene valori del campo indice e puntatori ai blocchi del file dati.

---

# Indici ordinati di singolo livello

## 3. Idea generale

Un indice ordinato di singolo livello funziona in modo simile all’indice analitico di un libro.

Nel libro troviamo:

```text
parola → pagine in cui compare
```

Nel database troviamo:

```text
valore del campo indice → blocco del file dati
```

L’indice è ordinato, quindi può essere interrogato tramite **ricerca binaria**.

Dato che il file indice è molto più piccolo del file dati, cercare nell’indice è molto più efficiente che cercare direttamente nel file dati.

---

## 4. Tipi principali di indici di singolo livello

Gli indici di singolo livello si distinguono in:

1. **indice primario**
    
2. **indice di clustering**
    
3. **indice secondario**
    

La differenza dipende soprattutto da due aspetti:

|Tipo di indice|Il file dati è ordinato rispetto al campo?|Il campo è chiave?|
|---|--:|--:|
|Indice primario|Sì|Sì|
|Indice di clustering|Sì|No|
|Indice secondario|No|Può esserlo o no|

---

# Indice primario

## 5. Definizione

Un **indice primario** è un indice costruito sul campo chiave rispetto al quale il file dati è fisicamente ordinato.

Quindi il campo è contemporaneamente:

- **ordering field**, perché ordina fisicamente i record sul disco;
    
- **key field**, perché identifica univocamente ogni record.
    

Esempio:

```text
Studenti(matricola, nome, cognome)
```

Se il file è ordinato fisicamente per `matricola` e `matricola` è chiave primaria, posso costruire un indice primario su `matricola`.

---

## 6. Struttura dell’indice primario

Un indice primario è un file ordinato composto da record di lunghezza fissa.

Ogni entry dell’indice ha la forma:

```text
<chiave primaria, indirizzo blocco>
```

Più precisamente:

```text
<k(i), p(i)>
```

dove:

- `k(i)` è il valore della chiave del primo record significativo del blocco;
    
- `p(i)` è il puntatore al blocco del file dati.
    

Il primo record di ogni blocco del file dati è detto:

> **anchor record** o **block anchor**

---

## 7. Indice primario come indice non denso

Un indice primario è un **indice non denso**.

Un indice è detto:

- **denso**, se contiene una entry per ogni record del file dati;
    
- **non denso**, se contiene una entry solo per alcuni record, ad esempio uno per ogni blocco.
    

Nel caso dell’indice primario:

```text
una entry dell’indice → un blocco del file dati
```

e non:

```text
una entry dell’indice → un record del file dati
```

Questo è possibile perché il file dati è ordinato fisicamente rispetto alla chiave.

---

## 8. Ricerca con indice primario

Supponiamo di cercare un record con chiave `k`.

Il record si trova nel blocco puntato da `p(i)` tale che:

```text
k(i) ≤ k < k(i+1)
```

Procedura:

1. si esegue una ricerca binaria sull’indice;
    
2. si trova la entry corretta;
    
3. si legge il blocco puntato da `p(i)`;
    
4. dentro il blocco si cerca il record desiderato.
    

---

## 9. Vantaggi dell’indice primario

L’indice primario è efficiente perché:

- è ordinato;
    
- è piccolo rispetto al file dati;
    
- è non denso;
    
- permette di evitare la scansione lineare del file dati.
    

---

# Indice di clustering

## 10. Definizione

Un **indice di clustering** si usa quando il file dati è ordinato fisicamente rispetto a un campo che però **non è chiave**.

Questo campo prende il nome di:

> **clustering field**

Significa che più record possono avere lo stesso valore su quel campo.

Esempio:

```text
Impiegati(codice, nome, dipartimento)
```

Se il file è ordinato per `dipartimento`, più impiegati possono appartenere allo stesso dipartimento.

Quindi `dipartimento` non è una chiave, ma può essere un clustering field.

---

## 11. Struttura dell’indice di clustering

Un indice di clustering è un file ordinato con entry del tipo:

```text
<clustering field, indirizzo blocco>
```

Esiste una entry per ogni **valore distinto** del clustering field.

La entry punta al **primo blocco** del file dati che contiene record con quel valore.

Esempio:

```text
<"Informatica", puntatore al primo blocco degli impiegati di Informatica>
```

---

## 12. Proprietà importante

Un file può essere ordinato fisicamente rispetto a un solo campo.

Quindi un file può avere:

```text
o un indice primario
o un indice di clustering
```

ma non entrambi sullo stesso file fisicamente ordinato.

Il motivo è che il file non può essere ordinato fisicamente contemporaneamente rispetto a due campi diversi.

---

# Indice secondario

## 13. Definizione

Un **indice secondario** è un indice costruito su un campo che **non determina l’ordinamento fisico del file dati**.

Un file può avere più indici secondari.

Esempio:

```text
Studenti(matricola, nome, cognome, corso)
```

Il file può essere ordinato per `matricola`, ma avere indici secondari su:

```text
cognome
corso
nome
```

---

## 14. Indice secondario su campo chiave

Se l’indice secondario è costruito su un campo chiave, cioè un campo con valori tutti distinti, allora contiene una entry per ogni record del file dati.

La struttura è:

```text
<secondary key, indirizzo blocco>
```

Esempio:

```text
<codice_fiscale, indirizzo blocco>
```

Anche se il campo è chiave, il file dati non è fisicamente ordinato rispetto a quel campo.

Per questo motivo non posso usare i block anchor.

---

## 15. Indice secondario come indice denso

Un indice secondario su campo chiave è un **indice denso**.

Contiene:

```text
una entry per ogni record del file dati
```

Questo lo rende più grande di un indice primario.

Conseguenze:

- occupa più spazio;
    
- richiede più tempo per la ricerca nell’indice;
    
- però evita la scansione lineare del file dati.
    

---

## 16. Puntatori a blocco, non a record

Nelle slide viene sottolineato che gli indici secondari usano puntatori a blocco, non direttamente a record.

Quindi:

```text
valore indice → blocco che contiene il record
```

e non necessariamente:

```text
valore indice → record esatto
```

Dopo aver caricato il blocco in memoria, bisogna cercare il record al suo interno.

Questo è conveniente perché l’unità di trasferimento tra disco e memoria è il blocco.

---

# Indice secondario su campo non chiave

## 17. Problema

Un indice secondario può anche essere costruito su un campo non chiave.

Esempio:

```text
Studenti(matricola, nome, corso)
```

Indice secondario su:

```text
corso
```

Più studenti possono appartenere allo stesso corso.

Quindi molti record possono condividere lo stesso valore dell’indexing field.

---

## 18. Possibili implementazioni

### Soluzione 1: più entry con lo stesso valore

Si crea una entry per ogni record.

Esempio:

```text
<Informatica, blocco1>
<Informatica, blocco2>
<Informatica, blocco5>
<Economia, blocco3>
```

È una soluzione semplice, ma può produrre molte entry duplicate.

---

### Soluzione 2: entry con lista di puntatori

Per ogni valore distinto del campo indice, si mantiene una lista di puntatori.

```text
<Informatica, [p1, p2, p5]>
<Economia, [p3, p7]>
```

Questa soluzione evita di ripetere lo stesso valore molte volte, ma le entry possono diventare di lunghezza variabile.

---

### Soluzione 3: blocco intermedio di puntatori

L’indice contiene una entry:

```text
<valore, puntatore a blocco di puntatori>
```

Il blocco di puntatori contiene i riferimenti ai blocchi del file dati.

Schema:

```text
indice → blocco di puntatori → blocchi dati
```

Se i puntatori sono troppi per un solo blocco, si usa una lista di blocchi di puntatori.

Questa soluzione è particolarmente utile quando molti record condividono lo stesso valore.

---

# Confronto tra indici primari, clustering e secondari

|Tipo|Campo usato|File dati ordinato fisicamente?|Campo chiave?|Denso?|Numero massimo per file|
|---|---|--:|--:|--:|--:|
|Primario|Ordering key field|Sì|Sì|No|1|
|Clustering|Ordering field non chiave|Sì|No|In genere no, una entry per valore distinto|1|
|Secondario su chiave|Campo non ordinante|No|Sì|Sì|Molti|
|Secondario su non chiave|Campo non ordinante|No|No|Dipende dall’implementazione|Molti|

---

# Indici multilivello

## 19. Limite degli indici di singolo livello

Un indice di singolo livello può comunque occupare molti blocchi.

Se l’indice occupa `bi` blocchi, una ricerca binaria richiede circa:

```text
log2(bi)
```

accessi a blocco.

L’idea degli indici multilivello è ridurre più velocemente lo spazio di ricerca.

---

## 20. Fan-out

Il **fan-out** di un indice multilivello è indicato con:

```text
fo
```

Rappresenta il numero di puntatori che possono stare in un blocco indice.

Invece di ridurre lo spazio di ricerca di un fattore 2, come nella ricerca binaria, un indice multilivello lo riduce di un fattore `fo`.

La ricerca richiede circa:

```text
log_fo(bi)
```

accessi a blocco.

Dato che `fo` è di solito molto maggiore di 2, la ricerca è molto più efficiente.

---

## 21. Costruzione di un indice multilivello

Il primo livello è un indice ordinato.

Su questo primo livello si costruisce un altro indice, cioè un indice primario del primo livello.

Quindi:

```text
livello 1 → indice sui dati
livello 2 → indice sul livello 1
livello 3 → indice sul livello 2
...
```

Si continua finché il livello superiore entra in un solo blocco.

Questo livello più alto si chiama:

> **top index level**

---

## 22. Numero di livelli

Se il primo livello ha `r1` entry e il fan-out è `fo`, il numero approssimativo di livelli è:

```text
t = log_fo(r1)
```

Più precisamente, si continua a creare livelli finché:

```text
r1 / fo^t ≤ 1
```

Quindi il livello più alto contiene una sola pagina/blocco.

---

## 23. Ricerca in un indice multilivello

La ricerca procede dall’alto verso il basso:

1. si parte dal top index level;
    
2. si sceglie il puntatore corretto;
    
3. si scende al livello successivo;
    
4. si ripete fino al primo livello;
    
5. dal primo livello si arriva al blocco del file dati.
    

Schema:

```text
top level
   ↓
livello intermedio
   ↓
primo livello indice
   ↓
file dati
```

---

# Alberi di ricerca

## 24. Collegamento con gli indici multilivello

Un indice multilivello può essere visto come una variante degli **alberi di ricerca**.

Ogni nodo contiene chiavi e puntatori.

A ogni livello si restringe la ricerca a un sottoalbero.

---

## 25. Albero di ricerca di ordine p

Un albero di ricerca di ordine `p` è un albero in cui ogni nodo contiene al massimo:

```text
p - 1 valori di ricerca
p puntatori
```

La struttura generale di un nodo è:

```text
<P1, K1, P2, K2, ..., Pq-1, Kq-1, Pq>
```

con:

```text
q ≤ p
```

dove:

- `Ki` sono valori di ricerca;
    
- `Pi` sono puntatori a sottoalberi;
    
- i valori `Ki` sono ordinati.
    

---

## 26. Vincoli di ordinamento

In ogni nodo vale:

```text
K1 < K2 < ... < Kq-1
```

Inoltre, per i valori `X` contenuti nei sottoalberi:

```text
P1 contiene valori X < K1
Pi contiene valori Ki-1 < X < Ki
Pq contiene valori Kq-1 < X
```

Questi vincoli permettono di decidere quale puntatore seguire durante la ricerca.

---

## 27. Alberi di ricerca su disco

Un albero di ricerca può essere usato per cercare record memorizzati su disco.

Ogni nodo dell’albero può essere memorizzato in un blocco.

Le chiavi contenute nei nodi sono valori del campo di ricerca.

A ogni valore di ricerca può essere associato un puntatore:

```text
chiave → record
```

oppure:

```text
chiave → blocco contenente il record
```

---

## 28. Problema degli alberi non bilanciati

Gli algoritmi generici di inserimento e cancellazione non garantiscono che l’albero resti bilanciato.

Un albero non bilanciato è problematico perché alcuni record potrebbero richiedere molti più accessi a blocco rispetto ad altri.

Inoltre, le cancellazioni possono creare nodi poco pieni, aumentando:

- spazio inutilizzato;
    
- numero di livelli;
    
- costo di ricerca.
    

Soluzione:

```text
B-alberi
B+-alberi
```

---

# B-alberi

## 29. Definizione

Un **B-albero** è un albero di ricerca bilanciato con vincoli aggiuntivi.

Questi vincoli servono a garantire che:

- tutte le foglie siano allo stesso livello;
    
- i nodi non siano troppo vuoti;
    
- l’altezza dell’albero rimanga bassa;
    
- gli accessi a blocco siano limitati.
    

---

## 30. Struttura di un nodo interno

Un B-albero di ordine `p` ha nodi della forma:

```text
<P1, <K1, Pr1>, P2, <K2, Pr2>, ..., <Kq-1, Prq-1>, Pq>
```

dove:

- `Pi` sono **tree pointer**, cioè puntatori ad altri nodi del B-albero;
    
- `Ki` sono valori della chiave di ricerca;
    
- `Pri` sono **data pointer**, cioè puntatori ai record o ai blocchi dati;
    
- `q ≤ p`.
    

---

## 31. Condizioni dei B-alberi

Un B-albero di ordine `p` deve soddisfare queste condizioni:

1. ogni nodo ha al massimo `p` tree pointer;
    
2. un nodo con `q` tree pointer contiene `q - 1` chiavi;
    
3. le chiavi in ogni nodo sono ordinate:
    

```text
K1 < K2 < ... < Kq-1
```

4. per i sottoalberi valgono i vincoli di ricerca:
    

```text
P1 contiene X < K1
Pi contiene Ki-1 < X < Ki
Pq contiene Kq-1 < X
```

5. ogni nodo, tranne la radice, ha almeno:
    

```text
ceil(p / 2)
```

tree pointer;

6. la radice ha almeno due tree pointer, a meno che non sia l’unico nodo dell’albero;
    
7. tutte le foglie sono allo stesso livello.
    

---

## 32. Data pointer nei B-alberi

Nel B-albero, i data pointer possono trovarsi anche nei nodi interni.

Quindi una chiave presente in un nodo interno può puntare direttamente al record o al blocco dati corrispondente.

Questo distingue il B-albero dal B+-albero.

---

## 33. Inserimento nei B-alberi

Quando si inserisce una nuova chiave:

1. si cerca la posizione corretta;
    
2. si inserisce la chiave nel nodo appropriato;
    
3. se il nodo ha spazio, l’inserimento termina;
    
4. se il nodo è pieno, bisogna dividerlo.
    

La divisione del nodo pieno si chiama:

> **split**

Durante lo split:

- una chiave mediana sale al nodo padre;
    
- il nodo viene diviso in due nodi;
    
- se anche il padre è pieno, lo split può propagarsi verso l’alto.
    

Se lo split arriva alla radice, viene creata una nuova radice e l’altezza dell’albero aumenta.

---

## 34. Cancellazione nei B-alberi

La cancellazione è più complessa dell’inserimento.

Dopo aver rimosso una chiave, un nodo potrebbe diventare troppo vuoto, cioè avere meno del numero minimo di puntatori/chiavi.

In questo caso si può procedere con:

1. **redistribuzione** con un nodo fratello;
    
2. **fusione** con un nodo fratello;
    
3. eventuale propagazione della modifica verso l’alto.
    

L’obiettivo è mantenere validi i vincoli del B-albero.

---

# B+-alberi

## 35. Dal B-albero al B+-albero

Un **B+-albero** è una variante del B-albero in cui i data pointer sono memorizzati solo nei nodi foglia.

Quindi:

```text
nodi interni → servono solo per guidare la ricerca
nodi foglia → contengono le entry che puntano ai dati
```

Questa è una differenza fondamentale rispetto ai B-alberi.

---

## 36. Struttura dei nodi interni

Un nodo interno di un B+-albero di ordine `p` ha forma:

```text
<P1, K1, P2, K2, ..., Pq-1, Kq-1, Pq>
```

dove:

- `Pi` sono tree pointer;
    
- `Ki` sono valori della search key;
    
- `q ≤ p`.
    

Nei nodi interni non ci sono data pointer.

---

## 37. Vincoli sui nodi interni

Per ogni nodo interno:

```text
K1 < K2 < ... < Kq-1
```

Ogni nodo interno ha al massimo `p` tree pointer.

Ogni nodo interno, esclusa la radice, ha almeno:

```text
ceil(p / 2)
```

tree pointer.

La radice, se è un nodo interno, ha almeno due tree pointer.

---

## 38. Struttura dei nodi foglia

I nodi foglia hanno forma:

```text
<<K1, Pr1>, <K2, Pr2>, ..., <Kq, Prq>, Pnext>
```

dove:

- `Ki` sono valori della search key;
    
- `Pri` sono data pointer;
    
- `Pnext` è un puntatore al nodo foglia successivo.
    

Quindi le foglie sono collegate tra loro in una lista ordinata.

---

## 39. Funzione di Pnext

Il puntatore `Pnext` collega ogni foglia alla foglia successiva.

Questo è molto utile per le **range query**.

Esempio:

```sql
SELECT *
FROM Studenti
WHERE matricola BETWEEN 1000 AND 2000;
```

Una volta trovata la prima foglia contenente `1000`, il DBMS può scorrere le foglie successive usando `Pnext`, senza dover ripartire ogni volta dalla radice.

---

## 40. B+-albero su campo chiave

Se il B+-albero è costruito su un campo chiave:

- ogni valore della chiave compare in una foglia;
    
- ogni entry della foglia punta al record o al blocco che contiene il record;
    
- alcuni valori possono essere ripetuti nei nodi interni per guidare la ricerca.
    

Quindi i valori nei nodi interni sono copie usate solo per orientare il percorso.

---

## 41. B+-albero su campo non chiave

Se il campo di ricerca non è una chiave, più record possono avere lo stesso valore.

In questo caso, il data pointer della foglia può puntare a:

```text
un blocco contenente puntatori ai record
```

Quindi serve un passaggio aggiuntivo:

```text
foglia → blocco di puntatori → record dati
```

---

# Differenza tra B-albero e B+-albero

|Aspetto|B-albero|B+-albero|
|---|---|---|
|Dove stanno i data pointer?|Nei nodi interni e nelle foglie|Solo nelle foglie|
|I nodi interni puntano ai dati?|Sì, possono|No|
|Le foglie sono collegate?|Non necessariamente|Sì, tramite `Pnext`|
|Range query|Meno efficienti|Molto efficienti|
|Valori duplicati nei nodi interni|Non necessariamente|Sì, alcuni valori delle foglie sono copiati nei nodi interni|
|Uso nei DBMS|Importante teoricamente|Molto usato per gli indici|

---

# Ricerca in un B+-albero

## 42. Procedura

Per cercare una chiave `K`:

1. si parte dalla radice;
    
2. si confronta `K` con le chiavi del nodo;
    
3. si sceglie il puntatore corretto;
    
4. si scende al nodo figlio;
    
5. si continua fino a una foglia;
    
6. nella foglia si cerca la entry con chiave `K`;
    
7. si segue il data pointer verso il record o il blocco dati.
    

Schema:

```text
radice
  ↓
nodi interni
  ↓
foglia
  ↓
record/blocco dati
```

---

# Inserimento in un B+-albero

## 43. Idea generale

Per inserire una nuova chiave:

1. si cerca la foglia in cui la chiave dovrebbe essere inserita;
    
2. se la foglia ha spazio, si inserisce la nuova entry;
    
3. se la foglia è piena, si divide la foglia;
    
4. si copia/promuove una chiave nel nodo padre;
    
5. se anche il padre è pieno, lo split si propaga verso l’alto.
    

Nel B+-albero, a differenza del B-albero, le entry dati restano sempre nelle foglie.

---

# Cancellazione in un B+-albero

## 44. Idea generale

Per cancellare una chiave:

1. si trova la foglia contenente la chiave;
    
2. si elimina la entry;
    
3. se la foglia rimane sufficientemente piena, l’operazione termina;
    
4. se la foglia va in underflow, si prova a redistribuire con un fratello;
    
5. se non è possibile redistribuire, si fondono due foglie;
    
6. le modifiche possono propagarsi ai nodi interni.
    

---

# Range query nei B+-alberi

## 45. Perché i B+-alberi sono efficienti per intervalli

I B+-alberi sono particolarmente efficienti per query del tipo:

```sql
WHERE valore BETWEEN a AND b
```

Perché:

1. si cerca `a` partendo dalla radice;
    
2. si arriva alla prima foglia utile;
    
3. si scorrono le foglie collegate tramite `Pnext`;
    
4. ci si ferma quando si supera `b`.
    

Questo evita di ripetere una ricerca dalla radice per ogni valore dell’intervallo.

---

# Schema riassuntivo finale

## 46. Organizzazione degli indici

```text
Indici
│
├── Indici ordinati di singolo livello
│   │
│   ├── Indice primario
│   │   ├── su campo chiave
│   │   ├── file dati ordinato fisicamente
│   │   └── indice non denso
│   │
│   ├── Indice di clustering
│   │   ├── su campo non chiave
│   │   ├── file dati ordinato fisicamente
│   │   └── una entry per valore distinto
│   │
│   └── Indice secondario
│       ├── su campo non ordinante
│       ├── possono essercene molti
│       ├── su chiave: indice denso
│       └── su non chiave: liste/blocchi di puntatori
│
├── Indici multilivello
│   ├── più livelli di indice
│   ├── fan-out fo
│   └── costo circa log_fo(n)
│
├── Alberi di ricerca
│   ├── nodi con chiavi e puntatori
│   ├── possono non essere bilanciati
│   └── motivano B-alberi e B+-alberi
│
├── B-alberi
│   ├── bilanciati
│   ├── data pointer anche nei nodi interni
│   └── nodi almeno mezzi pieni
│
└── B+-alberi
    ├── data pointer solo nelle foglie
    ├── nodi interni solo per guidare la ricerca
    ├── foglie collegate tramite Pnext
    └── ottimi per range query
```

---

# Concetti da sapere bene per l’esame

## 47. Domande tipiche

### Che cos’è un indice?

È una struttura di accesso che associa valori di un campo indice a puntatori verso blocchi o record, rendendo più veloce la ricerca.

---

### Che differenza c’è tra indice denso e non denso?

Un indice è **denso** se ha una entry per ogni record.

Un indice è **non denso** se ha una entry solo per alcuni record, ad esempio una per blocco.

---

### Perché l’indice primario può essere non denso?

Perché il file dati è ordinato fisicamente rispetto alla chiave primaria.

Quindi basta sapere in quale intervallo di chiavi cade il record cercato per individuare il blocco corretto.

---

### Perché un file può avere un solo indice primario o clustering?

Perché un file può essere ordinato fisicamente rispetto a un solo campo.

---

### Perché un file può avere più indici secondari?

Perché gli indici secondari non modificano l’ordinamento fisico del file dati.

Sono cammini di accesso alternativi.

---

### Perché gli indici multilivello sono più efficienti della ricerca binaria su un indice di singolo livello?

Perché riducono lo spazio di ricerca di un fattore pari al fan-out `fo`, invece che di un fattore 2.

---

### Perché servono B-alberi e B+-alberi?

Per mantenere gli alberi bilanciati e impedire che inserimenti e cancellazioni producano strutture inefficienti o nodi troppo vuoti.

---

### Qual è la differenza principale tra B-albero e B+-albero?

Nel B-albero i data pointer possono stare anche nei nodi interni.

Nel B+-albero i data pointer stanno solo nelle foglie.

---

### Perché i B+-alberi sono adatti alle range query?

Perché le foglie sono collegate tra loro tramite puntatori al nodo foglia successivo, permettendo una scansione ordinata efficiente.

---

# Mini-glossario

|Termine|Significato|
|---|---|
|Index|Struttura di accesso per velocizzare la ricerca|
|Indexing field|Campo su cui viene costruito l’indice|
|Ordering field|Campo rispetto al quale il file dati è ordinato fisicamente|
|Key field|Campo che identifica univocamente i record|
|Primary index|Indice su ordering key field|
|Clustering index|Indice su ordering field non chiave|
|Secondary index|Indice su campo non usato per ordinare fisicamente il file|
|Dense index|Indice con una entry per ogni record|
|Non-dense index|Indice con meno entry dei record, spesso una per blocco|
|Block anchor|Primo record di un blocco dati|
|Fan-out|Numero di puntatori contenibili in un nodo/blocco indice|
|Tree pointer|Puntatore a un nodo dell’albero|
|Data pointer|Puntatore a un record o blocco dati|
|B-albero|Albero di ricerca bilanciato con data pointer anche nei nodi interni|
|B+-albero|Albero bilanciato con data pointer solo nelle foglie|
|Pnext|Puntatore alla foglia successiva in un B+-albero|