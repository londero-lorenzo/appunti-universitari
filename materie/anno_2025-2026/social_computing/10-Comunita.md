---
title: 10-Comunita
aliases:
  - 10-Comunita
tags:
  - università
  - materie
  - anno-2025-2026
  - social-computing
created: 2025-11-03
description: INCLUDE ANALISI GRAFO DI FACEBOOK
---
# Comunità

Le comunità possono essere:
+ Esplicite (gruppi Facebook, associazioni LinkedIn)
+ Implicite (Legami interni forti all'interno della comunità e legami esterni deboli fra comunità diverse)

>[!definition]
>Comunità
>>Gruppo di nodi connessi fra di loro e non connessi con gli altri.

>[!definition]
>Omofilia
>>Tendenza delle persone ad associarsi e formare legami con persone simili a loro

>[!example]
>+ Un conflitto in un club di karate ha separato in due gruppi le persone dl club che avevano più legami di amicizia con uno con l'altro
>+ In una scuola di solito i bianchi sono amici di bianchi e i neri sono amici dei neri
>+ I repubblicani hanno amici dello stesso pensiero politico e così anche i democratici

Proviamo a dare una vera definizione utile a noi di comunità:
>[!definition]
>1-Definizione ideale di comunità
>>Dato un grafo G una comunità C è un sottografo di G tale che:
>+ C è connesso (o addirittura completo)
>+ $\forall$ nodo $v \notin C$, $v$ è sconnesso da C

Questa definizione è fatta per casi ideali, estremi e in realtà computazionalmente difficili, quindi non va bene (soprattutto il secondo punto della definizione).

>[!definition]
>2-Definizione di comunità
>>Dato un grafo G una comunità C è un sottografo di G tale che:
>>+ C è **connesso**
>>+ $\forall$ nodo $v \notin C$, $v$ è **poco connesso** a C


>[!question] Come individuare le comunità?
>Esistono vari algoritmi e noi vediamo il più importante (anche se non il più efficace):
>+ Edge betweenness centrality

### Edge betweenness centrality

##### Algoritmo di Girvan-Newman
**Idea**: rimuovere ricorsivamente i legami deboli, ovvero rimuovendo gli archi con alta centralità di betweenness (weak ties) e disconnettendo così via via la rete, rendendo le comunità delle componenti sconnesse e potendo così trovarle.

Viene quindi prodotto un albero detto dendogramma dove in ogni livello più lontano dalla radice ci sono componenti (comunità) sempre più piccole, essendo l'albero formato da comunità, sottocomunità e sopracomunità.


___

# Grafo di Facebook

### Lavoro 1: The Anatomy of the Facebook Social Graph
Grafo sociale di Facebook nel 2011:

Primo grafico rappresenta la degree distribution per gli utenti, il secondo rappresenta la CCDF della degree distribution:

![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-04 195601.png|500]]
+ Utenti: 721 milioni di nodi, 10% della popolazione mondiale
+ Archi: circa 69 miliardi, 190 amici a persona in media
+ La degree distribution non è proprio una power law, ma presenta un punto di flessione (sembrano due powerlaw fuse al punto di flessione). Si vede inoltre il limite imposto da Facebook stesso di 5000 amici. 
+ Complementary cumulative distribution funtion (CCDF).
  La CCDF al grado k misura la frazione di utenti che hanno grado k o maggiore in termini di degree distribution. Si vede bene come nella coda il rumore scompare.
+ 
___

Il seguente grafico mostra la distribuzione delle **componenti connesse**:

![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-04 195734.png|350]]
+ Distribuzione delle componenti connesse rappresentata da una power law, in cui si vede che con l'aumentare della grandezza della componente si abbassa il numero di componenti, quindi ci sono poche componenti grandi e molte più piccole. Curiosa la presenza di una componente connessa estremamente grande (100 milioni), che rappresenta praticamente tutto il grafo ed è di fatto la **giant component** della rete di Facebook, il che fa capire che la rete è praticamente connessa o quasi.
+ La dismensione media quando si parla di componenti connesse è un'informazione praticament irrilevante: in questo grafico vediamo che la dimensione media è circa del'ordine dei 100 nedi, ma non ci frega niente perché l'unica componente che ci interessa è l'outlier ovvero la giant component

___

Vennero studiate poi le distanze medie in un grafico rappresentante le distanze cumulativa.
![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-08 114513.png|350]]

+ Vediamo come il 92% delle coppie di nodi ha una distanza inferiore a 5. La distanza minore uguale a 6 ce l'hanno quasi il 100% delle coppie di nodi.

___

Venne analizzato anche il **coefficiente di clustering**:
![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-11-08 114702.png|350]]

+ Andamento monotono decrescente (più un nodo ha grado alto più il coefficiente del nodo sarà di grado basso e viceversa)
+ Appena prima dei 5000 c'è una decrescita ripida del coefficiente di clustering. Questo perché i profili con così tanti amici probabilmente non sono persone ma aziende o cose simili che chiedono quindi amicizia a tutti senza avere davvero rapporti con queste persone

___
#### Paradosso degli amici

"I tuoi amici hanno più amici di te"
>[!question] Cosa vuol dire?
>Se prendo un nodo a caso su una rete e conto quanti amici ha otterrò un certo valore, ma se prendo un nodo a  caso e seguo un link e conto quanti amici ha tenderà ad averne di più del nodo iniziale.

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-11-08 115959 1.png|350]]

+ La linea tratteggiata è quello che ci aspetteremmo se non ci fosse il paradosso degli amici: i miei amici avrebbero esattamente gli amici che ho io
+ In realtà gli amici dei miei amici sono mediamente un numer più grande dei miei
+ Si vede però che circa oltre il grado 700 i miei amici hanno meno a mici di me, perché più amici ho io e più è difficile per i miei amici avere tanti amici quanti ne ho io.


#### Paese di appartenenza
In base all'IP si è potuto vedere come l'85% degli archi di un nodo sono all'interno del paese di appartenenza del nodo.

---

### Lavoro 2: Four Degrees of Separation
Grafo di Facebook nel 2012:

#### Osservazioni rispetto allo studio precedente
+ Aumento del numero di nodi e numero di archi aumentato in modo abbastanza costante.
+ Grado medio dei nodi è pure chiaramente in crescita con il passare del tempo.
+ La densità (numero di archi effettivo / numero di archi possibili) invece cala nel tempo. I legami dei nuovi utenti non riescono a sopperire la densità rispetto agli archi che ci potrebbero essere.
+ Distanza fra due nodi: Come si vede dal grafico la distanza media tra due nodi è di 4. Più precisamente in tutto facebook la distanza è uguale a 5. Se i nodi su cui si misura la distanza sono dello stesso paese allora si abbassa a 4.
![[materie/anno_2025-2026/social_computing/assets/distanza.png|400]]
+ Andamento della varianza della distanza: ha un convergenza rapida fino al 2008, in cui si stabilizza praticamente a 0.
+ La distanza media ha una sorta di convergenza fino al 2008 per poi stabilizzarsi ad una distanza media di 4-5. Questo nonostante la densità cali.

___
### Lavoro 3: 
2016

+ Si rianalizzò la distanza media e attennero un valore di 3.5, calore leggermente inferiore al precedente.

