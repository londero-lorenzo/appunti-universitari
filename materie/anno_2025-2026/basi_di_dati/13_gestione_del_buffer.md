---
title: "13 Gestione del Buffer"
aliases: ["13 Gestione del Buffer"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "13-gestione-del-buffer"]
created: 2026-05-05
---
# Gestione del buffer nei DBMS

Fonte: slide _13__Buffer.pdf_ sulla gestione del buffer in un Database Server centralizzato.

#basi-di-dati #dbms #buffer-manager #memoria-secondaria #transazioni

---

## 1. Idea generale

Il **buffer** è una grande area di **memoria centrale** riservata al DBMS e condivisa tra più transazioni.

> [!definition] Buffer  
> Il buffer è una zona di RAM usata dal DBMS per conservare temporaneamente pagine della base di dati, evitando di accedere continuamente alla memoria secondaria.

Il motivo principale per cui esiste è che:

- accedere alla **RAM** è molto più veloce che accedere al **disco**;
    
- molte pagine vengono richieste più volte;
    
- se una pagina è già nel buffer, il DBMS può evitare una lettura fisica dal disco;
    
- le scritture possono essere ritardate, quando l’affidabilità lo consente.
    

Negli ultimi anni i buffer sono diventati sempre più grandi perché la memoria costa meno. In alcuni casi, una parte molto grande o perfino l’intera base di dati può stare in memoria centrale.

---

## 2. Dove si colloca il buffer manager nel DBMS

Il DBMS non accede direttamente al disco ogni volta che una transazione chiede un dato. C’è una catena di componenti.

Schema logico:

```text
Interrogazione SQL
        ↓
Gestore delle interrogazioni
        ↓
Gestore dei metodi di accesso
        ↓
Buffer manager
        ↓
Gestore della memoria secondaria / file system
        ↓
Disco
```

### Gestore delle interrogazioni

Il **gestore delle interrogazioni** si occupa di:

- tradurre la query in un formato interno;
    
- ottimizzare la query;
    
- scegliere una strategia di esecuzione efficiente.
    

Per esempio, una query SQL non viene eseguita “così com’è”, ma trasformata in operazioni più elementari.

---

### Gestore dei metodi di accesso

Il **gestore dei metodi di accesso** trasforma le operazioni logiche in operazioni più vicine alla struttura fisica dei dati.

Esempi di operazioni elementari:

- scansione di un file;
    
- ordinamento;
    
- accesso diretto a un record;
    
- lettura tramite indice;
    
- scrittura di una pagina.
    

Queste operazioni fanno riferimento all’organizzazione fisica dei file.

---

### Buffer manager

Il **buffer manager** è il componente che media tra le richieste del DBMS e l’accesso fisico alla memoria secondaria.

> [!definition] Buffer manager  
> Il buffer manager mantiene temporaneamente in memoria centrale alcune porzioni della base di dati, allo scopo di migliorare l’efficienza e garantire l’affidabilità del sistema.

Il buffer manager decide:

- quali pagine caricare nel buffer;
    
- quali pagine mantenere;
    
- quali pagine scaricare;
    
- quando scrivere fisicamente su disco;
    
- quando evitare un accesso fisico perché la pagina è già presente in RAM.
    

---

## 3. Compiti principali del buffer manager

Il buffer manager ha due grandi compiti:

1. **Caricamento e scaricamento delle pagine**
    
    - da memoria secondaria a memoria centrale;
        
    - da memoria centrale a memoria secondaria.
        
2. **Accesso alle pagine presenti nel buffer**
    
    - permette alle transazioni di leggere o modificare pagine già caricate.
        

Inoltre, per il controllo della concorrenza, il buffer manager interagisce con lo **scheduler**, spesso realizzato tramite un **lock manager**.

> [!important] Da ricordare  
> Il buffer manager non lavora da solo: deve coordinarsi con il sistema di concorrenza e con il gestore dell’affidabilità.

---

## 4. Organizzazione del buffer

Il buffer è organizzato in **pagine**.

Una pagina del buffer ha dimensione pari a uno o più **blocchi** di memoria secondaria.

> [!definition] Blocco  
> Il blocco è l’unità minima o tipica usata dal sistema operativo per leggere e scrivere dati dalla memoria secondaria.

Nelle slide si assume, per semplicità, che:

