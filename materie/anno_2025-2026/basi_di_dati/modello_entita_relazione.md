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

![[materie/anno_2025-2026/basi_di_dati/basi_dei_dati.excalidraw.md#^frame=Q36H2577]]

>[!definition]
>Relazioni ricorsive
>>Relazioni tra un'entità e se stessa.

![[materie/anno_2025-2026/basi_di_dati/basi_dei_dati.excalidraw.md#^frame=4hXLvdXx]]

Successione non è **simmetrica**: necessario stabilire i due ruoli che l'entità coinvolta gioca nella relazione.

>[!definition]
>Relazioni n-arie
>>Relazioni che coinvolgono più di due entità

![[materie/anno_2025-2026/basi_di_dati/basi_dei_dati.excalidraw.md#^frame=LnY1hIjv]]
Fornitore rifornisce un dipartimento di un certo prodotto.
Un possibile insieme di occorrenze di questa relazione potrebbe stabilire che:
+ la ditta Pinto fornisce stampanti al dipartimento **Vendite** e calcolatori al dipartimento **Sviluppo**
+ la ditta **Sami** fornisce calcolatori al dipartimento **Ricerca** e fotocopiatrici al dipartimento **Vendite**

