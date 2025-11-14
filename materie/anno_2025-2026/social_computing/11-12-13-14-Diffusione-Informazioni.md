---
title: "11-12-13-14-Diffusione-Informazioni"
aliases: ["11-12-13-14-Diffusione-Informazioni"]
tags: [università, "materie", "anno-2025-2026", "social-computing", "11-12-13-14-Diffusione-Informazioni"]
created: 2025-11-08
---
# Diffusione delle informazioni

le pubblicità non dipendono solo dalle possibilità economiche delle aziende.

>[!example]
>Oreo durante il blackout del Super Bowl di 30 minuti ha twittato "Rimasti senza luce, nessun problema potete anche inzupparlo al buio". Strategia questa che ha reso subito virale il tweet e di conseguenza l'azienda Oreo.

#### Esempi di diffusione di informazioni
+ Barzellette
+ Rumors (possono anche essere fake news)
+ Video virali
+ Meme

Mezzo principale delle fake news sono i social.

>[!definition]
>Diffusione delle informazioni
>>Processo per cui un'informazione si diffonde e raggiunge altri individui, ma anche un comportamento (come l'adozione di una tecnologia piuttosto che un'altra).
>>Ci sono metodi per studiare queste diffusioni: sociologia, epidemiologia, statistica,...

##### Temi comuni delle diffusioni:
+ **Mittente**: uno o pochi mittenti che iniziano il processo
+ **Destinatari**: Uno o molti destinatari che ricevono l'informazione (insieme dei destinatari di solito più grande dell'insieme dei mittenti)
+ **Mezzo**: mezzo tramite cui la diffusione avviene (ad esempio retweettare)
+ **Intervention**: processo di interferire col processo di diffusione delle informazioni in atto (ad esempio se voglio che un'informazione venga maggiormente diffusa, o bloccare la diffusione di un'informazione)

#### Modelli per la diffusione delle informazioni
+ Herd behaviour (comportamento del gragge)
+ Information cascade
+ Epidemics (e social contagion)
+ Modello dei benefici diretti (Morris)

## Herd behavior

Idea easy: "Si tende ad imitare quello che fanno gli altri"

>[!example]
>+ Ordino in un ristorante A, arrivato lì vedo che A è vuoto e invece dall'altra parte della strada il ristorante B è pieno nonostante abbiano lo stesso menù. Secondo questo modello sceglierei di andare nel ristorante B perché è quello che tutti gli altri hanno fatto.
>+ Ad un asta se vedo una persona offrire molto io sarò più tentato di offrire a mia volta di più pensando che il tipo sappia il valor elevato dell'oggetto venduto.
>

#### Caso di studio
+ C'è un'urna con tre palline dentro che possono essere rosse o blu. ogni persona deve estrarre una pallina e dire qual è il colore che sta in maggioranza dentro l'urna: o blu o rosso. 
  Il primo studente estrae blu e dice blu.
  Il secondo studente osserva blu e dice blu.
  Il terzo studente se osserva rosso, ma i due precedenti hanno detto blu, dirà blu.
  Il quarto studente qualsiasi cosa peschi dirà blu perché tutti precedentemente hanno detto blu.

+ Probabilità che sia blu =probabilità che sia rosso = 1/2
+ P(blue | maggioranza-blu) = P(red | maggioranza-red)= 2/3
+ Bayes: $p(C|I)=\frac{p(C)\*p(I|C)}{p(I)}$ 
+ Quindi P(maggioranza-blu | blu) = (2/3 x 1/2) / (1/2) = 2/3 > 1/2
+ Quindi il primo studente dovrebbe indovinare blu se pesca blu e anche il secondo studente. 
+ Quindi **razionalmente** il terzo studente dovrebbe indovinare blu anche se vede rosso, in quanto P(maggioranza-blu | blue, blue, red) = (4/27 x 1/2) / (1/9) = 2/3 > 1/2

>[!tip]
>Razionalmente non istintivamente. La scelta da fare è quella razionale.


