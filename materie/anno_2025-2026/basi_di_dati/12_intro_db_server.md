---
title: "12 Intro Db Server"
aliases: ["12 Intro Db Server"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "12-intro-db-server"]
created: 2026-05-05
---
# Tecnologia di un Database Server — Appunti

Fonte: slide _12__introDBserver.pdf_

## 1. Obiettivo della lezione

Le slide introducono la **tecnologia interna di un database server centralizzato**.

L’idea principale è passare:

> dalle funzionalità visibili all’utente  
> ai meccanismi interni che permettono al DBMS di funzionare correttamente.

In altre parole, non ci si limita più a chiedere:

> “Che cosa posso fare con SQL?”

ma si inizia a studiare:

> “Come fa il DBMS a eseguire correttamente le query, gestire più utenti, evitare errori e recuperare dopo un guasto?”

---

## 2. Perché studiare i meccanismi interni del DBMS?

Studiare l’architettura interna di un database server serve per tre motivi principali.

### 2.1 Configurazione del database server

Un database server può essere configurato in molti modi.

Esempi:

- dimensione del buffer;
    
- gestione della concorrenza;
    
- politiche di logging;
    
- isolamento delle transazioni;
    
- gestione del commit e del rollback.
    

Capire i meccanismi interni aiuta a configurare meglio il sistema.

---

### 2.2 Modalità di esecuzione delle applicazioni

Il comportamento del DBMS dipende anche da come le applicazioni interagiscono con esso.

Per esempio:

- un’applicazione può usare una transazione lunga;
    
- un’altra può eseguire molte istruzioni singole in modalità `autocommit`;
    
- più utenti possono accedere contemporaneamente agli stessi dati.
    

Queste scelte influenzano:

- prestazioni;
    
- correttezza;
    
- isolamento;
    
- rischio di conflitti tra transazioni.
    

---

### 2.3 Tendenza moderna: meccanismi come servizi di rete

Le slide sottolineano anche una tendenza:

> molti meccanismi che prima erano interni al DBMS vengono oggi estratti e resi disponibili come servizi nel software di rete.

Questo è importante perché nelle architetture moderne alcune funzionalità possono essere gestite fuori dal DBMS tradizionale, per esempio:

- caching distribuito;
    
- gestione delle transazioni distribuite;
    
- servizi di autenticazione;
    
- servizi di replica;
    
- sistemi di logging esterni;
    
- middleware applicativi.
    

---

# 3. Componenti di un database server

Un database server non è un blocco unico. È composto da diversi moduli, ciascuno con un ruolo specifico.

Le slide individuano cinque componenti principali:

1. **ottimizzatore / gestore delle interrogazioni**;
    
2. **gestore dei metodi di accesso**;
    
3. **buffer manager**;
    
4. **controllore della concorrenza**;
    
5. **controllore dell’affidabilità**.
    

---

## 3.1 Ottimizzatore o gestore delle interrogazioni

L’**ottimizzatore** è il componente che decide **come eseguire una query**.

Quando scriviamo una query SQL, specifichiamo _che cosa vogliamo ottenere_, non necessariamente _come_ il DBMS deve ottenerlo.

Esempio:

```sql
SELECT *
FROM Studente
WHERE matricola = 12345;
```

L’utente chiede:

> “Dammi lo studente con matricola 12345.”

Il DBMS deve decidere:

- leggere tutta la tabella?
    
- usare un indice?
    
- fare prima un filtro?
    
- fare prima una join?
    
- quale piano di esecuzione costa meno?
    

Queste decisioni sono prese dall’ottimizzatore.

### Idea chiave

> L’ottimizzatore trasforma una richiesta logica SQL in una strategia concreta di esecuzione.

---

## 3.2 Gestore dei metodi di accesso

Il **gestore dei metodi di accesso** traduce i comandi di alto livello in operazioni più vicine alla memoria fisica.