```text
dimensione pagina del buffer = dimensione blocco del disco
```

Quindi possiamo pensare così:

```text
Disco:       blocco 1 | blocco 2 | blocco 3 | ...
Buffer:      pagina 1 | pagina 2 | pagina 3 | ...
```

Quando il DBMS deve lavorare su un dato, in realtà spesso lavora sulla **pagina** che contiene quel dato, non sul singolo record isolato.

---

## 5. Letture e scritture: richiesta logica vs operazione fisica

Un punto fondamentale è che la tempistica delle richieste non coincide sempre con la tempistica delle operazioni fisiche.

Una transazione può chiedere:

```text
leggi pagina X
```

ma il buffer manager può scoprire che la pagina X è già nel buffer. In quel caso non serve leggere dal disco.

---

### Lettura

Caso 1: la pagina è già nel buffer.

```text
Transazione chiede X
        ↓
X è già nel buffer
        ↓
nessuna lettura fisica dal disco
```

Questo è un caso favorevole, perché l’accesso alla RAM è molto più veloce dell’accesso al disco.

Caso 2: la pagina non è nel buffer.

```text
Transazione chiede X
        ↓
X non è nel buffer
        ↓
il buffer manager deve caricarla dal disco
```

---

### Scrittura

Quando una transazione modifica una pagina, non è detto che la modifica venga subito scritta fisicamente su disco.

Il buffer manager può decidere di:

- scrivere subito;
    
- ritardare la scrittura;
    
- scrivere quando serve liberare spazio;
    
- scrivere quando il gestore dell’affidabilità lo richiede.
    

> [!important] Idea chiave  
> Il buffer manager cerca di ridurre i tempi di risposta delle applicazioni evitando accessi fisici inutili e ritardando alcune scritture quando possibile.

---

## 6. Principio di località

Le politiche di gestione del buffer si basano sul **principio di località**.

> [!definition] Principio di località  
> I dati acceduti di recente hanno una probabilità maggiore di essere acceduti di nuovo nel futuro prossimo.

Esempio intuitivo:

Se una transazione sta leggendo molte righe di una tabella, è probabile che continui ad accedere a pagine vicine o già usate.

Per questo conviene mantenere nel buffer le pagine usate di recente.

---

## 7. Variante del principio di Pareto

Le slide richiamano anche una variante del principio di Pareto:

```text
circa il 20% dei dati viene acceduto dall’80% delle applicazioni
```

Significa che in molti sistemi non tutti i dati sono usati con la stessa frequenza.

Alcune pagine sono molto più “calde”, cioè molto più richieste.

Conseguenza:

> [!important] Conseguenza  
> Se il buffer riesce a contenere le pagine più frequentemente usate, molte richieste possono essere servite senza accedere al disco.

---

## 8. Strutture dati del buffer manager

Per gestire il buffer, il buffer manager mantiene alcune informazioni interne.

Le principali sono:

|Struttura / variabile|Funzione|
|---|---|
|**Direttorio**|Indica quali pagine sono attualmente presenti nel buffer|
|**Contatore di utilizzo**|Conta quanti programmi/transazioni stanno usando una certa pagina|
|**Bit dirty**|Indica se la pagina è stata modificata e quindi deve prima o poi essere scritta su disco|

---

### Direttorio

Il **direttorio** descrive il contenuto corrente del buffer.

Per ogni pagina caricata, indica:

- il file fisico di provenienza;
    
- il numero del blocco corrispondente;
    
- la posizione nel buffer.
    

Esempio concettuale:

|Pagina nel buffer|File fisico|Blocco su disco|
|---|---|---|
|frame 0|Clienti.dat|blocco 12|
|frame 1|Conti.dat|blocco 5|
|frame 2|Prestiti.dat|blocco 20|

Quando una transazione chiede una pagina, il buffer manager consulta il direttorio per capire se quella pagina è già presente.

---

### Contatore di utilizzo

Ogni pagina ha un contatore che indica quante transazioni o programmi stanno usando quella pagina.

Esempio:

```text
contatore = 0
```

La pagina non è attualmente usata da nessuno.

```text
contatore = 2
```

Due transazioni o programmi stanno usando quella pagina.

Il contatore è importante perché una pagina con contatore maggiore di 0 non può essere trattata come pagina libera.

---

