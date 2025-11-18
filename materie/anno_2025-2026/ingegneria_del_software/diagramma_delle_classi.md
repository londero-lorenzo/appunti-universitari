---
title: "Diagramma delle Classi"
aliases: ["Diagramma delle Classi"]
tags: [università, "materie", "anno-2025-2026", "ingegneria-del-software", "diagramma-delle-classi"]
created: 2025-11-08
---
# Diagramma UML delle classi
- Diagramma **strutturale**
- mostra una visita **statica** del modello
	- l'organizzazione del progetto del sistema
	- **non mostra informazioni temporali**
- i suoi elementi corrispondo a concetti del paradigma object-oriented
## Rappresenta
- Tipi di **oggetti** (le classi) del sistema che corrispondono alle entità che esistono nel sistema
- relazioni **statiche** tra classi e vincoli che si applicano a tali relazioni
- caratteristiche delle classi: **proprietà** e **responsabilità**
Proprietà = attributi
Responsabilità = metodi

## Nel processo software
- utilizzato nella fase di definizione dei requisiti
- consente una vista concettuale delle **entità** nel dominio del problema
- cattura i concetti principali del dominio
- fissa i **confini del sistema**
- modello architetturale per capire **cosa fa** il sistema non come lo fa
- può essere usato in fase di **progettazione**
- identifica **entità** del sistema e le relazioni tra esse
- **prescinde dall'implementazione**
- identifica le **classi** del software e le relazioni tra esse
- corrisponde alla **reale struttura del software** dato che ne modella l'implementazione object-oriented
---
# Sintassi
## Classe
>[!definition]
>Classe
>>Descrittore di un insieme di oggetti con le **stesse proprietà** (attributi), **comportamento** (operazioni) e **relazioni** tra oggetti.

- ogni oggetto è un'istanza di una sola classe
- in un certo istante un oggetto ha uno specifico stato
- in base al proprio stato due oggetti possono rispondere diversamente alla stessa operazione
>[!example]
>Se si cerca di prelevare 100 euro da un oggetto conto corrente, il risultato sarà diverso a seconda della disponibilità.

### Rappresentazione
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=shRMvAv2]]
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=mdOrslqT|100%]]

## Attributi
### Visibilità
- **+ pubblico**: accesso esteso a tutte le altre classi
- **# protetto**: l'accesso è consentito soltanto alle classi che derivano dalla classe originale
- **- privato**: solo la classe originale può accedere

![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=1IaPJvLZ]]
### Nome e tipo
- **nome**: unico parametro obbligatorio
- **tipo**:
	- primitivo (int, double, char, ecc...)
	- **nome di una classe** definita nello stesso diagramma (attributo può essere indicato con un'**associazione**)
	- definisce un vincolo sugli oggetti che possono corrispondere all'attributo
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=WlKdzycI]]
### Molteplicità
>[!definition]
>>Quantitativo degli attributi di un certo tipo: array o matrici (valore default = 1)
- numero minimo e massimo racchiusi tra []
	- [1..1] o [1] = 1
	- [0..1] al più uno
	- [0..* ] numero imprecisato
	- [1.. * ] almeno 1
- elementi di una molteplicità a più valori sono considerati come un **insieme**
- Notazione **{ordered}**: se dotati di ordine
- Notazione **{nonunique}**: se sono possibili valori duplicati

### Valore di default e proprietà
>[!definition]
>>Valore assegnato all'attributo di default se nessun valore viene specificato durante la creazione

>[!definition]
>{**proprietà**} 
>>Indica caratteristiche aggiuntive dell'attributo (es. la sola lettura)

![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=lP42dWQG]]
## Operazioni
`visibilità nome(listaParametri): tipoRestituito{proprietà}`
- Sono i **metodi** di una classe
- operazioni invocabili sugli oggetti istanza della classe
- **azioni** che possono essere svolte da una classe di oggetti
- nei diagrammi non sono riportate le operazioni che si occupano soltanto di **modificare gli attributi** dato che sono **facilmente deducibili**
### Caratteristiche
- **visibilità** e **nome** analoghi agli attributi
- **tipoRestituito** è il tipo del valore di ritorno
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=EWPG1ykT]]
- **listaParametri**: nome e tipo dei parametri nella forma
	- direzione nome parametro: tipo = valoreDefault
	- **direzione**:
		- input (in) ---> valore default
		- output (out)
		- entrambi (inout)