SQL è un linguaggio dichiarativo. Quando scriviamo:

```sql
UPDATE ContoCorrente
SET saldo = saldo - 100
WHERE numero = 123;
```

non diciamo al DBMS:

- quale pagina leggere;
    
- dove si trova il record;
    
- quale indice usare;
    
- come modificare fisicamente il dato.
    

Il gestore dei metodi di accesso si occupa proprio di questo passaggio.

### Funzione principale

> Trasforma le richieste SQL in operazioni di lettura e scrittura su strutture fisiche, come tabelle, indici e pagine.

---

## 3.3 Buffer manager

Il **buffer manager** gestisce il trasferimento dei dati tra:

- **memoria secondaria**, cioè disco/SSD;
    
- **memoria principale**, cioè RAM.
    

I dati del database non sono normalmente tutti in RAM. Sono conservati su memoria secondaria, ma per essere elaborati devono essere caricati in memoria principale.

Il buffer manager decide:

- quali pagine caricare in RAM;
    
- quali pagine mantenere nel buffer;
    
- quali pagine eliminare dal buffer quando serve spazio;
    
- quando scrivere su disco le pagine modificate.
    

### Idea chiave

> Il buffer manager è fondamentale per le prestazioni, perché l’accesso alla RAM è molto più veloce dell’accesso al disco.

---

## 3.4 Controllore della concorrenza

Il **controllore della concorrenza** gestisce gli accessi contemporanei alla base di dati.

In un DBMS reale, più utenti o applicazioni possono lavorare nello stesso momento.

Esempio:

- una transazione legge il saldo di un conto;
    
- un’altra transazione modifica lo stesso saldo;
    
- una terza transazione esegue un bonifico.
    

Senza controllo della concorrenza, il database potrebbe produrre risultati sbagliati.

### Obiettivo

> Fare in modo che l’esecuzione concorrente di più transazioni sia corretta, come se le transazioni fossero state eseguite una alla volta.

Questa idea sarà collegata alla proprietà di **isolamento** delle transazioni.

---

## 3.5 Controllore dell’affidabilità

Il **controllore dell’affidabilità** garantisce il corretto funzionamento del sistema anche in presenza di guasti.

Esempi di guasti:

- crash del server;
    
- interruzione di corrente;
    
- errore durante una transazione;
    
- perdita temporanea di dati in memoria volatile.
    

Il controllore dell’affidabilità deve permettere al DBMS di recuperare uno stato corretto.

### Obiettivo

> Garantire che le transazioni concluse correttamente non vengano perse e che quelle non concluse vengano annullate.

Questa componente è collegata soprattutto a:

- **atomicità**;
    
- **persistenza**.
    

---

# 4. Architettura di un database server

La slide sull’architettura mostra come i vari moduli siano collegati tra loro.

Lo schema contiene questi elementi principali:

- gestore di interrogazioni e aggiornamenti;
    
- gestore delle transazioni;
    
- gestore dei metodi d’accesso;
    
- gestore della concorrenza;
    
- gestore del buffer;
    
- gestore della memoria secondaria;
    
- gestore dell’affidabilità;
    
- memoria secondaria.
    

---

## 4.1 Flusso generale di una query

Una query o un aggiornamento segue, semplificando, questo percorso:

```text
SQL dell'utente
        ↓
Gestore di interrogazioni e aggiornamenti
        ↓
Gestore dei metodi d'accesso
        ↓
Gestore del buffer
        ↓
Gestore della memoria secondaria
        ↓
Disco / memoria secondaria
```

Esempio:

```sql
SELECT *
FROM ContoCorrente
WHERE NumConto = 43719;
```

Il DBMS deve:

1. ricevere la query;
    
2. scegliere un piano di accesso;
    
3. capire dove si trova il dato;
    
4. caricare la pagina dal disco alla RAM;
    
5. restituire il risultato.
    

---

## 4.2 Ruolo del gestore delle transazioni