### Bit dirty

Il **bit dirty** indica se una pagina è stata modificata.

|Stato|Significato|
|---|---|
|dirty = 0|La pagina non è stata modificata rispetto alla copia su disco|
|dirty = 1|La pagina è stata modificata e prima o poi deve essere scritta su disco|

Esempio:

```text
Pagina X caricata dal disco
dirty = 0

La transazione modifica X
dirty = 1

Prima o poi X dovrà essere salvata su disco
```

> [!warning] Attenzione  
> Una pagina dirty contiene modifiche presenti in RAM ma non ancora riportate in memoria secondaria.

---

## 9. Primitive del buffer manager

Il buffer manager offre alcune primitive alle transazioni.

Le primitive principali sono:

|Primitiva|Significato|
|---|---|
|`fix`|Richiede l’accesso a una pagina|
|`setDirty`|Segnala che una pagina è stata modificata|
|`unfix`|Segnala che la transazione ha finito di usare la pagina|
|`force`|Scrive una pagina su disco in modo sincrono|

---

### 9.1 `fix`

La primitiva `fix` viene usata quando una transazione vuole accedere a una pagina.

Effetto:

- cerca la pagina nel buffer;
    
- se non c’è, la carica dal disco;
    
- restituisce un riferimento alla pagina nel buffer;
    
- incrementa il contatore di utilizzo.
    

Schema:

```text
fix(X)
```

significa:

```text
voglio usare la pagina X
```

---

### 9.2 `setDirty`

La primitiva `setDirty` viene chiamata quando una pagina è stata modificata.

Schema:

```text
setDirty(X)
```

significa:

```text
la pagina X è stata modificata
```

Effetto:

```text
dirty bit di X = 1
```

---

### 9.3 `unfix`

La primitiva `unfix` viene usata quando la transazione ha terminato di usare una pagina.

Schema:

```text
unfix(X)
```

significa:

```text
non sto più usando la pagina X
```

Effetto:

```text
contatore di X = contatore di X - 1
```

Quando il contatore arriva a 0, la pagina può essere considerata libera o candidabile alla sostituzione.

---

### 9.4 `force`

La primitiva `force` forza la scrittura della pagina in memoria secondaria.

Schema:

```text
force(X)
```

significa:

```text
scrivi subito X su disco
```

È una scrittura **sincrona**, cioè il sistema aspetta che la scrittura sia completata.

Questa operazione è importante per l’affidabilità, perché in certi momenti bisogna garantire che alcune modifiche non vadano perse.

---

## 10. Esecuzione della primitiva `fix`

La `fix` è la primitiva più importante da capire.

Quando viene chiamata:

```text
fix(P)
```

il buffer manager deve rendere disponibile la pagina `P`.

---

### Caso 1: la pagina è già nel buffer

```text
fix(P)
        ↓
P è già nel buffer
        ↓
incremento il contatore
        ↓
restituisco il riferimento a P
```

Questo è il caso migliore.

Non serve accedere al disco.

Si parla di **buffer hit**.

---

### Caso 2: la pagina non è nel buffer, ma c’è una pagina libera

```text
fix(P)
        ↓
P non è nel buffer
        ↓
cerco una pagina libera con contatore = 0
        ↓
se la pagina libera è dirty, prima faccio flush
        ↓
leggo P dal disco
        ↓
carico P nel buffer
        ↓
incremento il contatore
```

La pagina libera può essere usata per caricare la nuova pagina richiesta.

Se però la pagina libera era stata modificata, deve prima essere salvata su disco tramite **flush**.

---

### Caso 3: la pagina non è nel buffer e non ci sono pagine libere

Se non esistono pagine libere, il buffer manager deve scegliere una politica.

Le slide distinguono due possibilità:

1. politica **steal**;
    
2. politica **no-steal**.
    

---

## 11. Politica steal

Con la politica **steal**, il buffer manager può sottrarre una pagina a un’altra transazione.

La pagina scelta viene detta **vittima**.

Schema:

```text
non ci sono pagine libere
        ↓
scelgo una pagina vittima
        ↓
se è dirty, la scarico su disco con flush
        ↓
carico la nuova pagina richiesta
```

Questa politica permette di continuare l’esecuzione della transazione che ha richiesto la pagina, ma può essere più delicata dal punto di vista dell’affidabilità e del coordinamento tra transazioni.

