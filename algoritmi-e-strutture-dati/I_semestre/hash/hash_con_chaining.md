---
title: "Hash con Chaining"
aliases: ["Hash con Chaining"]
tags: [università, "algoritmi-e-strutture-dati", "I-semestre", "hash", "hash-con-chaining"]
created: 2025-07-14
---

## Hash con Chaining
uso un vettore $T$ di liste concatenate

### Esempio:
T\[i\] = lista concatenata contenente studenti che frequentano ASD per esempio quelli che hanno un numero di matricola $k\quad\text{t.c.}\quad k \mod{200} = i$

Considero una funzione di hash
$$
h: U \to \{0, ..., n-1\}
$$
$$
h(x.key) \in \{0, ..., n-1\}
$$

- L'elemento $x$ viene inserito nella lista $T[h(x.key)]$
- Per cercare $x$ scandisco la lista $T[h(x.key)]$

### Collisione
dato che $m < |U|$ h non è iniettiva

>[!definition]
>Collisione
>>$\exists x, y \in U$ t.c.$$
h(x.key) = h(y.key)
$$

Non posso garantire che non succeda
$$
h(x.key) = h(y.key) \quad\text{con x,y} \in K
$$
perché $K$ non è noto a priori e varia dinamicamente nel tempo, questo implica che nell'hash con chaining le liste concatenate gestiscono le collisioni (inserendo gli elementi le cui chiavi collidono nella stessa lista concatenata)

### Costo nel caso Peggiore
- funzione di costo: $h(key) \to \Theta(1)$
- Inserimento: $\Theta(1)$
- Ricerca/Cancellazione $\Theta(n)$

### Costo nel caso medio
#### Ipotesi di Hashing uniforme semplice

>[!definition]
>Ipotesi di Hashing uniforme semplice
>>Dato $x\in U$ senza esaminare $x.key$ ha probabilità $\frac{1}{n}$ di finire in $T[i]$
>>>[!quote] Significato
>>>>Ogni elementi dell'universo ha uguale probabilità di finire in una qualsiasi lista concatenata nella tabella.

>[!note] Costanti in gioco
>$|U|= M, |K|=n, |T|=m$


>[!definition]
>Fattore di carico
>> $\alpha = \frac{n}{m}$
>> >[!quote]
>> >>Indica che all'incirca avrò $\frac{n}{m}$ elementi in ogni lista nella tabella.


### Teorema
In una tabella di hash con chaining sotto ipotesi di hasing uniforme semplice:
La ricarca di x con esito negativo costa in media $\Theta(1+\alpha)$
La ricerca di x con esito positivo costa in media $\Theta(1+\alpha)$

>[!question] Perché ho scritto $\Theta(1+\alpha)$?
>Se $\alpha < 1 \implies \Theta(1+\alpha) = \Theta(1)\quad|T|\ge|K|$ (ho una tabella T di circa la dimensione di k)
>Se $\alpha > 1 \implies \Theta(1+\alpha) = \Theta(\alpha)\quad|T|\lt|K|$ (ho una tabella troppo piccola)


>[!question] Perché ho distinto la ricerca con esito negativo e esito positivo?
>Esito negativo implica che se sei sfortunato devi scorrere per tutta la lista (che sarà lunga circa $\alpha$).
>Nell'esito positivo sarebbe potuto succedere che facendo la media su tutte le lunghezze delle liste poteva essere che avrei ottenuto un risultato più piccolo di $\alpha$, questo viene smentito dal teorema. **Non si ottiene una ricerca con costo minore di $\Theta(1+\alpha)$**


#TODO _dimostrazione esito negativo_ [Video lezione (31 dicembre 2023, ora 01:14:50)](https://uniudamce.sharepoint.com/sites/117802-ALGORITMIESTRUTTUREDATIELABORATORIO/_layouts/15/stream.aspx?id=%2Fsites%2F117802%2DALGORITMIESTRUTTUREDATIELABORATORIO%2FDocumenti%20condivisi%2FGeneral%2FRecordings%2FASD%20lezione%2016%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E09893331%2D2056%2D475b%2D9e34%2Ddbffed3d7ace)

### Corollario
In una tabella di hash gestita con chaining sotto ipotesi di hashing uniforme semplice se $\alpha \le 1$ il costo nel caso medio di Inserimento, Ricerca e Cancellazione è $\Theta(1)$
(Sto mantenendo all'incirca lo spazio del sottoinsieme dell'Universo)


---


>[!example] Rappresentazione di funzione di hash
>$$
>h: U \to \{0, 1, 2,...,n-1\}
>$$

>[!question] Cosa controllare se effettivamente $h$ è una funzione di Hash?
>- controllare che effettivamente $\forall x\in U \quad h(x.key)\in[0, ..., n-1]$
>- $|U| >> m$ sicuramente $\exists x,y \text{ t.c. } h(x.key) = h(y.key)$[^1]
>- $\forall j\in [0, ..., n-1]\quad\exists x \text{ t.c. } h(x.key) = j$[^2]
>-  "Equiprobabilità" circa $\frac{|U|}{m}$ elementi di $U$ per ogni posizione di $T$
>
>[^1]: $h$ sicuramente non è iniettiva
>[^2]: per ogni posizione di $T$ deve esistere almeno un elemento di $U$ che finirebbe in quella posizione, questo implica che **$h$ è suriettiva**

## Funzioni di Hash standard
(chiavi con numeri interi)

### Metodo della divisione
$$
h(k) = k \mod m
$$
è garantito che $h(k) \in [0, ..., n-1]$
è suriettiva -> $|U| >> m$ (copre tutto)

>[!danger]
>Non prendere $m = 2^P$, guarderei solo gli ultimi $P$ bit

Soluzione:
prendere $m$ come primo, lontano da potenze di 2

>[!problem]
>Non posso avere una tabella delle dimensioni che scelgo io, devo andare dietro alla precedente soluzione

### Metodo della moltiplicazione

Chiavi: $0\le k \lt 1$
$$
h(k) = \lfloor{k\cdot m}\rfloor \quad \quad \quad 0\le\lfloor k\cdot m\rfloor \lt m-1
$$


>[!question] Dove abbiamo già visto questo metodo?
>Nel BacketSort:
>$A$ ha elementi uniformemente distribuiti in $[0,1)$
>($h$ soddisfa ipotesi di hashing uniforme semplice)
>$B$ viene riempito in modo uniforme
>BacketSort lineare


>[!question] Come faccio se ho chiavi maggiori di uno?
>Scelgo un numero $R$   $0\lt R \lt 1$
>Data una chiave $k$:
>$$0 \le k\cdot R - \lfloor{k\cdot R}\rfloor \lt 1$$
>applicando il metodo moltiplicativo:
>$$h(k) = \lfloor{(k\cdot R - \lfloor{k\cdot R}\rfloor)\cdot m}\rfloor$$
>>[!note] Da notare che
>>Non serve modificare $m$


