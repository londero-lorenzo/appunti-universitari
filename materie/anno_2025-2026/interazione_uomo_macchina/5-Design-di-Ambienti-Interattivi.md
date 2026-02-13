---
title: "5-Design-Di-Ambienti-Interattivi"
aliases: ["5-Design-Di-Ambienti-Interattivi"]
tags: [università, "materie", "anno-2025-2026", "interazione-uomo-macchina", "5-Design-di-Ambienti-Interattivi"]
created: 2025-11-28
---
# Principi di design dell'Interazione

Alcuni li abbiamo già visti:
+ Coerenza
+ Metafore
+ Manipolazione diretta
Ma ce ne sono ulteriori, ad esempio:
+ **Affordance**

### Affordance

Ci possono essere ad esempio maniglie con buona o pessima affordance, ovvero design che rendono intuitivo o meno il metodo di utilizzo di un oggetto.

>[!tip]
>Per i pessimi design con pessima affordance sono utili i **feedforward**, ovvero delle immagini che fanno vedere cosa succede se si usa un oggetto, quindi ad esempio immagine dell'acqua nello scarico se si tira lo sciacquone.

>[!definition]
>Design
>>Design è un progetto per produrre un concept; che in inglese equivale a "Design is to design a design to produce a design", che è manifesto della non proprio chiara definizione di design, ma corrisponde a disegnare, progettare, ideare, creare,...

>[!tip]
>Ad esempio design è differente per un artista e per un ingegnere.
>

## Interaction design e il ruolo del contesto d'uso

>[!definition]
>Interaction design
>>Contribuisce allo sviluppo dei sistemi interattivi con un pensiero critico, creativo, provocatorio ed estetico
#### User center design
+ Coinvolgimento degli utenti già dalle prime fasi di sviluppo.
+ Iterazione di sviluppo e test
+ Multi-disciplinarità

#### Design partecipato
Utenti usati proprio come designers, in modo che le persone che utilizzeranno la tecnologia abbiano modo di influenzarne direttamente le scelte e lo sviluppo.

>[!example]
>Per un'edizione delle olimpiadi vennero chiamati degli atleti a gestire anche l'organizzazione dei maxi-schermi e cose così.

___
## Processo di design di un sistema interattivo

Simile al modello a cascata di ingegneria del software. Dagli obiettivi si passa all'analisi, poi al progetto (in caso con la creazione di un prototipo e vedendo ciò che non va si può tornare indietro all'analisi) e poi allo sviluppo e distribuzione.
![[materie/anno_2025-2026/interazione_uomo_macchina/assets/Screenshot 2025-12-08 113107.png]]

### Obiettivi
Per averli chiari c'è bisogno di parlare con lo stakeholder (portatore di interesse per la cosa che stiamo facendo) in modo da comprenderli.
###### Stakeholder
+ **Primari**: Forniscono direttamente input e ricevono direttamente output
+ **Secondari**: Forniscono direttamente input e ricevono indirettamente output (attraverso intermediari)
+ **Terziari**: Non rientrano nei casi precedenti (non danno input e non danno output)
+ **Key stakeholder:** i più importanti per il progetto (qualsiasi categoria)
>[!example]
>Esempio nel contesto delle pompe di infusione (iniettare merda ai pazienti)
>+ Il primario è l'infermiere
>+ Il paziente è anch'esso uno stakeholder primario
>+ il più key stakeholder dei due è ovviamente l'infermiere
>
>+ Fornitore di farmaci è un stakeholder secondario
>+ I parenti del paziente sono stakeholder terziari (non fanno niente ma se il paziente sta bene o sta male impatta su di loro)
>+ Chi finanzia (l'ospedale) è uno stakeholder terziario
>+ Nonostante questo l'ospedale ha un ruolo chiave quindi rappresenta un key stakeholder, perché va tutto in base al budget ad esempio che ha l'ospedale.

>[!example]
>(Finire di scrivere)
>Esempio di sistema di training VR per assistenti di volo.
>+ Compagnia aerea è terziaria
>+ Costruttore dell'aereo è secondario (perchè è lui che decide effettivamente come fare l'aereo)
>+ Passeggeri sono terziari


