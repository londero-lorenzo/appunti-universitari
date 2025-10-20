---
title: "Modelli 2 Evolutivi"
aliases: ["Modelli 2 Evolutivi"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "3-modelli-processi-sw", "modelli-2-evolutivi"]
created: 2025-10-20
---
# Modelli Evolutivi
Modelli adatti a contesti in cui i requisiti non sono chiari fin dall'inizio del processo:

## Modello a sviluppo/consegna incrementale

>[!definition]
>>Lavorare con il cliente per esaminare i requisiti iniziali e farli evolvere fino al sistema finale.

### Caratteristiche
Sviluppare un'implementazione iniziale:
+ esporla agli utenti
+ perfezionarla con versioni successive (**incrementi**) ----> finché non si ottiene il sistema richiesto
![modellosviluppoincrementale](/materie/anno_2025-2026/ingegneria_del_software/assets/modellosviluppoincrementale.svg)

#### Descrizione sommaria
Parte da pochi requisiti **ben compresi** o da una descrizione sommaria

#### Specifica, sviluppo e convalida
Attività di specifica, sviluppo e convalida sono intrecciate anziché separate ---> feedback veloci tra le varie attività
#### Versione iniziale
+ Versione iniziale che implementa i requisiti fondamentali è esposta agli utenti
+ Più facile dare un **feedback** su una versione iniziale (**demo**) piuttosto che su documenti
#### Versioni intermedie
+ Ulteriori funzionalità e requisiti (es. proposti dal cliente) implementati in versioni intermedie successive
+ Le versioni intermedie non sono **solitamente** mostrate al cliente
#### Versioni finale
+ **Ultimo incremento** = versione finale rilasciata al cliente
+ **Versione finale** = **evoluzione** della versione iniziale

### Modello a consegna incrementale

>[!definition]
>>Sistema non è consegnato direttamente nella sua forma finale alla fine del progetto. 
>>Alcuni degli incrementi sviluppati sono consegnati ai clienti e installati nel loro ambiente operativo.

+ **Vantaggio:** cliente usa l'incremento nell'ambiente operativo reale ---> **feedback più realistico**
+ **Limitazione:** gli utenti devono avere tempo sufficiente per **sperimentare** ciascun incremento

#### Caratteristiche
+ Ogni incremento rilascia parte delle funzionalità richieste + quelle precedenti
+ ai requisiti utente vengono assegnati **livelli di priorità**
	+ requisiti a priorità maggiore rilasciati per primi
+ requisiti di un incremento sono "congelati" (**non possono essere modificati**) dopo che tale incremento è stato consegnato
	+ gli altri requisiti possono evolvere


![modelloconsegnaincrementale](/materie/anno_2025-2026/ingegneria_del_software/assets/modelloconsegnaincrementale.svg)

+ Funzionalità comuni a più requisiti dovrebbero essere individuate tempestivamente e implementate all'inizio del processo (**integration test**)
	+ convalida da esterno ----> appena sviluppo mando all'utente esterno per ricevere un feedback
#### Esempio di modello a consegna incrementale Plan-Driven
>[!example]
>Requisiti: R1, R2, R3
>Architettura: M1, M2, M3, M4
>Pianificazione: 3 incrementi
>
>Iterazione 1
>R1, richiede M1, M2
>Sviluppare e integrare M1, M2
>Consegnare R1
>
>Iterazione 2
>R2, richiede M1, M3
>Sviluppare M3, integrare M1, M2, M3
>Consegnare R1+R2
>
>Iterazione 3
>R3, richiede M3, M4
>Sviluppare M4, integrare M1, M2, M3, M4
>Consegnare R1+R2+R3

#### Sviluppo incrementale vs Consegna incrementale
##### Sviluppo incrementale:
+ valutazione della prima versione effettuata da un **proxy** degli utenti finali in ambiente operativo diverso da quello target
>[!warning]
>Versioni intermedie non sono solitamente rilasciate al cliente

##### Consegna incrementale:
+ valutazione più realistica dell'utilizzo reale del software 
>[!warning]
>Ciascun incremento può essere rilasciato agli utenti finali nell'ambiente operativo del sistema.

