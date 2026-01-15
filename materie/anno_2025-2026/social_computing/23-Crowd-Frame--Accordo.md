---
title: 23-Crowd-Frame--Accordo
aliases:
  - 23-Crowd-Frame--Accordo
tags:
  - università
  - materie
  - anno-2025-2026
  - social-computing
created: 2025-12-22
---
(tutta la parte su Crowd_Frame)

# Accordo

Anche dopo avere pagato il worker e a lavoro finito, posso scegliere di dar un peso diverso ad un dato worker rispetto agli altri.

Due tipi di accordo:
+ **Accordo globale**: guardare quanto i worker sono in accordo fra loro:
	+ Se sono in accordo, i dati sono affidabili
	+ Se sono in disaccordo, dati non affidabili
+ **Accordo individuale**  (slide 65)
	+ Non guardo l'agreement generale di un worker ma considero ogni singolo worker e guardo quanto correla con l'aggregato degli altri worker (sullo stesso task): sostanzialmente se il worker è d'accordo con gli altri è un buon worker, se è in disaccordo con la maggioranza degli altri è un cattivo worker
	+ Posso quindi in seguito decidere di escludere una percentuale dei worker in base ai più piccoli o i più grandi

>[!question] Come misuro l'accordo (agreement)?
>Ovvero: quanto i vari worker che lavorano sullo stesso task danno la stessa risposta?
>+ NON si usano Aggregazione e Ground Truth
>+ Quello che si fa è guardare i singoli worker che stanno facendo la stessa task nella matrice con i worker come righe e i task come colonne
>+ Variabili che determinano il risultato:
>	+ numero di worker
>	+ Tipo di scala (nominale, binaria, ordinale, intervalli, rapporti)
>	+ Sparsità della matrice (non tutte le celle della matrice sono piene)

>[!tip]
>Accordo visto come un proxy/ un'approssimazione della qualità del lavoro
### Misure di accordo per scale nominali (non vediamo quelle ordinali)
+ 2 worker
	+ Percent(age) agreement
	+ Cohen's kappa
+ Più worker (n worker)
	+ Pairwise agreement
	+ Fleiss's kappa

#### Percent(age) agreement
Accordo percentuale
Si parte dalla solita matrice workers / tasks e la semplifichiamo
>[!example]
>Caso semplice: matrice di 2 workers non sparsa (tutti i task di tutti i worker hanno risposta) e con scala nominale binaria (Y/N):
>+ Trasformiamo la matrice in una matrice di confusione che contiene i dati su quante volte i worker hanno dato tutte le combinazioni possibili di risposte (W1_Y/W2_Y, W1_Y/W2_N, ecc...) 

>[!tip]
>Ad una matrice workers/tasks corrisponde una sola matrice di confusione, ad una matrice di confusione possono corrispondere più matrici workers/tasks.

Il Percent agreement quindi sostanzialmente somma tutte le volte in cui i workers hanno risposto allo stesso modo (diagonale della matrice di confusione) e divide per la totalità delle risposte (somma di tutti i valori della matrice di confusione).
![[materie/anno_2025-2026/social_computing/assets/Screenshot 2026-01-15 114151.png|400]]
Il risultato è la percentuale di accordo dei workers.
La misura è estendibile facilmente a più categorie (sempre scala nominale), basta aggiungere righe e colonne alla matrice di confusione
##### Svantaggi
+ Agreement by chance: se i worker rispondono a caso avranno comunque un accordo percentuale, che però non corrisponde al reale.
  Con l'aumento delle categorie l'accordo percentuale, se sparato a caso, viene comunque diminuito
+ Se i worker sanno che il 90% dei casi è N, faranno in modo di rispondere N al 90% delle domande, quindi l'accordo percentuale aumenta notevolmente
+ questa cosa funziona con 2 worker, altrimenti con più worker mi servirebbe una matrice di confusione a più dimensioni
+ Funziona solo con scale nominali

____
### Cohen's kappa
Restiamo sempre sul caso 2 workers, con scala nominale.
Corregge la formula del percent agreement inserendo anche il percent agreement atteso.
$$k = \frac{p\_0-p\_e}{1-p\_e}$$
+ $p\_0$ è il percent agreement osservato
+ $p\_e$ è il percent agreement atteso: è calcolato aggiungendo sulla matrice di confusione una riga e una colonna che contengano le somme dei valori delle colonne e delle righe corrispondenti ai valori delle task dati dai workers, e calcolando il percent agreement delle volte in cui entrambi hanno detto Y ed entrambi hanno detto N e il $p\_e$ sarà la somma di questi 2 agreement
>[!tip]
>$k$ può essere anche < 0 se il percent agreement atteso è maggiore del percent agreement ottenuto

____

### Fleiss's kappa
Sempre su scala nominale, ma estende ad $m$ workers e con $n$ categorie
Invece di guardare tutti i worker insieme, applico il pairwise agreement, quindi guardo le coppie di worker e guardo quale frazioni di coppie è in accordo di più
>[!example]
>Ho $m$ worker, le coppie di worker saranno $m(m-1)/2$
>Ricerco quindi la % di coppie in accordo.
>Esempio: ho 5 task e 4 worker, con tre categorie A, B, C
>+ $4\*3/2=6$ coppie
>+ Per ogni task guardo tutte le 6 coppie possibili e vedo la percentuale di coppie che ha risposto uguale (se ad esempio al primo task tutti hanno risposto A, il pairwise agreeement sarà 6/6)
>+ Infine si fa la somma di tutti i pairwise agreement (ad esempio $18/(6\*5)$) e si trova il kappa di Fleiss

#### Definizione generale
$$k = \frac{\bar{P}-\bar{P\_e}}{1-\bar{P\_e}}$$
(godo si skippa fino a slide 62)
(si skippa ulteriormente perché boh fino a slide 73)
___
#### Schema sulla ricerca della qualità delle task
+ Qualità 1: **Pre raccolta dati**
	+ Design delle task
	+ Ridondanza & Aggregazione
+ Qualità 2: **Mentre si raccolgono i dati**
	+ Teoria della misurazione
	+ Aggregazione reloaded
+ Qualità 3: **In seguito alla raccolta di dati**
	+ Accordo

>[!warning]
>Non esiste una soluzione finale da usare in tutti i casi.
>