#### Herding Intervention
Intervention nel modello di herding. L'herding può essere interventato ad esempio rilasciando informazioni private che non erano accessibili prima (ad esempio facendo vedere la pallina che si è estratto nell'esempio)
>[!tip]
>La prima persona che fa notare l'errore che il gruppo sta commettendo, l'herd behavior viene interrotto.


#### **Riassunto Herd behavior**
+ Basato sull'osservazione di azioni/comportamento
+ Razionale, non istintivo
+ è un risultato/effetto, non un'operazione di base
+ rete quasi completa: vedo i comportamenti di tutti (unidirezionale: vedo tutti e soli i "precedenti")
+ Poco realistico/interessante
+ Comportamento di gregge è abbastanza facile e si può rompere (intervention) in modo semplice.

___

## Information cascade

Tipicamente gli user repostano ciò che è stato postato da altri, e l'informazione diventa diffusa tra gli amici a cascata. 
Information cascade:
+ Ognuno vede ciò che fanno/decisioni dei vicini, localmente. 
+ Herd behavior invece vedeva globalmente.

>[!example]
>Hotmail ad esempio crebbe in iscritti molto velocemente grazie all'aggiunta in appendice in ogni mail mandata di un link per poter creare il proprio account Hotmail.


#### Assumpion per modelli cascade
+ Un nodo può influenzare solo i nodi a cui è connesso
+ Decisioni binarie
+ Singoli nodi possono essere:
	+ Attivi (aderiscono alla decisione adottata)
	+ Non attivi (non aderiscono alla decisione)
+ La rete è un grafo diretto. ("Follow" su X)
+ Non si torna indietro (Se aderisco a hotmail non posso disiscrivermi)

### Independent Cascade Model (ICM)
+ Basato sul mittente
+ Ogni nodo ha un'unica occasione di attivare i suoi vicini, subito dopo la sua attivazione
+ In ICM, i nodi che sono attivi sono mittenti e i nodi che vengono attivati sono riceventi.
##### Algoritmo ICM
>[!warning]
>+ Il nodo attivato al tempo $t$ ha **una sola** possibilità (in base ad una probabilità $p\_{vw}$) di attivare i suoi vicini al tempo $t+1$.
>+ $p\_{vw}$ può essere differente per paia di nodi differenti.
>+ L'attivazione può avvenire solo al tempo $t+1$

Questo modello cerca di rispondere a questa domanda:
>[!question] Come faccio a scegliere i nodi per massimizzare la mia cascata, ovvero la diffusione delle informazioni?
>
>

>[!example]
>Con un limite di budget per una pubblicità voglio sapere come raggiungere una grande fetta di persone.
>In base ai nodi che attacco, esse attivano a loro volta (con un certa probabilità) i loro vicini. Quindi i nodi da attivare inizialmente devono essere accurati e con un ampio numero di vicini che non intaccano con i vicini di altri nodi attivati in modo da massimizzare la crescita della cascata.

>[!problem]
>Si tratta quindi un problema di ottimizzazione.
>+ Dato un paramentro k (budget)
>+ Trovare un set iniziale S per cui |S|=k, che massimizza $f(S)$, con $f$ funzione di diffusione. 

>[!definition]
>Maximizing the Spread of Cascades
>>Problema di trovare un piccolo set di nodi in una rete sociale tali che la loro diffusione aggregata nella rete sia massimizzata.


#### Rendere il problema deterministico
+ Rendere randomiche le attivazioni
+ Generare i numeri random per tutti gli archi, all'inizio del processo ICM
+ Nondeterministic/random --> deterministic

##### Proprietà $f(S)$
+ Non negativa 
+ Monotona: $f(S+v)\geq f(S)$ 
+ Submodulare: Se N è un set finito, la funzione del set è submodulare solo e solo se $$f:2^N \rightarrow R,\forall S \subset T \subset N, \forall v \in N \setminus T, f(S+v)-f(S)\geq f(T+v)-f(T)$$ ovvero "S ci guadagna di più di T", "i sottoinsiemi ci guadagnano di più".

