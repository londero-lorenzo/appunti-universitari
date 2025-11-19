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
(S + I = N)  --->  $\frac{dI}{dt} = \beta I(N-I)$  --->  $I(t)=\frac{N\*I\_0\*e^{\beta tN}}{N+I\_0\*(e^{\beta tN}-1)}$   con $I\_0$ numero degli individui infettati al tempo 0. Questa è la curva di crescita logistica:

![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-12 143421.png|350]]

>[!warning]
>All'inizio gli individui sono tutto suscettibili, col passare di t gli infetti crescono sempre di più finché non raggiungono il 100% sempre, senza scampo.

___
+ **SIR (susceptible/infected/recovered)**    ---> variante del modello SI
	+ Gli infetti possono guarire o morire
	+ Una volta che un host è guarito (o rimosso):
		+ Non possono più infettare
		+ non possono più essere infettati e non sono più suscettibili (restano in R)

**Equazioni**
$$\frac{dS}{dt}= -\beta IS$$

$$\frac{dI}{dt}= \beta IS - \gamma I$$
$$\frac{dR}{dt}= \gamma I$$
>[!tip]
>$\gamma$ definisce la probabilità di recovery di un infetto individuale in un lasso di tempo

**Grafico del modello SIR**

![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-14 103024.png|400]]

+ All'inizio tutti tranne 1 sono suscettibili, poi calano a favore degli infetti, che però dopo un po' cominciano a calare essendo sopraffatti dai recovered che non possono riammalarsi
+ Alla fine non ci saranno più infetti e quasi tutti saranno recovered ($< 100$%) e con pochissimi suscettibili (> 0%) pioché quando on ci sono più I non resta nessuno a contagiare i rimanenti S.
>[!tip]
>Un buon dato per capire quanto l'epidemia è stata importante è vedere il numero finale di recovered, ma anche se la curva degli infetti non è molto pronunciata vuol dire che è più difficile prendere la malattia piuttosto che guarire da essa.

**Commenti**:
+ Gli S decrescono monotonicamente
+ Gli R crescono monotonicamente
+ Gli I crescono inizialmente, per poi decrescere man mano che gli individui guariscono e vanno a 0 per $t\rightarrow \infty$ 

#### $R\_0$: Basic reproduction number
+ $R\_0=\beta/\gamma$
+ $R\_0$ è i numero medio di individui che I contagia prima di guarire/morire e $\beta$ e $\gamma$ misurano quanto i due "rubinetti" sono aperti (da S a I e da I a R)
+ $R\_0=\beta / \gamma$  = 1 marca la **soglia epidemica**, ovvero c'è epidemia se $R\_0 \geq 1$, ovvero si forma una componente gigante e l'epidemia esplode.

>[!tip]
>$R\_0 = \beta / \gamma \leq 1$ Non abbiamo epidemia in quanto gli I guariscono più in fretta di quanto gli S si ammalino.
>Il numero di I parte basso e diminuisce.

### Transizione epidemica

>[!definition]
>Transizione epidemica
>>Transizione fra regime epidemia e regime non-epidemia alla soglia $\beta = \gamma$  --> $R\_0 = \beta/\gamma = 1$

Transizione di fase brusca, improvvisa
>[!tip]
>Fenomeno analogo alla comparsa della giant component in G(n, p) per c >1

$S=1-e^{-cS}$   =       $r(t) = 1-e^{-\beta/\gamma \*r(t)}$ 

___

+ **SIS (susceptible/infected/susceptible)**
	+ Gli infetti che guariscono diventano suscettibili nuovamente
	+ Il modello SI è sostanzialmente una variazione dello SIS in cui il valore $\gamma$ è molto basso, vicino a 0

**Equazioni**
$$\frac{dS}{dt}= \gamma I - \beta IS$$
$$\frac{dI}{dt}= \beta IS - \gamma I = I(\beta N -\gamma) - \beta I^2$$
+ $\beta$ passaggio da S a I
+ $\gamma$ passaggio da I a S


**Grafico del modello SIS**

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-11-14 105718.png|400]]

+ Il numero di infetti si alza così come il numero di suscettibili si abbassa, per poi stazionarsi ad un valore (<100% e >0%)

