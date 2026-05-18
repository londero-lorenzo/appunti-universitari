---
title: "15 2 Sql Transazioni"
aliases: ["15 2 Sql Transazioni"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "15-2-sql-transazioni"]
created: 2026-05-18
---
# Transazioni in SQL

> Appunti basati sulle slide **“Transazioni in SQL”** del corso di Basi di Dati.

---

## 1. Concetto di transazione

Una **transazione** è una sequenza di operazioni SQL che costituisce una **unità logica di lavoro** sulla base di dati.

L’idea fondamentale è:

> Una transazione deve essere eseguita **tutta intera**, oppure non deve produrre alcun effetto.

Esempio intuitivo:

```sql
update accounts
set balance = balance + 100
where acctnum = 12345;

update accounts
set balance = balance - 100
where acctnum = 7534;
```

Queste due operazioni rappresentano un trasferimento di denaro.  
Non avrebbe senso eseguire solo una delle due, perché il database finirebbe in uno stato scorretto.

---

## 2. Proprietà ACID

Le transazioni devono rispettare quattro proprietà fondamentali, dette **ACID**.

|Proprietà|Significato|
|---|---|
|**Atomicità**|La transazione è indivisibile: o tutti i suoi effetti diventano visibili, oppure nessuno.|
|**Consistenza**|La transazione porta il database da uno stato consistente a un altro stato consistente.|
|**Isolamento**|Le transazioni concorrenti non devono interferire tra loro in modo scorretto.|
|**Persistenza**|Gli effetti di una transazione conclusa con successo devono rimanere permanenti anche in caso di guasti.|

### Atomicità

Una transazione non può essere eseguita “a metà”.

Se qualcosa va storto, il DBMS deve annullare tutte le modifiche già effettuate dalla transazione.

### Consistenza

Il database deve rispettare i vincoli di integrità:

- chiavi primarie;
    
- chiavi esterne;
    
- vincoli `not null`;
    
- vincoli `check`;
    
- regole aziendali implementate nel database.
    

Attenzione: durante l’esecuzione della transazione i vincoli possono anche essere temporaneamente violati, ma **prima e dopo** la transazione devono essere rispettati.

### Isolamento

Se più transazioni vengono eseguite contemporaneamente, il risultato deve essere equivalente a una qualche esecuzione sequenziale.

In altre parole, anche se fisicamente le operazioni sono intrecciate, logicamente il risultato dovrebbe sembrare quello di transazioni eseguite una dopo l’altra.

### Persistenza

Dopo una `commit`, gli effetti della transazione devono restare salvati in modo permanente.

Se invece la transazione fallisce, le modifiche devono essere annullate.

---

## 3. Commit e rollback

Le due operazioni fondamentali sono:

|Operazione|Significato|
|---|---|
|`commit`|Conferma la transazione. Le modifiche diventano permanenti.|
|`rollback`|Annulla la transazione. Le modifiche vengono disfatte.|

Una transazione si dice **attiva** dal momento in cui inizia fino al momento immediatamente precedente alla `commit` o alla `rollback`.

Finché una transazione è attiva, le sue modifiche sono considerate **provvisorie**.

---

## 4. Transazioni in SQL

In SQL, l’inizio di una transazione può essere:

- **implicito**, perché una qualunque istruzione SQL può iniziare automaticamente una transazione;
    
- **esplicito**, tramite:
    

```sql
start transaction;
```

La fine deve invece essere indicata esplicitamente con:

```sql
commit;
```

oppure:

```sql
rollback;
```

Esempio:

```sql
start transaction;

update accounts
set balance = balance + 100.00
where acctnum = 12345;

update accounts
set balance = balance - 100.00
where acctnum = 7534;

commit;
```

Questa transazione garantisce che entrambi gli aggiornamenti vadano a buon fine, oppure nessuno dei due venga applicato.

---

## 5. Autocommit

Molti DBMS usano di default la modalità **autocommit**.