### Tecniche di design

Gli stakeholder (come gli assistenti di volo) possono appartenere a categorie diverse di persone. Ad esempio Ci può essere un assistente di volo giovane videogiocatore e che ha il VR a casa, o uno vecchio che non ha mai toccato un videogioco in vita sua. 

>[!example]
>In un bar ci possono essere diversi clienti:
>+ Chi vuole sedersi e gustarsi il caffè
>+ Chi vuole sempre andare di fretta e prendere il caffè al bancone e scappare
>Tra gli obiettivi quindi ci deve essere il posto rilasso per un cliente e il bancone per l'altro

#### Tecniche per comunicare il design
+ **Personas e scenari**
	+ storyboard descrittivi di utenti tipo che descrivono l'uso in un contesto come una storia
+ **Mock-up**
	+ Concretizzazioni del sistema futuro usando materiali veloci da assemblare (stampa 3D o carta o materiali di recupero)
+ **Prototipo**
	+ Rappresentazione concreta ma parziale di un prodotto/sistema/applicazione per sperimentare e discuterne gli aspetti

___
### Analisi

>[!tip]
>La parte di **Analisi** è formata da:
>+ Personas
>+ Scenari
>+ Task analysis
#### Personas e scenari
##### Personas:
+ Possibile creare i personaggi proprio credibili, con delle statuine fatte appositamente con i vari accessori e caratteristiche
##### Scenari:
+ Possibile fare anche degli scenari sotto forma di storyboard veri e propri come quelli per i film, con scenari e vignette. Anche utilizzare l'AI per creare le vignette è una soluzione plausibile 

>[!example]
>Giovanni è uno studente fuorisede che non fa il pendolare quindi è in un appartamento. Dopo lezione alle 13.30 vuole rientrare a casa e trovare il piatto caldo per il pranzo. 
>+ Quindi mette il piatto in microonde e imposterà il timer alle 13.20.
>+ Poi imposterà durata per 10 minuti.
>+ Imposterà la potenza del microonde.
>+ Se Giovanni è un piscialletto e non vuole calcolare il tempo di partenza posso poter impostare l'orario di fine (13.30) e la durata (10 minuti).
>+ Allo stesso modo si può quindi impostare:
>	+ Fine - Durata
>	+ Inizio - Durata
>	+ Inizio - Fine
#### Task analysis

>[!definition]
>Task
>>Attività da svolgere per raggiungere un obiettivo.
>>Utile a stabilire quali sono i compiti più rilevanti per l'applicazione.

+ Può essere utile coinvolgere l'utente finale e osservare come svolge le attività.
+ Capire le task più importanti tramite interviste, workshop, questionari, osservazione degli utenti nel contesto usuale.
+ Risultato: identificazione dei task più importanti con le informazioni necessarie per svolgerli, relativi problemi e preferenze dell'utente.

>[!tip]
>Concur Task Trees Environment (CTTE) è una piattaforma per editare e analizzare le task utili a supportare un certo design di applicazioni interattive, partendo dalle attività umane come supporto.
>Funziona attraverso la creazione di alberi con le diverse task come nodi.

___
### Progetto

+ Flusso del sistema
	+ immagini che fanno vedere cosa succede  e dove rimanda se si clicca un determinato bottone ad esempio
+ Mock-up
>[!example]
>Ad esempio se si vuole mettere uno schermino con funzioni touch su un coltellino svizzero, senza realizzarlo veramente si può mettere una placchetta su un coltellino svizzero normale e magari uno stuzzicadenti per vedere se è pratico o altrimenti se cambiare approccio.

