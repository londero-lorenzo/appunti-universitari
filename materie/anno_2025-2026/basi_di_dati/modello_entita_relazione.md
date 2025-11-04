---
title: "Modello Entita Relazione"
aliases: ["Modello Entita Relazione"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "modello-entita-relazione"]
created: 2025-10-09
---
La **modellazione concettuale** costituisce una fase importante nella progettazione di una buona applicazione di basi di dati.

>[!definition]
>Applicazione di basi di dati
>> Si riferisce a una base di dati specifica e ai programmi associati che ne implementano le interrogazioni e gli aggiornamenti.

Questi programmi forniscono **interfacce grafiche amichevoli** tramite **moduli e menu**.

# Progettazione di base di dati

## Raccolta e analisi dei requisiti
I progettisti intervistano i futuri utenti della base di dati:
+ per capire e documentare i **requisiti sui dati**.

## Schema concettuale
+ Usando un modello di dati concettuali di **alto livello**
+ **Progettazione concettuale**
>[!definition]
>Schema concettuale
>>Descrizione concisa dei requisiti sui dati degli utenti e comprende descrizioni dettagliate dei tipi di identità, associazioni e vincoli


# Costrutti del modello
## Entità
>[!definition]
>Entità
>>Rappresentano classi di oggetti che hanno proprietà comuni ed esistenza "autonoma" ai fini dell'applicazione.

>[!example]
>Esempi positivi
>- Cliente
>- CC

>[!example]
>Esempi negativi:
>- Età
>- Numero di telefono

### Entità debole
>[!definition]
>>Tipi di entità che **non hanno** propri attributi chiave.

>[!definition]
>Relazione identificante
>>Entità **deboli** identificate tramite il loro **collegamento** con entità di **un altro tipo** in combinazione con **dei loro attributi** chiamate **entità identificante**.

>[!definition]
>Chiave parziale
>>Insieme di attributi che possono identificare univocamente le entità deboli **collegate alla stessa entità identificante**.
#### Esempio dell'albergo
![entita_debole_ex_1](/materie/anno_2025-2026/basi_di_dati/assets/entita_debole_ex_1.svg)
+ Stanza è detta entità debole, entità per cui non esiste un identificatore senza far riferimento ad un'altra identità esterna che è la coppia numero e albergo, che viene detta **entità proprietaria**.
+ La relazione 'IN' è detta **relazione identificante**.
+ La partizione delle stanze in blocchi disgiunti è dovuta al fatto che l'arco è (1, 1): ad ogni stanza corrisponde un albergo. Se ci fosse N non potrei partizionare le stanze.
### Occorrenza di un'entità
Oggetto della classe che l'entità rappresenta.
>[!example]
>Roma, Milano e Palermo esempi di occorrenze dell'entità Città.
>Marini e Ferrari esempi di occorrenze dell'entità Impiegato.

>[!warning]
Un'occorrenza di entità non è un valore che identifica un oggetto (come il cognome o il CF di un impiegato) ma è l'oggetto stesso (impiegato in carne e ossa).

+ Un'occorrenza di entità ha esistenza **indipendente** dalle proprietà ad esso associate
	+ un impiegato esiste indipendentemente dal fatto di avere un nome, cognome, ecc...

![[materie/anno_2025-2026/basi_di_dati/assets/costruttiModelloE-R.jpg]]
## Relazioni (o associazioni)

>[!definition]
>>Rappresentano legami logici tra due o più entità.

>[!example]
>Residenza relazione che può sussistere tra le **entità** Città e Impiegato.
>Esame relazione tra Studente e Corso.

>[!tip]
>Relazioni = insieme di n-uple

>[!tip]
>Ogni relazione ha un nome che la identifica **univocamente**.
>Nella scelta dei nomi preferibile usare **sostantivi** invece di verbi.

>[!warning] Insieme delle occorrenze di una relazione del modello E-R:
>- è una relazione matematica tra le occorrenze delle entità coinvolte.
>- un **sottoinsieme** del prodotto cartesiano
>- questo significa che tra le occorrenze di una relazione del modello E-R **non** ci possono essere **ennuple** ripetute.

>[!example]
>La relazione Esame in figura non è in grado di descrivere il fatto che a uno studente ha sostenuto più volte lo stesso esame (perché produrrebbe ennuple identiche).
>In tal caso anche Esame va rappresentato come entità collegata mediante relazioni alle entità Studente e Corso.

![esempiorelazione](/materie/anno_2025-2026/basi_di_dati/assets/esempiorelazione.svg)

![relazione2](/materie/anno_2025-2026/basi_di_dati/assets/relazione2.svg)
Ogni cliente compare almeno 1 volta e in generale N volte come elemento di una coppia nella relazione POSSIEDE

### (-,N)---(-,N): **relazioni molti a molti**
>[!example]
>**Studenti e Corsi**
>- Uno studente può iscriversi a **molti corsi**
>- Un corso può avere **molti studenti**

