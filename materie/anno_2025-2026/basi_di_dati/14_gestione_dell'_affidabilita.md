---
title: "14 Gestione Dell' Affidabilita"
aliases: ["14 Gestione Dell' Affidabilita"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "14-gestione-dell'-affidabilita"]
created: 2026-05-05
---
Fonte: appunti ricavati dalle slide **“Gestione dell’affidabilità”** del corso di Basi di Dati / Complementi di Basi di Dati.

# Gestione dell’affidabilità nei DBMS

## Obiettivo generale

La **gestione dell’affidabilità** è la componente del DBMS che serve a garantire che, anche in presenza di guasti, la base di dati rimanga corretta.

In particolare, il controllore dell’affidabilità garantisce due proprietà fondamentali delle transazioni:

- **atomicità**
    
- **persistenza**
    

Queste due proprietà fanno parte delle proprietà **ACID**.

|Proprietà|Significato|
|---|---|
|**Atomicità**|Una transazione deve essere eseguita tutta oppure per niente.|
|**Persistenza**|Se una transazione ha fatto `commit`, i suoi effetti devono rimanere nella base di dati anche dopo un guasto.|

> [!important] Idea centrale  
> Il DBMS usa un file speciale chiamato **log** per poter ricostruire lo stato corretto della base di dati dopo un malfunzionamento.

---

# Controllore dell’affidabilità

Il **controllore dell’affidabilità** è il componente del DBMS responsabile della protezione delle transazioni rispetto ai guasti.

## Compiti principali

Il controllore dell’affidabilità:

1. realizza i comandi transazionali:
    
    - `begin transaction`
        
    - `commit work`
        
    - `rollback work`
        
2. realizza le procedure di recovery:
    
    - **ripresa a caldo**
        
    - **ripresa a freddo**
        
3. riceve richieste di lettura e scrittura di pagine e le passa al **buffer manager**;
    
4. genera scritture aggiuntive necessarie per garantire la resistenza ai guasti;
    
5. gestisce strumenti come:
    
    - **log**
        
    - **checkpoint**
        
    - **dump**
        

---

# Architettura del gestore dell’affidabilità

Nelle slide viene mostrata un’architettura a livelli:

```text
Gestore dei metodi d’accesso
Gestore delle transazioni
        ↓
Gestore dell’affidabilità
        ↓
Gestore del buffer
        ↓
Gestore della memoria secondaria
        ↓
BD + Log
```

Il gestore dell’affidabilità sta quindi tra:

- il **gestore delle transazioni**, che invia operazioni come `begin`, `commit`, `abort`;
    
- il **gestore del buffer**, che si occupa delle pagine della base di dati e del log.
    

> [!note] Da ricordare  
> Il gestore dell’affidabilità non lavora da solo: coordina transazioni, buffer, base di dati e log.

---

# Memoria stabile

## Definizione

La **memoria stabile** è una memoria considerata resistente ai guasti.

In realtà, nessuna memoria è veramente immune da guasti. La memoria stabile è quindi un’**astrazione**: si assume che sia così affidabile da poter ignorare, dal punto di vista teorico, la possibilità che fallisca.

## Come si può realizzare?

Esempi di tecniche per avvicinarsi alla memoria stabile:

- unità a nastro;
    
- copia delle stesse informazioni su nastro e disco;
    
- due dischi in mirroring;
    
- scrittura attenta su più dispositivi.
    

> [!important]  
> Se anche la memoria stabile fallisse, il guasto sarebbe considerato **catastrofico**, perché verrebbe compromesso anche il log.

---

# Il log

## Definizione

Il **log** è un file sequenziale scritto in memoria stabile.

Serve a registrare, in ordine temporale, le azioni eseguite dalle transazioni.

Il log è fondamentale perché permette di:

- **disfare** operazioni non confermate;
    
- **rifare** operazioni confermate ma non ancora sicuramente scritte nella base di dati.
    

---

# Tipi di record nel log

I record del log possono essere di due tipi:

## 1. Record di transazione

Registrano le azioni delle transazioni.

Esempi:

```text
B(T)               begin della transazione T
C(T)               commit della transazione T
A(T)               abort della transazione T
U(T, O, BS, AS)    update dell’oggetto O
I(T, O, AS)        insert dell’oggetto O
D(T, O, BS)        delete dell’oggetto O
```

Dove:

|Simbolo|Significato|
|---|---|
|`T`|transazione|
|`O`|oggetto modificato|
|`BS`|before state, cioè valore prima della modifica|
|`AS`|after state, cioè valore dopo la modifica|

## 2. Record di sistema

Registrano operazioni di sistema, come:

- **checkpoint**
    
- **dump**
    

---

# Before state e after state

Ogni modifica deve poter essere annullata o rifatta.

Per questo, nei record di update sono memorizzati due valori:

|Valore|Significato|Serve per|
|---|---|---|
|`BS`|valore prima della modifica|`undo`|
|`AS`|valore dopo la modifica|`redo`|

Esempio:

```text
U(T1, X, 10, 20)
```

Significa:

- la transazione `T1` modifica l’oggetto `X`;
    
- prima `X` valeva `10`;
    
- dopo `X` vale `20`.
    

Quindi:

```text
undo → X = 10
redo → X = 20
```

---

# Undo e redo

## Undo

L’operazione di **undo** serve a disfare un’azione.

Si usa quando una transazione non ha fatto commit oppure quando bisogna annullare i suoi effetti.

Esempi:

|Record|Undo|
|---|---|
|`U(T, O, BS, AS)`|si rimette `O = BS`|
|`I(T, O, AS)`|si cancella `O`|
|`D(T, O, BS)`|si reinserisce `O = BS`|

## Redo

L’operazione di **redo** serve a rifare un’azione.

Si usa quando una transazione ha fatto commit, ma non siamo sicuri che le sue modifiche siano già arrivate stabilmente nella base di dati.

Esempi:

|Record|Redo|
|---|---|
|`U(T, O, BS, AS)`|si assegna `O = AS`|
|`I(T, O, AS)`|si inserisce `O = AS`|
|`D(T, O, BS)`|si cancella `O`|

---

# Idempotenza di undo e redo

Undo e redo sono **idempotenti**.

Significa che eseguire più volte la stessa operazione produce lo stesso effetto di eseguirla una sola volta.

```text
undo(undo(A)) = undo(A)

redo(redo(A)) = redo(A)
```

## Perché è importante?

Perché durante il recovery potrebbe verificarsi un altro errore.

Se il sistema riparte e ripete alcune operazioni di undo o redo, non crea danni: il risultato resta corretto.

> [!example]  
> Se un redo deve mettere `X = 20`, anche se lo eseguo due volte, `X` rimane comunque `20`.

---

# Checkpoint

## Definizione

Il **checkpoint** è un’operazione periodica che serve a semplificare il recovery.

Durante un checkpoint il DBMS registra quali transazioni sono attive in quel momento.

## Fasi del checkpoint

1. Si sospendono temporaneamente:
    
    - scritture;
        
    - commit;
        
    - abort.
        
2. Si scrivono in memoria di massa le pagine modificate da transazioni che hanno già fatto commit.
    
3. Si scrive nel log un record di checkpoint:
    

```text
CK(T1, T2, ..., Tn)
```

dove `T1, T2, ..., Tn` sono le transazioni attive al momento del checkpoint.

4. Si riprende l’esecuzione normale.
    

## Perché serve?

Il checkpoint evita di dover ripercorrere tutto il log dall’inizio.

Dopo un guasto, il DBMS può partire dall’ultimo checkpoint utile.

> [!important]  
> Le transazioni che hanno fatto commit prima del checkpoint hanno già le loro modifiche rese persistenti nella base di dati.

---

# Dump

## Definizione

Il **dump** è una copia completa della base di dati.

È una forma di backup.

A differenza del checkpoint, il dump viene fatto quando il sistema non è operativo, cioè in mutua esclusione con le transazioni.

## Cosa succede durante un dump?

1. Si blocca il normale funzionamento del sistema.
    
