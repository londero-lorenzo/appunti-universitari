---
title: "Algebra Relazionale"
aliases: ["Algebra Relazionale"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "algebra-relazionale"]
created: 2026-03-12
---
R(nome, gelato)
dom(nome)={Mario, Marco, Anna,...} |dom(nome)|=N    
dom(gelato)={cioccolato, panna, ...} |dom(gelato)|=M
|dom(nome) x dom(gelato)|=NxM

$\overline{S}=U \backslash S$
$\overline{R}=(dom(nome)xdom(gelato))\backslash R$

$S=(A\_{1}, A\_{2})$
$|dom(A\_{1})|=\infty$
$|dom(A\_{2})|=N$

>[!tip]
>Non può esistere l'operazione di complemento perché parte da un oggetto finito e arrivare ad una relazione infinita e non ho la proprietà di chiusura, quindi non può essere la complementazione

chi_arriva_prima

| x   | y   |
| --- | --- |
| b   | a   |
| c   | a   |
dom(x)=dom(y)={a,b,c}

chi_arriva_dopo=(dom(x) x dom(y)) \ chi_arriva_prima


# Oprazioni
-  Unary Relational Operations
	- SELECT (symbol: σ (sigma))
	- PROJECT (symbol: π (pi))
	- RENAME (symbol: ρ (rho))
- Relational Algebra Operations From Set Theory
	- UNION (∪), INTERSECTION (∩), DIFFERENCE (or MINUS, −)
	- CARTESIAN PRODUCT (×)
- Binary Relational Operations
	- JOIN (▷◁, note that several variations of JOIN exist)
	- DIVISION
- Additional Relational Operations
	- OUTER JOINS
	- AGGREGATE FUNCTIONS (These compute summary of information: for example, SUM, COUNT, AVG, MIN, MAX)

## SELECT
- operatore unario 
- ritorna in output una relazione
- agisce come un **filtro**
- mantiene solo le tuple che soddisfano quella condizione
>[!example]
>Seleziona le tuple EMPLOYEE il cui numero di dipartimento sia 4:
>- $\sigma\_{DNO=4}(EMPLOYEE)$
>Seleziona le tuple di employee il cui salario è maggiore di 30.000$:
>- $\sigma_{SALARY>30.000}(EMPLOYEE)$

In generale: $\sigma_{\langle selection\;condition\rangle}(R)$
- sigma: denota l'operatore select
- selection condition è l'espressione booleana specificata sugli attributi della relazione R, dove ogni termine è nella forma:
	- $\langle attribute\;name \rangle$ $\langle comparison\;op\rangle$ $\langle constant \;value\rangle$
	- $\langle attribute\;name \rangle$ $\langle comparison\;op\rangle$ $\langle attribute \;name\rangle$

## PROJECT

- denotare una lista di attributi da tenere nella relazione di output
- crea un partizionamento verticale
	- lista degli attributi specificati è mantenuta in ogni tupla
	- gli altri scartati
>[!example]
>Lista di ogni nome, cognome e salario di ogni dipendente:
>- $\pi_{LNAME,FNAME,SALARY}(EMPLOYEE)$

In generale: $\pi_{\langle attribute\;list \rangle}(R)$
- $\pi$ : rappresenta operazione project
- $\langle attribute\;list\rangle$: lista di attributi 
- ordine degli attributi è quello specificato nella lista
- Project rimuove ogni tupla duplicata
- il grado dell'operazione equivale al numero degli attributi nella lista
- la \*\*cardinalità\*\* nella proiezione $\pi_{\langle list \rangle}(R)$ è sempre \*\*minore o uguale\*\* al numero di tuple in R

>[!warning] PROJECT non è commutativa:
>$\pi_{\langle list1\rangle}(\pi_{\langle list2\rangle}(R))=\pi_{\langle list1\rangle}(R)$ finche $\langle list1 \rangle \subseteq \langle list2 \rangle$

