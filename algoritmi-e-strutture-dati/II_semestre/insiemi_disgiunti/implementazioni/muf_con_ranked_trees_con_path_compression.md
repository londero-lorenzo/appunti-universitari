---
title: "Muf con Ranked Trees con Path Compression"
aliases: ["Muf con Ranked Trees con Path Compression"]
tags: [università, "algoritmi-e-strutture-dati", "II-semestre", "insiemi-disgiunti", "implementazioni", "muf-con-ranked-trees-con-path-compression"]
created: 2025-06-14
---

# Make Union Find con Rank Trees e Path Compression
Rank Trees con Path Compression sono gli stessi alberi utilizzati nelle operazioni [[muf_con_rank_trees|Muf con Rank Trees]], utilizzato per ottimizzare le operazioni di `UNION`.

Le operazioni che verranno modificate sono:
- [[muf_con_alberi#Implementazione di `FIND(x)`|FIND(X)]]
in modo tale da:
Quando eseguo una `FIND(x)` tutti inodi sul cammino `x-radice` vengono agganciati alla radice.
Esempio:

![[algoritmi-e-strutture-dati/II_semestre/insiemi_disgiunti/insiemi_di_dati_disgiunti_schema.md#^frame=PZuUhoUR5DdfJOMgOpH_p]]

---

## Implementazione di `FIND_PC`

```c
FIND-PC(x){
	if (x != x.parent){
		x.parent = FIND-PC(x.parent)
	}else{
		return x
	}
}
```


#TODO aggiungere immagine per mostrare la ricorsione + costi. \[[Video lezione 38 (7 aprile 2021, minuto 1:24:20)](https://uniudamce.sharepoint.com/sites/117802-ALGORITMIESTRUTTUREDATIELABORATORIO/_layouts/15/stream.aspx?id=%2Fsites%2F117802%2DALGORITMIESTRUTTUREDATIELABORATORIO%2FDocumenti%20condivisi%2FGeneral%2FRecordings%2FASD%20lezione%2038%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ea20b36cb%2Da660%2D450d%2D89eb%2D761698d974b6) e [Video lezione 39 (14 aprile 2021, minuto 3:30)](https://uniudamce.sharepoint.com/sites/117802-ALGORITMIESTRUTTUREDATIELABORATORIO/_layouts/15/stream.aspx?id=%2Fsites%2F117802%2DALGORITMIESTRUTTUREDATIELABORATORIO%2FDocumenti%20condivisi%2FGeneral%2FRecordings%2FASD%20lezione%2038%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ea20b36cb%2Da660%2D450d%2D89eb%2D761698d974b6)\]

Comprimiamo solo il cammino `x-radice`


---

## Implementazione di `FIND_PC_WHILE`

```c
FIND-PC-WHILE(x){
	y = x
	while(y != y.prent){
		y = y.parent
	}
	// y è la root
	while(x != y){
		z = x.parent
		x.parent = y
		x = z
	}
	return y
}
```


Costo
$O(\log{n})$ per un operazione find perché sto usando alberi `UNION-BY-RANK`

Il costo complessivo è:
$$
O(m \cdot \alpha(n,m))
$$
Dato costo delle find non è cambiato.

Risparmio in spazio in quanto non ho più la pila delle chiamate ricorsive

