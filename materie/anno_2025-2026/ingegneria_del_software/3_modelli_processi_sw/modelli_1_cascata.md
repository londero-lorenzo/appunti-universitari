---
title: "Modelli 1 Cascata"
aliases: ["Modelli 1 Cascata"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "3-modelli-processi-sw", "modelli-1-cascata"]
created: 2025-10-20
---
# Modello a cascata
>[!definition]
>**Plan-driven**:
>>+ ciascuna fase segue quella precedente
>>+ pianificare in **anticipo** le attività di processo prima di iniziare lo **sviluppo del software**
>>+ **output** di una fase sono gli **input** della successiva
>>+ fasi del modello a cascata **riflettono** direttamente le **attività di sviluppo fondamentali** del software

**Document-centric**: produzione di documentazione
+ risultato di ogni fase costituito da uno o più **documenti approvati**
+ fase successiva non parte finché **quella precedente non sia finita** e i relativi **documenti completati e approvati**
**Rigido**:
+ prodotti di una fase vengono:
	+ "**congelati**" 
	+ **non sono più modificabili** se non innescando un processo formale e sistematico di modifica
+ **fine di ogni fase** è un punto rilevante del processo (*milestone*)
+ definizione precisa di **milestone** e **output** è importante per **misurare il progresso di un progetto**
**Monolitico**:
+ cliente vede il software **solo al completamento di tutte le fasi**
+ se si commette un **errore** nei requisiti **viene rilevato solo alla fine** (costi elevati)
+ **processi non lineari**: ciascuna fase **scambia feedback** con le altre

### **Vantaggi**:
+ fasi ben definite
+ **output** di ciascuna fase sono **precisamente individuati**
### **Svantaggi**:
+ richiede **conoscenza immediata e stabilità dei requisiti**
	+ Difficile avere requisiti congelati all'inizio del progetto, spesso poco chiari anche al cliente
+ sviluppo di **eccessiva documentazione**
+ **poco flessibile**: difficile gestire **necessità di modifiche** che emergono durante l'**esecuzione del processo**, ad es. nuove richieste del cliente
>[!tip]
>+ Adatto a software che richiedono una **documentazione dettagliata** (sistemi critici o grossi sistemi sviluppati da più società)
>+ adatto a **sistemi integrati** in cui il software deve interfacciarsi con **sistemi hardware non flessibili**

## Modello a cascata con retroazione

![[materie/anno_2025-2026/ingegneria_del_software/assets/modellocascataretroazione.jpg]]
>[!tip]
>Introduce dei **feedback** in ogni fase in modo da rilevare errori prima della successiva

+ **Mitiga la monoliticità** del modello a cascata tradizionale:
	+ non si deve aspettare il termine del processo per modificare il prodotto
+ **Non è completamente flessibile** rispetto a cambiamenti che possono avvenire in qualunque momento del processo
+ Modello utile quando si prevede che il sistema sarà **poco soggetto a cambiamenti**

## Modello a V
![[materie/anno_2025-2026/ingegneria_del_software/assets/modello_v.jpg]]
+ Attività del **ramo superiore** (**progetto**) sono collegate a quelle del **ramo inferiore** (**V&V**)
+ il team definisce il corrispondente **piano di test** della fase di V&V
+ V&V guidato da un **insieme di piani di test**: eseguito da un **team indipendente** da quello di sviluppo
+ Se si trova un errore in fase di V&V si rieseguono le fasi di processo collegate 
+ può **anticipare la validazione** **dei requisiti** da parte del cliente e quindi garantire il rilevamento precoce di eventuali errori

>[!example]
>Sviluppo Electronic Control Unit in ambito automotive
![[materie/anno_2025-2026/ingegneria_del_software/assets/esempio_modello_v.jpg]]
