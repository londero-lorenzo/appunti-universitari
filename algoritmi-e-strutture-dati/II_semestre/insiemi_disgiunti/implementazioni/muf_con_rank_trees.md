---
title: Muf con Rank Trees
aliases:
  - Muf con Rank Trees
tags:
  - insiemi-disgiunti
  - implementazioni
  - muf-con-rank-trees
created: 2025-06-14
---
# Make Union Find con Rank Trees
Rank Trees sono la diretta evoluzione degli alberi utilizzati nelle operazioni [[muf_con_alberi|MUF con Alberi]], con l'aggiunta di un parametro `x.rank` che indica l'altezza dell'albero radicato in `x`, utilizzato per ottimizzare le operazioni di `UNION`.

Le operazioni che non verranno modificate sono:
- [[muf_con_alberi#Implementazione di `FIND(x)`|FIND(X)]]
- [[muf_con_alberi#Implementazione `FIND(x)`|FIND(x)]]

---

## Implementazione di `MAKE(x)`

```c
MAKE(x){
	x.parent = x
	x.rank = 0
}
```

Esempio di struttura:
![[algoritmi-e-strutture-dati/II_semestre/insiemi_disgiunti/insiemi_di_dati_disgiunti_schema.md#^frame=FPH6XZahYNi1GASadV74l|25%]]


---

## Implementazione di `UNION-BY-RANK`

```c
UNION-BY-RANK(x, y){
	z = FIND(x)
	w = FIND(y)
	if (z != w){
		if (z.rank > w.rank){
			LINK(z, w)
		}else{
			LINK(w, z)
			// w è il nuovo rappresentante
			if (z.rank == w.rank){
				w.rank = w.rank + 1
			}
		}
	}

}
```


---

Esempio

- Costruire gli insiemi disgiunti con chiavi 1, 2, ..., 10
- Eseguire `UNION(2, 1)`, `UNION(3, 1)`, `UNION(4, 1)`, `UNION(7, 8)`, `UNION(1, 8)`

Utilizzando `UNION-BY-RANK`
> Nel caso di alberi aventi lo stesso rango, si utilizza come radice quello con chiave maggiore

![[algoritmi-e-strutture-dati/II_semestre/insiemi_disgiunti/insiemi_di_dati_disgiunti_esempi.md#^frame=3GXzPtmD3BfvZaWVQrsdT|100%]]


---

## Complessità
Quale è la complessità nel caso peggiore?


| Operazione | Costo            |
| ---------- | ---------------- |
| Make       | $\Theta(1)$      |
| Find       | $\mathcal{O}(h)$ |
| Union      | $\mathcal{O}(h)$ |

### Complessivamente

Supponiamo `m` operazioni Make Find Union in totale, di cui `n` sono `MAKE`.
Quindi $m = n + f + u$

|  Operazione   |       Costo        |  Quantità   |                       Costo Complessivo                       |
| :-----------: | :----------------: | :---------: | :-----------------------------------------------------------: |
|     MAKE      |    $\Theta(1)$     | $n \leq m$  |                          $\Theta(n)$                          |
|     FIND      |  $\mathcal{O}(h)$  |  $f\leq m$  | $\mathcal{O}(h)\cdot\mathcal{O}(m)$ = $\mathcal{O}(h\cdot m)$ |
|     UNION     |  $\mathcal{O}(h)$  | $u\leq n-1$ |  $\mathcal{O}(h)\cdot\mathcal{O}(n) = \mathcal{O}(h\cdot n)$  |
| ------------- | ------------------ | ----------  |                   $\mathcal{O}(h \cdot m)$                    |

## Lemma
Utilizzando `UNION-BY-RANK` a partire da `n` operazioni `MAKE` si ottengono alberi aventi altezza $\mathcal{O}(\log{n})$

### Dimostrazione
Per induzione sul numero di union:
> #TODO: [Video lezione (7 aprile 2021, minuto 59:35)](https://uniudamce.sharepoint.com/sites/117802-ALGORITMIESTRUTTUREDATIELABORATORIO/_layouts/15/stream.aspx?id=%2Fsites%2F117802%2DALGORITMIESTRUTTUREDATIELABORATORIO%2FDocumenti%20condivisi%2FGeneral%2FRecordings%2FASD%20lezione%2038%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ea20b36cb%2Da660%2D450d%2D89eb%2D761698d974b6)




 >💬 _Domanda: "È veramente possibile raggiungere il costo di $n^2$?"  
 > #TODO
 
 ---
## Ottimizzazione

Se ripeto tante volte `FIND`, ogni volta ho costo $\Theta(\log{n})$ e ogni volta ripercorro lo stesso ramo.

Voglio modificare l'albero in modo tale da ridurre i costi accorciando i vari rami.

Introduzione a find_compression