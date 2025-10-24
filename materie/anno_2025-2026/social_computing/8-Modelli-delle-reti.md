---
title: 8-Modelli-Delle-Reti
aliases:
  - 8-Modelli-Delle-Reti
tags:
  - università
  - materie
  - anno-2025-2026
  - social-computing
  - 8-Modelli-delle-reti
created: 2025-10-24
description: (INCLUDE SLIDE 8-9)
---
# Modelli delle reti

>[!question] Ci sono pattern sottostanti riguardo ai legami di amicizia?
>Sì, ci sono dei modelli di rete sociale.

>[!question] Che processi stocastici (casuali) di creazione degli archi posso immaginarmi?
>Varie possibilità che vedremo in questo capitolo

Utilità dei modelli che generano grafi: 
+ Possiamo ipotizzare che gli stessi processi generativi siano alla base delle reti reali
+ Possiamo studiarle in modo più efficiente ed efficace
+ Possiamo classificare anche le reti in varie tipologie che consentono di giustificare e spiegare fenomeni.

4 modelli classici:
+ **Regolari**
+ **Reti casuali**
+ **Piccolo mondo**
+ **Scale-free**

## Regolare

Reti con una tipologia regolare, non casuali (stocastiche).

>[!example]
>Forme geometriche come il nodo centrale al centro geografico della rete con tutti gli altri nodi attorno oppure in maniera circolare, o a griglia, o a rete triangolare.


>[!tip]
>Nella rete circolare la distanza media è la metà dei nodi che compongono la rete, ad esempio se la rete è di 10 nodi, la distanza media tra due nodi sarà 5, cosa che sicuramente non rappresenta un **piccolo mondo** con questi modelli regolari

Quindi questi modelli hanno:
+ **Distanze** medie spesso grandi.
+ **Coefficiente di clustering** è spesso alto (come si vede sul reticolo triangolare)
+ **Distribuzione dei gradi** è tipicamente con un picco, e capita spesso che tutti i nodi abbiano lo stesso grado.
+ **Connettività** spesso completa e totale.

>[!warning]
>Raramente le reti nel mondo reale seguono questo modello.


___
## Reti casuali

Idea:
+ Ogni arco possibile in una rete ha una probabilità $p$ di esserci, quindi 'tirando una moneta' decido se ci sarà quell'arco nella mia rete, e così avanti per tutti gli archi, ogni presenza di un arco indipendente dagli altri.
+ Nei social media corrisponderebbe a dire che le amicizie si formano totalmente a caso, cosa che non è proprio veritiera (ma vedremo che è comunque un modello utile).

Studi:
+ Connettività
+ Diametro
+ Formazione Giant Component (poi vediamo)
+ Limite termodinamico sui grafi grandi, ovvero cosa succede quando il numero di archi è tendente all'infinito.


2 diversi modelli di grafi casuali:
+ G(n, m)
+ G(n, p)

### G(n, m)

>[!definition]
>G(n, m)
>>Grafo con n nodi e con una disponibilità di m archi piazzati a caso, solitamente senza multi-archi (due archi tra gli stessi nodi) e auto-archi (verso sé stesso).
>>Solitamente su grafi indiretti.
>>
>>Altra definizione equivalente: Scelgo un grafo a caso fra tutti quelli aventi n nodi e m archi.

Puntualizzazioni: 
+ Si studiano i grafi grandi per studiare il $lim\_{n \rightarrow \infty}$ e prendo il caso medio quindi analizzando virtualmente infiniti grafi casuali.
+ Diametro di G(n, m) è la media tra tutti i grafi G(n, m)
+ Grado medio sarà definito come: $2m/n$, in quanto ci sono 2 estremità per ogni arco diviso per la totalità dei nodi.
+ Non ci sono casi speciali (poco interessanti)
+ Di solito le distribuzioni sono con un picco e non a coda lunga come quelle reali caso tipico è rappresentativo per tutte)

### G(n, p)

>[!definition]
>G(n, p)
>>Genero o non genero un arco in base alla probabilità di esistenza di ogni singolo arco, sempre con gli archi indipendenti gli uni dagli altri. Invece di fissare il numero di archi, fisso la probabilità di esistenza degli archi.

+ In G(n, p) il **numero di archi** che in G(n, m) era ESATTAMENTE m è IN MEDIA: $p\*n(n-1)/2$

+ **Grado medio** lo ricavo considerando tutte le estremità degli archi e dividendo per il numero di nodi: $\frac{2\*[m]}{n}=(n-1)p$

>[!example] Differenza G(n, m) / G(n, p)
>Ad esempio un grafo G(n, m) = G(4, 2) non sarà mai connesso, mentre un grafo G(n, p) = G(4, 1/3) PUO' essere connesso.

