---
title: Muf con Alberi
aliases:
  - Muf con Alberi
tags:
  - insiemi-disgiunti
  - implementazioni
  - muf-con-alberi
created: 2025-06-14
---

Nodi con i seguenti campi:
- x.key
- x.parent

Dato che non so quanti nodi andrò ad inserire nell'insieme, evito l'elaborazione aggiuntiva per i figli, ci limitiamo quindi solo ad avere i puntatori al padre.

> _Il nodo radice ha un puntatore che punta a se stesso_


![[algoritmi-e-strutture-dati/II_semestre/insiemi_disgiunti/insiemi_di_dati_disgiunti_schema.md#^frame=68pt9ukvLetUMZHZRNdqo|25%]]

--- 

## Implementazione `MAKE(x)`

```c
MAKE(x){ // x è un oggetto di tipo nodo                                                     // x.key contiene già il valore
	x.parent = x
	return x
}
```


---

## Implementazione `FIND(x)`
Il rappresentante di un albero è la radice

```c
FIND(x){
	if (x != x.parent){
		return (FIND(x.parent))
	}else{
		return x
	}
}
```


---

## Implementazione `UNION(x,y)`

![[algoritmi-e-strutture-dati/II_semestre/insiemi_disgiunti/insiemi_di_dati_disgiunti_schema.md#^frame=EI2Gfrtii7SqRst591ZkR|75%]]

```c
UNION(x,y){
	z = FIND(x)
	y = FIND(y)
	if (z != w){
		LINK(z, w)
	}
}
```



```c
UNION(x,y){
	w.parent = z
}
```


---

## Confronto dei costi

Supponiamo `m` operazioni `Make` `Find` `Union` in totale, di cui `n` sono `MAKE`.

| Operazione | Costo            |
| ---------- | ---------------- |
| Make       | $\Theta(1)$      |
| Find       | $\mathcal{O}(n)$ |
| Union      | $\mathcal{O}(n)$ |


---


## Costo Complessivo per `m` operazioni

Supponiamo `m` operazioni Make Find Union in totale, di cui `n` sono `MAKE`.

|  Operazione   |                Costo                |  Quantità   |                       Costo Complessivo                       |
| :-----------: | :---------------------------------: | :---------: | :-----------------------------------------------------------: |
|     MAKE      |             $\Theta(1)$             |     `n`     |                          $\Theta(n)$                          |
|     FIND      |          $\mathcal{O}(n)$           |  $f\leq m$  | $\mathcal{O}(n)\cdot\mathcal{O}(m)$ = $\mathcal{O}(n\cdot m)$ |
|     UNION     | $\mathcal{O}(n-1) = \mathcal{O}(n)$ | $u\leq n-1$ |    $\mathcal{O}(n)\cdot\mathcal{O}(n) = \mathcal{O}(n^2)$     |
| ------------- |         ------------------          | ----------  |                   $\mathcal{O}(m \cdot n)$                    |


### Costo complessivo
Il costo complessivo delle operazioni MUF risulta essere $\mathcal{O}(m\cdot n)$ con $m = n + u + f$ (make + union + find), non possiamo semplificare, poiché $m$ dipende dalle `FIND` che sono state fatte


---

### Caso Peggiore – Costo $m\cdot n$

💬 _Domanda: "È veramente possibile raggiungere il costo di $m\cdot n$?"  
> _Risposta:_ Si se siamo nel caso sfortunato in cui la lista più corta viene unita alla lista più lunga.

Facciamo tante operazioni make
ottengo tanti alberi singoletto e li unisco in modo che l'i-esima lista singoletto sia unita all'i-1esima lista lista, la quale contiene quindi $i-1$ oggetti.
Facendo così, l'iesima `UNION` costerà $\Theta(1)$.
Esempio:
![[algoritmi-e-strutture-dati/II_semestre/insiemi_disgiunti/insiemi_di_dati_disgiunti_schema.md#^frame=mPu8eQWChJldywIADDZSU|100%]]
Possiamo fare di peggio?
Si basta unire sempre con il primo elemento aggiunto alla lista più lunga.
Esempio:
![[algoritmi-e-strutture-dati/II_semestre/insiemi_disgiunti/insiemi_di_dati_disgiunti_schema.md#^frame=kq6rQMCKSD4Uhzxsh5w0h|100%]]

Alla fine arrivo ad un albero in cui il rappresentante è `n` fino ad arrivare ad 1
eseguo `f` `FIND(1)`

Quindi: complessità finale:
$$
\Theta(n) + \sum_{i=2}^{n}\Theta(i) + f\cdot\Theta(n) = \Theta(n) + \Theta(n^2) + \Theta(m)\cdot\Theta(n) = \Theta(m\cdot n)
$$

---

## Come miglioro il costo?

Devo fare in modo che l'albero non si sbilanci, il problema sono le union in quanto se l'albero con altezza più grande viene unito ad un albero con altezza più piccola allora l'altezza di quello più grande cresce di 1 in quanto viene agganciato alla nuova radice.
Esempio:
![[algoritmi-e-strutture-dati/II_semestre/insiemi_disgiunti/insiemi_di_dati_disgiunti_schema.md#^frame=DGHWflxSye_QPvZyW20Ay|100%]]


Devo unire gli alberi in modo da far cresce l'altezza solo quando è necessario:
- Devo aggiungere l'albero più basso e quello più alto
- L'altezza cresce solo quando unisco due alberi aventi la stessa altezza

Questa implementazione di `UNION` si chiama `UNION-BY-RANK` dove il rango dell'albero sarà all'incirca l'altezza.