#### Vantaggi
+ rapido feedback del cliente su **versione preliminare del software** invece che documenti di progetto
+ possibilità di far cambiare i requisiti prima della consegna finale del prodotto ----> **riduco i costi di modifica**
+ consegnare versioni preliminari: **funzionalità fondamentali sono già implementate**
+ primi incrementi utilizzati per **dedurre requisiti** per incrementi successivi
+ funzionalità con **priorità più elevata** testate più approfonditamente
#### Problemi
+ mancanza di visibilità del processo (**antieconomico documentare ogni versione del sistema**)
+ sistemi diventano spesso mal strutturati per i **continui cambiamenti**
#### Applicabilità
+ Componenti di piccole e medie dimensioni (es. interfaccia utente)
+ Sistemi destinati a vita breve
+ Sistemi i cui requisiti è probabile che cambiano durante lo sviluppo

![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw#^frame=JOyRGJyA]]

## Modello Prototipale

**Prototipo:** versione inziale di un sistema software o parte di esso.

>[!definition]
>>Finalizzato a comprendere i requisiti di sistema.
>>Da **requisiti poco chiari** -----> a prototipi per esplorare i requisiti e chiarirli.
>>Sviluppato rapidamente per:
>>	 - contenere i costi
>>	 - **sperimentare** con il cliente prima della consegna (fasi iniziali del processo)

### Caratteristiche
+ **Usa e getta**: deve essere **scaricato** dopo la sua validazione poiché non è una buona base per sviluppare sistema finale
+ Pur realizzando le funzionalità richieste potrebbe non rispettare aspetti come:
	+ le **prestazioni**
	+ il **rispetto** di standard aziendali
+ potrebbe non essere **documentato** in modo appropriato
+ rapidità dello sviluppo ed i frequenti cambiamenti potrebbero **deteriorarne l'efficacia**

![modelloprototipale](/materie/anno_2025-2026/ingegneria_del_software/assets/modelloprototipale.svg)

### Stabilire gli obiettivi del prototipo: piano di prototipazione

>[!warning]
>Bisogna stabilire **esplicitamente** gli obiettivi del prototipo all'**inizio** del processo.

+ Se gli obiettivi non sono espliciti o chiari:
	+ il management o utenti finali possono fraintendere la funzione del prototipo e la prototipazione risulta inefficace
### Definire le funzionalità del prototipo

+ Non tutte le funzionalità del sistema finale devono essere incluse nel prototipo (**ridurre** i costi di prototipazione)
>[!example]
>Il prototipo può focalizzarsi su aree ancora non comprese bene.
### Valutazione del prototipo
+ Formazione utenti sull'utilizzo di ciascun prototipo **prima di valutarlo**.
+ Problema della rappresentatività:
	+ prototipo non è parte del sistema reale (a differenza degli incrementi)
	+ valutatori potrebbero essere **non rappresentativi** degli utenti finali
	+ modo di usare il prototipo **varia** dall'utilizzo del sistema reale

>[!tip] Modello prototipale
>Molto utile nei vari modelli di sviluppo (si può integrare).
>Può essere usato per identificare, validare e raffinare i requisiti.

![modelloprototipale2](/materie/anno_2025-2026/ingegneria_del_software/assets/modelloprototipale2.svg)
>[!tip]
>Prototipazione può essere combinata con altri cicli di vita classici.

>[!example]
>Può essere usato per identificare, validare e raffinare i requisiti.

![modelloprototipale3](/materie/anno_2025-2026/ingegneria_del_software/assets/modelloprototipale3.svg)

>[!tip]
>Durante la fase di progettazione in un modello cascata: prototipazione può essere usata per valutare opzioni alternative nella progettazione.

### Back to back testing

![backtobacktesting](/materie/anno_2025-2026/ingegneria_del_software/assets/backtobacktesting.svg)

Prototipo può essere utilizzato nella fase di **Validazione** per:
+ controllare che il sistema sviluppato si **comporti come modellato** nel prototipo nella fasi iniziali del progetto.