>[!example]
>- +saldoAllaData(in giorno: Date): float
## Responsabilità
- Nei diagrammi concettuali non si inseriscono i metodi perché rappresenterebbero un elemento del dominio della soluzione
- si possono usare le **responsabilità**: insieme di funzioni principali che la classe dovrebbe garantire, utili per controllare la completezza del modello di dominio
- riportate come stringhe di commento precedute da "--" nel riquadro operazioni
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=j6eZzVcb|100%]]
## Note e testo descrittivo
- commenti aggiuntivi in linguaggio naturale
- come commento in linguaggio di programmazione
- collegati tramite linea tratteggiata o fluttuare senza collegamenti

![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=izunGbZk]]
# Relazione tra classi
- Relazione di **associazione**
- Relazione di **generalizzazione-specializzazione**
- Relazione di **contenimento**

## Associazioni
- associazione tra due classi esprime una relazione tra le istanze delle classi
- Caratterizzata da:
	- **nome**: esprime il legame semantico tra le classi associate
	- **ruolo** giocato da ciascuna delle parti associate
	- **molteplicità** dell'associazione
	- **verso di navigazione** dell'associazione
>[!example]
>Ogni Automobile ha per proprietario una Persona.

![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=r3Dt5HUv]]
#### Nome
- Etichetta dell'associazione (verbo)
- permette di formare frasi di senso compiuto ("Una persona possiede un'automobile")
- Specificare la direzione dell'associazione (con < o >)

#### Ruolo
- si può specificare il **ruolo** che gli oggetti di una classe rivestono quando sono collegati da istanze dell'associazione
- usato spesso in **alternativa** al nome
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=jwXzzpND|100%]]
>[!example]
>- Persona è dipendente dell'Azienda
>- L'Azienda è datore di lavoro della Persona
#### Ruoli e nomi
- non tutte le associazioni necessitano di un nome: assegnare solo se **migliora la chiarezza** e **la comprensione** del modello
- evitare nomi generici tipo "has" o "is related to"
- quando due classi sono coinvolte in associazioni diverse tra le stesse classi è opportuno riportare un nome dell'associazione o il **ruolo** delle classi nelle diverse associazioni
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=RKo3nmgc|100%]]

### Molteplicità
>[!definition]
>>Vincola il numero di oggetti di una classe che possono partecipare ad una associazione in ogni istante.

Sono riportate sull'estremità dell'associazione prossima alla classe nella forma: **minimo..massimo**

| **0..1** | Zero (partecipazione opzionale) o uno   |
| -------- | --------------------------------------- |
| **1**    | Esattamente 1                           |
| **0..*** | Zero o più (non c'è limite superiore)   |
| **1..*** | Uno (partecipazione obbligatoria) o più |
| **1..6** | Da 1 a 6                                |

#### Esempi
>[!example]
>Ciascun badge è utilizzato per identificare uno e un solo studente.

- uno studente ha molteplicità 1 nell'associazione
- Non è specificato ciascuno studente quanti badge può possedere. Se ipotizziamo 1, abbiamo un'associazione 1 a 1
- **Uno a uno**: uno studente può possedere un solo badge in un dato istante. Un badge è posseduto da un solo studente.
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=Pjkr08EX|70%]]
- Se ad esempio vogliamo modellare il caso di smarrimento o di attesa di rilascio dopo la prima iscrizione 
- **Uno ad al più uno (0..1)**: uno studente può possedere nessuno o al massimo un solo badge in un dato istante.
	- Un badge è posseduto da un solo studente.

![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=HtHekQU5|70%]]

>[!example]
>Una persona possiede almeno un'Automobile.
>Un'Automobile può essere posseduta da una e una sola Persona.

- Le persone che non possiedono Automobile non fanno parte del problema
- Non è nel problema in oggetto il mantenimento di info riguardo i proprietari di automobili di seconda, terza mano, ecc...
**Associazione uno a molti**: una persona, una o più automobili
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=UzLxSixW|70%]]

>[!example]
>Uno Studente può conseguire più Esami. Ciascun Esame può essere conseguito da più Studenti.