2. Si produce una copia completa della base di dati.
    
3. La copia viene salvata in memoria stabile.
    
4. Si scrive nel log un record:
    

```text
DUMP
```

5. Il sistema riprende il funzionamento normale.
    

## Differenza tra checkpoint e dump

|Operazione|Cosa fa|Frequenza|Scopo|
|---|---|---|---|
|**Checkpoint**|registra transazioni attive e forza alcune pagine su disco|frequente|semplificare recovery|
|**Dump**|crea una copia completa della base di dati|raro|backup per guasti gravi|

---

# Regola Write-Ahead Log

## Definizione

La regola **WAL**, cioè **Write-Ahead Log**, impone che il record di log venga scritto prima della corrispondente modifica sulla base di dati.

In particolare, il valore `BS`, cioè il before state, deve essere salvato nel log prima che la pagina venga modificata stabilmente nella base di dati.

## Perché serve?

Serve a poter fare undo.

Se una transazione modifica una pagina ma poi fallisce prima del commit, il DBMS deve sapere qual era il vecchio valore.

Senza il before state nel log, non sarebbe possibile tornare indietro.

> [!important]  
> Prima salvo nel log il valore vecchio, poi posso modificare la base di dati.

---

# Regola di commit-precedenza

## Definizione

La regola di **commit-precedenza** impone che i record di log contenenti l’after state siano scritti in memoria stabile prima del commit.

## Perché serve?

Serve a poter fare redo.

Se una transazione ha fatto commit, ma le sue pagine modificate non sono ancora state scritte definitivamente nella base di dati, il DBMS deve poterle ricostruire a partire dal log.

> [!important]  
> Prima salvo nel log il valore nuovo, poi posso considerare definitivo il commit.

---

# Riassunto delle due regole fondamentali

|Regola|Ordine imposto|Serve per|
|---|---|---|
|**WAL**|log prima della scrittura sulla BD|undo|
|**Commit-precedenza**|log prima del commit|redo|

Schema mentale:

```text
Prima del dato su disco → devo avere il log
Prima del commit → devo avere il log
```

---

# Scrittura dei record di commit e abort

## Commit

Il commit è il punto in cui la transazione sceglie definitivamente di terminare con successo.

Il record:

```text
C(T)
```

deve essere scritto stabilmente nel log.

## Guasto prima del commit

Se il guasto avviene prima che il record di commit sia nel log:

```text
la transazione non è confermata → undo
```

## Guasto dopo il commit

Se il guasto avviene dopo che il record di commit è nel log:

```text
la transazione è confermata → redo
```

## Abort

Il record:

```text
A(T)
```

indica che la transazione viene abortita.

L’abort serve a registrare la decisione di annullare la transazione.

---

# Protocolli di scrittura del log e della base di dati

Le slide presentano tre schemi principali.

Tutti rispettano:

- WAL;
    
- commit-precedenza;
    
- scrittura stabile del record di commit.
    

Cambiano però nel momento in cui le pagine modificate vengono scritte nella base di dati.

---

## Schema A

Nel primo schema:

1. si scrive `B(T)` nel log;
    
2. per ogni update:
    
    - si scrive prima il record di log;
        
    - poi si scrive la pagina nella base di dati;
        
3. prima del commit, tutte le pagine modificate devono essere già scritte nella base di dati;
    
4. poi si scrive il commit.
    

```text
Log: B(T), U(T,X,BS,AS), U(T,Y,BS,AS), C(T)
BD:          w(X)          w(Y)
```

## Conseguenza

Questo schema **non richiede redo**, perché al momento del commit tutte le modifiche sono già nella base di dati.

Può però richiedere undo se una transazione scrive nella base di dati prima di fare commit e poi fallisce.

---

## Schema B

Nel secondo schema:

1. si scrivono i record di log;
    
2. si scrive il commit;
    
3. solo dopo si scrivono le pagine nella base di dati.
    

```text
Log: B(T), U(T,X,BS,AS), U(T,Y,BS,AS), C(T)
BD:                                      w(Y), w(X)
```

## Conseguenza