**Numero di archi medio**: 
$$[m]=\frac{n(n-1)}{2}p=\binom{n}{2}p$$
**Distribuzione dei gradi** (stesso per G(n, p) e G(n, m)): 
+ Tutti i nodi sono uguali in questo grafo, senza privilegi, quindi sarà raro che un nodo possa ricevere maggiori archi o minori archi degli altri, rendendo la distribuzione simile alla **distribuzione di Poisson**, con la probabilità di avere un grado diverso da quello medio che si abbassa subitamente allontanandosi dal valore medio.
  Non si trovano cosiddetti hub, ovvero nodi con un alto numero di archi collegati. (intuitivamente aggiungendo archi a caso capita raramente di ri-aggiungere allo stesso nodo, soprattutto $n \rightarrow \infty$)
  Le distribuzioni reali però abbiamo visto avere una distribuzione a coda lunga, lontana da quella a campana dei grafi casuali.
+ Grado medio:
  $$[k]=\frac{2[m]}{n}=(n-1)p$$

**Coefficiente di clustering** (probabilità che i vicini di un nodo siano vicini tra loro):
+ Sarà molto basso, e sarà tendente a 0 più $n$ tende a infinito: $C=\frac{c}{n-1}$  con $c$ che rappresenta il grado medio

>[!tip] Pensiero fino ad ora
>Una prima conclusione è che queste reti non vadano bene per modellare reti reali ma hold on diamo fiducia ancora un po'.

>[!question] Grafo G(n, p) è connesso?
>In generale no. In genere ci sono diverse componenti connesse isolate.
>

Però questa non è la domanda giusta, in quanto:
>[!example]
>Se ad esempio ho 50 miliardi di nodi e sono tutti connessi tranne 1 la rete praticamente è connessa, quindi la domanda sulla connettività non è giusta.

La domanda giusta è:
>[!question] Grafo G(n, p) è connesso all'incirca/ più o meno/ in pratica?

Che equivale a:
>[!question] Esiste una componente gigante?
>Ovvero se esiste una componente che comprende quasi tutti i nodi, o almeno la maggior parte rispetto alle altre componenti.

Pensando a due casi estremi:
+ p=0, nessun arco viene generato e il grafo è disconnesso e la componente più grande sarà grande 1.
+ p=1, tutti gli archi vengono generati e il grafo è completo e connesso e la componente più grande sarà grande n.
Differenze tra i due casi:
+ Qualitativamente nel primo è costante all'aumentare di n, nel secondo no, aumenta con n

>[!definition]
>Componente gigante (GC)
>>Definizione più precisa di componente gigante:
>>Una GC è una componente connessa, la più grande della rete
>>GC ha una grandezza che cresce in proporzione a $n$ (si fa infatti il $lim$ $n \rightarrow \infty$)

Una rete ha una CG se ha una frazione finita di $n$ connessa (90%, 50%, ma anche ad esempio 10%, se tutte le altre componenti connettono un numero minore del 10% dei nodi. La GC deve rappresentare in pratica la frazione più grande).

>[!warning]
>Il grado medio dei nodi per avere una componente gigante è $c=1$.
>

$c=1$ è effettivamente un valore controintuitivo incredibilmente basso, ma in effetti se ogni nodo connesso presenta due archi che connettono altri due nodi, ci saranno anche nodi che non possiedono alcun arco, e quindi di media il grado sarà 1.
Equivalente ad un valore $c=1$ è la probabilità $p$ che $c$ sia 1: $p=c/(n-1)=1/(n-1)$           $\leftarrow$ (ricordare per sicurezza)

Quindi se $c \geq 1 \rightarrow$ componente gigante: grafo 'quasi connesso' 

**Transizione di fase:**
+ In reti reali c'è una transizione di fase (cambiamento brusco) in cui appare la GC. se $c < 1$ no GC, se $c\geq1$ la connettività aumenta velocemente

>[!tip] Attenzione
>E' $n$, che varia, per $c$ fissato:
>- Fisso $c\geq1$, faccio lim $n\rightarrow \infty$ e scopro che c'è GC.
>- Fisso $c<1$, faccio lim $n\rightarrow \infty$ e scopro che non c'è GC.

Riassuntino efficace dei GC nei grafi casuali:
+ Per $c<1$: Ci saranno cluster piccoli e isolati
+ Per $c=1$: Appare la Giant Component
+ Per $c>1$: Quasi tutti i nodi sono connessi
![[materie/anno_2025-2026/social_computing/assets/Immagine 2025-10-24 225246.png|300]]

___
