---
title: "Albero Bilanciato"
aliases: ["Albero Bilanciato"]
tags: [università, "algoritmi-e-strutture-dati", "II-semestre", "nozioni-generali", "albero", "albero-bilanciato"]
created: 2025-06-09
---
# 📌 Definizione

Un **albero binario** si dice **bilanciato** se la sua **altezza** è **$\mathcal{O}(\log n)$**, dove `n` è il numero di nodi.

🔎 Questo implica che:

- le operazioni di **ricerca**, **inserimento** e **cancellazione** in un [[albero_binario_di_ricerca|Albero Binario di Ricerca]] avranno **costo logaritmico**, nel caso peggiore.


---

# ❗ Perché serve il bilanciamento

Un **BST arbitrario** (senza vincoli di bilanciamento) può degenerare in una **lista** se i dati sono inseriti in ordine (es. crescente o decrescente), portando la complessità a $\mathcal{O}(n)$ per tutte le operazioni.

🔧 Serve quindi un **meccanismo automatico** che mantenga l'albero **strutturato** in modo da evitare casi degeneri.


---

# 🧠 Come si ottiene il bilanciamento

Esistono più approcci:

### ✅ Bilanciamento **implicito**

Strutture che **impongono vincoli** sui cammini o sul colore dei nodi, garantendo il bilanciamento come conseguenza logica:

- [[b_tree|BTree]]:  vincola il numero di chiavi per ogni nodo interno
    
- [[red_black_tree|Red Black Tree]]: vincola i cammini neri e la disposizione dei nodi rossi