Possiamo usare un algoritmo greedy: 
+ iniziamo con un set vuoto S
+ per k interazioni ad ogni step aggiungiamo ad S il nodo $v$ che massimizza $f(S \cup {v}) - f(S)$ 
+ l'algoritmo greedy fornisce un'approssimazione di (1-1/$e$)
+ Il set S risultante attiva almeno (1-1/$e$)=63% del numero di nodi che ogni set S di grandezza k può attivare.

#### Intervention cascade
+ **Limit(increase)** numero di out-links (disconnettere nodi porta a non attivarne altri)
+ **Limit(increase)** numero di in-links (ridurre la possibilità di essere attivato da altri)
+ **Decrease(increase)** la probabilità di attivazione $p\_{vw}$ (ridurre la possibilità di attivare altri)

___

## Epidemics models

>[!definition]
>Epidemics
>>Descrive il processo con il quale una malattia viene diffusa.

**Componenti:**
+ **Un elemento patogeno:** virus infettante, virus informatico, tweet che viene retweettato
+ **Una popolazione di host:** umani, animali, piante,...
+ **Un meccanismo di diffusione:** respirare, bere, sessare,...

>[!scopo]
>Provare a modellare la diffusione di malattie contagiose e trasferirle nel mondo digitale.

##### Differenza con Herd behavior:
+ In herd behavior tutti sono in contatti con tutti.
+ Nei modelli epidemici tutti potrebbero contattare tutti ma non si sa con chi si è stati in contatto.
+ Quindi diversamente dall'herding, le connessioni esistono ma sono sconosciute

### Metodi di analisi delle epidemics:
+ Metodo **Fully-mixed**
	+ analizza solo i gradi a cui ciascun host viene infettato e guarito, evita di considerare le informazioni della rete
+ Usando **Contact Network**
	+ Un grafo dove i nodi rappresentano gli host e gli archi rappresentano le interazioni tra questi host
>[!example]
>Per il covid-19 gli host che sono connessi vuol dire che respirano la stessa aria.

I metodi assumono che:
+ non ci sono informazioni dalla contact network
+ Il processo con il quale gli host vengono infettati è sconosciuto

### Modelli epidemici
+ **SI (susceptible/infected)**
	+ suscettibili possono venire infettati
	+ infettati non guariranno mai. Possono infettare i suscettibili
	+ S(t) numero di suscettibili al tempo t
	+ I(t) infettati al tempo t
	+ $s(t)=S(t)/N$
	+ $i(t) = I(t)/N$
	+ $\beta$ è la probabilità di contatto (ovvero infezione)
	+ $N=S(t)+I(t)$
	+ $1=s(t)+i(t)$
>[!tip]
>Al tempo t un infetto incontrerà $\beta N$ persone e infetterà $\beta S$ di loro. La variazione di individui che diventerà infetta è data dalla moltiplicazione $\beta I S$ nel time step successivo.

**Equazioni**:
+ Ad ogni time step la variazione del numero di individui in S e I è di $\beta IS$ :
  $$\frac{dS}{dt}= -\beta IS$$$$\frac{dI}{dt}=\beta IS$$ 
(S + I = N)  --->  $\frac{dI}{dt} = \beta I(N-I)$  --->  $I(t)=\frac{N\*I\_0\*e^{\beta tN}}{N+I\_0\*(e^{\beta tN}-1)}$   con I_0 numero degli individui infettati al tempo 0. Questa è la curva di crescita logistica:

![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-12 143421.png|350]]

>[!warning]
>All'inizio gli individui sono tutto suscettibili, col passare di t gli infetti crescono sempre di più finché non raggiungono il 100% sempre, senza scampo.

___
+ **SIR (susceptible/infected/recovered)**    ---> variante del modello SI
	+ Gli infetti possono guarire o morire
	+ Una volta che un host è guarito (o rimosso):
		+ Non possono più infettare
		+ non possono più essere infettati e non sono più suscettibili (restano in R)
+ SIS
+ SIRS