In modalità autocommit, ogni singola istruzione SQL viene automaticamente confermata con una `commit`.

Quindi:

```sql
insert into R values (1, 'a');
```

viene trattata come se fosse:

```sql
start transaction;
insert into R values (1, 'a');
commit;
```

Per raggruppare più istruzioni in una stessa transazione bisogna quindi scrivere esplicitamente:

```sql
start transaction;
...
commit;
```

---

## 6. Le transazioni non si annidano

Le transazioni SQL normalmente **non si possono annidare**.

Non è quindi possibile fare:

```sql
start transaction;

start transaction; -- non ammesso

commit;
```

Bisogna concludere la prima transazione con `commit` o `rollback` prima di iniziarne un’altra.

---

## 7. Esempio di rollback e commit

```sql
create table R (
    A int primary key,
    B char
);

start transaction;

insert into R(A,B)
values (1,'a'), (2,'b'), (3,'c');

update R
set B = 'z';

rollback;

start transaction;

insert into R(A,B)
values (10,'x'), (20,'y');

commit;

table R;
```

Risultato:

```text
A  | B
---+---
10 | x
20 | y
```

La prima transazione viene annullata dalla `rollback`, quindi gli inserimenti `(1,'a')`, `(2,'b')`, `(3,'c')` e l’aggiornamento a `'z'` non rimangono nel database.

La seconda transazione invece viene confermata con `commit`.

---

# Transazioni e vincoli d’integrità

## 8. Controllo immediato dei vincoli

Normalmente, i vincoli d’integrità vengono controllati **subito dopo ogni istruzione SQL**.

Esempio:

```sql
insert into Ordine(cliente)
values ('cliente_inesistente');
```

Se `cliente` è una chiave esterna verso una tabella `Cliente`, il DBMS rifiuta subito l’inserimento.

---

## 9. Vincoli differibili

In alcuni casi può essere necessario rimandare il controllo dei vincoli alla fine della transazione.

Questo accade, per esempio, con vincoli di integrità referenziale circolari.

Schema concettuale:

```text
R(X, Y)
Y references S

S(W, Z)
Z references R
```

A partire da un database vuoto, per inserire una tupla in `R` serve già una tupla in `S`, ma per inserire una tupla in `S` serve già una tupla in `R`.

È un circolo.

---

## 10. Uso di `deferrable`

Per permettere il controllo posticipato dei vincoli, i vincoli devono essere dichiarati **differibili**.

Esempio:

```sql
create table R (
    X int primary key,
    Y int not null
);

create table S (
    W int primary key,
    Z int not null references R deferrable
);

alter table R
add foreign key (Y) references S deferrable;
```

Poi nella transazione:

```sql
start transaction;

set constraints all deferred;

insert into R(X,Y)
values (1,10);

insert into S(W,Z)
values (10,1);

commit;
```

La prima `insert` viola temporaneamente il vincolo, ma la seconda ristabilisce la consistenza.

Alla `commit`, il DBMS verifica che tutti i vincoli siano rispettati.

> Nota importante: se un vincolo non è stato dichiarato `deferrable`, non può essere rimandato con `set constraints ... deferred`.

---

# Anomalie delle transazioni concorrenti

Quando più transazioni vengono eseguite contemporaneamente, possono verificarsi anomalie se il DBMS non controlla bene la concorrenza.

Le principali anomalie trattate nelle slide sono:

1. perdita d’aggiornamento;
    
2. lettura sporca;
    
3. lettura inconsistente / non ripetibile;
    
4. aggiornamento fantasma;
    
5. inserimento fantasma.
    

---

## 11. Perdita d’aggiornamento

La **perdita d’aggiornamento** avviene quando due transazioni leggono lo stesso valore, lo modificano e poi una delle due modifiche viene sovrascritta dall’altra.

Forma generale:

```text
r1(X) ... w2(X) ... w1(X) ... c1
```

Esempio:

|T1|T2|
|---|---|
|legge X = 100||
||legge X = 100|
||X = X + 20|
||scrive X = 120|
||commit|
|X = X + 30||
|scrive X = 130||
|commit||

