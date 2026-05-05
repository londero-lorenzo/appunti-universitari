---
title: "Gestione del Buffer"
aliases: ["Gestione del Buffer"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "gestione-del-buffer"]
created: 2026-04-22
---
# Politiche di gestione del buffer
- Sono analoghe a quelle di gestione della memoria centrale da parte del S.O.
- rispondono al medesimo principio di località dei dati: i dati acceduti di recente hanno maggiore probabilità di essere nuovamente acceduti nel futuro prossimo
# Direttorio e variabili di stato
- buffer manager mantiene le seguenti informazioni/strutture dati:
	- un **direttorio**: descrive il contenuto corrente del buffer
		- indicando per ciascuna pagina caricata il file fisico e il numero di blocco corrispondenti
	- per ogni pagina due **variabili di stato**
# Primitive per gestione del buffer
1. **fix**: utilizzata per richiedere l'accesso ad una pagina e restituisce al chiamante il riferimento alla pagina del buffer, in modo da consentire l'effettivo accesso ai dati
2. **setDirty**: indica al buffer manager che una pagina è stata modificata
3. **unfix**: indica che il chiamante ha terminato di utilizzare la pagina. Ha l'effetto di decrementare il contatore di utilizzo della pagina
4. **force**: trascrive in memoria secondaria, in modo sincrono, una pagina del buffe. Tale operazione è richiesta dal gestore dell'affidabilità quado risulta necessario garantire che alcuni dati non vengano persi

## Fix
Esecuzione:
- cerca la pagina fra quelle già presenti nel buffer.
	- se la trova l'operazione termina con successo
	- se non è presente si cerca nel buffer una pagina libera (valore contatore = 0)
		- se il bit di stato segnala che è stata modificata viene aggiornata in memoria secondaria (**flush**)
		- vengono fatte le conversioni di indirizzi per identificare la pagina da caricare nel buffer e viene effettuata l'operazione di lettura
	- se non esistono pagine libere:
		- Politica **steal**: consente di sottrarre una pagina ad un'altra transazione
			- la pagina selezionata (vittima) viene scaricata in memoria di massa
		- Politica **no-steal**: non consente di sottrarre pagine alle transazioni attive.
			- la transazione viene sospesa ed entra in coda di transazioni gestita dal buffer manager
			- quando si libera una pagina il buffer manager procede come nel secondo punto
	- quando si effettua un accesso ad una pagina viene incrementato il contatore relativo agli utilizzatori della pagina
### Pre-fetching e pre-flushing
- Possibilità di anticipare i tempi di caricamento e di scaricamento delle pagine
>[!definition]
>Pre-fetching
>>Caricamento delle pagine anticipato rispetto alla richiesta delle transazioni, in quei casi in cui sono note a priori le modalità di accesso alle pagine della base di dati da parte di una transazione

>[!definition]
>Pre-flushing
>>Scaricamento anticipato delle pagine rispetto al momento in cui vengono scelte come vittime: scrittura anticipata di pagine rese libere dall'esecuzione di un'operazione di unfix, che sono state modificate nel corso del loro utilizzo (bit di stato con valore *dirty*).
>>L'esecuzione del pre-flushing rende più efficienti le successive operazioni di fix.

>[!tip] Una pagina utilizzata da molte applicazioni può restare a lungo nel buffer, subendo varie modifiche, e venire trascritta in memoria secondaria con una sola operazione di scrittura.

# DBMS e file system
Interazione tra i due non banale

- DBMS usa alcune **funzionalità del file system**
- crea una propria **astrazione** dei file che consentono di garantire **efficienza** e **transazionalità**

## Primitive del file system usate dai DBMS
- **create**
- **delete**
- **open**
- **close**
- Accesso diretto ad un blocco di file: **read(fileid, block, buffer)**
- Accesso sequenziale ad un numero fisso di blocchi: **read_seq(fileid, f-block, count, f-buffer)**
- **write(fileid, block, buffer)**
- **write_seq(fileid, f-block, count, f-buffer)**