## Espressioni
- catene di operazioni in algebra
Ricava il nome, cognome e salario di ogni impiegato che lavora nel dipartimento 5:
1. $\pi_{FNAME, LNAME, SALARY}(\sigma_{DNO=5}(EMPLOYEE))$
2. $DEP5_EMPS\leftarrow \sigma_{DNO=5}(EMPLOYEE)$
	1. RESULT $\leftarrow \pi_{FNAME, LNAME, SALARY}(DEP5_EMPS)$

## RENAME
- operatore denotato da $\rho$
- rinominare gli attributi della relazione o del nome della relazione:
	- utile quando una query richiede operazioni multiple
	- necessario in alcuni casi (JOIN)
- cambiare entrambi nome relazione a S e il nome dell'attributo a B1,B2, ... Bn: $\rho_{S(B1,B2, ... Bn)}(R)$

## UNION
- denotata da $\cup$
- risultato di $R\cup S$ è una relazione che include tutte le tuple che sono sia in R o in S o in entrambe
	- degree(R)=degree(S)=degree(R $\cup$ S)
- tuple duplicate sono eliminate
- S e R devono essere di tipi compatibili

## SET DIFFERENCE
- simbolo: -
- due insiemi R e S faccio R - S ottengo tutte le istanze che stanno in R ma non in S
### Proprietà di UNION, INTERSECT e DIFFERENCE
- union e intersezione sono commutative
- unione e intersezione trattate come operazioni n-arie applicabili a ogni relazione dato che sono entrambe associative
	- R $\cup$ (S $\cup$ T) = (R $\cup$ S) $\cup$ T
	- (R $\cap$ S) $\cap$ T = R $\cap$ (S $\cap$ T)
- set difference non è ne commutativa ne associativa

### Esercizio
Impiegato che NON hanno persone a carico
$\{i \in I | \forall \; c$ persona\_a\_carico$(i, c)\}$  I+c almeno 1 persona a carico
         (DEPENDENT)
$\{ i \in I \; | \; \exists \; c \textrm{ persona carico}(i,c)\}$

CANDIDATI $\leftarrow$ $\Pi_{SSN}$(EMPLOYEE)
NO\_GOOD(SSN) $\leftarrow$ $\Pi_{SSN}$(DEPENDENT)

R$\leftarrow$ CANDIDATI - NO\_GOOD

## CARTESIAN PRODUCT
- usato per combinare tuple da due relazioni in modo combinatorio
- $R(A_1, A_2, ... A_n) \times S(B_1, B_2, ..., B_n)$
- Risultato: $Q(A_1, A_2, . . . , A_n, B_1, B_2, . . . , B_m)$ in \*\*questo ordine\*\*
- la relazione ha una tupla per ogni combinazione di tuple  una da R e una da S
- se $R=n_R$ tuple e $S=n_S$ tuple allora $R\times S$ avrà $n_R \times n_S$ tuple
>[!example]
>CROSS PRODUCT non è un operatore significativo: può diventarlo quando è seguito da altre operazioni.
>FEMALE EMPS ← σSEX=′F ′ (EMPLOYEE)
>EMPNAMES ← πFNAME, LNAME, SSN(FEMALE EMPS)
>EMP DEPENDENTS ← EMPNAMES × DEPENDENT
>EMP DEPENDENTS conterrà ogni combinazione di EMPNAMES e
>DEPENDENT, se sono veramente in relazione o no

- per mantenere ogni combinazione dove il DEPENDENT è in relazione a EMPLOYEE, aggiungiamo operazione SELECT cosi:
	- Esempio: trovare il nome di ogni dipendente donna e i loro sottoposti
- FEMALE EMPS ← $σ_{\textrm{SEX=′F′}}$ (EMPLOYEE)
- EMPNAMES ← $π_{FNAME, LNAME, SSN}$(FEMALE EMPS)
- EMP DEPENDENTS ← EMPNAMES × DEPENDENT
- ACTUAL DEPS ← $σ_{SSN=ESSN}$(EMP DEPENDENTS)
- RESULT ← $π_{FNAME, LNAME, DEPENDENT NAME}$(ACTUAL DEPS)