Risultato finale:

```text
X = 130
```

Il problema è che l’incremento di `20` fatto da `T2` viene perso.

Il risultato corretto sarebbe stato:

```text
X = 150
```

---

## 12. Lettura sporca

Una **lettura sporca** avviene quando una transazione legge un dato scritto da un’altra transazione non ancora confermata.

Forma generale:

```text
w1(X) ... r2(X) ... abort1
```

Significa:

1. `T1` scrive `X`;
    
2. `T2` legge il valore scritto da `T1`;
    
3. `T1` fa `rollback`.
    

A quel punto `T2` ha letto un valore che in realtà non esiste più nel database.

Esempio:

```text
T1 scrive X = 42
T2 legge X = 42
T1 fa rollback
```

Il valore `42` era provvisorio, quindi `T2` ha letto un dato non affidabile.

---

## 13. Analisi inconsistente

L’**analisi inconsistente** avviene quando una transazione calcola un risultato aggregato mentre un’altra transazione modifica alcuni dei dati coinvolti.

Esempio:

Abbiamo tre saldi:

```text
X = 40
Y = 50
Z = 30
```

La somma corretta è:

```text
40 + 50 + 30 = 120
```

Ma le operazioni possono intrecciarsi così:

|T1|T2|
|---|---|
|somma = 0||
|legge X = 40||
|somma = 40||
|legge Y = 50||
|somma = 90||
||legge Z = 30|
||Z = Z - 10|
||scrive Z = 20|
||legge X = 40|
||X = X + 10|
||scrive X = 50|
||commit|
|legge Z = 20||
|somma = 110||
|commit||

`T1` calcola:

```text
40 + 50 + 20 = 110
```

Ma la somma reale dei saldi dovrebbe rimanere `120`.

Quindi la transazione legge una combinazione di valori che non corrisponde a uno stato consistente del database.

---

## 14. Lettura inconsistente o non ripetibile

Una **lettura inconsistente** avviene quando una transazione legge due volte lo stesso dato e ottiene due valori diversi, perché nel frattempo un’altra transazione ha modificato quel dato e ha fatto `commit`.

Forma intuitiva:

```text
T1 legge X = 30
T2 modifica X = 90
T2 commit
T1 rilegge X = 90
```

Per `T1`, il dato `X` cambia durante la stessa transazione.

Questa anomalia viene anche chiamata **lettura non ripetibile**.

---

## 15. Inserimento fantasma

Un **inserimento fantasma** avviene quando una transazione esegue due volte la stessa interrogazione con una condizione e ottiene insiemi diversi perché un’altra transazione ha inserito nuove tuple che soddisfano quella condizione.

Esempio:

```sql
select sum(balance)
from account;
```

Prima lettura:

```text
somma = 120
```

Poi un’altra transazione inserisce:

```sql
insert into account values ('Joe', 60);
commit;
```

Seconda lettura:

```text
somma = 180
```

La nuova riga è un **fantasma** perché compare nella seconda esecuzione della stessa query.

---

## 16. Differenza tra aggiornamento fantasma e inserimento fantasma

|Anomalia|Cosa succede|
|---|---|
|**Aggiornamento fantasma**|Una transazione modifica dati già esistenti mentre un’altra li sta leggendo.|
|**Inserimento fantasma**|Una transazione inserisce nuove tuple che soddisfano il predicato letto da un’altra transazione.|

L’inserimento fantasma è più difficile da evitare, perché non basta bloccare le tuple esistenti: bisognerebbe bloccare anche il **predicato** della query.

---

## 17. Lock di predicato

Per evitare gli inserimenti fantasma, il DBMS deve impedire che altre transazioni inseriscano nuove tuple che soddisfano una certa condizione.

Esempio:

```sql
select *
from ContoCorrente
where cliente = 'Silvio';
```

Per evitare fantasmi, finché la transazione è attiva, nessun’altra transazione dovrebbe poter inserire un nuovo conto corrente per `Silvio`.