Il **gestore delle transazioni** controlla l’esecuzione delle transazioni.

Interagisce con:

- gestore della concorrenza;
    
- gestore dell’affidabilità;
    
- gestore dei metodi di accesso.
    

Questo perché una transazione deve:

- essere eseguita correttamente;
    
- non interferire in modo scorretto con altre transazioni;
    
- poter essere confermata con `commit`;
    
- poter essere annullata con `rollback`.
    

---

## 4.3 Collegamento tra concorrenza e affidabilità

Nel diagramma delle slide, il gestore della concorrenza e il gestore dell’affidabilità sono collegati al sistema delle transazioni.

Questo ha senso perché:

- la **concorrenza** riguarda cosa succede quando più transazioni lavorano insieme;
    
- l’**affidabilità** riguarda cosa succede se qualcosa va male.
    

Quindi il DBMS deve rispondere a due domande diverse:

|Problema|Componente responsabile|
|---|---|
|Più transazioni accedono agli stessi dati|Controllore della concorrenza|
|Una transazione fallisce o il sistema va in crash|Controllore dell’affidabilità|

---

# 5. Le transazioni

## 5.1 Definizione informale

Una **transazione** è un’unità elementare di lavoro svolta da un programma applicativo.

Più precisamente, è un insieme di operazioni che devono essere considerate come un blocco unico.

Esempio classico:

> trasferire denaro da un conto corrente a un altro.

Questa operazione è composta da almeno due modifiche:

1. sottrarre denaro dal conto di partenza;
    
2. aggiungere denaro al conto di destinazione.
    

Queste due operazioni devono avvenire insieme.

Non sarebbe accettabile:

- togliere soldi da un conto senza aggiungerli all’altro;
    
- aggiungere soldi a un conto senza sottrarli dall’altro.
    

---

## 5.2 Sistema transazionale

Un sistema che permette di definire ed eseguire transazioni viene detto:

> **sistema transazionale**.

Un DBMS transazionale deve garantire che le transazioni abbiano proprietà di:

- correttezza;
    
- robustezza;
    
- isolamento;
    
- recuperabilità in caso di errore.
    

---

## 5.3 Comandi di delimitazione della transazione

Una transazione può essere delimitata da due comandi:

```text
begin transaction
...
end transaction
```

oppure:

```text
start transaction
...
end transaction
```

Nelle slide vengono indicati anche come:

|Comando|Significato|
|---|---|
|`begin transaction` / `start transaction`|inizio della transazione|
|`end transaction`|fine della transazione|

Spesso `end transaction` è implicito.

---

## 5.4 Modalità autocommit

Se non viene specificato `begin transaction`, il sistema può assumere che ogni singola istruzione SQL sia una transazione autonoma.

Questa modalità si chiama:

> **autocommit**.

Esempio:

```sql
UPDATE ContoCorrente
SET Saldo = Saldo - 100
WHERE NumConto = 43719;
```

In modalità autocommit, questa singola istruzione viene trattata come:

```sql
start transaction;

UPDATE ContoCorrente
SET Saldo = Saldo - 100
WHERE NumConto = 43719;

commit work;
```

### Conseguenza importante

In autocommit, ogni istruzione viene confermata automaticamente se va a buon fine.

Questo è comodo negli ambienti interattivi, ma può essere pericoloso quando più operazioni devono essere trattate come un unico blocco logico.

---

# 6. Commit e rollback

## 6.1 Le due istruzioni fondamentali

All’interno di una transazione ci sono due possibili conclusioni:

|Istruzione|Significato|
|---|---|
|`commit work`|conferma la transazione|
|`rollback work` / `abort`|annulla la transazione|

Una transazione ben formata deve terminare con una sola delle due.

---

## 6.2 Commit

Il `commit` indica che la transazione è andata a buon fine.

Con il commit:

- gli aggiornamenti diventano permanenti;
    
