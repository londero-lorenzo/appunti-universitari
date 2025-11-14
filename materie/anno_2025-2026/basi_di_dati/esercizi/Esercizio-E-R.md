---
title: Esercizio-E-R
aliases:
  - Esercizio-E-R
tags:
  - università
  - materie
  - anno-2025-2026
  - basi-di-dati
  - esercizi
created: 2025-11-13
---
## Testo
Testo dell'esercizio 3 preso da un esame passato del 04-09-19 :

Si vuole realizzare una base di dati per la gestione di informazioni circa un insieme di automobili caratterizzato
dal seguente insieme di requisiti.
+  Ogni automobile sia identificata univocamente dalla sua targa e sia caratterizzata da un modello, un anno di fabbricazione, un colore, un valore di mercato e uno o più proprietari. Fra le automobili, vogliamo tener traccia del sottoinsieme delle automobili storiche (un'auto si dice storica se sono trascorsi 25 o più anni dall'anno di fabbricazione), del sottoinsieme delle automobili sportive, caratterizzate dalla velocità massima, e del sottoinsieme delle auto storiche sportive.
+ Ogni modello sia caratterizzato da un nome, una casa costruttrice e una cilindrata. Il nome identifichi univocamente il modello all'interno dei modelli proposti dalla casa costruttrice (non si esclude la possibilità che case costruttrici diverse propongano modelli, ovviamente diversi, con lo stesso nome).
+ Ogni casa costruttrice sia identificata univocamente dal proprio nome e sia caratterizzata dall'anno di fondazione e da un insieme di stabilimenti. Una stessa persona possa essere presidente di più case costruttrici.
  Ogni stabilimento sia caratterizzato un nome, che lo identifica univocamente nell'ambito della casa costruttrice, una città ove ha sede e un numero di addetti.
Si definisca uno schema Entità-Relazioni che descriva il contenuto informativo del sistema, illustrando con chiarezza le eventuali assunzioni fatte. Lo schema dovrà essere completato con attributi ragionevoli per ciascuna entità (identificando le possibili chiavi) e relazione. Vanno specificati accuratamente i vincoli di cardinalità e partecipazione di ciascuna relazione. Si definiscano anche eventuali regole di gestione (regole di derivazione e vincoli di integrità) necessarie per codicare alcuni dei requisiti attesi del sistema.


## Schema Entità-Relazioni

Schema completo:

![[materie/anno_2025-2026/basi_di_dati/basi_dei_dati.excalidraw.md#^frame=a1Aq0SJv|100%]]
___

### Divisione in parti dello schema:

Relazione fondamentale:
![[materie/anno_2025-2026/basi_di_dati/assets/Immagine 2025-11-13 165726.png]]

Generalizzazione di automobile:
![[materie/anno_2025-2026/basi_di_dati/assets/Immagine 2025-11-13 170141.png|80%]]

Schema PROPRIETARIO:
![[materie/anno_2025-2026/basi_di_dati/assets/Immagine 2025-11-13 170329.png]]

Relazione tra MODELLO e CASA PRODUTTRICE:
![[materie/anno_2025-2026/basi_di_dati/assets/Immagine 2025-11-13 170622.png]]

Schema CASA PRODUTTRICE:
![[materie/anno_2025-2026/basi_di_dati/assets/Immagine 2025-11-13 170832.png]]
