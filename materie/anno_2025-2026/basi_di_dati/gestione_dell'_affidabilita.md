---
title: "Gestione Dell' Affidabilita"
aliases: ["Gestione Dell' Affidabilita"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "gestione-dell'-affidabilita"]
created: 2026-04-22
---
# Controllo dell'affidabilità
Il controllore grantisce:
- **atomicità**
- **persistenza**

- responsabile della scrittura del **log**
- operazione di scrittura sul DB viene protetta tramite un'azione sul log
	- così che si possa **disfare** le azioni a seguito di malfunzionamenti o guasti
	- **rifare** queste azioni nel caso in cui il loro esito positivo sia dubbio 
- log deve essere **robusto**

## Compiti del controllore
- realizza i comandi transazionali:
	- begin transaction
	- commit woek
	- rollback work
- realizza le primitive di ripristino dopo i malfunzionamenti / guasti
	- ripresa a caldo
	- ripresa a freddo
- riceve le richieste di accesso alle pagine in lettura e in scrittura
- predispone i dati essenziali per i meccanismi di ripristino dai guasti
	- azioni di checkpoint
	- dump
### Memoria stabile
Memoria resistente ai guasti

### Organizzazione dei log
- è un file sequenziale scritto in memoria stabile
- vengono registrate le azioni eseguite dalle transazioni
- ha un blocco corrente
	- record vengono scritti sequenzialmente in tale blocco

### Struttura dei record nel log
- **record di begin, commit e abort**: contengono il tipo di record e l'identificativo $t\_{i}$ della transazione
- **record di update**: contengono 
	- l'identificativo $t\_{i}$, 
	- l'identificativo $O\_j$ dell'oggetto modificato, 
	- i valori $BS\_i$ before state
	- $AS\_i$ after state che descrivono rispettivamente il valore di $O\_j$ prima e dopo la modifica
- **record di insert e delete**: i primi privi del valore $BS\_i$, i secondi privi del valore $AS\_i$

### Primitive undo e redo
**Convenzioni notazionali:** data una transazione T
- B(T) record di begin
- C(T) commit
- A(T) abort
- U(T,O,BS,AS) record di update
- I(T,O,AS) insert
- D(T,O,BS) delete
- **primitive undo**: per disfare un'azione su un oggetto O basta ricopiare in O il valore BS
- **primitive di redo:** per rifare un'azione su un oggetto O, sufficiente ricopiare in O il valore AS
### Proprietà di idempotenza
L'esecuzione di un numero arbitrario di undo e redo di una stessa azione è equivalente ad una singola esecuzione di tale azione.

Formalmente,
*undo(undo(A))* = *undo(A)*
*redo(redo(A))* = *redo(A)*
utile nel caso di errori in fase di ripristino: si ripetono le operazioni fino a quando verranno portate a termine con successo

### Operazione di checkpoint
Svolta periodicamente in stretto coordinamento con il buffer manager per registrare le **transazioni attive**.
1. si sospende l'accettazione di operazioni di scrittura, commit o abort
2. si trasferiscono in memoria di massa tutte le pagine del buffer su cui sono state eseguite delle modifiche da parte di transazioni che hanno già effettuato il commit
3. si scrive in modo sincrono nel log un record di checkpoint che contiene gli identificatori delle transazioni attive
4. si riprende l'accettazione delle operazioni sospese

### Dump
Produce una copia completa del DB in mutua esclusione con tutte le altre transazioni quando il sistema non è operativo

- copia memorizzata in memoria stabile
- al termine viene scritto nel log un record di dump: segnala l'avvenuta esecuzione dell'operazione in un certo istante

### Regola write-ahead-log
Durante il funzionamento delle transazioni il gestore garantisce il rispetto:
- **regola write-ahead-log** impone la parte before-state dei record di un log venga scritta nel log **prima** di effettuare la corrispondente operazione sulla base di dati.
	- consente di disfare le scritture già effettuate in memoria di massa da parte di una transazione che non ha ancora effettuato un commit
- **regola di commit-precedenza**: impone che la parte after-state dei record di un log venga scritta nel log **prima** di effettuare il commit
	- consente di rifare le scritture di una transazione che ha effettuato il commit le cui pagine modificate non sono ancora state trascritte dal buffer manager in memoria di massa

### Scrittura dei record di commit e abort
- **commit**: transazione sceglie in modo atomico e indivisibile tra abort e commit nel momento in cui scrive sul log, in modo asincrono, il record di commit
- 
- **abort**: definisce in modo atomico la decisione di abortire la transazione. Dato che tale decisione non modifica le decisioni del gestore della recovery, la scrittura del record di abort può essere fatta in modo asincrono con un'operazione di flush

### Protocolli di scrittura del log della base di dati
Le due regole precedenti impongono i seguenti protocolli per la scrittura del log e della base di dati

#### Schema a
- transazione scrive inizialmente il record B(T)
- esegue le operazioni di update scrivendo prima il record di log U(T,O,BS,AS) e poi la pagina della base di dati che passa da BS a AS

>[!warning] Tutte queste pagine devono essere scritte prima del commit, che fa una scrittura sincrona

Al commit, tutte le pagine della base di dati modificate dalla transazione sono state scritte in memoria di massa. **Non** richiede operazioni di **redo**.

#### Schemi b e c
- nel b la scrittura dei record di log precede quella delle azioni sulla base di dati che avvengono dopo la decisione di commit e la conseguente scrittura sincrona del record di commit sul log.
	- **Non** richiede operazioni di **undo**
- nel c e scritture sulla base di dati, una volta protette dalle opportune scritture sul log, possono avvenire in un qualunque momento rispetto alla scrittura del record di commit sul log. Tale schema consente al gestore del buffer di ottimizzare le operazioni di flush relative ai suoi buffer, indipendentemente dal controllore dell’affidabilità.
	- **Può** richiedere operazioni sia di **undo** sia di **redo**

### Costi
- Si differenziano per il momento in cui scrivono le pagine della base di dati
- il costo delle scritture del log è paragonabile al costo dell'aggiornamento della base di dati: l'uso di protocolli transazionali robusti introduce, quindi, un notevole **sovraccarico** per il sistema ma garantisce le proprietà acide