- il DBMS considera conclusa positivamente la transazione;
    
- gli effetti della transazione devono rimanere nel database.
    

Esempio astratto:

```text
begin transaction
X := X - 10;
Y := Y + 10;
commit work;
end transaction
```

Qui il sistema conferma definitivamente che:

- `X` è stato diminuito di 10;
    
- `Y` è stato aumentato di 10.
    

---

## 6.3 Rollback / abort

Il `rollback` indica che la transazione deve essere annullata.

Con il rollback:

- tutte le modifiche fatte dalla transazione vengono eliminate;
    
- il database torna allo stato precedente all’inizio della transazione;
    
- è come se la transazione non fosse mai avvenuta.
    

Esempio:

```text
begin transaction
X := X - 10;
Y := Y + 10;
rollback work;
end transaction
```

Dopo il rollback:

- `X` torna al valore iniziale;
    
- `Y` torna al valore iniziale.
    

---

# 7. Esempio: trasferimento tra conti correnti

Le slide mostrano una transazione che trasferisce 10000 euro dal conto `43719` al conto `65286`.

```sql
start transaction;

update ContoCorrente
set Saldo = Saldo + 10000
where NumConto = 65286;

update ContoCorrente
set Saldo = Saldo - 10000
where NumConto = 43719;

commit work;
```

---

## 7.1 Cosa fa questa transazione?

La transazione esegue due aggiornamenti:

1. aumenta di 10000 il saldo del conto `65286`;
    
2. diminuisce di 10000 il saldo del conto `43719`.
    

Poi esegue il `commit`.

Quindi il trasferimento diventa definitivo.

---

## 7.2 Perché serve una transazione?

Perché le due operazioni devono essere atomiche.

Non vogliamo che il DBMS esegua solo una delle due.

Situazione corretta:

```text
conto 43719: -10000
conto 65286: +10000
```

Situazioni scorrette:

```text
conto 43719: -10000
conto 65286: invariato
```

oppure:

```text
conto 43719: invariato
conto 65286: +10000
```

La transazione impedisce questi stati intermedi scorretti.

---

# 8. Variante con controllo del saldo

Le slide propongono poi una variante: il trasferimento deve essere annullato se il conto di partenza va in negativo.

La logica è:

```sql
start transaction;

update ContoCorrente
set Saldo = Saldo + 10000
where NumConto = 65286;

update ContoCorrente
set Saldo = Saldo - 10000
where NumConto = 43719;

select Saldo into A
from ContoCorrente
where NumConto = 43719;

if A >= 0
then commit work;
else rollback work;
```

Nella slide il codice è molto sintetico; concettualmente va letto così:

- se il saldo del conto `43719` è ancora maggiore o uguale a zero, allora si fa `commit`;
    
- se invece il saldo diventa negativo, si fa `rollback`.
    

---

## 8.1 Interpretazione passo per passo

Supponiamo che il conto `43719` abbia saldo iniziale `15000`.

Dopo il prelievo di `10000`:

```text
15000 - 10000 = 5000
```

Il saldo è positivo.

Quindi:

```text
commit
```

La transazione va a buon fine.

---

Supponiamo invece che il conto `43719` abbia saldo iniziale `7000`.

Dopo il prelievo di `10000`:

```text
7000 - 10000 = -3000
```

Il saldo è negativo.

Quindi:

```text
rollback
```

La transazione viene annullata.

Il database torna allo stato precedente:

- il conto `43719` torna a `7000`;
    
- il conto `65286` non riceve i `10000`.
    

---

# 9. Proprietà ACID delle transazioni

Le transazioni devono soddisfare quattro proprietà fondamentali, dette proprietà **ACID**:

|Lettera|Proprietà|Significato|
|---|---|---|
|A|Atomicità|tutto o niente|
|C|Consistenza|rispetto dei vincoli|
|I|Isolamento|indipendenza dalle altre transazioni|
|D|Durabilità / Persistenza|gli effetti del commit non si perdono|