Questo tipo di blocco si chiama **lock di predicato**.

---

# Livelli di isolamento SQL

## 18. Perché esistono i livelli di isolamento?

Garantire sempre la serializzabilità può ridurre molto la concorrenza.

Per questo SQL definisce diversi **livelli di isolamento**, che permettono di scegliere un compromesso tra:

- correttezza;
    
- prestazioni;
    
- grado di concorrenza.
    

Più il livello è alto, meno anomalie sono permesse.

---

## 19. I quattro livelli di isolamento

|Livello di isolamento|Letture sporche|Letture inconsistenti|Fantasmi|
|---|--:|--:|--:|
|**Read Uncommitted**|Possibili|Possibili|Possibili|
|**Read Committed**|Non possibili|Possibili|Possibili|
|**Repeatable Read**|Non possibili|Non possibili|Possibili|
|**Serializable**|Non possibili|Non possibili|Non possibili|

---

## 20. Read Uncommitted

È il livello più debole.

Permette:

- letture sporche;
    
- letture inconsistenti;
    
- fantasmi.
    

Una transazione può leggere dati scritti da altre transazioni non ancora confermate.

È molto rischioso dal punto di vista della correttezza.

---

## 21. Read Committed

Impedisce le letture sporche.

Una transazione può leggere solo dati confermati da transazioni che hanno già fatto `commit`.

Tuttavia permette ancora:

- letture inconsistenti;
    
- fantasmi.
    

Quindi due `select` uguali nella stessa transazione possono restituire risultati diversi.

---

## 22. Repeatable Read

Impedisce:

- letture sporche;
    
- letture inconsistenti.
    

Se una transazione legge un dato, successive letture dello stesso dato devono restituire lo stesso valore.

Secondo lo standard SQL, però, gli inserimenti fantasma possono ancora verificarsi.

---

## 23. Serializable

È il livello più forte.

Impedisce:

- letture sporche;
    
- letture inconsistenti;
    
- fantasmi.
    

L’esecuzione concorrente deve essere equivalente a una qualche esecuzione seriale delle transazioni.

---

## 24. Attenzione: assenza delle tre anomalie ≠ serializzabilità

Le slide sottolineano un punto importante:

> Lo standard SQL definisce i livelli di isolamento sulla base di alcune anomalie, ma l’assenza di quelle anomalie non implica necessariamente la vera serializzabilità.

Questo è importante soprattutto per capire l’esempio di PostgreSQL con `Repeatable Read`.

Possono esistere schedule non serializzabili che non mostrano nessuna delle tre anomalie classiche.

---

# PostgreSQL

## 25. Comportamento generale di PostgreSQL

Secondo le slide, PostgreSQL usa una tecnica chiamata **snapshot isolation**, implementata tramite **MVCC**.

Caratteristica importante:

> Le letture non bloccano mai le scritture e le scritture non bloccano mai le letture.

Solo scritture concorrenti possono causare l’annullamento di transazioni.

---

## 26. Livello di default in PostgreSQL

Il livello di isolamento di default in PostgreSQL è:

```sql
Read Committed
```

Anche se lo standard SQL prevede come default `Serializable`.

---

## 27. Impostare il livello di isolamento in PostgreSQL

In PostgreSQL:

```sql
start transaction;

set transaction isolation level read committed;
```

oppure:

```sql
start transaction;

set transaction isolation level repeatable read;
```

oppure:

```sql
start transaction;

set transaction isolation level serializable;
```

Attenzione:

> In PostgreSQL, `set transaction` va dato dopo `start transaction` e vale solo per la transazione corrente.

---

## 28. PostgreSQL e Read Uncommitted

PostgreSQL non implementa davvero quattro livelli distinti.

Se si chiede:

```sql
set transaction isolation level read uncommitted;
```

PostgreSQL si comporta comunque come `Read Committed`.

Quindi in PostgreSQL non si osservano vere letture sporche.