- RESULT conterrà il nome di ogni dipendente donna e i rispettivi dipendenti
### Come comparare tuple dalla stessa tabella ?
1. fare il merge di due copie della stessa tabella: RENAME e CARTESIAN PRODUCT
2. applichiamo SELECT sulla relazione risultante dal merge

#### Esempio
1. Trovare impiegati che appartengono allo stesso dipartimento
	EMPLOYEE 1(SSN 1, FNAME 1, . . . , DNO 1) ← EMPLOYEE
	TEMP ← EMPLOYEE × EMPLOYEE 1
	RESULT ← $σ_{(DNO = DNO_1) \textrm{ AND } (SSN < SSN_1)}$(TEMP)
2. Trovare impiegati che hanno 2 o più persone a carico
	DEPENDENT\_1(BSSN\_1, D\_NAME\_1,...)$\leftarrow$ DEPENDENT
	$\sigma_{(ESSN=ESSN1)\wedge(D_NAME \neq D_NAME1)}$(DEPENDENTE x DEPENDENT)
	- se si dovesse trovare almeno 3 persone a carico si deve fare il prodotto cartesiano sulla tabella di prima
	- se si dovesse trovare al più 2: prendo la tabella almeno 3 e tolgo dall'insieme totale degli impiegati
		- AL\_PIU\_2 = $\rho_{ESSN}(\pi_{SSN}(EMPLOYEE))-ALMENO 3$

## JOIN
- combina tuple da varie relazioni
- R $\bowtie_{\langle \textrm{join condition}\rangle}S$
### Esempio
Dobbiamo recuperare il nome del manager per ogni dipartimento:
- per prendere il nome dobbiamo combinare ogni tupla DEPARTMENT con le tuple EMPLOYEE il cui SSN corrisponde al MGRSSN nella tupla del dipartimento
- DEPT\_MGR $\leftarrow$ DEPARTMENT $\bowtie_{\textrm{MGRSSN=SSN}}EMPLOYEE$

### NATURAL JOIN
- Non è possibile avere attributi con lo stesso nome
- abbiamo due relazioni
- non specifichiamo nessuna condizione di join
- viene applicata la join alle due colonne che hanno lo stesso nome

# Query with universal conditions
## Caso "all"
> “per \*\*ogni progetto\*\* di Rossi, anche il candidato deve lavorarci”.

Quindi è una condizione con \*\*“per tutti”\*\*, cioè \*\*universale\*\*. Le slide la esprimono infatti così:
- dal punto di vista insiemistico:  
    \*\*projects by rossi ⊆ projects by candidate\*\*
    
Cioè:
- prendi l’insieme dei progetti di Rossi
    
- prendi l’insieme dei progetti del candidato
    
- vuoi che il primo sia \*\*sottoinsieme\*\* del secondo

La frase naturale è:
> trova i dipendenti che lavorano su \*\*tutti\*\* i progetti su cui lavora Rossi

Le slide la scompongono così:
- \*\*Candidates\*\*: tutti gli impiegati
    
- per ogni progetto p, \*\*se\*\* Rossi lavora su p, \*\*allora\*\* anche il candidato deve lavorare su p
    
- un candidato è \*\*non buono\*\* se esiste almeno un progetto di Rossi che lui non copre
>[!tip] Invece di cercare direttamente i candidati buoni, si cercano i \*\*testimoni del fallimento\*\*.

### Ragionamento