### (-,1)---(-,N): **relazioni molti a uno**
>[!example]
>**Dipendenti e Dipartimenti**
>- ogni dipendente lavora in **un solo dipartimento**
>- un dipartimento può avere **molti dipendenti**
### (-,1)---(-,1): **relazioni uno a uno**
>[!example]
>**Persona e Passaporto**
>- ogni persona possiede **un solo passaporto**
>- ogni passaporto appartiene a **una sola persona**

## Relazioni ricorsive

>[!definition]
>Relazioni ricorsive
>>Relazioni tra un'entità e se stessa.

![relazioniricorsive](/materie/anno_2025-2026/basi_di_dati/assets/relazioniricorsive.svg)

Successione non è **simmetrica**: necessario stabilire i due ruoli che l'entità coinvolta gioca nella relazione.

### Esempi
![relazioni_ricorsive_ex_1](/materie/anno_2025-2026/basi_di_dati/assets/relazioni_ricorsive_ex_1.svg)
potremmo confondere gli archi quindi li distinguo con PARTENZA e ARRIVO
+ PARTENZA (1,N)
+ ARRIVO (1,N)

>[!tip] CHIUSURA TRANSITIVA
>La **chiusura transitiva** della relazione “può volare verso” indica **tutti i collegamenti indiretti** ottenibili da una catena di voli.
>In altre parole:
>- Se da **TS** (Trieste) posso volare **direttamente** a **MI** (Milano),
>- e da **MI** posso volare a **NY** (New York),
>allora, **per chiusura transitiva**, si dice che da **TS** posso volare **anche a NY**, _con uno scalo_.

![relazioni_ricorsive_ex_2](/materie/anno_2025-2026/basi_di_dati/assets/relazioni_ricorsive_ex_2.svg)
+ ogni RE di quanti altri è predecessore? (0,1)
+ di quanti altri RE è stato successore? (0,1)
## Relazioni n-arie
>[!definition]
>Relazioni n-arie
>>Relazioni che coinvolgono più di due entità

![relazionin-arie](/materie/anno_2025-2026/basi_di_dati/assets/relazionin-arie.svg)
Fornitore rifornisce un dipartimento di un certo prodotto.
Un possibile insieme di occorrenze di questa relazione potrebbe stabilire che:
+ la ditta Pinto fornisce stampanti al dipartimento **Vendite** e calcolatori al dipartimento **Sviluppo**
+ la ditta **Sami** fornisce calcolatori al dipartimento **Ricerca** e fotocopiatrici al dipartimento **Vendite**

### Esempio
Relazioni binarie tra Progetto, Componente, Fornitore: PC, CP, PF.
![relazioni_ternarie_ex_1](/materie/anno_2025-2026/basi_di_dati/assets/relazioni_ternarie_ex_1.svg)


![relazioni_ternarie_ex_2](/materie/anno_2025-2026/basi_di_dati/assets/relazioni_ternarie_ex_2.svg)
### Reificazione
>[!definition]
>>Trasformare la relazione in entità.

![reificazione_ex](/materie/anno_2025-2026/basi_di_dati/assets/reificazione_ex.svg)
Ogni istanza dentro alla nuove entità 'R-fornisce' è sempre una tripla come la relazione ternaria, ed ogni tripla può avere solo un determinato componente, un determinato fornitore ed un determinato progetto. E questo succede sempre in ogni reificazione.
R-fornisce viene identificato solo attraverso le entità esterne, ed è quindi un'entità debole
## Attributi

### Attributo semplice
Tutti gli attributi **non divisibili**: nell'esempio dell'Indirizzo la via, numero civico, CAP e Città.
### Attributo composto
Possono essere divisi in parti più piccole, che rappresentano più attributi di base con **significati indipendenti**.

>[!example]
>Attributo INDIRIZZO può essere diviso in:
>- Indirizzo Via
>- Città
>- Stato
>- CAP

+ Possono formare una gerarchia
+ il suo valore è la concentrazione dei valori degli attributi semplici che lo costituiscono
+ utili quando l'utente fa riferimento all'attributo composto come un **tutt'uno** (a volte fa riferimento ai suoi componenti specifici)
+ se ci si riferisce come un tutt'uno puoi fare a meno di dividerlo negli attributi componenti

### Attributi a singolo valore
>[!example]
>Età è un attributo a valore singolo di persona.
### Attributi multivalore
>[!example]
>COLORI per una automobile:
>- automobili con un solo colore hanno valore singolo
>- automobili bicolori hanno due valori per COLORI
>LAUREE per una persona:
>- una persona può avere 0 lauree
>- una persona può avere 1 o più lauree

>[!tip]
Può avere **limiti inferiori e superiori** per i numero di valori consentiti per ciascuna singola entità.
### Attributo obbligatorio
Se metto (0, 1) vuol dire che ci deve essere obbligatoriamente massimo 1 dato
### Attributo opzionale
Se mettessi (0,N) vuol dire che l'utente non è obbligato a inserire niente
### Attributo derivato
Data di nascita e Età sono derivati dal CF
(FORMA DI RIDONDANZA)
### Attributo primitivo
L'attributo CF è primitivo perché da quello deriviamo altri.

Numero di conti correnti posseduti: posso ricavare questo valore ma devo navigare tutto lo schema E/R