Nelle slide la quarta proprietà viene chiamata **persistenza**.

---

# 10. Atomicità

## 10.1 Definizione

L’**atomicità** significa che una transazione è un’unità indivisibile di esecuzione.

Quindi:

> o produce tutti i suoi effetti, oppure non ne produce nessuno.

Questa è la logica del:

> tutto o niente.

---

## 10.2 Esempio

Transazione:

```sql
start transaction;

update ContoCorrente
set Saldo = Saldo - 10000
where NumConto = 43719;

update ContoCorrente
set Saldo = Saldo + 10000
where NumConto = 65286;

commit work;
```

Se tutto va bene:

- il conto `43719` viene diminuito;
    
- il conto `65286` viene aumentato;
    
- viene eseguito il commit.
    

Se qualcosa va male a metà:

- il DBMS deve annullare gli effetti già prodotti;
    
- il database torna allo stato precedente.
    

---

## 10.3 Undo

Se una transazione non può essere completata, il sistema deve disfare ciò che è stato fatto fino a quel momento.

Questa operazione si chiama:

> **undo**.

Esempio:

```text
1. sottraggo 10000 dal conto A
2. errore prima di aggiungere 10000 al conto B
3. undo: ripristino il saldo del conto A
```

L’undo serve prima del commit, quando la transazione fallisce.

---

## 10.4 Redo

Dopo il commit, invece, il sistema deve garantire che gli effetti della transazione rimangano.

Se avviene un guasto subito dopo il commit, può essere necessario rifare alcune operazioni.

Questa operazione si chiama:

> **redo**.

Esempio:

```text
1. la transazione esegue commit
2. il sistema va in crash
3. al riavvio, il DBMS controlla il log
4. se alcune modifiche non erano ancora fisicamente scritte su disco, le rifà
```

---

## 10.5 Commit come istante atomico

Il commit è il punto decisivo.

Prima del commit:

> se avviene un guasto, la transazione viene annullata.

Dopo il commit:

> se avviene un guasto, la transazione deve essere recuperata e mantenuta.

Schema:

```text
prima del commit  → rollback / undo
commit            → punto atomico di successo
dopo il commit    → redo se necessario
```

---

# 11. Cause di abort di una transazione

Una transazione può abortire per diverse ragioni.

Le slide indicano tre casi principali.

---

## 11.1 Rollback deciso dalla transazione

La transazione può decidere autonomamente di annullarsi.

Esempio:

```text
se il saldo diventa negativo
allora rollback
```

Le slide lo chiamano una specie di “suicidio” della transazione.

---

## 11.2 Abort deciso dal sistema

Il sistema può accorgersi che una transazione non può concludersi correttamente.

Esempi:

- violazione di un vincolo;
    
- deadlock;
    
- errore grave durante l’esecuzione;
    
- impossibilità di accedere a una risorsa necessaria.
    

In questo caso il DBMS può “uccidere” la transazione.

---

## 11.3 Abort causato da guasto di sistema

Se il sistema va in crash, alcune transazioni attive possono non aver ancora eseguito il commit.

In quel caso, al riavvio, il DBMS deve annullarle.

Esempio:

```text
T1 ha fatto modifiche ma non ha ancora fatto commit
↓
crash del sistema
↓
al riavvio T1 viene annullata
```

---

# 12. Consistenza

## 12.1 Definizione

La **consistenza** significa che una transazione non deve violare i vincoli di integrità della base di dati.

I vincoli possono essere, per esempio:

- chiavi primarie;
    
- chiavi esterne;
    
- vincoli `NOT NULL`;
    
- vincoli `UNIQUE`;
    
- vincoli `CHECK`;
    
- vincoli di dominio;
    
- vincoli di integrità referenziale.
    

---

## 12.2 Esempio di violazione di consistenza