>[!tip]
>Esempi di strumenti utilizzabili per il mock-up:
>+ Adobe Xd
>+ Figma
>+ Sketch
>+ ...e altri

>[!Problem]
>Non tutti gli utenti target hanno la capacità di immaginare la soluzione finale. Questo può essere un problema per capire l'usabilità del progetto.
>In questi casi è necessario usufruire dei software per magari creare il modello preciso in 3D in modo da far vedere all'utente una versione virtuale del modello finale, senza quindi usare una creazione fisica alla buona.

___

### Prototipo

#### Principi
Euristiche di Nielsen e Molich:
 + 10 regole/principi da seguire che nel caso medio vanno bene, quindi per la maggior parte delle progettazioni di un sistema.
	1. Dialogo semplice e naturale
	2. Parla il linguaggio utente
	3. Minimizza il carico mentale utente
	4. È coerente e standard
	5. Fornisce feedback e visibilità dello stato del sistema
	6. Fornisce uscite chiaramente indicate
	7. Efficienza e flessibilità d'uso
	8. Buoni messaggi d'errore
		+ Ad esempio se compare l'errore con il codice errore non serve a niente e non aiuta l'utente a capire il problema
	9. Previene gli errori
	10. Fornisce aiuto e documentazione
		+ Ad esempio le caselline che spiegano cosa fanno i bottoni che compaiono quado il mouse è sopra al bottone.
		  Inutili se ad esempio la placchetta per il bottone "Back" ripete semplicemente il nome del bottone, "Back".

#### Guidelines
Istruzioni da analizzare per vedere se l'applicazione è conforme rispetto ad un modello.
>[!example]
>Microsoft che per i suoi software ha delle linee guida che spingono i programmatori dei diversi strumenti Microsoft a svolgere ad esempio sempre lo stesso tipo di menu con le stesse opzioni, in modo da fornire continuità tra i diversi software.

##### Standard per le guidelines
###### ISO 9241: 
+ Riguarda requisiti ergonomici per il lavoro d'ufficio con terminali a display visivo.  Focalizzato sui compiti di elaborazione dati testuali in ufficio.
+ Definizione di usabilità secondo ISO 9241
>[!definition]
>Usabilità
>>Efficacia, efficienza, soddisfazione con cui gli utenti specificati raggiungono obiettivi specificati in particolari ambienti.
>>
>>Efficacia = accuratezza e completezza
>>Efficienza = le risorse spese in relazione con l'accuratezza e completezza degli obiettivi raggiunti.
>>Soddisfazione = comfort e accettabilità del sistema di lavoro per i suoi utenti.

>[!example]
>La struttura dei menu deve riflettere le aspettative dell'utente e facilitare l'abilità dell'utente di trovare e selezionare le opzioni di menu rilevanti per il compito che deve svolgere.

___
### Sviluppo e distribuzione
#### Help

##### Esigenze di help utente. Motivi per cui può servire un help
+ **Esplorazione** (cosa posso fare con questo sistema?)
	+ Tutorial
+ **Definizione/descrizione** (Che cos'è/a cosa serve questo?)
	+ Tooltip, help integrato
+ **Svolgimento compiti** (Come faccio questo?)
	+ Help integrato
+ **Diagnostica** (come è accaduto questo? --> errore + link verso pagina risolutiva, oppure meccanismo di undoing (Ctl-Z))
+ **Identificazione di stato** (dove sono?)
	+ Storia dei comandi

>[!example]
>Governo americano aveva problema nei servizi digitali per i cittadini. 
>Crearono un playbook con 13 key plays, con annesse checklist per vedere se si sta producendo correttamente il servizio per il governo americano, di cui le prime 4, che si occupano di HCI, sono:
>+ Capisci cosa la gente necessita
>+ Considera l'esperienza completa dall'inizio alla fine
>+ Rendere semplice ed intuitivo
>+ Costruire il servizio utilizzando il metodo agile (*agiail*) e iterativo

