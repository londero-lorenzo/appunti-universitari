---
title: "18-Crowdsourcing"
aliases: ["18-Crowdsourcing"]
tags: [università, "materie", "anno-2025-2026", "social-computing", "18-Crowdsourcing"]
created: 2025-12-01
---
Il corso è sostanzialmente diviso in 2:
$$\frac{(Social Media)+(Crowdsourcing) =}{(Social Computing)}$$
+ **Social Media**: 
	+ Comportamento sociale viene supportato dai sistemi computazionali
	+ Persone comunicano sfruttando i sistemi computazionali
+ **Crowdsourcing:**
	+ Sistemi computazionali vengono supportati dal comportamento sociale
	+ Compiti che i calcolatori non riescono a svolgere vengono svolti da folle di persone tramite i sistemi computazionali

___
## Aspetti concettuali

Crowds = Folle

>[!definition]
>Folla
>>Tante persone.
>>Possono portare ad una isteria collettiva, ma anche ad un aiuto comune per svolgere qualcosa che il singolo non riuscirebbe.
>>(Due libri opposti: "Madness of the crowds" e "Wisdom of the crowds")


>[!example]
>+ Concorso a premi per vincere bisognava indovinare il peso di un bue. Ognuno scriveva il peso in un bigliettino. Tenendo la media dei pesi scritti si arrivava ad un valore molto vicino al valore corretto. A volte le decisioni prese da una folla di persone sono più corrette di quelle prese dal singolo.
>+ Caso OK della folla:
>	+ Uno shuttle è esploso, la collettività fece scendere in borsa le azioni della marca dello shuttle e in seguito si vide che la colpa era per l'appunto di questa azienda.
>+ Casi KO della folla:
>	+ Shuttle rientrato esploso al rientro, era danneggiato e il comitato decise che non si poteva far niente e lo fecero rientrare ed esplose.
>	+ C'erano delle informazioni su un possibile attacco l'11 settembre, che non vennero condivise tra i diversi enti di sicurezza e per questo non si fece niente

### Principi per cui può funzionare
Affinchè una folla funzioni bene servono questi 4 principi:
+ Diversità di opinioni (possono avere informazioni private)
+ Indipendenza (decisioni non determinate da chi sta intorno: no herding behavior, information cascade)
+ Decentralizzazione (Le varie persone devono essere in grado di specializzarsi in maniera diversa)
+ Aggregazione (deve essere possibile aggregare i dati)
+ Bonus:
	+ Fiducia nella folla (singoli individui devono credere che la folla funzioni)

### Motivi per cui non può funzionare
+ Omogeneità: deve esserci diversità
+ Centralizzazione: se c'è uno che comanda non va bene
+ Divisione: informazioni non accessibili agli altri
+ Imitazione: Formazione di information cascade o herding behavior
+ Emotività: Fatti emotivi possono portare a isteria.

>[!definition]
>Crowdsourcing 1
>>Crowd + outsourcing = Outsourcing to the Crowd ---> Una persona che devo svolgere un compito può svolgerlo in più modi, o dentro l'azienda svolto da pochi dipendenti o viene dato fuori alla folla

>[!definition]
>Crowdsourcing 2
>>Esternalizzare un compito, che tradizionalmente viene eseguito da un impiegato o contraente, a un gruppo di persone indefinito e ampio in forma di una chiamata aperta (chiunque può partecipare).

>[!example]
>Colgate aveva il problema di iniettare della polvere di fluoro dentro un tubetto di dentifricio, ha postato il compito su una piattaforma e un ingegnere a caso ha detto che bastava elettrizzare la polvere i modo da attrarli e si è guadagnato 25000 dollari nel chill easy per il poppin.

>[!tip]
>Piattaforma di crowdsourcing: Amazon Mechanical Turk

___
### Human computation

>[!definition]
>Human computation
>>Processo computazionale da in outsourcing alcuni passi a umani: ruoli tradizionali vengono invertiti, è il computer che chiede alla persona o un gruppo di risolvere il problema e poi raccoglie e interpreta le soluzioni.