Supponiamo di avere una tabella:

```sql
CREATE TABLE Studente (
    matricola INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);
```

Questa istruzione viola il vincolo `NOT NULL`:

```sql
INSERT INTO Studente(matricola, nome)
VALUES (123, NULL);
```

Il DBMS deve impedire che il database finisca in uno stato inconsistente.

---

## 12.3 Consistenza e transazioni

Una transazione deve portare il database:

```text
da uno stato consistente
a un altro stato consistente
```

Questo non significa che durante l’esecuzione non possano esistere stati intermedi temporanei problematici.

Dipende dal tipo di controllo dei vincoli.

---

## 12.4 Verifica immediata dei vincoli

La verifica è **immediata** quando il DBMS controlla un vincolo durante l’esecuzione della transazione.

Esempio:

```sql
INSERT INTO Studente(matricola, nome)
VALUES (123, NULL);
```

Il DBMS controlla subito il vincolo `NOT NULL`.

Se il vincolo è violato, l’istruzione viene rifiutata.

---

## 12.5 Verifica differita dei vincoli

La verifica è **differita** quando il DBMS controlla il vincolo alla fine della transazione, cioè al momento del commit.

Questo può essere utile quando una sequenza di operazioni crea temporaneamente una situazione non valida, ma alla fine la corregge.

Esempio concettuale:

```text
durante la transazione: stato temporaneamente non valido
alla fine: stato valido
commit: consentito
```

Se invece al momento del commit il vincolo è ancora violato:

```text
commit fallisce
rollback della transazione
```

---

# 13. Isolamento

## 13.1 Definizione

L’**isolamento** significa che l’esecuzione di una transazione deve essere logicamente indipendente dall’esecuzione contemporanea delle altre.

Anche se fisicamente più transazioni vengono eseguite nello stesso momento, il risultato deve essere equivalente a una qualche esecuzione seriale.

---

## 13.2 Esecuzione concorrente vs esecuzione seriale

Esecuzione concorrente:

```text
T1 e T2 vengono eseguite nello stesso intervallo di tempo
```

Esecuzione seriale:

```text
prima T1, poi T2
```

oppure:

```text
prima T2, poi T1
```

L’isolamento richiede che l’esecuzione concorrente produca un risultato corretto, cioè equivalente a una esecuzione una-per-volta.

---

## 13.3 Esempio intuitivo

Supponiamo che due transazioni lavorino sullo stesso conto.

Saldo iniziale:

```text
X = 100
```

Transazione T1:

```text
X := X + 50
```

Transazione T2:

```text
X := X - 30
```

Risultato corretto finale:

```text
X = 120
```

Infatti:

```text
100 + 50 - 30 = 120
```

Senza isolamento, però, le due transazioni potrebbero interferire.

Esempio scorretto:

```text
T1 legge X = 100
T2 legge X = 100
T1 scrive X = 150
T2 scrive X = 70
```

Risultato finale:

```text
X = 70
```

Questo risultato è sbagliato, perché l’aggiornamento di T1 è stato perso.

Questo problema è noto come:

> **lost update**, cioè aggiornamento perso.

---

## 13.4 Indipendenza dell’esito delle transazioni

L’isolamento non riguarda solo i valori finali dei dati.

Riguarda anche l’indipendenza degli esiti.

In particolare, il rollback di una transazione non deve costringere altre transazioni a fare rollback.

---

## 13.5 Effetto domino

Le slide parlano di **effetto domino**.

L’effetto domino può verificarsi quando una transazione legge dati scritti da un’altra transazione che non ha ancora fatto commit.

Esempio:

```text
T1 modifica X
T2 legge X modificato da T1
T1 fa rollback
```

A questo punto T2 ha letto un dato che non esiste più, perché la modifica di T1 è stata annullata.

Quindi anche T2 potrebbe dover essere annullata.

Se poi T3 aveva letto dati da T2, anche T3 potrebbe essere annullata.

