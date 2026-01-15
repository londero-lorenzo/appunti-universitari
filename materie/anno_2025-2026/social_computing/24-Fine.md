---
title: "24-Fine"
aliases: ["24-Fine"]
tags: [università, "materie", "anno-2025-2026", "social-computing", "24-Fine"]
created: 2026-01-15
---
# Fake news

>[!question] Si riesce ad individuare le notizie vere da quelle false, magari utilizzando il Crowdsourcing?
>Si tenta lo sviluppo di una macchina della verità, che riceve in input la notizia e rilascia il output la sua veridicità o falsità.

In realtà queste macchine della verità sono dei fact-checker expert, ovvero delle persone che manualmente controllano le notizie. Tuttavia ci sono molte più notizie che fact-checker, che non sono scalabili

Altra possibilità è integrare AI tools con i crowd workers e con i fact-checkers, per aumentarne l'efficienza.
Però sorgono delle domande:
+ Ha senso chiedere al crowd di dire se una notizia è vera o falsa, crowd che è lo stesso che mette in giro tale notizia
+ Generalmente AI e fact-checkers si contrappongono negli stats: ad esempio i fact-checkers hanno un'accuratezza maggiore e un controllo del bias maggiore, mentre l'AI ha una scala maggiore e un costo maggiore. Potrebbe quindi avere senso usarli insieme, con i crowd workers che probabilmente si pongono nel mezzo tra i due.

>[!example]
>Community notes è un sistema di Twitter che permette al crowd di aggiungere note sulle notizie dicendo se sono vere o false, giudicate dalla community.

**Efficacia** delle singole componenti:
+ Esperti: 100%
+ Crowd: 80%
+ AI: 80%
Effettivamente potrebbe bastare un'efficacia inferiore al 100%

**Confidenza**:
+ Le confidenze delle AI non sono per nulla affidabili, sono molto brave ad essere estremamente sicure dei loro errori
+ Anche Per i crowd workers non è detto che se c'è un maggior accordo allora le notizie sono più vere

**Valutazione**:
+ Benchmark (dare in pasto alla macchina una serie di notizie eticchettate come vere o false e vedere quante ne indovina)
	+ Problemi:
		+ **Data contamination**: Nelle AI spesso vengono date in allenamento delle notizie con relative risposte, quindi non sta facendo un vero ragionamento ma sta semplicemente incollando la risposta collegata a quella notizia

(siuuuuu si salta fino a slide 33)

___
### Esperimento

Sono stati presi vari statement già giudicati da esperti e vengono fatti giudicare ai worker

+ Distribuzione box-plot con sull'asse delle x i valori reali attribuiti da esperti e sull'asse delle y valori ad intervalli da 1 a 6 che corrispondono ai valori di verità partendo da 1=falso e 6=vero.
![[materie/anno_2025-2026/social_computing/assets/Screenshot 2026-01-15 125635.png|450]]
  Si vede come in alcune notizie il crowd non abbia fatto proprio un bel lavoro, soprattutto su quelle ritenute false dagli esperti, essendoci dei casi in cui alcune notizie sono state valutate intorno al 5, nonostante fossero completamente false.
  L'accuracy del crowd si attesta in questo caso intorno al 70%, che è più o meno alla pari all'epoca dei sistemi automatici, quindi non conveniva utilizzare il crowd che dava la stessa accuratezza dei sistemi AI.

Ci riprovarono successivamente negli scorsi anni e rivedendo i dati i crowd ebbero un'accuratezza dell'80%, maggiore delle AI (che però negli ultimi anni sono cresciute fino all'80% anche loro)

Riassunto di tutto è che praticamente lo studio non è ancora finito e quindi non si sa se il crowd e le AI vanno bene o no. Insomma in alcune cose si in altre no.

___
(skippone della madonna fino a slide 104)
#### Riassuntone del corso che non scriverò
![[materie/anno_2025-2026/social_computing/assets/Screenshot 2026-01-15 130715 1.png]]
#### Modalità d'esame che non scriverò

#### Esempi domande d'esame che non scriverò

# FINE