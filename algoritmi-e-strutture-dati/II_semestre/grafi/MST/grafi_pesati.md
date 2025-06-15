---
title: "Grafi Pesati"
aliases: ["Grafi Pesati"]
tags: [università, "algoritmi-e-strutture-dati", "II-semestre", "MST", "grafi-pesati"]
created: 2025-06-15
---
# Minimum Spanning Tree

$G = (V, E, W)$ $G$ non orientato, sconnesso e pesato con $W: E\to \mathbb{R}^+$

## Determinare
Sottografo $G'$ di $G$ t.c.:
1) $G' = (V, E', W_{E'})$ con $E'\subseteq E$
2) $G'$ connesso
3) $G'$ di peso minimo tra tutti i sottografi connessi di $G$
		$W(G') = \displaystyle\sum_{\{x,y\}\in E'}{W(\{x,y\})}$

![[grafi_pesati_schema#^frame=Wb-i8viPCIfKOpPSJw690]]

$G' \quad\quad W(G') = 1 + 1 + 1 + 2 + 2$
$G'' \quad\quad W(G'') = 1 + 1 + 1 + 2$

Domanda: _È unico?_
> No

Cosa rende il sottografo aciclico?
> il fatto che lo vogliamo connesso e di peso minimo (sono positivi) $\implies$ $G'$ sarà sempre un albero

## Problema
Da $G = (V, E, W)$ con pesi positivi determinare un `MST` (sotto grafo connesso di peso minimo)di $G$

Algoritmi usati per questo problema:
- Kruskal
- Prim
### Idea
- parto da $A \subseteq E$ con $A = \emptyset$
- Ad ogni passo $A = A \cup \{\{x,y\}\} \land \{x,y\}\in E$ (qui risiede il problema non so quale $\{x,y\}$ prendere)
- Itero fino a che |A| = |V|-1


Per farlo dobbiamo comprendere alcune proprietà fondamentali


---


### Definizione di Arco `SAFE`
$T = (V, E', W)$ sia un MST di $G = (V, E, W)$ e $A \subseteq E' \subseteq E$ (sottoinsieme della soluzione)

Dico che $\{x, y\} \in E$ è `SAFE` per $A$ se $A \cup \{\{x,y\}\} \subseteq E''$ con $T' = (V, E'', W)$ `MST` di $G$

Esempio:
![[grafi_pesati_schema#^frame=ZlxwIeipyBTQ_DWfn1-71|100%]]


Domanda: _$\{a,c\}$ è `SAFE` per $A$?_
> Equivale a rispondere verificare:
> $A' = \{\{a,b\}\, \{a,c\}\} \subseteq T'$ con $T'$ `MSG` di $G$?
> Si se considero $T = T'$

---

Proviamo con un altro:
![[grafi_pesati_schema#^frame=r3xSWvH72XyHJSoIFLGlP|100%]]

Domanda: _$\{b,c\}$ è `SAFE` per $A$?_
> Equivale a rispondere verificare:
> $A' = \{\{a,b\}\, \{b,d\}\} \subseteq T''$ con $T''$ `MSG` di $G$?
> Si se considero $T'' =\{\{a,b\}\, \{b,d\}, \{d,c\}\}$

---

### Cosa ci dice quindi definizione di arco `SAFE`?
>Sto costruendo un qualcosa che fino a questo momento è corretto perché sottoinsieme di un mst, l'importante è che io aggiunga un arco che fa si che ciò che ottengo sia sottoinsieme di uno mst, non mi importa quale


Esempio:
![[grafi_pesati_schema#^frame=rfkUWg5tS5lRXnWos562V|100%]]

---
### MST pseuso

```c
MST(G = (V, E, W)){
	A = {}
	while(|A| < |V| - 1){
		trovo {a, y} SAFE per A // -> come?
		A = Union(A, {{x, y}}) 
	}
	return A
}
```


---

### Taglio

Taglio $(S, V\textbackslash S)$ con $S \subseteq V$
Partizione di V in due blocchi

$\{u, v\}$ `ATTRAVERSA` il taglio $(S, V\textbackslash S)$ se $u \in S \text{ }\land\text{ } v \in V \textbackslash S \quad\lor\quad v \in S \text{ }\land\text{ } u \in V \textbackslash S$ 
Esempio:
![[grafi_pesati_schema#^frame=NGH1Jgc37CZPiviMfE4ei|100%]]

$A\subseteq E$  `RISPETTA` il taglio $(S, V\backslash S)$ se nessun arco di $A$ attraversa il taglio

![[grafi_pesati_schema#^frame=4A9-Fj_RFmXzy7jTi3xGY|100%]]


---


## Idea
Parto con $A = \emptyset$
1. In ogni istante $A \subseteq T$ $T$  soluzione del problema.
2. In ogni istante ho $(S,V\backslash S)$ t.c $A$ rispetta il taglio
3. ==Trovo un arco di peso minimo che attraversa il taglio e lo aggiungo ad $A$==

#TODO arco leggero + dimostrazione che l'arco che trovo è safe per A [Video lezione 14 maggio 2021; ora 1:20:20](https://uniudamce.sharepoint.com/sites/117802-ALGORITMIESTRUTTUREDATIELABORATORIO/_layouts/15/stream.aspx?id=%2Fsites%2F117802%2DALGORITMIESTRUTTUREDATIELABORATORIO%2FDocumenti%20condivisi%2FGeneral%2FRecordings%2FASD%20lezione%2049%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E6630e68b%2D62b2%2D4f99%2D9c2b%2D95605ff058b0)


---


STO COSTRUENDO UN MINIMUM SPANNING TREEE!!!
>Sto costruendo un minimum spanning tree ancora non lo conosco completamente, mio trovo difronte ad un taglio, ho costruito uno `MST` che rispetta quel taglio e quindi posso prendere un arco di peso minimo che attraversa il taglio e quello che ottengo è sempre un `MST`



USIAMO [[kruskal]]


---


## Kruskal vs Prim

Krunskal -> crea tanti piccoli alberelli che pian piano creano una foresta e infine un MST
Prim -> si crea un alberello e lo si espande fino a creare un MST


