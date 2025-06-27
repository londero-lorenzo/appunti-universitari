---
title: Red Black Tree
aliases:
  - Red Black Tree
tags:
  - II-semestre
  - RBT
  - red-black-tree
created: 2025-06-09
---
# Red Black Tree (RBT)

Sono [[albero_binario_di_ricerca|Alberi Binari di Ricerca]] [[albero_bilanciato|Bilanciati]] con altezza $\Theta(\log n)$, ottenuta grazie all’uso di colori (`Red` e `Black`) e rotazioni che mantengono le proprietà di bilanciamento.  
Le operazioni fondamentali — inserimento, ricerca e cancellazione — hanno costo $\mathcal{O}(\log n)$.

→ [[algoritmi-e-strutture-dati/II_semestre/RBT/definizione|Vedi definizione formale]]


---

## 📏 Bilanciamento e Altezza

### ⚫ Altezza nera

Per ogni nodo `x` di un RBT, definiamo la **black height** `bh(x)` come il numero di nodi neri nel cammino da `x` a una foglia (inclusa la foglia `NIL` ma escluso `x` stesso).

L’altezza nera dell’intero albero `T` è quindi:  
$bh(T)=bh(T.root)$

![[red_black_tree_schema#^frame=BosAn_yrXqRX4JfDZMjAV|75%]]

---

### 📐 Relazione tra altezza e altezza nera 

- L’altezza totale dell’albero è limitata da:  
    $h≤2⋅bh$
    Questo perché i nodi rossi non possono essere consecutivi (ogni nodo rosso ha figli neri), quindi nel cammino più lungo si alternano nodi rossi e neri.
    
- Ne consegue:  
    $bh\geq \frac{h}{2}​$
    
- Intuitivamente, i nodi neri formano almeno un albero binario completo di altezza `bh`.
    

---

### 📊 Lemma: numero minimo di nodi interni

In un RBT `T` con altezza nera `bh(T)`, il numero di **nodi interni** è sempre almeno:  
$n_i \geq 2^{bh(T)} - 1$

(Dimostrazione: **#TODO**)

![[red_black_tree_schema#^frame=JJwCBGkFq3S-3kL_Av4WC|100%]]

---

### 📎Conseguenze

Dato che: 
$$
ni \geq 2^{bh} - 1 \geq 2^{\frac{h}{2}} - 1
$$
Ne segue:
$$
h \leq 2 \cdot \log(n_i + 1) = \mathcal{O}(\log n)
$$

La costante 2 nasce dal fatto che i nodi rossi devono essere sempre separati da nodi neri, impedendo un eccessivo sbilanciamento.

---

### 🧠 Riassumendo

- Nel caso peggiore, tutti i nodi sono neri → altezza `h = bh`.
    
- Nel caso migliore, si alternano nodi rossi e neri → `h = 2 \cdot bh`.
    
- In ogni caso, per un RBT con `n` nodi interni:  
    $h = \Theta(\log n)$
    

→ [Video lezione con spiegazioni dettagliate (3 marzo 2021, minuto 23:17)](https://uniudamce.sharepoint.com/sites/117802-ALGORITMIESTRUTTUREDATIELABORATORIO/_layouts/15/stream.aspx?id=%2Fsites%2F117802%2DALGORITMIESTRUTTUREDATIELABORATORIO%2FDocumenti%20condivisi%2FGeneral%2FRecordings%2FASD%20lezione%2026%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E9f0efd42%2D4431%2D43e7%2D8c92%2D8c1a728dcc06)

![[red_black_tree_schema#^frame=TPHgNm67tqDthD8ZFVuaR|100%]]

---


## 🔄 Operazioni di modifica

Le operazioni che modificano la struttura del Red Black Tree mantenendone le proprietà sono:

- [[algoritmi-e-strutture-dati/II_semestre/RBT/modifiche/inserimento|Inserimento]]
    
- [[algoritmi-e-strutture-dati/II_semestre/RBT/modifiche/cancellazione|Cancellazione]]
    
- [[rotazione|Rotazioni]]
    
- [[algoritmi-e-strutture-dati/II_semestre/RBT/modifiche/fusione|Fusione]]


---

## ⏱️ Complessità

L’altezza `h` domina la complessità delle operazioni di ricerca, inserimento e cancellazione.

Poiché:  
$$
\mathcal{O}(\log n)
$$


tutte le operazioni principali hanno complessità:  
$$
\mathcal{O}(\log n)
$$

→ [[albero_bilanciato|Vedi Alberi Bilanciati per approfondimenti]]

---

## 📝 Esercizi

[[algoritmi-e-strutture-dati/II_semestre/RBT/esercizi/esercizi]]

---