___
#### Confronto curve degli infetti in SI-SIR-SIS

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-11-14 110046.png|400]]

___

+ **SIRS (susceptible/infected/recovered/susceptible)**
	+ Suscettibili si infettano, guariscono, sono immuni per un po' e poi tornano suscettibili

**Equazioni**
$$\frac{dS}{dt}= \lambda R - \beta IS$$
$$\frac{dI}{dt}= \beta IS - \gamma I$$
$$\frac{dR}{dt}= \gamma I - \lambda R$$

**Grafico del modello SIRS**

![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-11-14 110750.png|400]]

+ Grafico simile a SIR, ma i recovered non raggiungono mai la totalità, anzi dopo un po' tendono a diminuire e di conseguenza i suscettibili aumentano a loro volta, rendendo il grafico con una sorta di oscillazione dei valori all'aumentare del tempo, poiché l'epidemia è libera di continuare.

___

### Social contagion

**Idea**: Se un individuo vede un comportamento in un altro individuo, lo imita (adotta lo stesso comportamento), proprio come le epidemie.

Simile a guarire da una malattia può essere smettere di dire una barzelletta perché tutti dicono di saperla già.
+ Modello chiamato **ISR**
Da SIR a ISR --> 
+ Susceptible --> Ignorant (I)
	+ Individuo che non ha ancora ricevuto l'informazione (barzelletta)
+ Infected --> Spreder (S) (diffusore)
	+ Individuo che ha ricevuto l'informazione e la diffonde
+ Recovered --> Stifler (R) (soffocatore)
	+ Ha ricevuto l'informazione ma non la diffonde più (perché gli altri "la sanno già")

+ $\lambda$ tra I e S
+ $\alpha$ tra S e R

Anche se in realtà **Contagio fisiologico $\neq$ Contagio sociale**:
+ **Contagio fisiologico**:
	+ Contaminazione patogena
	+ Processo passivo (vengo contagiato)
	+ Basta un singolo I
	+ Transizione da I a R spontanea