#### 1. Identificare i candidati:
CANDIDATES (ESSN) $\leftarrow$ $\pi_{\textrm{SSN}}$(EMPLOYEE)
- prendo tutti gli impiegati
- tengo solo il loro identificativo
- "tutti gli impiegati sono candidati"
#### 2. costruire i requisiti minimi
Proj\_by\_ROSSI $\leftarrow$ $\pi_{Pno}$ (WORKS ON $\bowtie_{\textrm{ ESSN=SSN }\wedge\textrm{FNAME=ROSSI}}$ EMPLOYEE) 
REQUISITI $\leftarrow$ CANDIDATI $\times$ Proj\_by\_ROSSI

- \*\*Proj\_by\_ROSSI\*\*: trovi l'insieme dei progetti su cui lavora Rossi
- \*\*REQUISITI\*\*: contiene tutte le coppie (candidato, progetto di Rossi)
	- questa rappresenta tutto ciò che ogni candidato \*\*dovrebbe\*\* soddisfare per essere considerato buono
#### 3. Usare l'informazione reale e trovare chi non soddisfa il requisito
STATO DI FATTO(SSN, PNO) $\leftarrow$ $\pi_{\textrm{ESSN,Pno}}$ (WORKS ON)
TESTIMONI $\leftarrow$ REQUISITI - STATO DI FATTO

- \*\*STATO DI FATTO\*\*: le coppie reali (dipendente, progetto) che sono vere nella tabella WORKS ON
- \*\*REQUISITI\*\*: le coppie che \*\*dovrebbero\*\* esserci se il candidato fosse buono
- \*\*TESTIMONI:\*\* ottieni le coppie che dovrebbero esserci ma non ci sono.

#### 4. Trovare i candidati NO GOOD
NO GOOD $\leftarrow$ $\pi_{\textrm{ESSN}}$(TESTIMONI)
- qui prendi solo l'identificativo del dipendente dai testimoni
- se un dipendente compare almeno una volta nei testimoni, allora ha fallito
#### 5. Togliere i cattivi dai candidati
GOOD $\leftarrow$ CANDIDATI - NO GOOD
- da tutti i candidati
- tolgo quelli che lavorano almeno a uno progetto che non è di ROSSI

#### Riassunto
Invece di scrivere direttamente un “per ogni”, costruisce:
1. tutto ciò che dovrebbe essere vero
2. tutto ciò che è realmente vero
3. la differenza tra i due
4. elimina chi ha fallito

## Caso "only"
Trova gli impiegati che lavorano \*\*soltanto\*\* su progetti su cui lavora anche Rossi.

Dal punto di vista insiemistico:
$$
\textrm{projects by rossi }\supseteq \textrm{ projects by candidate}
$$
ovvero:
$$
\textrm{projects by candidati }\subseteq \textrm{ projects by rossi}
$$

- tutti i progetti del candidato devono appartenere all’insieme dei progetti di Rossi
- il candidato può lavorare su \*\*meno\*\* progetti di Rossi
- ma \*\*non può avere progetti extra\*\* che Rossi non ha
#### 1. Candidati
CANDIDATI (ESSN) $\leftarrow$ $\pi_{\textrm{SSN}}$ (EMPLOYEE)
- Tutti gli impiegati sono candidati
#### 2. Significato nuovo dei requisiti
1. \*\*Caso all:\*\* i requisiti erano ciò che il candidato deve soddisfare \*\*almeno\*\*
2. \*\*Caso only:\*\* i requisiti rappresentano ciò che il candidato può soddisfare \*\*al massimo\*\*. 
Proj\_by\_ROSSI $\leftarrow$ $\pi_{Pno}$ (WORKS ON $\bowtie_{\textrm{ ESSN=SSN }\wedge\textrm{FNAME=ROSSI}}$ EMPLOYEE) 
REQUISITI $\leftarrow$ CANDIDATI $\times$ Proj\_by\_ROSSI

- REQUISITI: ogni coppia rappresenta un progetto che è \*\*consentito\*\* per quel candidato 
>[!tip] Per ogni candidato, gli unici progetti ammessi sono P1 e P2.

