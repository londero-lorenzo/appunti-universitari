---
title: 22-Misurazione-Ridondanza-Aggregazione
aliases:
  - 22-Misurazione-Ridondanza-Aggregazione
tags:
  - università
  - materie
  - anno-2025-2026
  - social-computing
created: 2025-12-19
---
## Teoria della misurazione
+ Measurement
+ Scales (N, O, I, R)
+ Permissible transformations
+ Meaningful statements
+ Legit operations & statistics

### Measurement

>[!definition]
>Measurement - 1
>>Un processo con lo scopo di determinare una relazione tra una quantità fisica e un'unità di misura
>>$\omega:D\rightarrow R$
>>Un assegnamento $\omega$ è una funzione che assegna valori agli oggetti in un set $D$

>[!tip]
>Measurement = Assignment of a real number
>Si ma non solo...
>

>[!problem]
>Un po' di cose strane da capire
>Stessa misura vs. misura equivalente
>+ Numeri diversi per la stessa cosa (es. temperatura: gradi, celsius, kelvin, fahreneit)
>+ Confronti (es. 1-2-3    |     10-11-12)
>+ Numerare le categorie (es. cambio la numerazione di categorie da 1-2-3 a 1-3-5 oppure 3-2-1)
>+ Aggregazione (es. posizione media, colore medio riferito magari ad una temperatura)
>+ Aggettivi strani (tipo "doppio" può essere utilizzato con la temperatura? A è il doppio più caldo di B?)

>[!definition]
>Measurement - 2
>>Per essere una misura, un assegnamento deve essere un **omomorfismo** (esempio "agglomeration (+)", "heavier than (>)")
>
>Queste proprietà valgono in qualsiasi misura (es. un chilo di patate è ">" di 6 chili di patate)

___

### Measurement scale

>[!question]
>Che scale devo usare per una data misura?

**Standard set:**
+ Nominale
+ Ordinale
+ Intervallare
+ Ratio

#### Ratio scale
>[!example]
>"sono alto due volte lui"
>"lui è ricco due volte me"
>+ Parte da zero (Età, ricchezza, altezza)
>+ Non tutte le misure possono utilizzarla (es. oggi è caldo due volte ieri   -->   non va bene)

#### Interval scale
>[!example]
>"Negli ultimi giorni abbiamo avito un incremento di 5°C nella temperatura"
>Esempi sono temperatura e le date
>+ Stessa differenza (2019-2017 = 2006-1004)
>+ Non lo stesso ratio (2000 non è due volte 1000)

#### Ordinal scale
>[!example]
>la misura non è un ammontare ma un rank:
>+ "oggi è più caldo di ieri"   -->  oggi = prima posizione,     ieri = seconda posizione

#### Nominal scale
>[!example]
>Misure qualitative, categorie.
>+ Es. nomi, generi, nazionalità, colori...
>+ I numeri fungono da identificatori della classe

#### Trasformazioni permesse
Data una scala, la misura può essere trasformata per ottenere una misura equivalente?
+ Ovvero se tu **trasformi** la misura, stai ancora misurando la stessa cosa (es. nazionalità, rank, temperatura, soldi)

![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-12-20 174723.png]]

+ Alcuni frasi in una misurazione hanno senso, altre no. Es:
	+ Age: 40 anni = 20 anni $\*2$    -->  tu hai il doppio dei miei anni
	+ Scala nominale della nazionalità:  Greek = 1; Italian = 2; ....
	  Non posso dire che l'italiano è il doppio del greco, non vorrebbe dire niente. 

>[!tip]
>Data una scala, solo alcune delle frasi hanno senso (sono meaningful), e la loro truthfulness (o falsehood) rimane anche dopo le permissible transformations.

Anche solo alcune operazioni (legit operations) avranno senso in base alla scala:
+ relazionali: =, >, <
+ aritmetiche: +, -, $\*$, /
+ statistiche: media, mediana, moda

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-12-20 180437.png]]

>[!warning]
>Non confondere **permissible transformations** e **legit operations**:
>+ Permissible operations: trasformazioni che posso applicare alla misurazione mantenendo la stessa misurazione (una equivalente)
>+ Legit operations: Cose che posso usare per definire la relazione tra le misurazioni

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-12-20 180500.png]]
___
## Aggregazione reloaded

>[!question] A cosa serve?
>A ragionare sull'aggregazione   (Relevance assessment binario)

Secondo la teoria della misurazione la scala utilizzata è nominale; scelta tra moda e media cambia poco nel caso dell'esempio slide 59.
A volte però è più complicato, per esempio possiamo dover utilizzare le **Categorie ordinali** (es. Pants on Fire, False, Half True, True,....).
Utilizzando nuovamente la moda con queste categorie
>[!example]
>Utilizzando nuovament la moda nell'esempio se ad esempio abbiamo 51 True e 49 Mostly True, sarà come avere 99 T e 1 MT.
>+ Gli errori piccoli saranno uguali agli errori grandi (49 F e 51 T, sarà considerato True)
>+ Si perdono informazioni

>[!soluzione]
>Potrei fare una trasformazione iniettiva non monotona alle categorie assegnando numeri crescenti in base alla veridicità della categoria alle categorie stesse. (False = 1, Barely True = 2, Half True = 3,....).
>Rendo la scala nominale una **scala ordinale**.
>Con questa soluzione ci sono comunque cose che possiamo dire con certezza ed altre che non possiamo dire.

>[!tip]
>La scala può essere scelta in base all'impatto anche psicologiche le sue etichette si presume abbiano verso i worker, ma possono avere anche problemi di "ridondanza".
>Ad esempio una scala a 100 valori può essere probabilmente semplificata in una scala a 10 valori.
>Più le scali sono grandi e più si avvicinano a una scala a intervalli, ma più la scala è grande e più i risultati appaiono vicini magari alle misurazioni degli esperti.



