---
title: Grafi
aliases:
  - Grafi
tags:
  - II-semestre
  - grafi
created: 2025-06-14
---
# Grafo

E' una struttura dati in cui ho due insiemi:

$G = (V, E)$

- `V` è l'insieme dei nodi
- `E` è l'insieme degli archi

## Grafi orientati
L'insieme degli archi viene rappresentato come un insieme di coppie ordinate di nodi:

$E = \{(u,v), ...\}\quad\quad u,v\in V$

posso scegliere $u$ in $|V|$ modi, posso scegliere $v$ in $|V|$ modi, quindi
$0\leq|E|\leq{|V|}^2$
## Grafi non orientati

L'insieme degli archi viene rappresentato come un insieme di insiemi di due nodi:

$E = \{\{u,v\}, ...\}\quad\quad u,v\in V$
posso scegliere $u$ in $|V|$ modi, posso scegliere $v$ in $|V|$ modi, ma dato il fatto che nelle liste un arco $\{i, j\}$ e $\{j, i\}$ sono la stessa cosa:
$$
0\leq|E|\leq\frac{|V|\cdot{|V|-1}}{2}
$$


Esempio:
![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=zT5kzvlvqH5gcy9_Ss16T]]

## Nomenclatura
$|E| << |V|$ si dice grafo sparso
$|E| = \Theta({|V|}^2)$ si dice grafo denso
## Osservazioni
Un albero è un grafo non orientato aciclico connesso
- aciclico, che non è presente un ciclo
- connesso, c'è almeno una sequenza di archi che mi porta dal primo al secondo nodo
	- $\forall u,v \quad\exists u\to v$
	![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^clippedframe=8dGnRr_HX-5ysG2JvANXs|100%]]

- non c'è un numero massimo di figli
- non c'è un ordine tra i figli

## Domande

- Come memorizzo i grafi?
- Quali sono le operazioni di base? -> Visite (scandire i nodi una sola volta)


---

## Strutture dati
### Matrice di Adiacenza
$G$ indica la presenza di un arco tra due nodi

$$
M_G  \quad\quad |V|\times|V| \quad\quad V=\{1,..., n\}
$$
$$
M_G[i,j] = \begin{cases} 0 & \{u,v\}\notin E\\ 1 & \{u,v\}\in E \end{cases}
$$



Esempio
![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=enD6v-22BFqivoaM_HJFd|100%]]


$$
M_G=
\begin{pmatrix} 0 & 1 & 1 & 0 & 0 & 0 \\
				1 & 0 & 1 & 0 & 1 & 0 \\
				1 & 1 & 0 & 1 & 0 & 0 \\
				0 & 0 & 1 & 0 & 1 & 0 \\
				0 & 1 & 0 & 1 & 0 & 1 \\
				0 & 0 & 0 & 0 & 1 & 0 \\
\end{pmatrix}
$$


#### Osservazioni
Se $G$ è non orientato $M_G$ è **simmetrica** con diagonale di zeri

>Una generica matrice booleana quadrata rappresenta un grafo orientato (**potrei trovare un uno sulla diagonale, implicherebbe che c'è un arco da un nodo allo stesso nodo, dato che nei grafi orientati gli archi sono indicati con un insieme da due elementi allora l'insieme collasserebbe, di conseguenza deve essere un grafo orientato**)

### Liste di adiacenza

$L_G$ vettore di liste di dimensione $|V| = n$ se è densa ${|V|}^2$
$L_G[i]$ lista dei nodi raggiungibili con un arco dal nodo $i$

![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=L0A4DcNDApjkCJ8S-FSfN|100%]]

---

## Operazioni
#TODO aggiungere operazioni con liste e matrici. \[[Video lezione 41 (21 aprile 2021, minuto 15:00)](https://uniudamce.sharepoint.com/sites/117802-ALGORITMIESTRUTTUREDATIELABORATORIO/_layouts/15/stream.aspx?id=%2Fsites%2F117802%2DALGORITMIESTRUTTUREDATIELABORATORIO%2FDocumenti%20condivisi%2FGeneral%2FRecordings%2FASD%20lezione%2041%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E27673cf3%2D757b%2D4510%2D8432%2D27f7273f723d)\]

1. Decidere se $(i,j)\in E$

---

## Cicli
Un grafo $G$ contiene un ciclo se e solo se $G$ contiene almeno un [[ciclo_semplice|Ciclo Semplice]]


### Osservazione

>Nei grafi non orientati nella condizione di ciclo va aggiunta la condizione di non usare due volte lo stesso arco.
![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=Mrvwp7_nA16HyQLz06mrV|100%]]

Altrimenti tutti i grafi non orientati con conterrebbero cicli.


---

## Decidere se in un grafo non orientato c'è un ciclo con BFS.

Focalizziamoci su grafi non orientato. Osserviamo il comportamento della visita [[BFS]] su un ciclo:
![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=aa6cMz16XVNH9tJABaizM|100%]]

Utilizzando questa disposizione a rombo, si vede che partendo da `s`, in alto, la visita si sposta sui nodi sinistri e destri di `s`, rispettivamente prima verso `a` e poi verso `c`.  Successivamente ci si ritrova nel caso in cui `a` trova un nuovo nodo `b`, collegato anche a `c`, lo mette grigio e lo aggiunge alla coda, nell'iterazione successiva si parte da `c` e si scansionano i vicini, ci si accorge che c'è un nodo grigio nella lista di adiacenza e ci si ferma, quindi la visita ha prodotto: `s, a, c, b`, ci si accorge del ciclo perché da un nodo grigio sono passato ad un altro nodo non bianco.

---

## Decidere se in un grafo orientato c'è un ciclo con BFS.
Non si riescono a distinguere questi due casi per via della disposizione degli archi. Entrambi hanno un arco da `GRIGIO` a `NERO`, però in un caso c'è un ciclo e nell'altro no
![[algoritmi-e-strutture-dati/II_semestre/grafi/grafi_schema.md#^frame=H7fqgUWbJCoSeS04_LXRF|100%]]


Ci serve una nuova visita:
DFS, in profondità

----

#TODO sistemare collegamenti

- [[sssp]]
- [[apsp]]

Grafi pesati:
- [[grafi_pesati|Grafi Pesati]]