Persona----->Residente------->Città
Tra persona e residente il vincolo è (1,1)
Tra residente e città il vincolo è (1,N)

Quindi posso inserire in Città il numero di residenti.

Più è leggibile uno schema E/R e meglio è

## Attributi chiave

>[!definition]
>Chiave
>>Sottoinsieme di attributi
>>Mi consente di identificare univocamente ogni istanza dell'entità.

>[!example]
>L'attributo CF per una PERSONA.

>[!tip]
Se avete progettato bene le cose una chiave esiste sempre ed è l'insieme di tutti gli attributi.

+ se molti attributi formano una **chiave**:
	+ la **combinazione dei valori** degli attributi deve essere distinta per ciascuna entità
	+ **attributo composto**: se un insieme di attributi possiede questa proprietà
	+ attributo composto diventa un **attributo chiave** del tipo di entità

>[!warning]
>Chiave composta deve essere **minimale**: cioè tutti gli attributi componenti devono far parte dell'attributo composto per avere la proprietà di **univocità**.

>[!warning]
>Proprietà di **univocità** deve valere per **ogni estensione** del tipo di entità.
>Cioè proibisce a qualsiasi coppia di entità di avere contemporaneamente lo stesso valore per l'attributo chiave.

>[!tip]
A livello di scheda E-R, è bene esplicitare tutte le chiavi.

### Valore NULL
+ Dominio di un attributo A, DOM(A)
	+ DOM(CF)
	+ DOM(STIPENDIO)
+ NULL ha tanti significati

>[!example]
>Non conosciamo lo stipendio di un impiegato: mettiamo a 0 (scelta sbagliata per le funzioni aggregate)

In certi casi un'entità può non avere un valore adatto per un attributo.

>[!example]
>Attributo NumeroAppartamento di un indirizzo ha senso solo per un condominio  e non altri tipi di abitazioni come una casa monofamiliare.
>Attributo Lauree ha senso solo per persone che effettivamente hanno una laurea.

#### Tipi di NULL
+ **Non applicabile**: come nei casi dell'esempio precedente
+ **Sconosciuto**: se non è noto il valore di un attributo
	+ **mancante**: quando è noto che il valore per quell'attributo esiste
	+ **non è noto**: se il valore dell'attributo esista

# Generalizzazione
## Generalizzazioni totali vs parziali

### Totali
- **Entità generale** E: STUDENTE
- $E\_{1}$: STUDENTE IMMATRICOLATO
- $E\_{2}$: STUDENTE NON IMMATRICOLATO
![generalizzazioni_totali](/materie/anno_2025-2026/basi_di_dati/assets/generalizzazioni_totali.svg)
Tutte le entità sotto STUDENTE ereditano i suoi attributi e possono avere anche dei loro attributi specifici (es. NUMERO_MATRICOLA per STUDENTE IMMATRICOLATO)

>[!tip]
>Ogni istanza dell'entità padre (E) è anche istanza di almeno un entità figlia.

### Parziali
- **Entità generale** E: PROFESSIONISTA
- $E\_{1}$: AVVOCATO
- $E\_{2}$: INGEGNERE
- $E\_{3}$: DOTTORE
![generalizzazione_parziale|100%](/materie/anno_2025-2026/basi_di_dati/assets/generalizzazione_parziale.svg)

>[!warning]
>Può accadere che esista un'istanza del creatore che **non** è istanza di nessuna dei figli.

## Generalizzazioni disgiunte vs sovrapposte

### Disgiunta
- **Entità generale**: VEICOLO
- $E\_{1}$: AUTO
- $E\_{2}$: MOTO
- $E\_{3}$: CAMION
![generalizzazione_disgiunta|100%](/materie/anno_2025-2026/basi_di_dati/assets/generalizzazione_disgiunta.svg)
>[!tip]
>Ogni istanza del genitore appartiene al massimo a 1 dei figli.

### Sovrapposta
- **Entità generale**: PERSONA
- $E\_{1}$: STUDENTE
- $E\_{2}$: LAVORATORE
![generalizzazione_sovrapposta|100%](/materie/anno_2025-2026/basi_di_dati/assets/generalizzazione_sovrapposta.svg)
![esempio_generalizzazione|100%](/materie/anno_2025-2026/basi_di_dati/assets/esempio_generalizzazione.svg)

![eredita_selettiva|100%](/materie/anno_2025-2026/basi_di_dati/assets/eredita_selettiva.svg)

ISTANZE (PROPRIETARIO) $\subseteq$ ISTANZE (PERSONA) $\cup$ ISTANZE (AZIENDA) $\cup$ ISTANZE (BANCA)

Congiunzione PROPRIETARIO è sia una PERSONA, sia una BANCA, sia un'AZIENDA

- Non esiste una chiave comune: la eredita selettivamente

>[!definition]
>Ereditarietà selettiva
>>Ogni proprietario eredita gli attributi dalla categoria di appartenenza.

### Da non fare
![generalizzazione_sbagliata|100%](/materie/anno_2025-2026/basi_di_dati/assets/generalizzazione_sbagliata.svg)
