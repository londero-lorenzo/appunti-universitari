---
title: "Correttezza"
aliases: ["Correttezza"]
tags: [università, "algoritmi-e-strutture-dati", "BST", "visite", "in-order", "correttezza"]
created: 2025-06-04
---
Per induzione su $n$ numero di chiavi memorizzate in $T$
+ **Ipotesi:** $T$ è BST
+ **Tesi:** `InOrder` stampa in ordine crescente
+ **BASE:** $n=0$ `InOrder` non stampa niente
+ **TESI:** se $T$ è un BST con $n$ chiavi `InOrder(T)`
	+ ![[Algoritmi/Esame/Untitled Diagram 3.svg]]