- uno studente può conseguire potenzialmente illimitati esami
- un esame può essere conseguito da un numero non limitato di studenti
- possono esserci studenti che non hanno conseguito esami
- possono esserci esami non conseguiti da alcuno studente
**Associazione molti a molti**: molti studenti, molti esami
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=24LAooXk|70%]]

- se in alternativa avessimo voluto considerare il caso in cui uno studente era considerato dal sistema soltanto dal momento del conseguimento del primo esame avremmo avuto che la molteplicità di Esame 1..* poiché lo studente deve aver conseguito almeno un esame:
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=qHYEwyyd|70%]]

>[!example]
>Una prenotazione si riferisce sempre ad uno e un solo passeggero. 
>Un Passeggero può avere più Prenotazioni. 
>Una Prenotazione si riferisce ad un Volo. 
>Un Volo può avere più Passeggeri prenotati.

- prima di creare una prenotazione **devono esistere** passeggero e volo
- il passeggero può essere memorizzato nel sistema anche prima di effettuare una prenotazione: ci possono essere passeggeri senza prenotazione
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=FfDaFLbq|100%]]
#### Molteplicità discontinue

- UML 1 consentiva molteplicità discontinue come 2,4
- UML 2 ha eliminato le molteplicità discontinue
#### Molteplicità predefinita
- La molteplicità predefinita di un attributo è [1] nel meta-modello
- in un diagramma UML un attributo senza molteplicità non indica automaticamente [1] poiché la molteplicità potrebbe essere nascosta
- se la molteplicità [1] è importante, indicala esplicitamente per evitare ambiguità
### Verso di navigazione
- Se un'associazione non ha verso di percorrenza: se A è legato a B, B è legato ad A
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=s4vimkmC|100%]]
- Se specificata con una **freccia**:
	- direzionalità attribuisce alla classe origine del verso di percorrenza la responsabilità di tenere traccia dell'associazione
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=IC5521g7|100%]]

- in questo diagramma, da una persona è possibile sapere quali sono le auto che possiede
- considerata un'istanza di automobile non è possibile conoscere il possessore
>[!tip]
>Tale informazione è utile soprattutto nel **progetto di dettaglio**, rispecchiando una scelta di progetto. Non è presente nei **progetti concettuali**.

![[materie/anno_2025-2026/ingegneria_del_software/assets/verso_navigazione_uml2.jpg]]
>[!warning]
>Usare i nomi dell'associazione **oppure** i ruoli. Usarli insieme sarebbe ridondante e appesantirebbe il diagramma.

## Associazioni VS attributi
- Caratteristiche strutturali di una classe possono essere rappresentate come:
	- associazioni di una classe
	- attributi di una classe
- associazioni possono riportare anche le **molteplicità di entrambe le classi** ma sono **meno compatte**
- progettista deve scegliere le entità che hanno maggiore importanza e rappresentarle come classi per dar loro più enfasi
- non appesantire il diagramma con troppe **associazioni 1 a 1**
- si possono usare **attributi** per concetti secondari
- usare **associazioni** per classi più significative
- scelta dipende da cosa si vuole enfatizzare nel diagramma
![[materie/anno_2025-2026/ingegneria_del_software/assets/associazioni_vs_attributi.jpg]]
## Implementazione delle associazioni
- Nei linguaggi Object-Oriented associazione o attributo di un'entità corrispondono a un attributo di una classe (o getter o setter)
- Se definito verso di navigazione, la classe origine ha un attributo con:
	- Nome: il ruolo della destinazione
	- Tipo: la classe destinazione
	- Molteplicità: la molteplicità della destinazione
```
public Class Ordine{
	private LineaDOrdine[] elementiLinea;
}
```

![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=VkvKvJ6P]]
### Implementazione delle associazioni uno a molti
- Classe Persona ha un attributo vettore di Automobili
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=IC5521g7|100%]]
- La classe Automobile ha un attributo Persona
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=5iZrX81P|100%]]
- Entrambe: tutte e due le classi permettono di navigare l'altra classe dell'associazione
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=s4vimkmC|100%]]
- Persona ha un attributo automobili di tipo Automobile con molteplicità [1..*]
- Automobile ha un attributo proprietario di tipo Persona con molteplicità[1]
![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=DYTvOgc9|100%]]
## Esempi codifica in Java