Da qui l’idea di “domino”.

---

## 13.6 Lettura sporca

Il problema appena descritto è collegato alla cosiddetta:

> **dirty read**, cioè lettura sporca.

Una lettura sporca avviene quando una transazione legge un dato modificato da un’altra transazione non ancora confermata con commit.

Schema:

```text
T1 scrive X
T2 legge X
T1 fa rollback
```

Il dato letto da T2 era “sporco”, perché non era ancora definitivo.

---

# 14. Persistenza / Durabilità

## 14.1 Definizione

La **persistenza** significa che gli effetti di una transazione che ha eseguito correttamente il commit non devono essere persi.

Questa proprietà è anche chiamata:

> **durabilità**.

---

## 14.2 Esempio

Supponiamo che una transazione faccia:

```sql
start transaction;

update ContoCorrente
set Saldo = Saldo + 10000
where NumConto = 65286;

commit work;
```

Dopo il commit, il nuovo saldo deve rimanere nel database.

Anche se subito dopo:

- il server va in crash;
    
- manca la corrente;
    
- il processo del DBMS si interrompe.
    

Al riavvio, il DBMS deve recuperare gli effetti della transazione confermata.

---

## 14.3 Collegamento con il redo

La persistenza è collegata al `redo`.

Se una transazione ha fatto commit, ma alcune modifiche non erano ancora state scritte stabilmente su disco, il DBMS deve poterle rifare.

Per questo i DBMS usano meccanismi come:

- log;
    
- recovery;
    
- redo log;
    
- write-ahead logging.
    

Le slide non approfondiscono ancora questi strumenti, ma introducono il concetto generale.

---

# 15. Chi garantisce le proprietà ACID?

Le slide concludono collegando le proprietà ACID ai componenti del DBMS.

|Proprietà|Garantita principalmente da|
|---|---|
|Atomicità|controllo dell’affidabilità|
|Persistenza|controllo dell’affidabilità|
|Isolamento|controllo della concorrenza|
|Consistenza|controlli generati dal DDL e procedure di verifica dei vincoli|

---

## 15.1 Atomicità e persistenza

Sono garantite dal:

> **controllore dell’affidabilità**.

Motivo:

- l’atomicità richiede undo in caso di fallimento;
    
- la persistenza richiede redo in caso di guasto dopo il commit.
    

Entrambe riguardano il recupero corretto dopo errori o crash.

---

## 15.2 Isolamento

È garantito dal:

> **controllore della concorrenza**.

Motivo:

- deve impedire interferenze scorrette tra transazioni;
    
- deve evitare dirty read;
    
- deve evitare rollback a cascata;
    
- deve rendere corretta l’esecuzione concorrente.
    

---

## 15.3 Consistenza

È legata ai vincoli definiti nello schema tramite DDL.

Esempi di DDL:

```sql
CREATE TABLE Studente (
    matricola INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
);
```

Il DDL definisce vincoli come:

- `PRIMARY KEY`;
    
- `NOT NULL`;
    
- `UNIQUE`;
    
- `FOREIGN KEY`;
    
- `CHECK`.
    

Il DBMS genera poi controlli per verificare che le transazioni rispettino questi vincoli.

---

# 16. Schema riassuntivo generale

```text
Utente / Applicazione
        ↓
Query SQL / Aggiornamento
        ↓
Gestore interrogazioni e aggiornamenti
        ↓
Ottimizzatore
        ↓
Gestore metodi di accesso
        ↓
Buffer manager
        ↓
Gestore memoria secondaria
        ↓
Disco / memoria secondaria
```

Parallelamente intervengono:

```text
Gestore transazioni
        ↓
Controllore concorrenza  → isolamento
        ↓
Controllore affidabilità → atomicità + persistenza
        ↓
Controlli DDL            → consistenza
```

---

# 17. Parole chiave da ricordare

