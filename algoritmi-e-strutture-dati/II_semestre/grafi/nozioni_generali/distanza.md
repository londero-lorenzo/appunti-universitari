---
title: "Distanza"
aliases: ["Distanza"]
tags: [università, "algoritmi-e-strutture-dati", "II-semestre", "grafi", "nozioni-generali", "distanza"]
created: 2025-06-14
---
Dato un grafo $G = (V, E)$ e $s\in V$ la distanza $\delta$ vale:
$$
\delta(s,v)=
\begin{cases}
	+\infty & \text{se non esiste in } \\
	  & \text{ }G \text{ un cammino da } s \text{ a } v \\
	  & \text{se in } G \text{ esiste un camino da } \\ 
	l  & \text{ }s \text{ a } v \text{ di lunghezza } l \\
	  &\text{ e non esiste un cammino di lunghezza } l-1
\end{cases}
$$

#TODO completare con le altre proprietà (triangolare).  [Video lezione (23 aprile 2021, minuto 28:30)](https://uniudamce.sharepoint.com/sites/117802-ALGORITMIESTRUTTUREDATIELABORATORIO/_layouts/15/stream.aspx?id=%2Fsites%2F117802%2DALGORITMIESTRUTTUREDATIELABORATORIO%2FDocumenti%20condivisi%2FGeneral%2FRecordings%2FASD%20lezione%2042%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E356eff62%2D34d3%2D4333%2D9738%2D7168a0fb7cb5)