Questo schema **non richiede undo**, perché nessuna modifica non confermata viene scritta nella base di dati.

Può però richiedere redo, perché dopo il commit alcune pagine potrebbero non essere ancora state scritte nella base di dati.

---

## Schema C

Nel terzo schema, più generale e più usato:

- le scritture sulla base di dati possono avvenire in qualunque momento;
    
- l’importante è che siano sempre protette dal log.
    

```text
Log: B(T), U(T,X,BS,AS), U(T,Y,BS,AS), C(T)
BD:                w(X)                         w(Y)
```

## Conseguenza

Questo schema può richiedere sia:

- undo;
    
- redo.
    

È lo schema più flessibile perché permette al buffer manager di ottimizzare le scritture.

---

# Confronto tra i tre schemi

|Schema|Quando si scrivono le pagine della BD?|Serve undo?|Serve redo?|
|---|---|--:|--:|
|**A**|prima del commit|sì|no|
|**B**|dopo il commit|no|sì|
|**C**|prima o dopo il commit|sì|sì|

> [!important]  
> Lo schema C è quello più generale e più comunemente usato.

---

# Costi della gestione dell’affidabilità

La gestione dell’affidabilità ha un costo elevato.

Infatti, ogni aggiornamento della base di dati richiede anche una scrittura nel log.

Quindi:

```text
scrittura su BD + scrittura su log = maggiore costo
```

Il costo delle scritture sul log è paragonabile al costo degli aggiornamenti sulla base di dati.

## Perché si accetta questo costo?

Perché permette di garantire:

- atomicità;
    
- persistenza;
    
- correttezza dopo i guasti.
    

---

# Ottimizzazione del log

Per ridurre il costo del log si possono usare alcune tecniche.

## Scrivere più record nella stessa pagina

I record di log di una transazione possono essere scritti nella stessa pagina in cui viene scritto il record di commit.

In questo modo il flush viene fatto una sola volta.

## Group commit

Il **group commit** consiste nel mettere più record di commit nella stessa pagina del log e scriverli con una sola operazione sincrona.

Più transazioni attendono la stessa scrittura.

> [!example]  
> Invece di fare 100 scritture sincrone per 100 commit, il DBMS può raggrupparne molte in una sola scrittura.

## Scrittura parallela del log

Nei sistemi con moltissime transazioni al secondo, si possono usare tecniche parallele di scrittura del log.

---

# Gestione dei guasti

Le slide distinguono due classi principali di guasti:

## 1. Guasti di sistema

Sono guasti dovuti a:

- bug software;
    
- problemi del sistema operativo;
    
- interruzioni di corrente;
    
- crash del sistema.
    

## Effetto

Si perde il contenuto della memoria principale, quindi del buffer.

Restano invece conservati:

- base di dati su disco;
    
- log.
    

```text
Buffer perso
BD conservata
Log conservato
```

---

## 2. Guasti di dispositivo

Sono guasti relativi alla memoria di massa.

Esempio:

- rottura del disco;
    
- perdita di parte della base di dati.
    

Dato che il log si trova in memoria stabile, si assume che il guasto di dispositivo possa danneggiare la base di dati, ma non il log.

```text
Parte della BD persa
Log conservato
```

---

# Modello fail-stop

## Definizione

Il modello **fail-stop** assume che quando il sistema rileva un guasto:

1. si arresta completamente;
    
2. blocca le transazioni;
    
3. esegue il boot;
    
4. avvia una procedura di recovery;
    
5. torna al funzionamento normale.
    

Schema:

```text
Funzionamento normale
        ↓ guasto
Stop
        ↓ boot
Ripristino
        ↓ fine ripristino
Funzionamento normale
```

---

# Ripresa a caldo e ripresa a freddo

|Tipo di recovery|Quando si usa|Cosa succede|
|---|---|---|
|**Ripresa a caldo**|guasto di sistema|si usa il log per undo/redo|
|**Ripresa a freddo**|guasto di dispositivo|si usa il dump e poi il log|

---

# Logica generale del recovery

Dopo un guasto ci sono transazioni incerte.