> [!definition] Pagina vittima  
> È la pagina selezionata dal buffer manager per essere rimossa dal buffer e sostituita con un’altra pagina.

---

## 12. Politica no-steal

Con la politica **no-steal**, il buffer manager non può sottrarre pagine alle transazioni attive.

Se non ci sono pagine libere:

```text
non ci sono pagine libere
        ↓
non posso rubare pagine ad altre transazioni
        ↓
sospendo la transazione richiedente
        ↓
la metto in una coda
        ↓
quando una pagina si libera, riprendo l’esecuzione
```

Questa politica è più conservativa, ma può causare attese.

---

## 13. Differenza tra steal e no-steal

|Politica|Cosa fa|Vantaggio|Svantaggio|
|---|---|---|---|
|**steal**|Può sottrarre una pagina a un’altra transazione|Evita di bloccare subito la transazione richiedente|Richiede maggiore attenzione per affidabilità e concorrenza|
|**no-steal**|Non sottrae pagine a transazioni attive|Più prudente|La transazione può essere sospesa|

---

## 14. Politiche force e no-force

Le politiche **force** e **no-force** riguardano il momento in cui le modifiche vengono scritte su disco.

---

### Politica force

Con la politica **force**, la scrittura avviene in modo sincrono.

```text
la transazione modifica una pagina
        ↓
la pagina viene scritta su disco in modo sincrono
```

Questo significa che la transazione deve aspettare il completamento della scrittura.

Vantaggio:

- maggiore garanzia immediata di persistenza.
    

Svantaggio:

- può rallentare l’esecuzione.
    

---

### Politica no-force

Con la politica **no-force**, la scrittura può essere rimandata.

```text
la transazione modifica una pagina
        ↓
la pagina resta dirty nel buffer
        ↓
il buffer manager decide più avanti quando scriverla
```

La scrittura avviene in modo asincrono, in base a:

- necessità di recuperare spazio;
    
- criteri di ottimizzazione;
    
- esigenze del gestore dell’affidabilità.
    

Vantaggio:

- migliori prestazioni;
    
- si possono evitare scritture ripetute della stessa pagina.
    

Svantaggio:

- serve un meccanismo di recovery più accurato.
    

---

## 15. Differenza tra flush e force

Questi due termini sono collegati, ma non sono identici.

|Termine|Significato|
|---|---|
|**flush**|Scrittura fisica di una pagina dirty dal buffer al disco|
|**force**|Primitiva che impone una scrittura sincrona su disco|

Quindi:

```text
force = richiesta esplicita e sincrona di scrittura
flush = operazione concreta di scaricamento della pagina su disco
```

Un flush può avvenire anche in modo asincrono, per decisione del buffer manager.

---

## 16. Pre-fetching

Il **pre-fetching** consiste nel caricare pagine prima che vengano effettivamente richieste.

> [!definition] Pre-fetching  
> Caricamento anticipato di pagine nel buffer quando il DBMS può prevedere che saranno richieste a breve.

Esempio:

Una transazione sta facendo una scansione sequenziale di una tabella.

```text
sta leggendo blocco 10
```

È probabile che poi legga:

```text
blocco 11, blocco 12, blocco 13...
```

Allora il DBMS può anticipare il caricamento dei blocchi successivi.

Vantaggio:

- quando la transazione chiede la pagina, questa potrebbe essere già in memoria.
    

---

## 17. Pre-flushing

Il **pre-flushing** consiste nello scrivere in anticipo pagine dirty che non sono più usate.

> [!definition] Pre-flushing  
> Scrittura anticipata su disco di pagine dirty rese libere da una `unfix`, prima ancora che vengano scelte come vittime.

Esempio:

```text
una transazione modifica pagina X
        ↓
setDirty(X)
        ↓
poi termina l’uso di X
        ↓
unfix(X)
        ↓
X è dirty ma non più usata
        ↓
il buffer manager può fare pre-flush
```

Vantaggio:

- quando in futuro servirà spazio, la pagina sarà già pulita;
    
- le successive `fix` saranno più efficienti;
    
- si riduce il tempo necessario per sostituire una pagina.
    

---

## 18. Perché ritardare le scritture può essere conveniente

Una pagina può essere modificata molte volte mentre rimane nel buffer.