---

## 29. Conflitti scrittura-scrittura

Esempio:

|T1|T2|
|---|---|
|`start transaction;`||
|`insert into account values ('Bud', 90);`||
||`start transaction;`|
||`insert into account values ('Bud', 110);`|
|`commit;`||
||`commit;`|

Se due transazioni cercano di inserire la stessa chiave primaria:

- la seconda resta in attesa;
    
- se la prima fa `commit`, la seconda riceve errore di chiave duplicata;
    
- se la prima fa `rollback`, la seconda può proseguire.
    

Questo comportamento è indipendente dal livello di isolamento.

---

## 30. Perdita d’aggiornamento in PostgreSQL

In `Read Committed`, PostgreSQL può produrre una perdita d’aggiornamento in casi come questo:

1. `T1` legge il saldo di Zoe;
    
2. `T2` legge lo stesso saldo;
    
3. `T1` aggiorna e fa `commit`;
    
4. `T2` aggiorna usando il vecchio valore letto prima.
    

Risultato:

```text
saldo finale = vecchio valore + 1
```

invece di:

```text
saldo finale = vecchio valore + 2
```

In `Repeatable Read`, invece, PostgreSQL blocca questa anomalia con errore:

```text
ERROR: could not serialize access due to concurrent update
```

---

## 31. Lettura inconsistente in PostgreSQL

Nel livello `Read Committed`, due letture successive possono restituire valori diversi.

Esempio:

|T1|T2|
|---|---|
|legge Zoe = 50||
||aggiorna Zoe = 90|
||commit|
|legge Zoe = 90||

Quindi `T1` vede due valori diversi nella stessa transazione.

Con livelli più alti:

```sql
repeatable read
serializable
```

la lettura diventa consistente.

---

## 32. Aggiornamento fantasma in PostgreSQL

Nel livello `Read Committed`, una transazione può leggere valori provenienti da stati diversi del database.

Esempio:

```text
T1 legge X = 40
T1 legge Y = 50
T2 trasferisce 10 da Z a X
T2 commit
T1 legge Z = 20
```

`T1` calcola:

```text
40 + 50 + 20 = 110
```

ma la somma corretta sarebbe `120`.

Con `Repeatable Read` o `Serializable`, PostgreSQL fa vedere a `T1` uno snapshot consistente.

---

## 33. Inserimento fantasma in PostgreSQL

Nel livello `Read Committed`, gli inserimenti fantasma sono possibili.

Esempio:

```sql
select sum(balance) from account;
```

Prima restituisce:

```text
120
```

Poi un’altra transazione inserisce un nuovo conto:

```sql
insert into account values ('Joe', 60);
commit;
```

La stessa query può poi restituire:

```text
180
```

In PostgreSQL, però, `Repeatable Read` è più forte dello standard: gli inserimenti fantasma non si verificano nemmeno in `Repeatable Read`.

---

## 34. Repeatable Read non è uguale a Serializable in PostgreSQL

Anche se PostgreSQL evita i fantasmi in `Repeatable Read`, questo livello non equivale a `Serializable`.

Esempio concettuale:

Tabella:

```sql
create table mytab (
    class int,
    value int
);

insert into mytab(class, value)
values (1,10), (1,20), (2,100), (2,200);
```

Due transazioni:

- `T1` somma i valori di classe `1` e inserisce il risultato nella classe `2`;
    
- `T2` somma i valori di classe `2` e inserisce il risultato nella classe `1`.
    

Esecuzione concorrente in `Repeatable Read`:

```text
T1 legge somma classe 1 = 30
T2 legge somma classe 2 = 300
T1 inserisce (2,30)
T2 inserisce (1,300)
```

Il risultato ottenuto non corrisponde a nessuna possibile esecuzione seriale.

In `Serializable`, PostgreSQL rileva il problema e produce errore:

```text
ERROR: could not serialize access due to read/write dependencies among transactions
```

Questo dimostra che:

```text
Repeatable Read ≠ Serializable
```

