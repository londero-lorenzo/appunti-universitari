---
title: MUF con Liste
aliases:
  - MUF con Liste
tags:
  - insiemi-disgiunti
  - implementazioni
  - MUF-con-liste
created: 2025-06-13
---
# 🧩 Make-Union-Find con Liste

Utilizziamo liste per rappresentare insiemi disgiunti. Ogni oggetto `x` nella lista ha i seguenti campi:

- `x.key`: chiave identificativa
    
- `x.next`: puntatore al successivo elemento nella lista


### Esempio di rappresentazione

![[algoritmi-e-strutture-dati/II_semestre/insiemi_disgiunti/insiemi_di_dati_disgiunti_schema.md#^frame=vFiVqlHdLvnATNFd2IYqi|100%]]

---


## Operazione `FIND(x)` – struttura dei campi

Scopo: ottenere il rappresentante dell'insieme a cui `x` appartiene.

Problema iniziale:  
![[algoritmi-e-strutture-dati/II_semestre/insiemi_disgiunti/insiemi_di_dati_disgiunti_schema.md#^frame=0ALuzJZzsy2SCw0Tm2wh3|100%]]

### Problema

Iterare ogni lista per cercare `x` è inefficiente.

### Soluzione

Aggiungiamo a ogni elemento un puntatore `x.rap` al rappresentante (cioè il primo elemento della lista).

Nuova struttura per ogni elemento:

- `x.key`
    
- `x.rap`
    
- `x.next`
    

![[algoritmi-e-strutture-dati/II_semestre/insiemi_disgiunti/insiemi_di_dati_disgiunti_schema.md#^frame=OGO5m1z-4UQR68nnt7hlG|100%]]


---


## Operazione `UNION(x, y)` – struttura dei campi

Obiettivo: unire le liste $S_x$ e $S_y$.

1. Usiamo `FIND(x)` e `FIND(y)` per verificare se appartengono a insiemi diversi.
    
2. Concatenazione:
    
    - Scansione di $S_x$ per arrivare in fondo.
        
    - Scansione di $S_y$ per aggiornare i rappresentanti.
        

![[algoritmi-e-strutture-dati/II_semestre/insiemi_disgiunti/insiemi_di_dati_disgiunti_schema.md#^frame=4CI_3qvg2bunOlMv7KFxY|100%]]

**Complessità**: $\Theta(|S_x| + |S_y|)$

### Ottimizzazione: salvare l’ultimo elemento

Aggiungiamo un campo `x.last`, **solo nel rappresentante**, per evitare di scandire $S_x$.

Campi aggiornati:

- `x.key`
    
- `x.rap`
    
- `x.next`
    
- `x.last` (solo nel rappresentante)


![[algoritmi-e-strutture-dati/II_semestre/insiemi_disgiunti/insiemi_di_dati_disgiunti_schema.md#^frame=Dz8vUERmPXnfgG-g8U6qb|100%]]

**Risultato**: `UNION(x, y)` deve scandire solo $S_y$.


---

## Implementazione di `MAKE(x)`

Procedura che costruisce il singoletto di `x`
```c
MAKE(x){ // x è gia del tipo corretto (è una scatola pronta all'uso)                        // x.key è gia inizializzato
	x.rap = x
	x.next = NIL
	x.last = x
	return x
}
```

### Costo
$\Theta(1)$

---

## Implementazione di `FIND(x)`

Procedura per restituire il rappresentante

```c
FIND(x){
	return x.rap
}
```
### Costo
$\Theta(1)$

---

## Implementazione di `UNION(x,y)`

Procedura per unire le liste `x` e `y`

```c
UNION(x, y){
	z = FIND(x)
	w = FIND(y)
	if (z != w){
		LINK(z, w)
	}
}
```
### Costo
$\Theta(|L_y|)$ lunghezza della seconda lista

---

## Implementazione di `LINK(z, w)`

```c
LINK(z, w){ // z, w sono rappresentanti di 2 liste z != w
	z.last.next = w
	z.last = w.last
	while(w != NIL){
		w.rap = z
		w = w.next
	}
}
```



---

## Confronto dei costi

| Operazione | Costo             |
| ---------- | ----------------- |
| Make       | $\Theta(1)$       |
| Find       | $\Theta(1)$       |
| Union      | $\Theta(\|S_y\|)$ |
Non noterò sostanziali differenze sui singoli costi utilizzando le ottimizzazioni.
La differenza la vedo quando vado a valutare il costo di `m` operazioni complessive `MUT` di cui `n` `MAKE`.


---

## Costo Complessivo per `m` operazioni

Supponiamo `m` operazioni Make Find Union in totale, di cui `n` sono `MAKE`.

|  Operazione   |                Costo                |  Quantità   |                   Costo Complessivo                    |
| :-----------: | :---------------------------------: | :---------: | :----------------------------------------------------: |
|     MAKE      |             $\Theta(1)$             |     `n`     |                      $\Theta(n)$                       |
|     FIND      |             $\Theta(1)$             |  $f\leq m$  |   $\Theta(1)\cdot\mathcal{O}(m)$ = $\mathcal{O}(m)$    |
|     UNION     | $\mathcal{O}(n-1) = \mathcal{O}(n)$ | $u\leq n-1$ | $\mathcal{O}(n)\cdot\mathcal{O}(n) = \mathcal{O}(n^2)$ |
| ------------- |         ------------------          | ----------  |                 $\mathcal{O}(m + n^2)$                 |

### Costo complessivo
Il costo complessivo delle operazioni MUF risulta essere $\mathcal{O}(m + n^2)$ con $m = n + u + f$ (make + union + find), non possiamo semplificare, poiché $m$ dipende dalle `FIND` che sono state fatte


---

### Caso Peggiore – Costo Quadratico

> 💬 _Domanda: "È veramente possibile raggiungere il costo di $n^2$?"  
> _Risposta:_ Si se siamo nel caso sfortunato in cui la lista più corta viene unita alla lista più lunga.
>![[algoritmi-e-strutture-dati/II_semestre/insiemi_disgiunti/insiemi_di_dati_disgiunti_schema.md#^frame=zd0Bzk9hs3eqy5UgUbhEp|100%]]



#### Costo complessivo:
$$\sum_{i= 2}^{n}\Theta(i) = \frac{n(n+1)}{2}-1 = \Theta(n^2)$$
Le `UNION` sono costose se la lista lunga viene sempre messa come **prima**.


---

## Soluzione

Per risolvere il problema del costo quadratico si introducono le:  
👉 [[muf_con_weighted-lists|MUF con Weighted-Lists]]

---