#### 3. L'informazione reale
STATO DI FATTO(SSN, PNO) $\leftarrow$ $\pi_{\textrm{ESSN,Pno}}$ (WORKS ON)

- coppie reali (dipendente, progetto) su cui sappiamo che l'impiegato lavora davvero.
##### TESTIMONI cambia
TESTIMONI $\leftarrow$ STATO DI FATTO - REQUISITI

##### ESEMPIO
PROJS BY ROSSI={P1,P2}

e che l’informazione reale sia:

STATO DI FATTO={(E1,P1),(E2,P1),(E2,P2),(E3,P1),(E3,P3)}

Allora i REQUISITI sono:

REQUIREMENTS={(E1,P1),(E1,P2),(E2,P1),(E2,P2),(E3,P1),(E3,P2)}

Facciamo la differenza giusta per \*\*only\*\*:

TESTIMONI=STATO DI FATTO−REQUISITI

Otteniamo:

TESTIMONI={(E3,P3)}

>[!tip] si inverte la differenza rispetto al caso \*\*all\*\*.
>

Nel caso \*\*all\*\* era: manca qualcosa che il candidato dovrebbe avere?
Nel caso \*\*only\*\* è: il candidato ha qualcosa che non dovrebbe avere?

#### 4. NO GOOD
Come prima: NO GOOD $\leftarrow$ $\pi_{\textrm{ESSN}}$(TESTIMONI)
- prendo i candidati che hanno almeno un testimone
##### ESEMPIO CONTINUA
NO GOOD = {E3}
#### 5. GOOD
GOOD $\leftarrow$ CANDIDATI - NO GOOD

##### ESEMPIO CONTINUA
GOOD = {E1, E2}

- E1 lavora solo su progetti di Rossi
- E2 lavora solo su progetti di Rossi
- E3 no, perché ha un progetto extra

#### RIASSUNTO
- guardo su quali progetti lavora Rossi
- dico che questi sono i soli progetti consentiti
- guardo su quali progetti lavora davvero ogni candidato
- se trovo un progetto del candidato che non è nell’elenco di Rossi, ho una prova che il candidato non va bene
- elimino tutti quelli che hanno almeno una prova contro

# Funzioni di aggregazione
- SUM, AVERAGE, MAXIMUM, MINIMUM
- COUNT: usata per contare tuple o valori 

## Utilizzo
$F_{\langle \textrm{function list}\rangle}$(EMPLOYEE)

- $F_{\textrm{COUNT SSN, AVERAGE Salary}}$(EMPLOYEE): ritorna il numero di impiegati con il loro salario medio
## Raggruppamento con aggregazione
Esempio: per ogni dipartimento prendere il DNO, COUNT SSN e AVERAGE Salary

$_{\langle\textrm{grouping attributes}\rangle}F_{\langle\textrm{function list}\rangle}$: $_{\langle\textrm{DNO}\rangle}F_{\langle\textrm{COUNT SSN, AVERAGE Salary}\rangle}$(EMPLOYEE)

## OUTER JOIN
- Le slide spiegano che con **natural join** ed **equijoin** le tuple che non trovano corrispondenza vengono **eliminate**. Questo può causare perdita di informazione. 
- Per evitarlo si usano gli **outer join**, che conservano anche le tuple senza match, riempiendo con **NULL** gli attributi mancanti.

### LeftOuter JOIN
Il **left outer join** conserva **tutte le tuple della relazione sinistra** RRR. Se una tupla di R non trova corrispondenza in S, compare comunque nel risultato, e gli attributi di S vengono riempiti con **NULL**.

### RightOuter JOIN
Il **right outer join** è simmetrico: conserva **tutte le tuple della relazione destra** S. Se manca una corrispondenza con R, gli attributi di RRR vengono messi a **NULL**.

### Full outer join
Il **full outer join** conserva **tutte le tuple di entrambe le relazioni**. Quando non c’è corrispondenza, riempie con NULL la parte mancante.