|Termine|Significato|
|---|---|
|Database server|Sistema che gestisce dati in modo persistente e controllato|
|Ottimizzatore|Decide il piano migliore per eseguire una query|
|Metodo di accesso|Modalità concreta con cui il DBMS accede ai dati|
|Buffer manager|Gestisce il passaggio tra disco e RAM|
|Concorrenza|Esecuzione contemporanea di più transazioni|
|Affidabilità|Capacità di recuperare dopo errori o guasti|
|Transazione|Unità logica di lavoro|
|Commit|Conferma definitiva della transazione|
|Rollback|Annullamento della transazione|
|Autocommit|Ogni istruzione SQL è una transazione autonoma|
|Atomicità|Tutto o niente|
|Consistenza|Rispetto dei vincoli|
|Isolamento|Indipendenza dalle altre transazioni|
|Persistenza|Gli effetti del commit non si perdono|
|Undo|Disfare modifiche di una transazione fallita|
|Redo|Rifare modifiche di una transazione confermata|

---

# 18. Domande tipiche da esame

## Che cos’è una transazione?

Una transazione è un’unità elementare di lavoro svolta da un’applicazione, composta da una o più operazioni sulla base di dati, alla quale il DBMS associa proprietà di correttezza, isolamento e robustezza.

---

## Che differenza c’è tra commit e rollback?

Il `commit` conclude positivamente una transazione e rende permanenti i suoi effetti.

Il `rollback` conclude negativamente una transazione e annulla tutti gli aggiornamenti eseguiti, riportando il database allo stato precedente.

---

## Che cos’è l’autocommit?

L’autocommit è una modalità in cui ogni singola istruzione SQL viene trattata come una transazione autonoma. Se l’istruzione va a buon fine, viene confermata automaticamente.

---

## Che cosa significa atomicità?

Significa che una transazione è indivisibile: o vengono applicati tutti i suoi effetti, oppure non ne viene applicato nessuno.

---

## Che cosa sono undo e redo?

L’`undo` serve ad annullare modifiche fatte da una transazione non conclusa correttamente.

Il `redo` serve a ripristinare modifiche di una transazione che aveva già fatto commit, ma i cui effetti potrebbero non essere ancora stati scritti stabilmente su disco.

---

## Che cosa significa isolamento?

Significa che ogni transazione deve comportarsi come se fosse eseguita indipendentemente dalle altre. Anche se più transazioni vengono eseguite contemporaneamente, il risultato deve essere equivalente a un’esecuzione seriale.

---

## Che cos’è l’effetto domino?

È una reazione a catena di rollback. Può verificarsi quando una transazione legge dati modificati da un’altra transazione non ancora confermata. Se la prima transazione fa rollback, anche le transazioni che hanno letto quei dati potrebbero dover essere annullate.

---

## Che cosa significa persistenza?

Significa che, dopo un commit corretto, gli effetti della transazione non devono essere persi, nemmeno in caso di guasto.

---

# 19. Mini-riassunto finale

Un database server è formato da più componenti interni. L’ottimizzatore decide come eseguire le query, il gestore dei metodi di accesso traduce SQL in operazioni sui dati, il buffer manager gestisce il passaggio tra disco e RAM, il controllore della concorrenza gestisce più transazioni simultanee e il controllore dell’affidabilità permette il recupero dopo guasti.

Il concetto centrale della lezione è la **transazione**, cioè un’unità logica di lavoro che deve essere eseguita correttamente secondo le proprietà **ACID**.

Una transazione può terminare con:

- `commit`, se va a buon fine;
    
- `rollback`, se deve essere annullata.
    

Le proprietà ACID garantiscono che le transazioni siano:

- **atomiche**, cioè tutto o niente;
    
- **consistenti**, cioè rispettino i vincoli;
    
- **isolate**, cioè indipendenti dalle altre transazioni;
    
- **persistenti**, cioè definitive dopo il commit.