Esempio:

```text
Transazione T1 modifica pagina X
Transazione T2 modifica pagina X
Transazione T3 modifica pagina X
```

Se il DBMS scrivesse subito ogni modifica, farebbe molte scritture su disco.

Con una politica no-force, invece:

```text
X resta nel buffer
X viene modificata più volte
X viene scritta una sola volta su disco
```

Questo migliora le prestazioni.

> [!important] Idea da esame  
> Il buffer consente di raggruppare più modifiche sulla stessa pagina e ridurre il numero complessivo di scritture fisiche.

---

## 19. DBMS e file system

Il DBMS usa il file system, ma non si affida completamente alla sua organizzazione.

Il file system fornisce primitive di basso livello, come:

- creare file;
    
- eliminare file;
    
- aprire file;
    
- chiudere file;
    
- leggere blocchi;
    
- scrivere blocchi.
    

Però la struttura interna dei dati viene gestita direttamente dal DBMS.

Questo serve per garantire:

- efficienza;
    
- controllo sulle strutture fisiche;
    
- transazionalità;
    
- atomicità;
    
- persistenza;
    
- recovery.
    

---

## 20. Primitive del file system usate dai DBMS

Le primitive principali sono:

|Primitiva|Significato|
|---|---|
|`create`|Crea un file|
|`delete`|Elimina un file|
|`extend`|Estende dinamicamente il numero di blocchi del file|
|`open`|Apre un file|
|`close`|Chiude un file|
|`read`|Legge un blocco specifico|
|`read_seq`|Legge una sequenza di blocchi contigui|
|`write`|Scrive un blocco specifico|
|`write_seq`|Scrive una sequenza di blocchi contigui|

---

### `read`

```text
read(fileid, block, buffer)
```

Significato:

- `fileid`: identifica il file;
    
- `block`: indica quale blocco leggere;
    
- `buffer`: indica la pagina del buffer in cui copiare il blocco.
    

---

### `read_seq`

```text
read_seq(fileid, f-block, count, f-buffer)
```

Significato:

- `fileid`: identifica il file;
    
- `f-block`: primo blocco della sequenza;
    
- `count`: numero di blocchi da leggere;
    
- `f-buffer`: prima pagina del buffer dove copiare la sequenza.
    

Serve quando il DBMS vuole leggere più blocchi contigui.

---

### `write`

```text
write(fileid, block, buffer)
```

Scrive su disco un blocco specifico prendendo i dati da una pagina del buffer.

---

### `write_seq`

```text
write_seq(fileid, f-block, count, f-buffer)
```

Scrive su disco una sequenza di blocchi contigui.

---

## 21. Schema complessivo del funzionamento

```text
Transazione
    |
    | fix(P)
    v
Buffer Manager
    |
    | controlla se P è già nel buffer
    |
    |-- sì --> restituisce riferimento a P
    |
    |-- no --> cerca spazio libero
                |
                |-- spazio libero --> carica P dal disco
                |
                |-- nessuno spazio libero
                        |
                        |-- steal --> sceglie vittima e carica P
                        |
                        |-- no-steal --> sospende la transazione
```

Durante l’uso:

```text
la transazione legge/modifica la pagina
```

Se modifica:

```text
setDirty(P)
```

Quando finisce:

```text
unfix(P)
```

Se serve garantire la scrittura:

```text
force(P)
```

---

## 22. Esempio pratico

Immaginiamo che una transazione debba leggere il conto corrente di un cliente.

La pagina che contiene quel conto si chiama `P`.

### Primo accesso

```text
fix(P)
```

Il buffer manager controlla il direttorio.

Caso:

```text
P non è nel buffer
```

Allora:

```text
trova una pagina libera
legge P dal disco
carica P nel buffer
incrementa il contatore
restituisce il riferimento
```

La transazione legge il conto.

Quando ha finito:

```text
unfix(P)
```

---

### Secondo accesso ravvicinato

Un’altra transazione chiede di nuovo `P`.

```text
fix(P)
```

Questa volta:

```text
P è già nel buffer
```

Quindi:

```text
nessuna lettura fisica
accesso molto più veloce
```

Questo mostra il vantaggio del buffer.

---

### Modifica

Se una transazione modifica il saldo:

```text
setDirty(P)
```

Ora:

```text
dirty(P) = 1
```

La pagina è aggiornata in RAM, ma potrebbe non essere ancora aggiornata su disco.

Più avanti il buffer manager farà:

```text
flush(P)
```

oppure il gestore dell’affidabilità potrà richiedere:

```text
force(P)
```

---

## 23. Concetti da non confondere

|Concetto|Da non confondere con|
|---|---|
|Buffer|Disco|
|Pagina del buffer|Blocco su disco|
|`fix`|Lettura fisica obbligatoria|
|`unfix`|Cancellazione della pagina|
|`setDirty`|Scrittura immediata|
|`force`|Scrittura asincrona|
|Dirty bit|Errore|
|Flush|Semplice rimozione dalla RAM|
|Pre-fetching|Pre-flushing|
|Steal/no-steal|Force/no-force|

---

## 24. Mini-riassunto per ripasso veloce

Il **buffer** è una zona di memoria centrale usata dal DBMS per conservare temporaneamente pagine della base di dati.

Il **buffer manager**:

- carica pagine dal disco alla RAM;
    
- scarica pagine dalla RAM al disco;
    
- evita letture fisiche quando la pagina è già nel buffer;
    
- può ritardare le scritture;
    
- mantiene un direttorio;
    
- usa un contatore di utilizzo;
    
- usa un dirty bit per sapere quali pagine sono state modificate.
    

Le primitive principali sono:

```text
fix       → chiede accesso a una pagina
setDirty  → segnala che la pagina è stata modificata
unfix     → segnala che la pagina non è più usata
force     → forza la scrittura su disco
```

Le politiche principali sono:

```text
steal     → può sottrarre una pagina a un’altra transazione
no-steal  → non può sottrarre pagine attive, quindi sospende la transazione
force     → scrive subito su disco
no-force  → può rimandare la scrittura
```

Il **pre-fetching** carica pagine in anticipo.

Il **pre-flushing** scrive pagine dirty in anticipo.

---

## 25. Possibili domande d’esame

### Cos’è il buffer?

Il buffer è un’area di memoria centrale preallocata al DBMS e condivisa tra le transazioni. Serve per mantenere temporaneamente pagine della base di dati in RAM, riducendo il numero di accessi fisici alla memoria secondaria.

---

### Qual è il ruolo del buffer manager?

Il buffer manager decide quali pagine caricare, mantenere, scaricare e scrivere su disco. Media tra il DBMS e la memoria secondaria, migliorando l’efficienza e contribuendo all’affidabilità.

---

### A cosa serve il dirty bit?

Il dirty bit indica se una pagina è stata modificata dopo essere stata caricata nel buffer. Se una pagina è dirty, prima o poi deve essere scritta su disco.

---

### A cosa serve il contatore di utilizzo?

Il contatore indica quante transazioni o programmi stanno usando una pagina. Quando il contatore è 0, la pagina non è attualmente in uso e può essere candidata alla sostituzione.

---

### Cosa fa la primitiva `fix`?

La `fix` richiede l’accesso a una pagina. Se la pagina è già nel buffer, viene restituito il suo riferimento. Se non è presente, il buffer manager deve caricarla dal disco, eventualmente liberando spazio.

---

### Cosa fa la primitiva `unfix`?

La `unfix` segnala che la transazione ha finito di usare una pagina. Il suo effetto è decrementare il contatore di utilizzo della pagina.

---

### Cosa significa politica steal?

Una politica steal permette al buffer manager di sottrarre una pagina a un’altra transazione quando non ci sono pagine libere. La pagina scelta è detta vittima e, se dirty, deve essere scritta su disco.

---

### Cosa significa politica no-steal?

Una politica no-steal non permette di sottrarre pagine alle transazioni attive. Se non ci sono pagine libere, la transazione richiedente viene sospesa finché una pagina non diventa disponibile.

---

### Differenza tra force e no-force?

Con politica force, la pagina modificata viene scritta su disco in modo sincrono. Con politica no-force, la scrittura può essere rimandata e gestita in modo asincrono dal buffer manager.

---

### Differenza tra pre-fetching e pre-flushing?

Il pre-fetching anticipa il caricamento di pagine che probabilmente saranno richieste. Il pre-flushing anticipa la scrittura su disco di pagine dirty non più usate, così da rendere più efficienti future sostituzioni.