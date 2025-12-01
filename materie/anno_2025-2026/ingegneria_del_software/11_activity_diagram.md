---
title: "11 Activity Diagram"
aliases: ["11 Activity Diagram"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "11-activity-diagram"]
created: 2025-12-01
---
## Attività e azioni
>[!definition]
>Attività
>>Insieme coerente di azioni elaborative compiute dal sistema.

>[!definition]
>Azione
>>Unità discreta di lavoro atomica all'interno dell'attività.

### Rappresentazione
Con un rettangolo con il nome dell'azione.

## Flussi
Il flusso di controllo del programma si rappresenta con delle frecce che collegano le azioni.

## Decisione (Branch)
- Rombo: con un arco entrante e più archi uscenti
- Corrisponde ad un `if-then-else`
- ciascun output etichettato con una condizione booleana di **guardia** tra [...]
- Condizioni di guardia: **mutuamente esclusive**
- si intraprende solo uno dei flussi output
## Giunzione (Merge)
- la fine del comportamento condizionale iniziato con una decisione
- rombo con più input e un solo output (contrario della decisione)
>[!warning] Per ogni Decisione si deve mettere un Merge.

## Fork e Join
>[!definition]
>Fork
>>Una biforcazione del flusso in due o più thread.
### Rappresentazione
- un segmento orizzontale con un arco entrante e più di uno uscente
- archi uscenti = thread paralleli avviati contemporaneamente ed eseguiti in modo concorrente

>[!definition]
>Join
>>Sincronizza più flussi concorrenti.
### Rappresentazione
- Un segmento orizzontale in cui entra più di un arco e ne esce solo uno

**Fork** = l'ordine di esecuzione tra i due flussi non è rilevante e possono anche avvenire in parallelo
**Join** = attività successiva può essere eseguita solo quando tutti i flussi in entrata hanno terminato la propria esecuzione

# Scomposizione di un'azione

## Attribuzione e astrazione
>[!warning] Notazione precedente ha due limitazioni:
>- Non è rappresentato quale parte del software è responsabile di determinate azioni
>- In presenza di attività troppo complesse il diagramma diventa difficile da leggere

## Macroattività e sottoattività
- Racchiudere porzioni di un'attività complesse in attività generiche (**macroattività**)
- azioni di attività generiche sono dettagliate in grafici separati
- Macroattività indicata con il simbolo del rastrello dentro il rettangolo

## Partizioni
- esprimono "**chi fa cosa**"
- quale oggetto/classe è responsabile per ciascuna azione o quale organizzazione esegue ciascuna azione 
- diagramma può essere diviso in partizioni da linee verticali (**swimlanes**) assegnate a ciascuna organizzazione o classe/oggetto/organizzazione

# Segnali
- Non compaiono esplicitamente eventi
- **Segnali** = eventi diversi a cui possono rispondere le azioni
- segnale indica un qualsiasi evento asincrono proveniente da processi esterni che influenza l'esecuzione di un'activity
## Tipi di segnali
- **Invio segnale:** azione di invio di un segnale asincrono
- **Accetta evento:** aspetta che si verifichi l'evento specificato ed è attivato quando riceve l'evento
	- appena riceve l'evento il flusso prosegue
- **Accetta evento temporale:** genera eventi secondo la sua espressione temporale

# Pin e trasformazioni
>[!definition]
>Pin
>> Esprimono i parametri delle azioni (dati richiesti e forniti dalle azioni).

Sono i box dei parametri delle sottoattviità.

# Invocazioni multiple e regioni di espansione

## Invocazioni multiple
- Output di un'azione può provocare l'esecuzione multipla di una o più azioni successive
- Lista di argomenti in input e la lista di output sono riportate agli estremi dell'azione
	- output possono essere meno degli input se c'è un filtro
- Se l'azione da invocare più volte è una sola si utilizza la seguente notazione compatta
## Regioni di espansione
- contraddistingue un'area dell'activity diagram in cui le azioni contenute vengono ripetute una volta per ciascun elemento di una collezione
- se azioni sono svolte in parallelo si usa la parola << concurrent >>
## Fine di un flusso
- un flusso può terminare senza determinare la fine dell'attività
- simbolo di **fine flusso** = fine di un particolare flusso che non determina fine di un'attività
- permette alle regioni di espansione di agire come filtri producendo in output una collezione di dimensioni inferiori rispetto agli input

# Conclusioni
## Vantaggi
- comportamenti paralleli con fork e join
- compatibili con diagrammi di flusso
- descrivono processi e workflow
## Svantaggi
- Meno diffusi dello pseudocodice per descrivere la logica comportamentale
- possono essere utilizzati per descrivere gli scenari dei casi d'uso ma possono risultare poco comprensibili ai non esperti. In tali casi si preferisce la descrizione testuale

## Nella fase di analisi dei requisiti
- può modellare il flusso di un caso d'uso
- rappresentano graficamente più scenari di uno use case (più scenari paralleli che si sincronizzano)
-  modellano interazione tra entità concettuali nella risoluzione di un problema 
- modellano un algoritmo che deve essere implementato