### Associazione bidirez. Uno a Uno
![[materie/anno_2025-2026/ingegneria_del_software/assets/java_uno_a_uno.jpg]]
### Uno a uno caso generico
![[materie/anno_2025-2026/ingegneria_del_software/assets/java_uno_a_uno_generico.jpg]]
### Uno a molti
![[materie/anno_2025-2026/ingegneria_del_software/assets/java_uno_a_molti.jpg]]
### Uno a molti generico
![[materie/anno_2025-2026/ingegneria_del_software/assets/java_uno_a_molti_generico.jpg]]

# Costruzione del diagramma delle classi
>[!definition]
>System domain model
>> Modella le entità del dominio del problema che saranno presenti nel sistema (**dati di interesse**)
>> Possono contenere le responsabilità delle classi (**opzionale**)

>[!definition]
>System model
>> Include anche le classi che saranno usate per costruire il sistema completo:
>> - classi per l'interfaccia utente (menu)
>> - classi associate a parti dell'architettura (client, server, file, database)
>> - classi di utilità
>> Contiene metodi e informazioni sulla navigabilità

## Costruzione del System domain model
1. Identificare un primo insieme di **classi candidate**
2. Aggiungi **associazioni** ed **attributi** a queste classi
3. Trova le **generalizzazioni**
4. Trova le principali **responsabilità** di ogni classe
5. Itera il processo finché il modello ottenuto è soddisfacente

### 1. Identifica le classi
>[!question] Quali sono le classi che fanno parte del dominio ?

- Classi devono corrispondere a entità del dominio del problema
- Applicare concetti generali di modellazione Object Oriented: una classe identifica un tipo di dato astratto
#### Esempio buona classe
- Nome che rispecchia l'intento
- Astrazione che modella un elemento del dominio del problema
- Insieme ridotto e ben definito di responsabilità
![[materie/anno_2025-2026/ingegneria_del_software/assets/identifica_classi.jpg]]
#### Analisi dei nomi
- Tecnica per scoprire le classi del dominio
	1. Analizza la **documentazione** di partenza
	2. Elenca i nomi
	3. Elimina nomi:
		- ridondanti
		- rappresentano o caratterizzano istanze e non classi
		- sono vaghi, generici
		- corrispondono a classi che non sono necessarie a livello considerato
>[!example]
>Il sistema consente a un utente di aprire un conto corrente, diventandone il titolare.
>Il titolare può consultare il proprio saldo attuale.

##### Sostantivi
- **Classe**: indica un insieme di elementi distinti (*ContoCorrente*)
- **Attributo:** indica una proprietà di un elemento di un insieme (*Saldo*)
- **Ruolo:** indica il ruolo che un'istanza di una classe assume quando la si considera come parte di un legame con altri oggetti (*La Persona che ha aperto un ContoCorrente ne diventa il <U>titolare</U>*)

##### Esempio Analisi dei nomi
- Il **sistema** consente agli **utenti** di cercare **libri** per **titolo**, **autore** e **genere**.
- Gli **utenti** possono prendere in prestito e restituire **libri**.
- Gli **amministratori** del sistema possono aggiungere, modificare e rimuovere libri dal **catalogo**.
- Il **sistema** traccia lo stato di disponibilità di ciascun **libro**.
- Gli **utenti** possono iscriversi al **sistema**, creare un **profilo** e accedere alla **lista** dei **libri** in prestito.
**Elenco nomi:**
- Sistema: identifica l'intero sistema e non classi interne ad esso
- Utente
- Libro
- Titolo: attributo
- Autore: attributo
- Genere: attributo
- Catalogo
- Amministratore
- Profilo
- Cronologia
- Lista dei libri in prestito: attributo del profilo utente

>[!warning]
>Profilo e utente sono ridondanti quindi facciamo un'unica classe ProfiloUtente
 
- Gli amministratori del sistema possono aggiungere, modificare e rimuovere libri dal **catalogo**.
- Gli utenti possono iscriversi al sistema, creare un **profilo** e accedere alla **lista** dei **libri** in prestito.
>[!warning] Errore nel considerare il sistema e tutti gli utenti come se fossero classi.

