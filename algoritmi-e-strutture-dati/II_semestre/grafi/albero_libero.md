---
title: "Albero Libero"
aliases: ["Albero Libero"]
tags: [università, "algoritmi-e-strutture-dati", "II-semestre", "grafi", "nozioni-generali", "albero-libero"]
created: 2025-06-15
---
$G= (V, E)$ non orientato è un albero se e solo se $G$ è connesso e aciclico


## Proprietà $G=(V, E)$ grafo non orientato
Sono equivalenti le seguenti applicazioni:
1. $G$ è un albero (connesso e aciclico)
2. $\forall u,v\in V \exists ! u\to v$  (esiste un unico cammino)
3. $G$ è connesso e se viene rimosso un arco, $G$ si sconnette
4. $G$ è connesso e $|E| = |V|-1$
5. $G$ è aciclico e $|E| = |V| - 1$
6. $G$ è aciclico e aggiungendo un qualsiasi arco $G$ diventa ciclico


> Hanno la quantità minima richiesta per la connessione e la quantità massima per non essere ciclici

---
### Dimostrazione
[Video lezione (14 maggio 2021; minuto 3:20)](https://uniudamce.sharepoint.com/sites/117802-ALGORITMIESTRUTTUREDATIELABORATORIO/_layouts/15/stream.aspx?id=%2Fsites%2F117802%2DALGORITMIESTRUTTUREDATIELABORATORIO%2FDocumenti%20condivisi%2FGeneral%2FRecordings%2FASD%20lezione%2049%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E6630e68b%2D62b2%2D4f99%2D9c2b%2D95605ff058b0)

---

$1) \implies 2)$
$Hp)\quad G=(V,E)\text{ non orientato, connesso e aciclico}$
$Ts)\quad \forall u,v \in V \quad \exists ! u\to v$

$G$ connesso $\implies$ $\forall u,v \in V \exists u \to v$
se per assurdo $\exists u,v$ tale che ci sono 2 cammini distinti tra $u$ e $v$

#TODO aggiungere foto per l'individuazione del ciclo, video minuto 6:16

$2) \implies 3)$

#TODO continuare

---

## Quanto costa e come dedico se $G=(V, E)$ non orientato è un albero?
1) Connesso e aciclico:
	1) utilizzo DFS
		- un solo NIL in $\Pi$
		- nessun arco da `GRIGIO` a `GRIGIO` (tranne gli archi della forma $\{x, \Pi[x]\}$)
		- COSTO: $O(|V| + |E|) = O(|V|)$
	- 