Il DBMS deve dividerle in due gruppi.

## Transazioni con commit

Se nel log c’è:

```text
C(T)
```

la transazione deve essere considerata completata.

Quindi bisogna fare:

```text
redo
```

## Transazioni senza commit

Se nel log non c’è il commit, la transazione non è completata.

Quindi bisogna fare:

```text
undo
```

---

# Record di end

Alcuni sistemi aggiungono un record di:

```text
end
```

Questo record indica che tutte le pagine modificate dalla transazione sono state effettivamente scritte nella base di dati.

Con il record di end si potrebbe distinguere una terza categoria:

- transazioni già completamente sistemate;
    
- quindi non serve né undo né redo.
    

Tuttavia, nelle slide si assume un modello **senza record di end**.

---

# Ripresa a caldo

La **ripresa a caldo** si usa dopo un guasto di sistema.

Il log è ancora disponibile, ma il buffer è stato perso.

## Obiettivo

Ricostruire uno stato corretto della base di dati usando:

- undo;
    
- redo;
    
- ultimo checkpoint.
    

---

## Fase 1: trovare l’ultimo checkpoint

Si accede all’ultimo blocco del log e si percorre il log all’indietro fino all’ultimo checkpoint.

Il checkpoint contiene l’elenco delle transazioni attive in quel momento.

Esempio:

```text
CK(T2, T3, T4)
```

significa che al checkpoint erano attive `T2`, `T3`, `T4`.

---

## Fase 2: costruire UNDO e REDO

Si costruiscono due insiemi:

```text
UNDO = transazioni da disfare
REDO = transazioni da rifare
```

All’inizio:

```text
UNDO = transazioni attive al checkpoint
REDO = ∅
```

Poi si percorre il log in avanti:

- se trovo `B(T)`, aggiungo `T` a `UNDO`;
    
- se trovo `C(T)`, sposto `T` da `UNDO` a `REDO`.
    

Alla fine:

- `UNDO` contiene le transazioni senza commit;
    
- `REDO` contiene le transazioni con commit.
    

---

## Fase 3: eseguire undo

Si percorre il log all’indietro.

Per ogni azione appartenente a una transazione in `UNDO`, si esegue undo.

Si torna indietro fino alla prima azione della transazione più vecchia presente in `UNDO` o `REDO`.

> [!note]  
> Questa prima azione potrebbe trovarsi anche prima del checkpoint.

---

## Fase 4: eseguire redo

Si percorre il log in avanti.

Per ogni azione appartenente a una transazione in `REDO`, si esegue redo.

In questo modo vengono riprodotte correttamente le azioni delle transazioni confermate.

---

# Perché la ripresa a caldo garantisce atomicità e persistenza?

## Atomicità

Le transazioni non completate vengono annullate.

Quindi una transazione:

- o arriva al suo stato finale;
    
- oppure viene riportata allo stato iniziale.
    

## Persistenza

Le transazioni che hanno fatto commit vengono rifatte.

Quindi i loro effetti rimangono nella base di dati anche se, al momento del guasto, alcune pagine erano ancora solo nel buffer.

---

# Esempio di ripresa a caldo

Log dato dalle slide:

```text
B(T1)
B(T2)
U(T2, O1, B1, A1)
I(T1, O2, A2)
B(T3)
C(T1)
B(T4)
U(T3, O2, B3, A3)
U(T4, O3, B4, A4)
CK(T2, T3, T4)
C(T4)
B(T5)
U(T3, O3, B5, A5)
U(T5, O4, B6, A6)
D(T3, O5, B7)
A(T3)
C(T5)
I(T2, O6, A8)
GUASTO
```

---

## Passo 1: checkpoint

Il checkpoint è:

```text
CK(T2, T3, T4)
```

Quindi inizialmente:

```text
UNDO = {T2, T3, T4}
REDO = ∅
```

---

## Passo 2: scansione in avanti dopo il checkpoint

Troviamo:

```text
C(T4)
```

Quindi `T4` ha fatto commit:

```text
UNDO = {T2, T3}
REDO = {T4}
```