- Attenzione a classi nel domain model che rappresentano tipi di utente o altri attori
- Includere tali classi solo se occorre manipolare o salvare loro informazioni (ProfiloUtente) altrimenti sono esterni al sistema (Amministratore)

### 2. Identifica Attributi
>[!abstract] Il sistema consente agli utenti di cercare libri per **titolo**, **autore** e **genere**.

- cercare le informazioni che devono essere conservate per ciascuna classe
- è possibile che nomi che sono stati scartati come classi al passo 1 possano essere considerati attributi
	- nel nostro esempio, titolo, autore e genere sono attributi di libro di tipo stringa
- una classe **non dovrebbe** avere troppi attributi
- stare attenti quando un attributo contiene molteplici valori
- delicato trovare equilibrio tra classi e attributi delle classi
### 2. Identifica associazioni
>[!definition]
>Associazioni
>>Espressioni verbali che coinvolgono più classi indicano possibili relazioni tra esse.

#### Associazione esiste se una classe:
- possiede o controlla
- è collegata a, oppure si riferisce a 
- è parte di, oppure ha come parti
- è membro di, oppure ha come membri
#### qualche altra classe del modello

#### Cercare nell'ordine:
1. **Gen-Spec:** espressioni del tipo "**è un**"
2. **Contenimento:** espressioni del tipo "**è fatto di**", "**comprende**"
3. **Associazione:** ogni altra espressione
#### Quando identifichi un'associazione:
- **Specificare le molteplicità** da entrambi i lati
- Assegnare un **nome chiaro** all'associazione e/o **definire i ruoli** delle entità che partecipano all'associazione
#### Errore comune
- Considerare azioni come se fossero associazioni
![[materie/anno_2025-2026/ingegneria_del_software/assets/errore_comune_associazioni.jpg]]
### 3. Identifica generalizzazioni e interfacce
- Due modi per trovare **generalizzazioni**
	- Bottom-Up: **raggruppare classi simili** creando una nuova super-classe
	- Top-Down: cercare prima le **classi più generali** e poi specializzare
- Creare un'**interfaccia** invece di una superclasse:
	- le classi sono molto diverse fra loro, tranne che per poche operazioni in comune
	- diverse implementazioni della stessa classe
#### Esempio: Compagnia aerea
![[materie/anno_2025-2026/ingegneria_del_software/assets/esempio_compagnia_aerea.jpg]]
#### Esempio: Compagnia aerea con generalizzazione
![[materie/anno_2025-2026/ingegneria_del_software/assets/esempio_compagnia_aerea_generalizzazione.jpg]]
### 4. Trova le principali responsabilità di ogni classe
>[!definition]
>Responsabilità
>>Corrisponde ad una funzionalità richiesta al sistema software.

La responsabilità di ogni requisito funzionale deve essere attribuita ad **una delle classi**:
- se una classe ha troppe responsabilità: **dividerla in più classi**
- se una non ha responsabilità: **probabile sia inutile**
- quando non può essere attribuita a nessuna delle classi esistenti: dovrebbe essere creata una **nuova classe**
#### Come stabilire le responsabilità dei requisiti funzionali?
- Svolgere l'analisi dei casi d'uso
- Carcare verbi e nomi che descrivono azioni nella descrizione del sistema
#### Categorie di responsabilità generiche in un class diagram:
- accedere e modificare valori degli attributi
- creare e inizializzare nuove istanze
- prelevare da o memorizzare dati in una memoria persistente
- distruggere istanze
- aggiungere e cancellare istanze di associazioni
- copiare, convertire, trasformare, trasmettere o fornire dati in output
- calcolare risultati numerici
- navigare e cercare dati di particolari istanze
#### Esempio creazione istanze
>[!warning] 
>La responsabilità di creare istanze in una classe non può essere attribuita alla classe stessa, ma ad una classe collegata ad essa

![[materie/anno_2025-2026/ingegneria_del_software/ingegneria_del_software.excalidraw.md#^frame=MZxs5Haf|100%]]
#### Esempio di ricerca delle istanze
>[!warning]
>La responsabilità di **cercare** istanze di una classe che fanno parte di una collection, **non** può essere attribuita alla classe stessa, ma alla classe collection.

