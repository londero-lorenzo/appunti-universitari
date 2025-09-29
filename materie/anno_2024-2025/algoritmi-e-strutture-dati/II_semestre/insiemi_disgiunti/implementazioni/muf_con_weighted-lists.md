---
title: MUF con Weighted-Lists
aliases:
  - MUF con Weighted-Lists
tags:
  - insiemi-disgiunti
  - implementazioni
  - MUF-con-weighted-lists
created: 2025-06-14
---
# Make Union Find con Weighted Lists
Weighted Lists sono la diretta evoluzione delle liste utilizzate nelle operazioni [[muf_con_liste|MUF con Liste]], con l'aggiunta di un parametro `x.length` che indica la lunghezza della lista, utilizzato per ottimizzare le operazioni di `UNION`.

Le operazioni che non verranno modificate sono:
- [[muf_con_liste#Implementazione di `FIND(x)`|FIND(X)]]

---

## Implementazione di `MAKE(x, y)`
Per evitare il caso peggiore aggiungo il campo:
- `x.length`, lo aggiorno nel rappresentante
> Nelle union metto come seconda lista la più corta

### Codice
```c
MAKE(x){
	x.rap = x
	x.next = NIL
	x.last = x
	x.length = 1
	return x
}
```


---

## Implementazione di `WEIGHTED-UNION(x,y)`

Procedura per unire le liste `x` e `y`

```c
UNION(x, y){
	z = FIND(x)
	w = FIND(y)
	if (z != w){
		if (z.length >= w.length){
			LINK(z, w)
		}else{
			LINK(w, z)
		}
		
	}
}
```
### Costo
$\Theta(|L_y|)$ lunghezza della seconda lista

---

## Implementazione di `WEIGHTED-LINK(z, w)`

```c
LINK(z, w){ // z, w sono rappresentanti di 2 liste z != w
	z.last.next = w
	z.last = w.last
	z.length = z.length + w.length
	while(w != NIL){
		w.rap = z
		w = w.next
	}
}
```


---

## Costi

| Operazione | Costo                                                     |
| ---------- | --------------------------------------------------------- |
| Make       | $\Theta(1)$                                               |
| Find       | $\Theta(1)$                                               |
| Union      | $\Theta(\|L_2\|)\quad\quad \|L_2\|=min(\|L_x\|, \|L_y\|)$ |

## Quanto abbiamo ottimizzato `UNION`?

>`m` operazioni `MUF` di cui `n` `MAKE` usando `Weighted-Lists`

Posso valuta il costo di tutte le Union analizzando quanti puntatori `x.rap` vengono modificati complessivamente, in quanto il grosso del costo proviene dal `while` interno alla procedura `LINK`.

Concentriamoci su un oggetto `x`, quante volte al più modifico `x.rap`?
questo è equivalente a chiedersi quante volte al più `x` può finire nella seconda lista.

> Per finire nella seconda lista la prima lista deve essere più lunga della seconda lista.

Il che si traduce in: quante volte al più riesco ad unire la lista in cui sta x ad una lista più lunga?

### Analizziamo l'evolversi delle operazioni:

- Inizialmente `x` sta in una lista lunga 1 (grazie al `MAKE`)
	
- Faccio la prima operazione di union, gli viene modificato il rappresentante e finisce in una lista lunga 2.
	Affinché questa nuova lista venga messa per seconda deve venir unita ad una lista almeno lunga 2.

- Fatto ciò mi ritrovo con una lista lunga 4, si ripete il procedimento.



Quindi riesco a modificare il rappresentante di `x` al più $\Theta(\log n)$ volte

Questo ragionamento lo posso fare per tutti i possibili `x`, il costo diventa $\mathcal{O}(n\log{n})$

Questo significa che il costo complessivo delle `WEIGHTED-UNION` è:
$$
 \mathcal{O}(n\log{n})
$$


---

## Conclusioni 

Complessivamente le `m` operazioni `MUF` di cui `n` `MAKE` utilizzando `WEIGHTED-UNION` costano:
$$
\mathcal{O}(m + n\log{n})
$$