+ **Contagio sociale**:
	+ Atto intenzionale
	+ Processo attivo (cerco l'informazione)
	+ Servono più di un individuo
	+ Transizione da S a R in seguito a interazione S+R o S+S

Diffusione dell'epidemia per i due modelli SIR e ISR:
+ SIR
	+ I+S $\rightarrow^\beta$ 2I
	+ I $\rightarrow^\gamma$ R
+ ISR
	+ I+S $\rightarrow^\lambda$ 2S
	+ S+R $\rightarrow^\alpha$ 2R
	+ S+S $\rightarrow^\alpha$ R+S  oppure  S+S $\rightarrow^\alpha$ 2R

**Equazioni**
+ Si adotta una approccio fully-mixed
$$\frac{dI}{dt}= -\gamma I S$$
$$\frac{dS}{dt}= \gamma I S - \alpha S [S+R]$$
$$\frac{dR}{dt}= \alpha S [S + R]$$
In un istante $t$:
$$I + S + R = 1$$ 
>[!tip]
>+ Passaggio da I a R in SIR è spontaneo e dipende solo dal numero di I e dal tasso / parametro $\gamma$ 
>+ Passaggio da S a R in ISR è non spontaneo e dipende sia dal numero di S e dal parametro $\alpha$ sia dal numero di R


Per ISR:
+ A tempo $+\infty$ non ci sono più spreader: $s\_\infty = lim\_{t\rightarrow \infty}s(t) = 0$ 
+ Gli ignoranti saranno tanti di meno quanti di più saranno gli stifler: $i\_\infty=e^{-(1+\lambda/\alpha)\*r\_\infty}$ 
+ Gli stifler saranno tutti gli altri: $r\_\infty= 1-e^{-(1+\lambda/\alpha)r\_\infty}$
+ $r\_\infty$ è la misura della **diffusione** (frazione di stiflers: infettati e poi recovered): quanto si è diffusa la barzelletta (reliability)

>[!tip]
>Non è esattamente uguale alle epidemie, in quanto non esiste più la soglia epidemica, esiste sempre un'epidemia sociale qualsiasi siano i valori dei parametri.
>La diffusione nel modello ISR raggiunge sempre la componente gigante, quindi si diffonde sempre in una frazione macroscopica della popolazione ($r\_\infty > 0$ sempre) 


___


>[!question] E le reti cosa centrano con le epidemie?

Questi modelli per epidemie si basano sull'assunzione:
+ Fully mixed
+ Tutti sono in contatto con tutti, rete completa
 Questo non è vero nelle reti reali
 >[!example]
 >Le piante non vanno in giro a contagiare altre piante lontane
 >Nella realtà ci sono gruppi sociale che rendono più probabile incontrare una persona piuttosto che un'altra.

#### Epidemie sulle reti

+ Necessita quindi un'assunzione più debole di prima: rete omogenea, non completa.
	+ Tutti i nodi hanno grado simile
	+ Ogni individuo viene a contatto con lo stesso numero di individui
+ Basic reproduction number $R\_0$ su rete omogenea (tutti i nodi hanno grado simile alla media):
	+ A inizio epidemia sono quasi tutti S
	+ Ogni I infetta un vicino S con probabilità $\beta$
	+ Ad ogni istante $t$ ogni I può transitare in R con probabilità $\gamma$ 
	+ Quindi:
		+ $\bigtriangleup I\_{t+1} = \beta [k] I\_t$    
		+ $\bigtriangleup R\_{t+1} = \gamma I\_t$ 
		+ Per avere epidemia deve essere $\bigtriangleup I\_{t+1} > \bigtriangleup R\_{t+1}$ ossia $\beta[k]I\_t > \gamma I\_t$
		+ Quindi $R\_0 = [k] \beta/\gamma$


>[!question] Come diminuire $R\_0=[k] \beta/\gamma$?
>+ Diminuire la contagiosità $\beta$ (mascherine, vaccino)
>+ Aumentare la velocità di guarigione $\gamma$ (cure)
>+ Diminuire il grado medio $[k]$ (lockdown, quarantene)

___

### Reti eterogenee
Nel mondo reale le reti sono eterogenee (Power law, Hub)

**Intuizione**: 
+ Gli hub si contagiano facilmente
+ E contagiano molti altri nodi
**Intervention**:
+ Vaccinazioni mirate
+ Paradosso degli amici

>[!example]
>Epidemia della mucca pazza.
>Si è distribuita molto grazie ai legami deboli, ad esempio tramite le persone come turisti che andavano a vedere le mucche perché il virus si diffondeva anche attraverso il terreno.
>In queto caso è critico restare sotto la soglia epidemica ()

>[!definition] 
>**Paradosso degli amici**:
>>Chiedere ad un nodo a caso di scegliere altri individui secondo loro più fragili e di vaccinarli.

>[!tip]
>Coefficiente di clustering alto per il modello ISR vuole dire incontrare spesso gente che "sa già la barzelletta".

![[materie/anno_2025-2026/social_computing/assets/Screenshot 2025-11-19 150144.png|350]]

Piccolo mondo si verifica tra 10^-1 e 10^-2 di probabilità nel grafico.
**Spiegazione:**
+ Per $p$ bassi:
	+ Rete molto clusterizzata, alto C, molti triangoli
	+ Spreaders diffondono sempre agli stessi
	+ Quindi passano in fretta fra gli stiflers, poca diffusione
+ Per $p$ alti:
	+ Rete con shortcut
	+ Spreaders diffondono anche in parti lontane
	+ Quindi il rumor si diffonde
+ Ovviamente di più per $[k]$ alti
$$\begin{cases} S+R \rightarrow^\alpha 2R \\ S+S \rightarrow^\alpha R+S \end{cases}$$

Su **reti eterogenee**?
Gli hub dovrebbero essere degli spreader efficientissimi perché infatti gli hub diffondono le malattie ed è facile che un rumor raggiunga uno hub e la diffusione diviene più alta.
>[!tip]
>Però dati sperimentali mostrano che $r\_\infty$ è più alto su reti omogenee che su reti eterogenee

>[!question] Perché questo?

Non è vero che l'informazione si diffonde meno su reti eterogenee
+ Per le malattie gli hub aiutano la diffusione
+ Per i rumor no
+ Perché?
	+ è facile che un rumor raggiunga uno hub, e a quel punto la diffusione è molto alta
	+ Ma se hub diventano spreader, allora ci saranno subito molte interazioni spreader-spreader, che porteranno a stifler, e poi molte interazioni spreader-stifler, idem
Gli hub passano da spreader a stifler prima di contagiare molti nodi:
A quel punto gli hub-stifler frammentano la rete --> isolano i nodi --> i nodi isolati restano ignorant.

è quindi possibile modellare la diffusione di rumors con modelli analoghi a quelli per le epidemie. Ha senso quindi parlare di contagio sociale, **contagio sociale $\neq$ contagio fisiologico**:
+ Processo attivo vs. processo passivo
+ Atto intenzionale vs. contaminazione patogena
+ Decido io di adottare una moda vs. non decido io di ammalarmi
+ transizione da S a R in seguito a interazione S+R o S+S vs. transizione spontanea sa I a R

#### Riassunto sulle epidemie

Modelli: SI, SIR, SIS, SIRS
	Soglia epidemica $R\_0$
Contagio sociale IST
	No soglia epidemica

Reti
+ Epidemie
	+ Rete omogenea (G(n, p)): $R\_0=[k] \beta/\gamma$ 
	+ Rete eterogenea: hub, vaccinazione, paradosso degli amici
+ Contagio sociale
	+ Rete WSSW
	+ Rete eterogenea: ruolo "strani degli hub"

**Modelli sensati ma non perfetti   --> necessità di studiarne altri.**

___

### Modello di Morris (Direct benefit)

+ Basato su benefici diretti (che cosa ci guadagno)

>[!tip]
>Modelli basati su:
>+ Informazioni (faccio X perché vedo gli altri)
>+ Benefici diretti (faccio X perché mi conviene rispetto a non farlo)

>[!example]
>Uso Whatsapp al posto di Telegram perché tutti usano whatsapp e quindi **mi conviene** usarre quello per poter comunicare.

Idea:
+ Quindi una decisione arriva ad un nodo ed il nodo stesso decide se adottarla o meno. Solitamente se i nodi vicini l'hanno adottata la adotta anche lui.
>[!tip]
>Per un nodo, il beneficio di adottare un comportamento cresce al crescere del numero di vicini che lo adottano

#### Teoria dei giochi
+ Ogni nodo sceglie fra 2 possibili comportamenti A e B
+ Se due nodi sono collegati da un arco sono incentivati ad adottare comportamenti uguali
	+ Se v e w adottano entrambi A --> payoff a>0
	+ Se v e w adottano entrambi B --> payoff b>0
	+ Se v adotta A e w adotta B --> payoff 0

Matrice dei payoff presente per ogni arco.

Il payoff totale di un nodo v sarà la somma di tutti i payoff in base alle scelte svolte per qualsiasi arco. Lo scopo di tale nodo è massimizzare tale payoff.

>[!question] Se alcuni vicini adottano A e altri adottano B, quale mi conviene adottare?
>Dipende da:
>+ payoff a
>+ payoff b
>+ numero (o %) vicini che scelgono A
>+ numero (o %) vicini che scelgono B

+ $p$ = % vicini che adottano A
+ $1-p$ = % vicini che adottano B
+ $d$ = numero di vicini
+ Regola di decisione:
	+ $v$ adotta A solo se: $p \geq \frac{b}{a+b}$

>[!definition]
>Regola
>> Se almeno una frazione q  ($q = \frac{b}{a+b}$) dei miei vicini adotta A, allora lo faccio anche io (dove q dipende dai payoff).

##### Equilibri
+ tutti adottano A
+ tutti adottano B

>[!question] Come si passa da un equilibrio all'altro?

>[!example]
>tutti stanno adottando B ma alcuni nodi per motivi extra-payoff adottano A (altri vantaggi magari) e possono poi convincere altri B a cambiare e poi altri ancora a cascata. Alla fine possono farlo per tutta la rete.

+ Il processo è **monotono**: dopo la scelta di cambiare il nodo non torna indietro
+ Il processo si ferma quando:
	+ o tutti passano ad A
	+ o nessuno più vuole passare ad A

>[!question] Quando l'equilibrio non viene ribaltato completamente cosa succede e perché?
>Si passa da B ad A se almeno 2/5 dei vicini scelgono A. Se questo non accade il cambiamento da B ad A si ferma.
>Ad esempio se sono presenti dei sottografi completi difficilmente verranno convinti avendo solo un collegamento con il corpo della rete.

+ Si può svolgere un'intervention per far ripartire lo switch del comportamento cercando di far adottare quel comportamento ad un nodo "strategico", che permetterebbe di far ripartire lo switch di tutta la rete.
+ **Cascata di adozioni di A**: molti nodi stanno passando ad A
+ **Cascata completa**: tutti i nodi sono passati ad A

Differenze con l'ICM (Independent Cascade Model):
+ ICM è stocastico
+ Questo invece è deterministico
+ l'Intervention è di natura diversa nei due modelli

#### Intervention
Strategie per far passare ad A:
+ Migliorare il payoff di A
+ Convincere alcuni nodi chiave per far ripartire la reazione a catena (tramite regali, omaggi,...)

#### Cluster di densità $p$
Se ogni nodo che vi appartiene ha almeno una frazione $p$ dei suoi vicini nel cluster
+ "comunità coesa"

>[!tip]
>I cluster fermano le cascate. Anzi una cascata si ferma **solo se** c'è un cluster.

#### Teorema di Morris
+ Soglia q per adottare A
+ (1) Se il resto della rete contiene un cluster di densità > 1-q, allora non ci sarà una cascata completa
	+ **Dimostrazione**: 
		+ Sia $v$ il primo nodo nel cluster che adotta A al tempo $t$
		+ Allora a $t-1$: 
			+ c'è almeno una frazione $q$ di vicini di $v$ adottanti A
			+ nessuno nel cluster adotta A
			+ $v$ aveva almeno una frazione $q$ di vicini fuori dal cluster
		+ Il cluster di densità > 1-q --> >1-q vicini di $v$ devono essere nel cluster --> è impossibile averne q fuori --> assurdo. --> niente $v$ --> no complete cascade.
+ (2) Se non c'è una cascata completa, allora c'è un cluster di densità > 1-q
	+ **Dimostrazione**:
		+ Massa cumplica, varda sue slaid.


#### Ancora Intervention
Quindi per far ripartire una cascade bloccata posso:
+ Aggiungere archi fra cluster diversi (rinforzo i legami deboli)
+ Togliere archi all'interno di un cluster (indebolisco la densità dei cluster bloccanti)
Per bloccare una cascade:
+ Togliere archi fra cluster diversi (indebolisco i legami deboli)
+ Aggiungere archi all'interno dei cluster (rinforzo i cluster bloccanti)

>[!tip]
>Cluster e cascade sono due facce dalle stessa medaglia.
>+ Cluster bloccano le cascade
>+ Se una cascade si blocca ---> c'è un cluster
>+ I cluster però non bloccano le malattie o il contagio sociale

#### Awareness, adoption, weak ties
+ Weak ties: legami deboli
	+ Conoscenze non intime (es. utili se devo trovare lavoro)
+ Utili per diffusione informazioni (o malattie)
	+ **Awareness**, semplice consapevolezza
+ Molto meno utili per diffusione mode, innovazioni
	+ **Adoption**, adozione di un comportamento
+ **Awareness $\neq$ Adoption** 
>[!example]
>È facile raccontare una barzelletta ad uno sconosciuto. È difficile convincerlo a fare la rivoluzione.

#### Diffusioni
+ Movimenti sociali
	+ Diffusione lenta e locale
	+ Adoption
	+ soglia alta (mi costa fare la rivoluzione)
	+ NON sfruttano weak ties
+ Barzellette, meme
	+ Diffusione rapida e planetaria
	+ Awareness
	+ soglia bassa (mi costa poco condividere un video)
	+ sfruttano weak ties

#### Riassunto modello di Morris
+ Basato su Benefici Diretti
+ Diverso dai modelli di contagio sociale e malattie
+ Un nodo **decide** di adottare un comportamento perché **gli conviene**, non perché pensa che sia giusto o per imitare
+ Cascade complete, legame con cluster