Nasce così l'idea dei GWAP (Games with a Purpose), ad esempio:
+ ESP Game (Trovare etichette che descrivono l'immagine ed è da utilizzare la stessa etichetta di una seconda persona, si gioca in coppia) (intanto si etichettano immagini per le AI)
+ Duolingo (Imparare lingue)(intanto tradurre documenti)
+ ReCAPTCHA (test anti-bot)(intanto il calcolatore che sta dietro capisce cosa vuole dire il captcha quando l'utente lo traduce, chiedendo a più utenti e vedere se sono d'accordo)

Motivi per diventare questi "calcolatori umani":
+ Denaro
+ Divertimento
+ Fama
+ Altruismo

>[!tip]
>Il crowdsourcing è un caso particolare di human computation.
>Human computation sembra più efficace se i sistemi digitali sono usati nel processo.

>[!example]
>Ulteriori esempi:
>+ Ricercatore vuole dei dati per gli esperimenti può decidere di cercarli in crowdsourcing. 
>+ azienda che vende beni può fare indagini di mercato veloci e a poco prezzo in crowdsourcing
>+ Amministrazione comunale può chiedere di far foto alle buche in strada anche in maniera gratuita per vedere dove agire.

___
### Soylent: Find-Fix-Verify
>[!definition]
>Soylent
>>processore del mondo con una folla al suo interno.
>>Accorcia, Correzione bozze, human macros (trasforma al passato).

Flusso di lavoro di Soylent:
+ **Find**: identificare in un documento di testo dei pezzi che possono essere accorciati senza cambiare il significato del paragrafo
+ **Fix**: Modificare la parte selezionata per accorciarne la lunghezza senza cambiarne il significato
+ **Verify**: Scegliere almeno una riscrizione che ha errori di stile e almeno una riscrizione che cambia il significato del paragrafo

___
### Amazon Mechanical Turk
Rappresenta una piattaforma in un "mercato per lavoro che richiede intelligenza umana".
+ **Requester**: individuo con lavoro da far svolgere
+ **Worker**: Persona che vuole fare il lavoro
+ **HIT**: unità di lavoro da svolgere. Ad ogni HIT è associato un pagamento (pochi centesimi)
+ **Batch**: insieme di HIT caricato da un Requester
Solitamente sono richieste che richiedono meno di un minuto e pagano circa 1-3 centesimi a task
>[!tip]
>Amazon Mechanical Turk rispetta i 4 principi di Surowiecki:
>+ Diversità delle opinioni
>+ Indipendenza
>+ Decentralizzazione
>+ Aggregazione


____

>[!warning]
>**Take home message:** In certe condizioni le folle sembrano essere utili per svolgere compiti di buon qualità.

### Critiche

+ **Critica principale al crowdsourcing**: Qualità messa in dubbio. Attività amatoriale vs. attività di esperti del settore, portano qualità bassa i principianti. Posizione estrema ma con un fondo di verità. Difficile da capire come è veramente.

>[!example]
>Vedendo gli errori che ci sono su wikipedia (fatta da amatori) e sull'enciclopedia britannica (fatta da esperti) si vede come più o meno il numero di errore è lo stesso. Esempio di come gli amatori abbiano fatto comunque un buon lavoro.

+  **Altro problema**:
Molti compiti da qui a 5 anni fa vengono subappaltati alle AI, sia da parte degli esperti che da parte degli amatori.
>[!tip]
>Molti dicono che le Ai abbiano ucciso il crowdsourcing, anche se per il momento ad esempio i soldi messi in palio su amazon mechanical turk sono circa li stessi di anni fa. è comunque un fenomeno da tenere in conto.

+ **Ulteriore critica**: Etica del lavoro. Il worker non può essere un lavoro che rende indipendente una persona, la paga a task è minima (1-2 centesimi di solito). Rischio di cadere nello sfruttamento dei worker.
