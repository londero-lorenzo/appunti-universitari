---
title: "Diagramma delle Classi Avanzato"
aliases: ["Diagramma delle Classi Avanzato"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "diagramma-delle-classi-avanzato"]
created: 2025-11-19
---
## Dipendenza
- Dependency si rappresenta con una linea tratteggiata **unidirezionale**
	- termina con una freccia dall'oggetto dipendente (**client**) verso quello da cui dipende (**provider**)
- specifica i punti in cui modificare una classe fornitore potrebbe coinvolgerne altre
### Propagazione del cambiamento
- Finestra dei benefici non ha dipendenza diretta dalle **Gateway** dei dati
- **Non transitività delle dipendenze**

- si ha una dipendenza tra due classi se la modifica alla definizione della classe provider può causare un cambiamento alla classe client
- Esempi:
	- operazione del client invoca un'operazione del provider
	- il provider è il tipo di un attributo del client
	- il provider è un parametro o il tipo di ritorno 
### Tipologie di dipendenza
- << use >> : la sorgente (client) effettua un generico uso di qualcosa della destinazione (provider)
- << call >>: la sorgente (client) invoca un'operazione del provider
- << create >>: sorgente crea istanze della classe del provider

### Implicazioni delle dipendenze

# Interfacce e classi astratte
- Una classe astratta è una classe che non può essere direttamente istanziata
- ha **una o più operazioni astratte** (solo dichiarazione pubblica senza implementazione)
	- implementazione demandata alle **sottoclassi**
## Interfaccia
>[!definition]
>Interfaccia
>>Classe priva di implementazione (tutte le operazioni sono astratte)

# Vincoli
Si definiscono **tra parentesi graffe**:
- linguaggio naturale
- linguaggio di programmazione
- linguaggi formali specifici, come OCL
## Object Constraint Language
- **Contesto:** specifica l'elemento del modello UML a cui si applica
- **Regola**: specifica il tipo di vincolo
	- **inv:** invariante (deve essere sempre vero)
	- **pre:** precondizione (deve essere sempre vero prima dell'esecuzione di un'operazione della classe)
	- **post:** postcondizione
- **Espressione:** definisce il vincolo
>[!example]
>context < Contesto >
>< Regola >: < Espressione >

