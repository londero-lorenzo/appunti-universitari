---
title: "B-Tree"
aliases: ["B-Tree"]
tags: [università, "algoritmi-e-strutture-dati", "II-semestre", "B-Tree", "b-tree"]
created: 2025-06-12
---
# 🌳 B-Tree — Struttura e Proprietà Generali

Generalizzazione di:

- [[albero_binario_di_ricerca|Albero Binario di Ricerca]]
    
- [[red_black_tree|Red-Black Tree]]


---

## 🧠 Motivazione

I B-Tree sono progettati per **grandi quantità di dati** che **non stanno in memoria centrale (RAM)** ma **risiedono su memoria secondaria** (es. Hard Disk).  
La RAM può contenere solo un **numero limitato di nodi**, quindi si mira a **minimizzare il numero di accessi a disco (I/O)**.

### 📦 Esempi d’uso

- Database
    
- File system
    
- Sistemi GPS / Mappe

---
## 💡 Idea generale

Struttura ad albero **bilanciato** che suddivide i dati in **indici** e **sottoindici** a più livelli.

### 📏 Caratteristiche principali

- Ogni nodo può avere **un numero variabile di figli** (entro un intervallo definito dal grado `t`)
    
- Le **chiavi nei nodi** sono mantenute ordinate
    
- **Tutte le foglie** si trovano **allo stesso livello**
    

📷 _Schema di esempio_  
![[algoritmi-e-strutture-dati/II_semestre/B-Tree/b-tree_schema.md#^frame=wQYWDymk9-0x_OUMI9aSi|100%]]


---

## 🧮 Definizione formale

👉 Vedi file dedicato: [[definizione|Definizione di B-Tree]]  
Contiene:

- Struttura del nodo (`x.n`, `x.leaf`, `x.key`, `x.c`)
    
- Proprietà di grado minimo `t`
    
- Vincoli su chiavi e figli

---

## 🔢 Operazioni fondamentali

Tutte le operazioni mantengono le proprietà strutturali del B-Tree:

| Operazione                 | File                                                                                     |
| -------------------------- | ---------------------------------------------------------------------------------------- |
| 🔍 Ricerca                 | [[algoritmi-e-strutture-dati/II_semestre/B-Tree/ricerca\|Ricerca]]                       |
| ➕ Inserimento              | [[algoritmi-e-strutture-dati/II_semestre/B-Tree/modifiche/inserimento\|Inserimento]]     |
| ❌ Cancellazione            | [[algoritmi-e-strutture-dati/II_semestre/B-Tree/modifiche/cancellazione\|Cancellazione]] |
| 📤 I/O (modello a blocchi) | [[operazioni_di_input-output\|Operazioni di Input-Output]]                               |

---

## 📐 Proprietà strutturali

### 🔺 Altezza massima

Che altezza può raggiungere un B-Tree di grado `t` con `n` chiavi?

📷 _Schema illustrativo_  
![[algoritmi-e-strutture-dati/II_semestre/B-Tree/b-tree_schema.md#^frame=CCQAQvFxtojuzSOruiM0J|100%]]
#### 📊 Calcolo:
$$
\sum_{i=0}^{h-1}(2t^i(t-1)) + 1 = n \implies 2(t-1) \sum_{i=0}^{h-1}(t^i) + 1 = n 
$$

$$
\implies2(t-1) \cdot \frac{t^h-1}{t-1} + 1 = n \implies 2t^h -1 = n
$$

$$
\implies h = \log_{t}{\left(\frac{n+1}{2}\right)}
$$

---
### 🧾 Conclusione:

Un B-Tree di grado `t` e `n` chiavi ha altezza:
$$
h \leq \log_{t}{\left(\frac{n+1}{2}\right)} \implies h \in \mathcal{O}(\log_{t}n)
$$
📌 _Nota tecnica:_

> _Uso improprio della notazione asintotica: `t` è costante, ma viene lasciata esplicitamente per evidenziare la sua influenza._


---


## Che legame c'è tra B-Tree e [[red_black_tree|Red-Black Tree]]?

### Intuizione

Un Red-Black Tree può essere visto come un **B-Tree di grado `t = 2`**, in cui:

- I nodi **`RED` vengono "fusi"** visivamente con i genitori (come se fossero chiavi aggiuntive nello stesso nodo B-Tree)
    
- Il risultato è un albero più "compresso", che riflette esattamente la struttura di un B-Tree
    

> ![[algoritmi-e-strutture-dati/II_semestre/B-Tree/b-tree_schema.md#^frame=thSUf5aDiNwahYHt3PTKi|100%]]

---

### Il Red-Black Tree è effettivamente un B-Tree di grado 2?

- **Bilanciamento**: sì. L’altezza nera di ogni cammino nel RBT è costante ⇒ il B-Tree risultante è **completamente bilanciato**
    
- **Altezza**: l’altezza del B-Tree corrisponde all’altezza nera del RBT
    

---

### Complessità

- **CPU / R/W**:  
    Il costo di trasformazione RBT → B-Tree è
    
    $\Theta(n)$

---

### Vale anche il contrario?

È possibile trasformare un B-Tree di grado 2 in un Red-Black Tree?

**Sì**, ecco come:

|Caso|RBT risultante|
|---|---|
|1 chiave (nodo singolo)|nodo `BLACK` con due figli `NIL`|
|2 chiavi|un po’ ambiguo, ma si può definire una convenzione (es: `RED` a sinistra, `BLACK` a destra)|
|3 chiavi|nodo centrale `BLACK` con due figli `RED`|

> Esistono **più RBT validi** a partire dallo stesso B-Tree (dipende da come distribuisco i `RED`).

Si vale anche il contrario:
- se ho solo un nodo -> diventa un nodo `BLACK` con i due figli
- se ho tre nodi -> diventa nodo centrale `BLACK` con gli altri due figli `RED`
- se ho due nodi -> basta fissare la convenzione se prima `RED` e poi `BLACK` (è ambiguo, questo implica che posso costruire diversi RBT a partire da un unico B-Tree)


---

### È una trasformazione corretta?

**Domanda:** possono esserci nodi `RED` figli di altri `RED`?  
**Risposta:** no, perché la costruzione assume che le radici parziali siano `BLACK`, quindi una catena di `RED` è impossibile.

**Domanda:** le altezze nere sono rispettate?  
**Risposta:** sì, perché il B-Tree è completamente bilanciato e la sua altezza diventa esattamente l'altezza nera del RBT risultante.

---

### Conclusione

- È possibile utilizzare **le stesse operazioni** (inserimento, cancellazione, rotazioni, ricolorazioni) nel B-Tree trasformandolo prima in un Red-Black Tree
    
- Il **B-Tree è una generalizzazione** del Red-Black Tree:
    
    - Il RBT si limita a **grado 2**
        
    - Il B-Tree può avere **grado arbitrario `t`**, permettendo una gestione più efficiente del disco

---

## 🧭 Altri riferimenti utili

- 📘 [[b-tree_esempi|Esempi pratici di operazioni su B-Tree (Excalidraw)]]
    
- 📘 [[b-tree_schema|Schemi teorici su B-Tree (Excalidraw)]]

