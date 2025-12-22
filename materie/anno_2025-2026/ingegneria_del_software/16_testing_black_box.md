---
title: "16 Testing Black Box"
aliases: ["16 Testing Black Box"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "16-testing-black-box"]
created: 2025-12-22
---
>[!abstract] Conoscendo le specifiche funzionali, si progettano casi di test per dimostrare che ciascuna funzionalità è completamente operativa, ignorando i dettagli interni del software.

- Scatola nera = struttura interna non visibile
- quando non si ha accesso al codice sorgente
- esercita sistema inserendo input e osservando output
- sfrutta la conoscenza di:
	- interfaccia del sistema
	- documentazione, ad es. descrizione degli scenari
- **Non** tiene conto di:
	- codice sorgente
	- stato interno dell'applicazione

## Criteri di copertura per il testing black box
### Obiettivi
- copertura degli scenari di esecuzione definiti nei casi d'uso
- copertura delle funzionalità definite nella specifica dei requisiti
- capire quando è abbastanza
- uso criteri di adeguatezza
>[!warning] Problema è che lo spazio dei possibili input è molto ampio e quindi bisogna scegliere un sottoinsieme significativo.
>- richiede il giudizio di esperti di dominio

### Classi di equivalenza
>[!definition] Partizionamento in classi di equivalenza
>> In base ai requisiti del software testato, si suddivide lo spazio degli input in sottoinsiemi (**classi di equivalenza**)
>> Elementi si comporteranno allo stesso modo durante l'esecuzione.

- suddivisione in classi di equivalenza = partizione
- ogni intersezione tra classi è vuota
- i casi di test eseguiranno almeno un test per ogni classe di equivalenza
#### Suddivisione in classi di equivalenza
- anche lo spazio degli output può essere diviso in partizioni di equivalenza
- partizioni in cui il sistema avrà comportamento simile
- classe **Input validi**
- classe **Input non validi** (gestiti da eccezioni)
>[!example] Condizione sulle variabili di ingresso
> La variabile di input è valida se appartiene ad un intervallo di valori:
> - avremo input interni all'intervallo (validi)
> - input esterni all'intervallo (non validi)
> Dettagliando ancora la classe degli input non validi abbiamo:
> - una classe valida per valori interni all'intervallo
> - una classe non valida per valori inferiori al minimo 
> - una classe non valida per valori superiori al massimo

##### Intervallo di valori

>[!example] Se la variabile di input rappresenta il voto ad un esame ritenuto valido solo se nell'intervallo tra 18 e 30, consideriamo 3 classi di equivalenza (CE):
>- CE1 = {valori $\geq$ 18 e $\leq$ 30}
>- CE2 = {tutti i valori $<$ 18} (non validi)
>- CE3 = {tutti i valori $>$ 30} (non validi)
>Una possibile TS che copra tutte le classi di equivalenza ha 3 casi di test:
>- Input = {1,20,40} coprono tutte 3 le classi CE1, CE2, CE3

##### Insieme discreto
- se la variabile di input **valida** è un elemento di un insieme discreto avremo:
	- una classe valida per ogni elemento dell'insieme CE1, CE2, ..., CEn
	- una classe non valida per elementi non appartenenti all'insieme
##### Tipo booleano
- se la variabile di input è un elemento di tipo booleano avremo:
	- una classe CE1 valida costituita dall'elemento con valore `True`
	- una classe CE2 non valida costituita da un elemento con valore `False`

##### Tipo non valido
- nei casi precedenti si deve aggiungere anche un'altra classe non valida
- con elementi che non appartengono al tipo della variabile di input
- verifica se il programmatore ha effettuato gli opportuni controlli sul tipo di dato
>[!example] Se la variabile è di tipo intero, allora si consideri la classe (**non valida**) di valori di tipo carattere.

### Esercizio
Un metodo riceve in input una data composta da:
- Giorno: intero compreso tra 1 e 31
- Mese: stringa
- Anno: intero compreso tra 1900 e 2000
- Restituisce in output il giorno della settimana corrispondente: variabile numerica (1 = lunedi, ...)
- Selezionare i casi di test tramite partizione delle classi di equivalenza
- Consideriamo ogni variabile **separatamente:** giorno, mese, anno

#### Giorno
- Condizione di ingresso:
	- può essere compreso tra 1 e 31
- Classi di equivalenza
	- Valida
		- CE1: 1 $\leq$ Giorno $\leq$ 31
	- Non valida:
		- CE2: Giorno $<$ 1
		- CE3: Giorno $>$ 31
		- CE4: Giorno non intero
>[!warning] Stessa roba per gli altri input.
>

>[!warning] Fare una tabella che contenga tutte le informazioni del caso di test.

