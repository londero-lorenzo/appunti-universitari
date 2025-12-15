---
title: "15 Statechart"
aliases: ["15 Statechart"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "15-statechart"]
created: 2025-12-15
---
# Notazione
## Macchine a stati
**Fondamentali:**
- stati: numero finito
- eventi
- transizioni: in risposta agli eventi esegue transizioni tra gli stati
### Stato
Condizione della vita di un'entità:
- Soddisfare una condizione
- Eseguire un'attività
- Aspettare un evento
In un dato istante, l'entità si trova in uno e un solo stato
In un certo stato: entità si comporterà in uno specifico modo in risposta a degli eventi specifici

### Evento
- Occorrenza di interesse
	- collocata nel tempo e nello spazio
- possono scatenare il cambiamento di stato dell'entità
- in ciascuno stato di fronte agli eventi, l'entità si comporterà diversamente
- stessa entità può comportarsi in maniera diversa in risposta allo stesso evento se si trova in stati diversi

>[!example] L’evento usoInterruttore accende la luce se la lampadina é in stato Off, spegne la luce se la lampadina é in stato On

### Transizione di stato
- Passaggio da uno stato all'altro, in risposta ad un evento
- arco orientato tra gli stati
- **evento trigger[guardia]/attività**
	- **evento trigger**: evento o sequenza di eventi che scatena la transizione (potrebbe contenere parametri)
	- **guardia**: condizione booleana che deve essere verificata affinché possa scatenarsi la transizione
	- **Attività**: è un'azione elaborativa che si verifica contestualmente con la transizione

### Statechart Diagram completo
- Diagramma di stato = grafo diretto
	- nodi = stati
	- archi = transizioni
- Stati speciali o pseudostati:
	- **Stato iniziale** (non può essere raggiunto)
	- **Stato finale** (non può essere lasciato)

### Eventi con guardie mutuamente esclusive
- Quando il sistema si trova in uno stato: 
	- un evento può scatenare una sola transizione uscente da quello stato
	- lo stesso evento trigger può portare a due stati diversi solo se le guardie sono mutuamente esclusive

### Eventi che non scatenano transizioni
- Se in uno stato si verifica un evento per cui non c'è nessuna transizione valida, allora l'evento è ignorato

>[!example] Se il sistema si trova nello stato Cassaforte chiusa, gli eventi di cassaforte chiusa e candela rimossa non provocano nessuna transizione.

### Stato finale e distruzione
- stato finale = completamento dell'esecuzione della macchina a stati
- il passaggio allo stato finale sottintende la distruzione dell'oggetto
- si deve ricreare l'oggetto per ritornare allo stato iniziale
# Attività interne
Risposte ad eventi che conducono allo stesso stato: **auto-transizioni** o **attività interne**

- Nelle attività interne uno stato risponde agli eventi senza eseguire una transizione ad un altro stato
	- scatena attività interne
- evento, guardia e attività sono riportate dentro al box dello stato

- Differenza tra auto-transizioni e attività interne: nel caso di attività interne non avviene il nuovo ingresso nello stato e quindi non vengono eseguite nuovamente le attività entry ed exit

## Activity state
- L'oggetto svolge una determinata attività in modo continuo
- **do-activity** sono attività interne particolari svolte dall'entità mentre si trova nello stato:
	- dicitura: **do/** attività o **esegui/** attività
	- durano un tempo finito
	- possono essere interrotte
	- attività regolari invece sono istantanee ed atomiche, non sono influenzate o interrotte da altri eventi

## Riepilogo
![[materie/anno_2025-2026/ingegneria_del_software/assets/attivita_interne.jpg]]
# Superstati

## Annidamento

>[!definition]
>Stato composto
>>Annidamento di stati permette di dettagliare il comportamento interno di uno stato tramite sottostati.

- stati composti che contengono un intero statechart diagram
- stati del diagramma contenuto sono chiamati sottostati
- sottostati possono condividere alcune transizioni e attività interne
- superstato raccoglie il comportamento comune dei suoi sottostati
## Transizioni tra superstati
- Quando gli archi sono diretti verso il superstato, in genere si intende che sono diretti verso il suo stato iniziale di default

# Stati concorrenti
- Uno stato può essere diviso in regioni che contengono sottostati eseguiti contemporaneamente
- regioni concorrenti separate da linee tratteggiate dentro al superstato
# Implementazione
1. Utilizzando una catena di switch nidificati
2. Applicando il Pattern State
3. Usando Tabelle di Stato
## Statechart da implementare

### Switch nidificati
- **Vantaggi**:
	- Soluzione più intuitiva
- **Svantaggi:**
	- Complessa da implementare: codice complesso anche per i casi abbastanza semplici
	- Necessità di gestire modifiche apportate in più punti del codice
### Pattern state
Statechart tradotto con:
- una **classe controller**: 
	- mantiene traccia dello stato corrente 
	- implementa un metodo di cambiamento di stato
	- inoltra le chiamate alle classi stato
- **classe di stato**: 
	- dichiara i metodi corrispondenti a ogni evento
	- implementa in modo che non facciano nulla
- **classi stato derivate** = stati del diagramma
	- implementano soltanto i metodi corrispondenti agli eventi scatenabili su quello stato per overriding

### Tabelle di stato
- Rappresentazione tabellare delle informazioni contenute nel diagramma
- La tabella: 
	- é direttamente interpretata a runtime da un apposito interprete 
	- può essere trasformata in codice da uno strumento di generazione automatica del codice

## Applicabilità
**Vantaggi**:
- i diagrammi di stato servono a descrivere il comportamento di un oggetto in più casi d'uso
- utili a rappresentare le classi con una logica interna complessa o particolarmente interessante
**Svantaggi:**
- non molto utili per descrivere la collaborazione tra più oggetti
- loro implementazione corrisponde a codice piuttosto ripetitivo
	- spesso si utilizzano generatori di codice automatici