---
title: "21-Controlli-Ridondanza-Aggregazione"
aliases: ["21-Controlli-Ridondanza-Aggregazione"]
tags: [università, "materie", "anno-2025-2026", "social-computing", "21-Controlli-Ridondanza-Aggregazione"]
created: 2025-12-15
---
## Tecniche per migliorare la qualità

+ Metodologiche (già viste): Pairwise, scale,...
+ Controlli in itinere
+ Ridondanza e aggregazione
+ Ex-post (dopo l'esecuzione dell'esperimento)

### Controlli in itinere
**Design del task**: scegliere la giusta modalità di presentazione (uso colori, paginazione, ecc...)
+ L'atteggiamento deve essere duplice: semplificare il task il più possibile, ma inserire anche dei controlli per tenere d'occhio i comportamenti dei worker

Pe i controlli ci sono varie tecniche:
+ Test di qualificazione 
	+ prima del task il worker deve superare un test
	+ Obiettivo: selezionare worker effettivamente motivati che cercano di superare il qualification test
	+ Due possibilità: Da una piattaforma (mturk) oppure interno al task stesso
+ Controlli sintattici (parsing)
	+ Evitare risposte non date o campi vuoti (ad esempio un radio button che richiede una risposta obbligatoria)
	+ Conteggio dei caratteri/parole (mettere magari un minimo di parole)
	+ Verificare esistenza di URL inseriti dall'utente
	+ Blacklist di termini (per le bestemmie e cose così)
	+ Controllo copia-incolla (risposte uguali in più sezioni diverse)
	+ Controllo anti plagio
+ Test nascosti
	+ All'interno del task mettere delle domande per misurare la qualità del worker (solitamente domande estremamente semplici impossibili da sbagliare)
	+ Per i task di raccolta di opinioni è più complicata la faccenda. In questi casi si fanno magari due domande di cui si sa la risposta e vedere cosa risponde il worker (es. "più alto l'everest o il monte bianco?" e poi "più alto il monte bianco o l'everest?" e vedere se il worker risponde coerentemente a tutte e due)
+ Monitoraggio dei tempi
	+ Cutoff sul tempo totale (se il worker va troppo veloce non va bene)
	+ Anche per le soglie superiori (worker troppo lento, è distratto)
+ Monitoraggio azioni
	+ Verificare i spostamenti del mouse
	+ Scrolling (es. se per leggere un testo bisogna scrollare uno slider e l'utente non lo fa vuol dire che non sta leggendo quel testo)
	+ Monitorare l'ordine di inserimento dei dati

>[!question] Come usare i controlli in itinere?
>Se la qualità del worker è bassa, posso decidere di scartarlo (magari anche bloccarlo per il futuro o decidere di non pagarlo) o farlo pesare di meno in base alla qualità rilevata.

---
### Controlli ex-post

Posso anche valutare il worker alla fine dell'esecuzione del lavoro, analizzando in post quello che ha fatto (anche con analisi più sofisticate di quelle fatte online durante il task) e potendo quindi decidere di:
+ Non usare i dati
+ Non accettarli
+ Bloccarlo o non pagarlo
Le analisi più sofisticate che non posso inserire dentro a ciascun task ad esempio possono consistere in:
+ Usare le risposte degli altri worker allo stesso task
+ Usare le risposte di tutti i worker a tutte le task
+ Analisi manuale dei testi o delle risposte

>[!tip]
>L'attitudine del requester deve essere quella di massimizzare i dati buon da utilizzare, quindi non limitarsi a dividere binariamente in perfetto/sbagliato. Porre un "tipping point", una soglia oltre la quale la qualità è considerata "abbastanza".

---

### Ridondanza & Aggregazione

+ Raccogliere più risposte alla stessa domanda per più volte
+ Aggregare le risposte in un unico valore con qualche funzione di aggregazione (media, mediana, moda, ...) 

**Qualità:**
+ Individuale: risposta del singolo worker
+ Aggregata: risposte a un task
	+ Ridondanza: più worker fanno lo stesso task

>[!example]
>Per valutare la rilevanza di un documento si aggrega tutte le risposte dei worker e un oracolo ci dice quel è il valore corretto tramite il valore aggregato.

#### Notazione e funzioni di aggregazione

Leggiti le merdo-merda di slide dalla 36 alla 41


>[!example]
>Nell'esempio di prima sulla rilevanza dei documenti pongo 1 al posto di Relevant e 0 al posto di Not relevant. 
>+ Svolgo poi l'aggregazione attraverso la moda. Ottengo così dei valori ammissibili ma perdo informazione (se ad esempio in una colonna tutti dicono 1 ma in un'altra 51 dicono 1 e 49 dicono 0; il valore di aggregazione delle due colonne sarà però sempre 1)
>+ Provo allora ad aggregare utilizzando la media. Ottengo valori non ammissibili (diversi da solo 1 e solo 0) ma perdo meno informazione (tiene conto del numero di valori di 1 e 0).
>+ Non è così scontato capire cosa fare