#### Tabella poco efficiente
![[materie/anno_2025-2026/ingegneria_del_software/assets/tabella_validazione_input.jpg]]
#### Tabella efficiente
![[materie/anno_2025-2026/ingegneria_del_software/assets/tabella_validazione_input_efficiente.jpg]]

#### Boundary Values
- programmatori fanno errori per valori di input vicini ai confini delle classi di equivalenza
- si deve testare il software anche con valori di input che coincidono ai valori limite delle classi di equivalenza
- non ci si limiterà a scegliere solo valori interni alla classe di equivalenza
- tale criterio si applica efficacemente a sottoinsieme di insieme continui
- per ogni estremo dell'intervallo, 1 CE per l'estremo e 2 CE per i valori sulla frontiera
- per l'anno (valore compreso tra 1900 e 2000)
	- 1899: valore leggermente inferiore dell’estremo inferiore dell’intervallo
	- 1900: estremo inferiore
	- 1901: valore leggermente superiore all’estremo inferiore
	- 1950: valore nominale
	- 1999: valore leggermente inferiore all’estremo superiore
	- 2000: estremo superiore
	- 2001: valore leggermente maggiore dell’estremo superiore

##### Problemi
- Non è possibile determinare a priori gli input per coprire le classi di equivalenza ma bisogna conoscere le precondizioni
>[!example] Per una variabile password:
>**Classi valide**:
>- CE1: password corrispondente a un utente con diritto di accesso
>**Classi non valide:**
>- CE2: password corrispondente a un utente che non ha diritto di accesso
>- CE3: password vuota
>Si deve specificare la **precondizione** in modo da tenere conto di quale password corrisponde a un utente con diritto di accesso.

# White Box
>[!abstract] Conoscendo il funzionamento interno dei vari componenti del software, si progettano casi di test per verificare che meccanismi interni funzionino bene, cioè che le operazioni interne siano svolte correttamente.

## Testing strutturale
- Utilizzare la struttura interna del software per ricavare i dati di test
**Differenze dalle black box**
- possono fornire maggiori informazioni al debugger sulla posizione dell'errore
- complementa il testing black box: le "parti" di programma non testate dal testing black box potrebbero contenere errori
## Rappresentazione grafica del codice tramite CFG
**Control Flow Graph**: rappresenta la struttura di un programma P
Grafo orientato che rappresenta il trasferimento del flusso di controllo tra blocchi di istruzioni del programma

- **nodo**: un blocco di una o più istruzioni
- **arco:** trasferimento del flusso di controllo tra la coppia di nodi che esso collega
- CFG ha sempre due nodi speciali: ingresso e uscita
- Nodi possono appartenere a uno dei due insiemi disgiunti:
	- **Nodi istruzione:** hanno un solo arco uscente
	- **Nodi predicato:** corrispondono a condizioni
		- hanno due archi uscenti etichettati con Vero o Falso
		- più archi uscenti nel caso di switch-case

### Criteri di copertura del flusso di controllo
- adozione di metodi di Copertura degli oggetti che compongono la struttura dei programmi
- definire un insieme di test aventi dati in input in grado di **coprire** tutti i componenti di interesse del software almeno una volta durante l'esecuzione dei test case
- in base ai criteri di copertura del CFG, possiamo avere diversi tipi di coverage testing

#### Statement coverage
- richiede di coprire tutti i nodi del CFG durante il testing
- eseguire tutte le istruzioni dà una **debole garanzia** di scoprire i difetti
- semplice da soddisfare
- non assicura di coprire sia il ramo `true` che `false` delle decisioni
#### Decision coverage
- richiede che ogni arco sia attraversato almeno una volta
- ogni decisione nel programma deve assumere valore `true` e `false` durante il testing
- limite legato alle decisioni in cui sono valutate più condizioni (legate da AND e OR)

### Decisioni e condizioni
**Decisione:** predicato di un if o while, for (x > 0 || y > 0)
**Condizione:** espressione atomica booleana che appare in una decisione (x > 0) e (y > 0) prese singolarmente

#### Copertura delle condizioni:
##### Condition coverage
- ciascuna condizione dei nodi decisione di un CFG deve essere valutata sia per valori `true` che `false`
- bisogna assicurare che entrambe le condizioni assumano sia valori true che false

`if ((x>=0) && (x<=200))`
- TS1={5,; -5} garantisce solo copertura decisioni
- TS2={-3; 210} garantisce solo copertura condizioni
>[!warning] La copertura delle condizioni non sempre implica la copertura delle decisioni.

- Criterio più forte perché assicura che i casi di test coprano tutte le condizioni ma anche tutte le decisioni.
- TS3={-3; 10; 210} garantisce copertura sia delle decisioni che delle condizioni