---

## 35. Aggiornamento concorrente in PostgreSQL

Se due transazioni in `Repeatable Read` aggiornano lo stesso record:

```sql
update account
set balance = balance - 10
where name = 'Zoe';
```

e contemporaneamente:

```sql
update account
set balance = balance + 10
where name = 'Zoe';
```

PostgreSQL annulla una transazione con errore:

```text
ERROR: could not serialize access due to concurrent update
```

Questo accade in:

- `Repeatable Read`;
    
- `Serializable`.
    

In `Read Committed`, invece, entrambe le `update` possono avere successo.

---

# MySQL

## 36. Comportamento generale di MySQL

Secondo le slide, MySQL con InnoDB usa una combinazione di:

- MVCC;
    
- 2PL stretto.
    

Il livello di isolamento di default in MySQL/InnoDB è:

```sql
Repeatable Read
```

---

## 37. Attenzione al motore di memorizzazione

In MySQL bisogna usare InnoDB per avere il supporto alle transazioni.

Esempio:

```sql
create table account (
    name varchar(5) primary key,
    balance int not null
) engine = InnoDB;
```

Vecchi motori come ISAM non sono transazionali.

---

## 38. Impostare il livello di isolamento in MySQL

In MySQL:

```sql
set transaction isolation level read committed;

start transaction;
```

Attenzione:

> In MySQL, `set transaction` va dato prima di `start transaction` e vale per la transazione successiva.

Questa è una differenza importante rispetto a PostgreSQL.

---

## 39. MySQL e letture sporche

A differenza di PostgreSQL, MySQL distingue davvero `Read Uncommitted` da `Read Committed`.

Quindi in MySQL è possibile osservare letture sporche nel livello:

```sql
Read Uncommitted
```

Esempio:

|T1|T2|
|---|---|
|`start transaction;`||
|aggiorna Zoe = 42||
||`set transaction isolation level read uncommitted;`|
||`start transaction read only;`|
||legge Zoe = 42|
||`commit;`|
|`rollback;`||

`T2` legge `42`, ma poi `T1` annulla la modifica.

Quindi `T2` ha letto un dato sporco.

---

## 40. Differenze principali PostgreSQL / MySQL

|Aspetto|PostgreSQL|MySQL/InnoDB|
|---|---|---|
|Livello di default|`Read Committed`|`Repeatable Read`|
|`Read Uncommitted`|si comporta come `Read Committed`|permette letture sporche|
|Quando dare `set transaction`|dopo `start transaction`|prima di `start transaction`|
|Tecnica principale|Snapshot isolation + MVCC|MVCC + 2PL stretto|
|Fantasmi in `Repeatable Read`|non si verificano|comportamento dipende da locking InnoDB|
|Serializable|usa controllo di serializzabilità|approssimazione del locking dei predicati|

---

# Schema riassuntivo per l’esame

## 41. Domanda: cos’è una transazione?

Risposta:

> Una transazione è una sequenza di operazioni SQL che costituisce un’unità logica di lavoro. Deve essere eseguita interamente oppure non deve produrre effetti. Serve a garantire atomicità, consistenza, isolamento e persistenza.

---

## 42. Domanda: cosa sono commit e rollback?

Risposta:

- `commit`: conferma la transazione e rende permanenti le modifiche;
    
- `rollback`: annulla la transazione e ripristina lo stato precedente.
    

---

## 43. Domanda: quali sono le proprietà ACID?

Risposta:

|Proprietà|Spiegazione breve|
|---|---|
|Atomicità|tutto o niente|
|Consistenza|preserva i vincoli|
|Isolamento|evita interferenze scorrette|
|Persistenza|dopo commit i dati restano salvati|

---

## 44. Domanda: quali anomalie possono verificarsi con transazioni concorrenti?

Risposta:

|Anomalia|Descrizione|
|---|---|
|Perdita d’aggiornamento|una modifica viene sovrascritta da un’altra|
|Lettura sporca|si legge un dato non ancora committed|
|Lettura inconsistente|due letture dello stesso dato danno risultati diversi|
|Aggiornamento fantasma|un’analisi aggregata legge dati da stati diversi|
|Inserimento fantasma|una query ripetuta vede nuove tuple inserite da altri|

---

## 45. Domanda: quali sono i livelli di isolamento SQL?

Risposta:

```text
Read Uncommitted
Read Committed
Repeatable Read
Serializable
```

Dal più debole al più forte.

---

## 46. Domanda: quali anomalie evita ogni livello?

|Livello|Evita letture sporche?|Evita letture inconsistenti?|Evita fantasmi?|
|---|--:|--:|--:|
|Read Uncommitted|No|No|No|
|Read Committed|Sì|No|No|
|Repeatable Read|Sì|Sì|No secondo lo standard|
|Serializable|Sì|Sì|Sì|

---

## 47. Domanda: che differenza c’è tra Repeatable Read e Serializable?

`Repeatable Read` garantisce che, se una transazione legge un dato, successive letture dello stesso dato restituiscano lo stesso valore.

`Serializable` garantisce qualcosa di più forte: l’intera esecuzione concorrente deve essere equivalente a una qualche esecuzione seriale.

Quindi:

```text
Serializable implica Repeatable Read
```

ma:

```text
Repeatable Read non implica Serializable
```

---

## 48. Domanda: perché i fantasmi sono difficili da evitare?

Perché non basta bloccare le tuple già esistenti.

Bisogna impedire anche l’inserimento di nuove tuple che soddisfano il predicato della query.

Esempio:

```sql
select *
from ContoCorrente
where cliente = 'Silvio';
```

Per evitare fantasmi, bisogna impedire che altre transazioni inseriscano nuovi conti correnti per `Silvio`.

Questo richiede lock di predicato o tecniche equivalenti.

---

# Mini mappa mentale

```text
Transazioni
│
├── Proprietà ACID
│   ├── Atomicità
│   ├── Consistenza
│   ├── Isolamento
│   └── Persistenza
│
├── Operazioni
│   ├── start transaction
│   ├── commit
│   └── rollback
│
├── Vincoli
│   ├── controllo immediato
│   └── vincoli differibili
│
├── Anomalie concorrenti
│   ├── perdita d'aggiornamento
│   ├── lettura sporca
│   ├── lettura inconsistente
│   ├── aggiornamento fantasma
│   └── inserimento fantasma
│
├── Livelli isolamento SQL
│   ├── Read Uncommitted
│   ├── Read Committed
│   ├── Repeatable Read
│   └── Serializable
│
└── DBMS reali
    ├── PostgreSQL
    │   ├── default: Read Committed
    │   ├── Read Uncommitted = Read Committed
    │   └── Repeatable Read ≠ Serializable
    │
    └── MySQL/InnoDB
        ├── default: Repeatable Read
        ├── Read Uncommitted permette letture sporche
        └── set transaction prima di start transaction
```

---

# Frasi da ricordare per l’orale

- Una transazione è un’unità logica di lavoro: o viene eseguita tutta, oppure non lascia effetti.
    
- Le proprietà ACID garantiscono correttezza e affidabilità dell’esecuzione transazionale.
    
- `commit` rende permanenti le modifiche; `rollback` le annulla.
    
- L’isolamento serve a controllare le interferenze tra transazioni concorrenti.
    
- Una lettura sporca legge dati non ancora confermati.
    
- Una lettura inconsistente legge due valori diversi dello stesso dato nella stessa transazione.
    
- Un fantasma si verifica quando una query ripetuta vede nuove tuple inserite da un’altra transazione.
    
- `Serializable` è il livello più forte perché richiede equivalenza con un’esecuzione seriale.
    
- In PostgreSQL, `Repeatable Read` evita i fantasmi ma non è equivalente a `Serializable`.
    
- In MySQL/InnoDB, il livello di default è `Repeatable Read`, mentre in PostgreSQL è `Read Committed`.