Poi troviamo:

```text
B(T5)
```

Quindi `T5` è iniziata dopo il checkpoint:

```text
UNDO = {T2, T3, T5}
REDO = {T4}
```

Poi troviamo:

```text
C(T5)
```

Quindi `T5` ha fatto commit:

```text
UNDO = {T2, T3}
REDO = {T4, T5}
```

Risultato finale:

```text
UNDO = {T2, T3}
REDO = {T4, T5}
```

---

## Passo 3: undo

Si torna indietro nel log e si disfano le azioni di `T2` e `T3`.

Azioni di undo:

```text
I(T2, O6, A8)      → cancella O6
D(T3, O5, B7)      → reinserisce O5 = B7
U(T3, O3, B5, A5) → O3 = B5
U(T3, O2, B3, A3) → O2 = B3
U(T2, O1, B1, A1) → O1 = B1
```

---

## Passo 4: redo

Si rifanno le azioni di `T4` e `T5`.

Azioni di redo:

```text
U(T4, O3, B4, A4) → O3 = A4
U(T5, O4, B6, A6) → O4 = A6
```

---

## Perché T1 non viene considerata?

`T1` ha fatto commit prima del checkpoint.

Poiché il checkpoint forza in memoria di massa le pagine modificate dalle transazioni già confermate, non serve rifare `T1`.

---

# Ripresa a freddo

La **ripresa a freddo** si usa dopo un guasto di dispositivo, cioè quando una parte della base di dati è stata danneggiata.

## Fasi

### 1. Recupero dal dump

Si cerca il più recente record:

```text
DUMP
```

Poi si usa il dump per ricopiare la parte danneggiata della base di dati.

### 2. Ripercorrere il log dal dump

Dal record di dump in avanti, si ripercorre il log e si riapplicano le azioni relative alla parte danneggiata.

In questo modo si ricostruisce il lavoro svolto dopo il dump.

### 3. Eseguire una ripresa a caldo

Alla fine si esegue una normale ripresa a caldo, per garantire atomicità e persistenza rispetto all’istante del guasto.

---

# Differenza tra ripresa a caldo e ripresa a freddo

|Aspetto|Ripresa a caldo|Ripresa a freddo|
|---|---|---|
|Tipo di guasto|guasto di sistema|guasto di dispositivo|
|Cosa si perde|buffer|parte della base di dati|
|Log|conservato|conservato|
|Dump necessario?|no|sì|
|Operazioni principali|undo + redo|dump + log + ripresa a caldo|

---

# Schema finale da memorizzare

```text
Transazione senza commit → UNDO

Transazione con commit → REDO

Checkpoint → riduce il tratto di log da analizzare

Dump → serve per ricostruire la BD dopo guasti gravi

WAL → log prima della BD

Commit-precedenza → log prima del commit
```

---

# Domande tipiche d’esame

## A cosa serve il log?

Serve a registrare le azioni delle transazioni per poter fare undo o redo dopo un guasto.

## Perché il log deve stare in memoria stabile?

Perché dopo un guasto deve essere ancora disponibile. Se si perdesse anche il log, non sarebbe possibile ricostruire correttamente la base di dati.

## Qual è la differenza tra undo e redo?

- **Undo** annulla le azioni di transazioni non confermate.
    
- **Redo** rifà le azioni di transazioni confermate.
    

## Perché il commit è così importante?

Perché la presenza o assenza del record di commit nel log decide il destino della transazione dopo un guasto.

```text
commit presente → redo
commit assente → undo
```

## A cosa serve il checkpoint?

Serve a semplificare il recovery, evitando di dover analizzare tutto il log dall’inizio.

## A cosa serve il dump?

Serve come backup completo della base di dati, utile in caso di guasto di dispositivo.

## Perché lo schema C può richiedere sia undo sia redo?

Perché le pagine della base di dati possono essere scritte sia prima sia dopo il commit.

- Se sono scritte prima del commit e la transazione fallisce → serve undo.
    
- Se sono scritte dopo il commit e il sistema fallisce prima della scrittura → serve redo.