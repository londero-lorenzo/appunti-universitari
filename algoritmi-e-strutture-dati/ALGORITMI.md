# [[Algoritmi di Ordinamento]]

# Alberi

## [[Albero Binario di Ricerca]]





# RBTRee
RBTree nascono dalla necessità di evitare che inserimento / cancellazione / ricerca costino nel caso peggiore $\Theta(n)$ se l'albero è sbilanciato. (il caso medio è $O(h)$ con h altezza).

Possibile evitare questo caso con le rotazioni per mantenere gli alberi bilanciati.

### Definizione RBTree:
RBTree sono BST in cui ogni nodo ha un campo color che può assumere due valori: Red o Black e valgono le seguenti condizioni:
+ Tutte le foglie sono B e NIL
+ ogni nodo non foglia ha due figli
+ Ogni nodo R ha due figli B
+ Ogni nodo R ha genitore B
+ Per ogni nodo x lungo ogni cammino x-foglia trovo sempre lo stesso numero di nodi B
+ $bh(x)$ (altezza nera) nel cammino x-foglia non conto x e conto la foglia; $bh(T)=bh(T.root)$.
+ La radice è sempre B.

### Proprietà:
+ Nel peggiore caso in cui ho tutti nodi neri un ramo può essere alto $bh(T)$, nel migliore dei casi in cui c'è uno nero e uno rosso alternati un ramo è alto $h(T)=2*bh(T)$.
+ Se T è un RBTree allora $h(T)<=2*bh(T)$ e $n>=2^{bh(T)}-1$
+ Se T è un RBTree contenente n chiavi (numero nodi interni non foglie) allora $h=\Theta(logn)$
+ LEMMA: Se T è un RBTree allora $n>=2^{bh(T)}-1$
+ 

---

## Rotazioni:
Possono essere o a dstra o a sinistra.
##### proposizione: 
Se T è un BST, dopo aver effettuato LeftRotate(T, x) o RightRotate(T, x) T è ancora un BST.

#### Complessità:
$\Theta(1)$ in tutti i casi in qaunto basta cambiare i puntatori interessati nello scambio, per un massimo di 7 puntatori

#### Codice left-rotate:

```
LeftRotate(T, x){
	y = x.right
	x.right = y.left            //turn y's left subtree into x's right substree
	if (y.left != T.nil){        //if y's left subtree is not empty
		y.left.p = x
	}                            //then x becomes the parent of the subtree's 
	y.p = x.p                    //x's parent becomes y's parent
	if (x.p == T.nil){           //if x was the root...
		T.root = y                //...then y becomes the root
	}else if (x == x.p.left){     //otherwise, if x was a left child...
		x.p.left = y              //...then y becomes a left child
	}else{
		x.p.right = y            //otherwise, x was a right child, and now y is
	}
	y.left = x                   //make x become y's left child
	x.p = y
}
```

---

## Ricerca:
Come in un BST ma con costo: $O(logn)$

---

## Inserimento:
Diverse fasi di inserimento:
+ Inserisco la nuova chiave come nei BST
+ Il nuovo nodo viene colorato di rosso
+ Se la proprietà dei RBTree (ogni nodo R ha due figli B e genitore B) è violata applico rotazioni e ricolorazioni per correggere il problema
	+ Sposto il problema "R figlio di R" verso l'alto:
		+ o si risolve 
		+ o arrivo alla radice e la ricoloro

Le rotazioni e ricolorazioni si dividono in diversi casi:
+ ###### Caso fortunato: 
	+ x R figlio di R con zio di x Black opposto ad x (left-right | right-left)
	+ Risoluzione: RightRotate(T, n)
+ ###### Caso quasi fortunato:
	+ x R figlio di R con zio Black dallo stesso lato di x (left-left | right-right)
	+ Risoluzione: applico LeftRotate(T, p) e poi applico il caso fortunato
+ ###### Caso sfortunato:
	+ x R figlio di R con zio Red
	+ Risoluzione: Ricoloro genitore, zio e nonno e controllo: se nonno è figlio di rosso continuo sennò ho finito


#### Codice Inserimento:
```
RB-INSERT(T, z){
	 y ← nil[T]
	 x ← radice[T]
	 while (x != nil [T]){
		 y ← x
		 if (key[z] < key[x]){
			  x ← left[x]
		 }else{
			  x ← right[x]
		 }
	}
	 p[z] ← y
	 if (y = nil[T]){
		  radice[T] ← z
	 }else if (key[z] < key[y]){
		 left[y] ← z
	 }else{
		 right [y] ← z
	 left[z] ← nil [T]
	 right [z] ← nil[T]
	 color [z] ← ROSSO
	 RB-INSERT-FIXUP(T, z)
 }




RB-INSERT-FIXUP(T, z){
	while (color[p[z]] = ROSSO){
		 if (p[z] = left[p[p[z]]]){
			 y ← right[p[p[z]]]
			 if (color [y] = ROSSO){
				 color [p[z]] ← NERO    //Caso 1
				 color [y] ← NERO    // Caso 1
				 color [p[p[z]]] ← ROSSO     // Caso 1
				 z ← p[p[z]]       //Caso 1
			 }else if (z = right[p[z]]){
				 z ← p[z]      // Caso 2
				 LEFT-ROTATE(T, z)      // Caso 2
				 color [p[z]] ← NERO       // Caso 3
				 color [p[p[z]]] ← ROSSO       // Caso 3
				 RIGHT-ROTATE(T, p[p[z]])       // Caso 3
		 }else{
		  (come la clausola then con “right” e “left” scambiati)
	 color [radice[T]] ← NERO
}
```

##### Complessità inserimento:
Costo complessivo: $\Theta(logn)$.
Dato dal numero di volte in cui applico i tre casi di correzione ovvero l'altezza dell'albero, ovvero $O(logn)$. Infatti scendere da una radice ad una foglia costa $\Theta(n)$.

---

### Cancellazione:
Come nei BST cerco k chiave da cancellare e lo cancello oppure cancello il nodo che contiene il successore se k è un nodo con due figli.
Mi concentro sul nodo che sparisce dall'albero, che viene sostituito con suo figlio non NIL o con NIL------> potrebbe dare un problema!--------> se sostituisco un nodo nero con un'altro nero 
(B-B) avrò un ramo la cui $bh(x)$ sarà minore degli altri rami. (con R-B;  B-R; R-R non c'è problema).
Cerco di risolvere il problema con rotazioni e/o cancellazioni.
###### Soluzione: 
Conto momentaneamente il nodo possibilmente problematico come Double-Black:
+ Se il Double-Black è RED lo coloro di Black e ho finito
+ Se il Double-Black è BLACK sistemo con rotazioni/ricolorazioni
Possibili casi:
+ ###### Caso fortunato:
	+ x double-black con nipote n RED opposto a x (left-right | right-left)
	+ Soluzione: RightRotate(T, p), ricoloro nodo n
+ ###### Caso quasi fortunato:
	+ x double-black con nipote n RED dallo stesso lato di x (left-left | right-rigth)
	+ Soluzione: faccio LeftRotate(T, f) ricolorando f e n e mi riconduco al caso fortunato
+ ###### Caso sfortunato:
	+ x double-black con nipoti e fratello tutti BLACK
	+ Soluzione: ricoloro f, ricoloro radice se è rossa e apposto
+ ###### Caso antipatico:
	+ x double-black, con nipoti BLACK e fratello RED
	+ Soluzione: RightRotate(T, p) e dopo o finisco nel caso quai fortunato, o nel caso fortunato  o sposto il double-black in un Red e termino

#### Codice Cancellazione:
```
RB-DELETE(T, z){
	if (left[z] = nil [T] || right[z] = nil [T]){
		y ← z
	}else{
		y ← TREE-SUCCESSOR(z)
	}
	if (left[y] != nil[T]){
		x ← left[y]
	}else{
		x ← right[y]
	}
	p[x] ← p[y]
		if (p[y] = nil[T]){
			radice[T] ← x
		}else if (y = left[p[y]]){
			left[p[y]] ← x
		}else{
			right [p[y]] ← x
		}
	if (y != z){
		key[z] ← key[y]       //copia i dati satelliti di y in z
	}
	if (color [y] = NERO){
		RB-DELETE-FIXUP(T,x)
	}
	return y
}



RB-DELETE-FIXUP(T,x){
	while (x != radice[T] && color [x] = NERO){
		if (x = left[p[x]]){
			w ← right[p[x]]
			if (color [w] = ROSSO){
				color [w] ← NERO ✄ Caso 1
				color [p[x]] ← ROSSO ✄ Caso 1
				LEFT-ROTATE(T, p[x]) ✄ Caso 1
				w ← right[p[x]] ✄ Caso 1
			}
			if (color [left[w]] = NERO && color [right[w]] = NERO){
				color [w] ← ROSSO ✄ Caso 2
				x ← p[x] ✄ Caso 2
			}else if (color [right[w]] = NERO){
				color [left[w]] ← NERO ✄ Caso 3
				color [w] ← ROSSO ✄ Caso 3
				RIGHT-ROTATE(T,w) ✄ Caso 3
				w ← right [p[x]] ✄ Caso 3
			}
			color [w] ← color [p[x]] ✄ Caso 4
			color [p[x]] ← NERO ✄ Caso 4
			color [right [w]] ← NERO ✄ Caso 4
			LEFT-ROTATE(T, p[x]) ✄ Caso 4
			x ← radice[T] ✄ Caso 4
		}else{
		 (come la clausola then con “right” e “left” scambiati)
		}
	color [x] ← NERO
}
```

#### Fondere due RBTree:
Problema di fondere due RBTree avendo due RBTree e una chiave k tale che: tutte le chiavi di T1 sono < k  e tutte le chiavi di T2 sono > k.
(Se fossere BST porrei come radice k e metterei come figli T1 e T2)
Due casi:
+ Se $bh(T1)=bh(T2)$ posso fare la stessa cosa perché l'altezza nera è la stessa
+ Se $bh(T1)>bh(T2)$ devo scendere in T1 verso destra finchè non arrivo ad un nodo nero che ha la stesa altezza di T2. A quel nodo collego k RED posto sopra T2.
  Se il collegamento di T1 a k è rosso svolgo le 3 opzioni di aggiustamento
##### Costo:
$O(logn)$ con n numero totale di chiavi. (costo del join).

---

# BTree

I BTree sono una generalizzazione dei BST Bilanciati.
Per tutti i precedenti algoritmi è scontato il caricamento totale in RAM, invece per i BTree solo la parte in uso è in RAM. Si dividono quindi due costi: il costo della CPU per la RAM e R/W (lettura e scrittura) su disco.

#### Definizione BTree:
Btree di grado t (numero intero fissato $\geq$ 2) è un albero in cui in ogni nodo x diverso dalla radice sono memorizzate una quantità x.n di chiavi intere e sono ordinate in ordine crescente. Inoltre tutte le foglie si trovano allo stesso livello.
x.n --> campo del nodo x che dice quanti chiavi ha x in x.key (intero)
x.key --> campo del nodo x che contiene tutte le chiavi (vettore)
x.leaf --> campo che vale TRUE se il nodo è foglia (booleano)
x.c --> Se x non è foglia ha $x.n+1$ puntatori memorizzati in x.c  (che sta nella memoria secondaria) (vettore)

##### Proprietà x.n:
+ Se x è diverso dalla radice --> t1 $\leq$ x.n $\leq$ 2t -1
+ Se x è la radice --> $1\leq x.n \leq2t-1$

##### Proprietà x.c:
+ Tutte le chiavi appartenenti al sottoalbero radicato in x.c[i] devono essere > di x.key[i-1] e < di x.key[i]

##### Proprietà BTree:
+ Un BTree di grado t contenente n chiavi può essere alto al massimo $h=log_{t}\left(\frac{n+1}{2}\right)$ 
+ In generale $h\leq log_{t}\left(\frac{n+1}{2}\right)$ ; $h\in\Theta(log_{t}(n))$  (con t messo per consuetudine anche se è costante)

---
## Ricerca:

Per la ricerca di una chiave k utilizzo la ricerca binaria con un doppio contatore e mi fermo quando $k{1}<k\leq k{2}$  (se k2 = k ristituisco direttamente k2) e carico in memoria centrale il figlio e rifaccio la ricerca.
La procedura $DiskRead(T.root)$ va nel disco e legge le informazioni di T.root e le carica in RAM (memoria centrale).

#### Codice Ricerca:
```
BTreeSearh(x, k){
	i <- 1
	while(i <= x.n && x.key[i] < k){
		i <- i+1
	}
	if(i <= x.n && x.key[i] = k){     //caso fortunato
		return(x, i)
	}
	if(x.leaf){      //caso in cui il figlio non esiste -> k non c'é
		return NIL
	}
	y <- DisKRead(x.c[i])     //non scordarsi questo
	return BTreeSearch(y, k)
}
```

##### Complessità:
+ In memoria centrale (CPU)(tutto ciò che non è DiskRead e DiskWrite): $O(h*t)=O((log_{t}(n))*t)$
+ In memoria secondaria (R/W): $O(log_{t}(n))$ 

---

## Inserimento:

Fasi:
+ Parto dalla radice
+ Scendo nell'albero (usando la chiave k per vedere dove scendere come se la stessi cercando)
+ Arrivati ad un nodo x e individuato il figlio y di x in cui dovremmo scendere, se y è pieno prima di scendere splitto y (Preemptive Split).
+ Il nodo viene sempre inserito in un nodo foglia.

###### Preemptive split: 
quando un nodo ha il numero massimo di chiavi (prima di scendere in esso (preemptive)) lo splitto ovvero prendo il valore intermedio e lo passo al nodo genitore, separando poi le chiavi rimaste in due nodi. nel momento in cui facendo queste azioni si riempiono tutti i nodo fino alla radice, si aumenta l'altezza dell'albero.

### Codice Inserimento:

##### BTreeCreate:
Scopo di BTreeCreate è creare un nuovo BTree vuoto
```
BTreeCreate(T, t){
  x <- AllocateNode(t)      // Alloca un nuovo nodo x con capacità t
  x.leaf <- TRUE            // Il nodo è una foglia
  x.n <- 0                  // Nessuna chiave nel nodo
  DiskWrite(x)              // Salva il nodo su disco
  T.root <- x               // Il nodo diventa la radice dell'albero T
}
```

##### BTreeSplit:
Scopo di BTreeSplit è di dividere il nodo pieno y in due nodi e aggiorna il padre x per accogliere il nuovo figlio
```
BTreeSplit(x, i, y, t){ //x non è pieno, y i-esimo figlio di x, y è pieno,                             //sia x che y sono caricati in memoria centrale
	z <- AllocateNode(t)         // Alloca un nuovo nodo z
	z.leaf <- y.leaf             // z sarà una foglia se y lo è
	for (j <- 1 to t-1){
		z.key[j] <- y.key[t + j] //Copia la seconda metà delle chiavi di y in z
	}
	if (not y.leaf){
		for (j <- 1 to t){
		    z.c[j] <- y.c[t + j]     // Copia i figli se non è una foglia
	    }
	}
	y.n <- t - 1                 // y ora ha solo la prima metà delle chiavi
	z.n <- t - 1
	for(j <- x.n down to i){
		x.key[j+1] <- x.key[j]
	}
	x.key[i] <- y.key[t]
	for(j <- x.n+1 down to i+1){
		x.c[j+1] <- x.c[j]
	}
	x.c[i+1] <- z
	x.n <- x.n+1
	DiskWrite(x)
	DiskWrite(y)
	DiskWrite(z)
}
```
##### Complessità BTreeSplit:
+ CPU: $\Theta(t)$
+ R/W: $\Theta(1)$

##### BTreeInsertNotFull:
Scopo di BTReeInsertNotFull è inserire una chiave in un nodo non pieno
```
BTreeInsertNotFull(x, k, t){  // x è in RAM, x non è un nodo pieno
	if(x.leaf){                 // Se x è una foglia
		j <- x.n                 // j è l'indice dell'ultima chiave
		while(j > 0 && x.key[j] > k){   //complessità ciclo: O(t)
			x.key[j+1] <- x.key[j]        // Sposta le chiavi maggiori di k                                              //una posizione a destra
			j <- j-1
		}
		x.key[j+1] <- k            // Inserisce k nella posizione corretta
		x.n <- x.n+1               // Incrementa il numero di chiavi
		DiskWrite(x)               // Scrive il nodo su disco
	}else{           // x non è una foglia: bisogna scendere nel figlio giusto
		j <- 1
		while(j <= x.n && x.key[j] < k){    //complessità ciclo: O(t)
			j <- j+1       // Trova l'indice del figlio in cui inserire k
		}
		y <- DiskRead(x.c[j])     // Legge da disco il figlio y in cui andare
		if(y.n < 2t-1){          // Se y non è pieno
			BTreeInsertNotFull(y, k, t)    // Inserisce ricorsivamente in y
		}else{                   // y è pieno e va splittato
			BTreeSplit(x, j, y, t)      // Divide y in due nodi e promuove la                                         //chiave centrale in x
			DiskRead(x) //Rilegge x per aggiornare i riferimenti dopo lo split
			if(k < x.key[j]){   // Dopo lo split, decide in quale dei due                                     //figli inserire k
				y <- DiskRead(x.c[j])
			}else{    // Altrimenti, va nel figlio destro (nuovo)
				y <- DiskRead(x.c[j+1])
			}
			BTreeInsertNotFull(y, k, t)   // Inserisce ricorsivamente in y                                              // (o nel nuovo figlio)
		}
	}
}
```
##### Complessità BTreeInsertNotFull:
+ CPU: $\Theta(h)*O(t)=O(t*log_{t}(n))$
+ R/W: $\Theta(h)=\Theta(log_{t}(n))$

##### BTreeInsert:
Lo scopo di BTreeInsert è di inserire la chiave k in un albero BTree. è la procedutra principale che chiama in eveniente tutte le altre appena viste.
```
BTreeInsert(T, t, k){      //k è una chiave non già in T
	r <- T.root            // r è la radice corrente del B-Tree
	if(r.n < 2t-1){       // Se la radice NON è piena (ha meno di 2t-1 chiavi)
		BTreeInsertNotFull(r, k, t) // Inserisce direttamente nel sottoalbero                                      //radicato in r
	}else{                  // Se la radice è piena
		s <- AllocateNode(t)      // Alloca un nuovo nodo s
		s.n <- 0            // Inizia con 0 chiavi
		s.leaf <- FALSE       // La nuova radice non è una foglia
		s.c[1] <- r          // Il primo figlio della nuova radice è la                                     //vecchia radice r

		BTreeSplit(s, 1, r, t) // Divide r (pieno) in due figli, promuovendo                                  //la chiave centrale a s
		DiskRead(s)    //Rilegge s da disco per aggiornare eventuali modifiche
		T.root <- s    // Imposta s come nuova radice dell'albero
		BTreeInsertNotFull(s, k, t)   // Inserisce ricorsivamente la chiave k                                       //nella nuova struttura
	}
}
```

##### Complessità BTreeInsert:
Uguale a BTreeInsertNotFull
+ CPU: $\Theta(h)*O(t)=O(t*log_{t}(n))$
+ R/W: $\Theta(h)=\Theta(log_{t}(n))$

---
## Cancellazione:
Idea: 
+ Se k è in una foglia x cancello k da x
+ se k è in un nodo interno x uso predecessore o successore
Il problema sorge nel caso di nodi vuoti (t-1 chiavi)
Risoluzione: Ad ogni passo prima di scendere controllo che il nodo x non sia vuoto (abbia almeno t chiavi). 
Con y, z fratelli di x:
+ Se y (o z)ha t-1 chiavi -> Merge(x, y, M) (inverso dello split)
+ Se invece sia y che z hanno più di t-1 chiavi si ruba una chiave ad y

###### Diversi casi della cancellazione:
+ 1) Se k è in x e x è una foglia -> accorcio il vettore del nodo e cancello k da x
+ 2) Se k è in x ma x non è foglia:
	+ Se y ha almeno t chiavi userò il predecessore di k (in T[y])
	+ Se y ha t-1 chiavi e z ha almeno t chiavi uso il successore di k (in T[z])
	+ Se entrambi hanno t-1 chiavi faccio il Merge tra y e z portando giù la chiave k.
+ 3) Se k non è in x trovo il figlio di x (y) in cui dovrei scendere:
	+ Se y ha almeno t chiavi scendo in y
	+ Se y ha solo t-1 chiavi guardo i 2 fratelli di y (u e v)
		+ Se u ha almeno t chiavi rubo una chiave ad u (e ne passo una giù)
		+ Se v ha almeno t chiavi rubo una chiave a v (e ne passo una giù)
		+ Se u e v hanno t-1 chiavi eseguo Merge tra y e u

##### Codice cancellazione: (IMPOSSIBILE, né la carla né il libro ha il codice quindi presumo non sia da sapere)

---

# Insiemi disgiunti

Sono insiemi disgiunti due insiemi con intersezione vuota. Ovvero due insiemi A e B sono disgiunti se la loro intersezione è vuota. Ossia se $A\cap B=\emptyset$.

Gli elementi di ogni classe sono tutti equivalenti: per rappresentare una classe scelgo un suo rappresentante.

Ad esempio il rappresentante della classe 2 $mod$ 5  è 2 $mod$ 5 e 12 $mod$ 5 equivale a 2 $mod$ 5 (identificativo unico (chiave)).

##### Proprietà:
+ se due numeri hanno lo stesso rappresentante appartengono alla stessa classe

---

## Implementazione con liste concatenate:
Due tipi:
- prima:
	- x.key
	- x.next
	- x.rap
	- x.last
- seconda:
	- x.key
	- x.next
	- x.set
		- s.length
		- s.head (rappresentante)
		- s.tail
#### Find (primo caso):
```
Find(x){
	return x.rap
}
```

#### Find (secondo caso):
```
Find(x){
	return x.set.head
}
```
Complessità sempre $\Theta(1)$
#### Union:
Vedo se Find(x) e Find(y) sono uguali. Se sono diversi devo porre gli elementi di una lista in coda all'altra.
+ Scandisco tutta la prima lista per "aggiungere la seconda lista"
+ Scandisco tutte le seconde liste per modificare i raggruppamenti

Codice Union:
```
Union(x, y){
	z <- Find(x)
	w <- Find(y)
	if(z != w){
		v <- z
		while(v.next != NIL){
			v <- v.next
		}
		v.next <- w
		while( w != NIL){
			w.rap <- z
		}
	}else{
		"sono già nello stesso insieme"
	}
}
```

Costo di m operazioni (m = n+u+f) operazioni Make, Union, Find di cui n Make?
- Make(x) -> $\Theta(1)$ singola, complessivamente: $\Theta(n)$
- Find(x) -> $\Theta(1)$ singola, complessivamehte: O(m)
- Union(x) -> O(m) singola, complessivamente: $O(m^{2})$
Risposta: $O(m+n^2)$ 
Se ho una concatenazione di liste di un elemento e ad ogni Union metto quella appena fatta per seconda, alla i-esima iterazione la seconda lista avrà i elementi, quindi le Union avranno un costo complessivo di $\Theta(n^2)$.

---
## Weighted Union (con liste concatenate)
Euristica per evitare il caso peggiore $\Theta(n^{2})$ nella Union.
Idea: Aggiungo un campo nel caso 1 (con x.rap) x.length (aggiornato sono nel rappresentante) e nel caso 2 (con x.set) s.length.
Nella Union metto sempre per seconda la lista più corta.
+ Costo complessivo di u Union con Wighted Union è $O(n)$ per valutare quanti puntatori a rappresentanti vengono modificati
-  x.rap viene modificato al più $log_{2}(n)$ volte in quanto viene cambiato solo se il rappresentante appartiene alla seconda lista, quindi minimo la lista su cui fare Union deve essere ogni volta il doppio di quella precedente.
Teorema: con liste concatenate e Weighted Union n operazioni Make, Union, Find di cui n Make costano al più $O(m+n*log_{2}(n))$ con m costo Find, $n*log_{2}(n)$ ed n costo delle Make quindi viene assorbito.

Codice Weighted_Union:
```
Weighted_Union(x, y){
	z <- Find(x)
	w <- Find(y)
	if(z != w){
		if(z.set.length >= w.set.length){
			Link(z, w)
		}else{
			Link(w, z)
		}
	}
}

Link(u, v){   //u e v sono 2 rap. La lista di u è più lunga
	u.set.length <- u.set.length + v.set.length
	w <- v
	while(w != NIL){
		w.set <- u.set     //oppure w.rap <- u
		w <- w.next
	}
	u.set.tail.next <- v       //dovrà essere il primo della seconda lista
	u.set.tail <- v.set.tail
}
```

---

## Implementazione con Alberi:
Ogni nodo avrà due puntatori:
- x.key
- x.parent
#### Make:
```
Make(x){
	x.parent <- x
	return x
}
```


#### Find:
```
Find(x){
	while(x.parent != x){
		x <- x.parent
	}
	return x
}
```

#### Union:
```
Union(x, y){
	z <- Find(x)
	w <- Find(y)
	if(z != w){
		w.parent <- z
	}
}
```

Quanto costano m Make, Union, Find di cui n Make?
- Make(x) complessità: $\Theta(1)$ singola, complessivamente: $\Theta(n)$
- Find(x) complessità: $\Theta(n)$ singola, complessivamente: $O(m*f)=O(n*m)$
- Union(x, y) complessità: $\Theta(n)$ singola, complessivamente: $O(n*n)=O(n^{2})$

---
## Union by Ranks (con alberi):
Ogni nodo avrà:
- x.key
- x.parent
- x.rank (approssima l'altezza ed è aggiornato solo nella radice)
	- Aggancio la radice che ha rango minore a quella che ha rango maggiore

Codice Make:
```
Make(x){
	x.parent <- x
	x.rank <- 0
}
```

Codice Union_by_Ranks:
```
Union_by_Ranks(x, y){
	z <- Find(x)
	w <- Find(y)
	if(z != w){
		if(z.rank >= w.rank){
			w.parent <- z
			if(z.rank == w.rank){
				z.rank <- z.rank+1
			}
		}else{
			z.parent <- w
		}
	}
}
```

#### Costo m operazioni di cui n Make usando Union_by_Ranks:
- Make(x) -> $\Theta(1)$ singola, complessivamente: $\Theta(n)$
- Union_by_Ranks(x) -> $O(h)$ singola, complessivamente: $O(n)*O(h)$
- Find(x) -> $O(h)$ singola, complessivamente: $O(m)*O(h)$
h con Union_by_ranks può valere al massimo $O(log_{2}(n))$ (senza Union_by_ranks vale $h=O(n)$)
###### Proprietà: 
Un albero costruito con Union_by_Ranks avente altezza h contiene almeno $2^h$ nodi.
###### Dimostrazione della proprietà:
Per induzione sul numero di Union_by_Ranks che hanno portato alla costruzione di quell'albero.
- Caso base: 0 operazioni Union ->albero fatto con make infatti ha $2^0$ nodi ovvero 1.
- Passo induttivo: supponiamo vera la tesi che sono state fatte al più $l$ Union_by_Ranks.
	- Tesi: Vale la tesi anche se l'altezza è costruita con $l+1$ Union_by_Ranks
	- L'ultima operazione union ha agganciato un albero
- 1) Se S ha altezza inferiore a h-1 vuol dire che T aveva già altezza h prima dell'ultima Union_by_Ranks (per ipotesi induttiva, T contiene $2^h$ nodi prima di essere unito ad S).
- 2) Se S ha altezza h-1 T prima dell'ultima Union aveva altezza h-1. Per ipotesi induttiva su T prima dell'ultima union e su S abbiamo almeno $2^{h-1}+2^{h-1}=2*2^{h-1}=2^h$ 
	Union_by_Ranks -> $O(m*log(n))$

---
## Find con Path Compression (con alberi)
```
Find_PC(x){
	if(x != x.parent){
		x.parent = Find_PC(x.parent)
	}
	return x.parent
}
```
Cambio il puntatore di B facendolo puntare ad A e la funzione ritorna adesso B.parent ovvero A.

#### Costo di m operazioni Make, Union, Find di cui n Make con Union_by_Ranks e Path Compression:
Costo: $O(m*\alpha(m, n))$     di cui $\alpha(m, n)$ è l'inversa della funzione di Ackermann che è una funzione lentissima, quasi costante, quindi il costo è poco poco più che lineare.

---

# Grafi

Un grafo è una struttura dati dinamica (generalizzazione dell'albero) in cui non c'è più la regola del parent singolo, un nodo può essere figlio di un antenato o avere come figlio un antenato.
I grafi si distinguono in:
- Orientati:
	- Definizione: G=(V, E) con V insieme di nodi o vertici ed E insieme degli archi
	- Esempio: $v=[a, b, c]$ e $E=[(a, b), (b, c)]$ 
- Non orientato:
	- Definizione: G=(V, E) con V insieme dei nodi o vertici ed E è insieme di cerchi, in cui ogni arco è una coppia non ordinata di nodi. Esempio: {i, j}

Nozioni:
- Nodi adiacenti: Dato i $\in$ V i nodi adiacenti ad i sono i nodi collegati ad i con un arco
- Cammino: sequenza di archi:
	- Sorgente: primo nodo
	- Target: ultimo nodo
- Raggiungibili: Dato i $\in$ V i nodi raggiungibili da i sono tutti quelli che i raggiunge attraverso un cammino

### Implementazione dei grafi:
- Matrici booleane |V| x |V|:     $M[i, j] =$ 1 se (i, j) $\in$ E     oppure0 se (i, j) $\not\in$ E
	- Nei grafi non orientati la matrice appare simmetrica rispetto alla diagonale principale, formata da tutti zeri in quanto i nodi non sono collegati a loro stessi
	- Spazio occupato: $O(|V|^2)$
- Vettore di lunghezza |V| di liste di adiacenza ---> implementazione tramite liste
	- Esempio: L[i] = [j, k, l] lista di nodi adiacenti ad i
	- Spazio occupato: $\Theta(|E|)$
Spazio occupato in totale: $\Theta(|V|)+\Theta(|E|)=O(|V|^2)$
[Utilizzo Adj[i] se non specifico se uso matrici o vettori]

##### Operazioni fattibili con matrici e con liste:
- decidere se (i, j) appartiene  a E:
	- Matrici: ritorno M[i, j]  --> costo: $\Theta(1)$
	- Liste: Scandisco L[] --> Costo: $O(|V|)$
- Contare gli archi uscenti da i:
	- Matrici: scandisco la riga M[i, -] --> Costo: $\Theta(|V|)$
	- Liste: scandisco la lista L[i]  --> Coto: $\Theta(|L[i]|)=O(|V|)$
- Contare gli archi entranti in i:
	- Matrici: scandisco la colonna M[-, i] --> Costo: $\Theta(|V|)$
	- Liste: scandisco tutte le liste --> Costo: $\Theta(|V|+|E|)$
- Costruire $G^{-1}$ in cui tutti gli archi vengono invertiti
	- se $(i, j)\in E^{-1}$ se $(j, i)\in E$
	- $G^{-1}=(V, E^{-1})$
- Costruire il grafo dei cammini di lunghezza due in G chiamato $G^2$
	- $(i, j)\in E^2$ se $\exists  j$ tale che (i, j), (j, k) $\in$ E
	- Costo: $O(|V|^3)$       (forse si può fare in $\Theta(|V|^2)$)

$G^*$ grafo dei cammini di G fino a n-1 con n = |V|
$G^*=(V, E^*)$ 
Problema: Dato M calcolare $M^*$: 
- $M^*=Id + M+M^2+M^3+.....+M^{n-1}$

---
## Algoritmi sui grafi
- Grafi non pesati (G=(V, E)):
	- Visita BFS: Ampiezza
	- Visita DFS: 
		- Visite in profondità
		- Topological Sort DAG (aciclico)
		- Componenti fortemente connesse
- Grafi pesati (G=(V, E, W)):
	- Minimum Spanning Tree
		- Kruskal
		- Prim
	- Cammini minimi
		- SSSP Dijkstra
		- APSP Floyd Warshall

---
### BFS (Breadth First Search)
Partendo dal nodo s esploro tutti i nodi raggiungibili da s e trova i cammini minimi tra il nodo sorgente e tutti gli altri da lui raggiungibili.
Strutture dati per BFS:
- Vettore di |V| per marcare i nodi color
	- Bianchi (non segnato)
	- Grigi (segnato ma non analizzato)
	- Neri (già analizzato)
- Vettore di |V| per le distanze $\delta$
- Vettore di |V| dei predecessori $\Pi$ 
- Vettore di nodi che funge da coda
La coda viene riempita in ordine di distanza crescente dei nodi collegati a quello sorgente durante la visita.
La distanza è $+\infty$ se non c'è un cammino tra i due nodi, oppure k se k è la lunghezza più corta da u a v.
Al termine di BFS vorremmo che $\delta[u]$ = distanza(minima)(s, u)
Proprietà della distanza:
- $\forall$ x, y dist(x, y)=0 se x=y
- $\forall$ x, y dist(x, y) >= 0
- $\forall$ x, y siat(x, y) = dist(y, x)  (non vale però nei grafici orientati)
- $\forall$ x, y, z dist(x, y)$\leq$ dist(x, z) + dist(z, y)

##### Funzionamento BFS:
Inizializzo le strutture dati:
- color:   tutti BIANCHI
- $\delta$:  tutti $+\infty$
- $\Pi$:   tutti NIL
- coda Q:   vuota

Parto:
- s diventa GRIGIO
- $d[s]$ diventa 0
- Inserisco s in Q (la coda)
	- Itero: prendo u in testa a Q, analizzo la sua adiacenza, lo tolgo dalla coda e lo coloro di nero.
	- Scandisco gli archi uscenti da u e se trovo v BIANCO coloro v GRIGIO, modifico $\delta[s]$, $\Pi[v]$ e inserisco v in Q.

##### Codice BFS:
```
BFS(G, s){
	for(each v "appartenente" V){
		color[v] <- BIANCO
		d[v] <- "infinito"
		Pi[v] <- NIL
	}
	Q = "vuoto"
	color[s] <- GRIGIO
	d[s] <- 0
	EnQueue(Q, s)
	while(Q != "vuoto"){
		u <- head(Q)
		for(each v "appartenente" Adj[u]){
			if(color[v] == BIANCO){
				color[v] <- GRIGIO
				d[v] <- d[u] +1
				Pi[v] <- u
				EnQueue(Q, v)
			}
		}
		DeQueue(Q)
		color[u] <- NERO
	}
}
```

Complessità:
- Con le matrici come Adj: $O(|V|)*\Theta(|V|)=O(|V|^2)$
- Con liste di adiacenza come Adj: $O(\sum|L[u]|)+\Theta(|V|)=O(|E|+|V|)$  ------> $\sum|L[u]| = |E|$

### Correttezza BFS
BFS(G, s) termina con $\forall v \in V$:
- $d[v]=\delta(s, v)$
- $\Pi[v]$ predecessore di v su un cammino di lunghezza minima da s a v
- $d[c]=\delta(s, v)$
BFS termina perché:
 - Inserisco in coda solo nodi che erano BIANCHI
 - prima di inserirli in coda li coloro di GRIGIO
 - mai più ritornano BIANCHI
###### Proposizione:
- Dato $G=(V, E)$ e $s\in V$ se $(u, v)\in E$ allora   -->   $\delta(s, v) \leq \delta(s, u) + 1$
- Componendo due cammini minimi potrei ottenerne uno che non è minimo
- Se ho un cammino minimo e ne considero una parte, quella parte è sempre un cammino minimo
###### Lemma:
Al termine di BFS(G, v) $\forall v \in V$     --->    $d[v]\geq \delta(s, v)$
- Dimostrazione:
	- Passo base: 
		- 0 nodi in coda prima di v --> v=s
		- $d[s]=0=\delta(s, s)$
	- Passo induttivo:
		- Ipotesi induttiva: $d[v]\geq \delta(s, v)$ se prima di v sono entrati in coda al più k-1 nodi
		- Tesi: $d[v] \geq \delta(s, v)$ Se prima di v sono entrati in coda al più k nodi
		- v è il k+1-esimo nodo che entra in coda. $v \in Adj[u]$ -- > u è in testa alla coda. Per ipotesi induttiva su u --> $d[v]=d[u]+1\geq \delta(s, u)+1 \geq \delta(s, v)$

###### Proposizione:
Se durante BFS(G, s) ho Q=[u1, u2, ...., uh]:
- u1, u2, ....., uh sono GRIGI
- se u != s T[u1], T[u2], ....., T[uh] != NIL
- $d[u1] \leq d[u2] \leq .... \leq d[uh] \leq d[uh]+1$

- ###### Dimostrazione:
	- Passo base:
		- 0 operazioni Q=$\varnothing$
		- 1 operazioni $Q=[s]$ s è GRIGIO
		- $d[s]=0$
	- Passo induttivo:
		- Ipotesi induttiva: valgono le proprietà se su Q sono state effettuate al più k operazioni
		- Tesi: valgono le proprietà se su Q sono state effettuate al più k+1 operazioni
		- k+1-esima operazione se è un inserimento valgono le seguenti proprietà:
			- $Q=[u1, u2, ...., uh, u(h+1)]$ con i nodi da u1 a uh GRIGI e con $\Pi$ != NIL per ipotesi induttiva e u(h+1) è GRIGIO con le seguenti verità:
				- $\Pi[u(h+1)]=u1$
				- $d[u(h+1)]=d[u]+1$
				- $d[u]\leq d[u1]+1\leq d[u(h+1)] \leq d[u] +1$
		- Se invece è una cancellazione dalla coda (DeQueue(Q)):
			- $Q[u1, u2, ..., uh]$
			- $Q[u2, ...., uh]$

##### Alberi di visita BFS:
- $Tbfs(G, s)=(Vt, Et)$
- $Vt=${$u | u \in V \wedge color[u] = NERO al termine di BFS(G, s)$}
- $Et=${$(\Pi[v], v) | v \in Vt \wedge v \neq s$}

### Alberi liberi:
Compromesso tra avere pochi archi per rimanere aciclico ma abbastanza per essere connesso
Un albero libero è un grafo non orientato, connesso, e aciclico
- Connesso: $\forall u, v \in V \exists$ un cammino da u a v
- Aciclico: non ci sono cicli
	- Ciclo: in G è un cammino che parte da u e torna in u (senza utilizzare 2 volte lo stesso arco)
	- Ciclo semplice: u1, u2, ...., ui ciclo tale che: $\forall i, j \in [1, n]$ se $i \neq j$ allora $ui \neq uj$ (sostanzialmente ogni nodo è legato solo ad altri due nodi)
###### Caratterizzazione:
Sia G=(V, E) non orientato, i seguenti punti sono equivalenti tra loro e potrebbero sostituire la definizione:
- G è un albero (G è connesso e aciclico)
- G è connesso e rimuovendo un arco qualsiasi G diventa sconnesso
- G è aciclico e aggiungendo un arco qualsiasi G diventa ciclico
- G è connesso e |E| = |V| -1
- G è aciclico u |E| = |B| -1
- $\forall u, v \in V    \exists!$ cammino semplice da u a v
Dimostrazioni dei punti sopra: dimostrare che il primo impone il secondo e così via fino al sesto .
che impone il primo.

###### Vari problemi e risoluzioni
- Dato G=(V, E) non orientato decidere se G è connesso:
	- Scelgo s $\in$ V
	- Eseguo BFS(G, s)
	- Controllo che siano tutti NERI
- Dato G=(V, E) non orientato decidere se G è aciclico:
	- Eseguo BFS(G, s) (con s $\in$ V) e se durante la visita trovo un arco {u, v} da GRIGIO a un nodo non BIANCO (GRIGIO o NERO) con v $\neq \Pi[u]$  allora c'è un ciclo (se v non è predecessore di u)
	- Se ci sono BIANCHI al termine faccio ripartire la visita BFS da un BIANCO
- Dato G=(V, E) orientato decidere se G è ciclico:
	- Con visita BFS no riesco a capire se c'è un ciclo oppure no
A causa di questo ultimo problema si necessita di un altro algoritmo per capire se G possiede dei cicli oppure no

---

### DFS (Depth First Search)
Se restano nodi BIANCHI la procedura riparte.
Idea: Parto da un nodo e seguo un cammino fino a che il cammino non mi permette di seguirlo, ovvero scava il più a fondo possibile lungo ciascun ramo prima di fare marcia indietro verso altri rami.
Strutture dati per DFS:
- color (vettore come in BFS)
- $\Pi$ (vettore come in BFS dei predecessori)
- Tempo di inizio e di fine vita di ogni nodo:
	- $i$ vettore di lunghezza |V|:    $i[v]$ tempo in cui v diventa GRIGIO 
	- $f$ vettore di lunghezza |V|:     $f[v]$ tempo in cui v diventa NERO

##### Codice DFS:
```
DFS(G){
	for(each v "appartiene a" V){
		color[v] <- BIANCO
		Pi[v] <- NIL
	}
	TIME <- 0
	for(each v "appartiene a" V){
		if(color[v] == BIANCO){
			TIME <- DFS_Visit(G, v, TIME)
		}
	}
}


DFS_Visit(G, v, TIME){
	TIME <- TIME+1
	color[v]<- GRIGIO
	i[v] <- TIME
	for(each u "appartiene a" Adj[v]){
		if(color[u] == BIANCO){
			Pi[u] <- v
			DFS_Visit(G, u, TIME)
		}
	}
	TIME <- TIME+1
	color[v] <- NERO
	f[v] <- TIME
	return TIME
}
```

##### Complessità DFS:
- Matrici di Adj:   $\Theta(|V|) + \Theta(|V|)*\Theta(|V|)=\Theta(|V|^2)$
- Liste di Adj:   $\Theta(|V|) + \sum\Theta(1+|Adj[v]|)=\Theta(|V| + |E|)$

###### Teorema delle parentesi:
Se u e v $\in$ V allora al termine di DFS(G) si verifica uno dei seguenti casi:
- $[i[u], f[u]] \cap [i[v], f[v]] = \varnothing$
- $[i[u], f[u]] \subseteq [i[v], f[v]]$
- $[i[v], f[v]] \subseteq [i[u], f[u]]$

#### Corollario:
v è un discendente di u in DFS(G).
$i[u] \leq i[v]$ e $f[v] \leq f[u]$

Come faccio durante la visita DFS(G) al tempo $i[u]$ a capire se un nodo v diventerà discendente di u?
- v deve essere BIANCO al tempo $i[u]$
- deve esserci un cammino da u a v TUTTO di nodi BIANCHI

#### Teorema del cammino bianco
v sarà discendente di u (con v $\neq$ u) in DFS(G) se e solo se al tempo $i[u]$ esiste un cammino di nodi bianchi da u a v (escluso u che sarà grigio).

##### Dimostrazione:
Dimostrazione per induzione sulla lunghezza del cammino nel tutti i nodi del cammino diventano discendenti di u.
v discendente di u in uno degli alberi della finestra di visita DFS(G)

##### Classificazione degli archi durante DFS:
- 1) Archi di visita -> (u, v) con u = $\Pi[v]$ 
- 2) Archi all'indietro (BACKEDGES): Nell'albero di visita vanno da un nodo u ad un nodo antenato di u.    (Da GRIGIO a GRIGIO)
- 3) Archi in avanti (FORWARD EDGES): vanno da un nodo u ad un suo discendente v (non figlio) nell'albero di visita.       (Da GRIGIO a NERO)
- 4) Archi di attraversamento (CROSS EDGES): vanno da un nodo u a un nodo v con nessuno dei due che è discendente dell'altro.      (Da GRIGIO A NERO)

###### Teorema: 
G è ciclico se e colo se durante DFS(G) trovo almeno un BACKEDGE. Non dipende dall'ordine usato durante la visita DFS: posso avere una quantità esponenziale di cicli. I BACKEDGES sono al più $|V|^2$
###### Dimostrazione:
- All'istante t diventa grigio il nodo u e tutti gli altri nodi del ciclo sono bianchi.
- All'istante t c'è un cammino di bianchi da u a v e per il Teorema del cammino bianco v sarà discendente di u in un albero di visita. 
- Quando arrivo a v, u è ancora GRIGIO
- Scandisco l'adiacenza di v: trovo (v, u) --> BACKEDGE
- Durante DFS(G) ho trovato un BACKEDGE (v, u) e per definizione di BACKEDGE v è discendente di u nell'albero di visita

---
### DAG (Directed Acyclic Graph)
In un grafo aciclico sono possibili gli archi FORWARD e CROSS  e tutto ciò che non crea un ciclo.
###### Proprietà dei DAG:
- c'è almeno un nodo senza archi uscenti (pozzo)
- c'è almeno un nodo senza archi entranti (sorgente)
- Numero di archi nel caso peggiore è la somma di Gauss, quantità quadratica
Serve una nozione di ordinamento per i nodi di un DAG
- ##### Topological Sort
Definizione: Dato un DAG, un topological Sort di G è un ordinamento dei nodi di G tale che se l'arco (u, v) $\in$ E allora u < v ( u viene prima in ordinamento di v).
ogni grafo ha almeno un ordinamento topologico, ma ci possono essere anche più possibilità.
###### Idea:
Il primo nodo che diventa NERO è un pozzo e quando una sorgente diventa NERA tutti i suoi discendenti sono già NERI e devono quindi venire dopo di lui nell'ordinamento topologico.
Quindi quando un nodo diventa NERO lo aggiungo all'inizio del topological sort che sto costruendo.
###### Codice:
Sfruttiamo DFS e semplicemente aggiungiamo l'azione di porre ogni nodo NERO all'inizio di L.
```
DFS_topolog(G){
	L <- vuoto
	for(...)
		DFS_Visit_top(G, u, L)
	}
}

DFS_visit_top(G, u, L){
	...
	for(...)
		if(...)
	...
	}
	...
	color[u] <- Nero
	Insert_in_testa(L, u)    ----> metto nella lista i nodi solo quando                                           diventano neri
```

#### Componente fortemente connessa (Strongly connected component SCC)
Dato G=(V, E) una componente fortemente connessa C di G  è un sottoinsieme di v di nodi mutuamente raggiungibili.
C $\subset$ V    $\forall u, v \in C$ u è raggiungibile da v e v è raggiungibile da u
$\forall C'$ tale che  C $\subset$ C' non è fatto da nodi mutuamente raggiungibili --> $\exists$ u, v $\in$ C' tale che u non è connesso a v

Dato G=(V, E)
C1,..., Cm   s.c.c di G:
- Ci $\neq \varnothing$ $\forall$i 
- se i $\neq$ j Ci $\cap$ Cj = $\varnothing$
- Ci $\cup$ C2 $\cup$ ....... $\cup$ Cm = V       -->   L'insieme delle s.c.c è una partizione di V

Dato Ci e Cj con i $\neq$ j:
- Sia $\exists$ Ci --> Cj ($\exists$ u $\in$ Ci $\exists$ v $\in$ Cj   (u, v) $\in$ E)  allora non c'è un cammino da Cj a Ci
- Gscc= (Vscc, Escc)
- Vscc = {C1, ...., Cm} tutte e sole le s.c.c. di G
- Escc = {(Ci, Cj) | $\exists$ u $\in$ Ci $\exists$ v $\in$ Cj (u, v) $\in$ E}
###### Gscc è un DAG
- Riesco a dare un ordinamento a livello di s.c.c.  Ovvero in un grafo con diverse componenti connesse riesco comunque a dare un ordinamento topologico tra le diverse s.c.c.

Ma dato u $\in$ V come calcolo la s.c.c. in cui si trova u? 
Prendo tutti e soli i nodi mutuamente raggiungibili con u   (u $\in$ Cu          $\forall$ v, w $\in$  Cu $\exists$ v --> w)
Cu = Forward(u) $\cup$ Back(u)
- Forward(u): Tutti i nodi raggiungibili da u  -->  BFS(G, s) saranno i nodi NERI al termine
- Back(u): Tutti i nodi che raggiungono u   --> BFS($G^{-1}$, s) saranno tutti i nodi NERI al termine
Trovato Cu poi continuo la ricerca su G'=(V \ Cu, E') togliendo una per una tutte le s.c.c.
Costo di questa soluzione: $O(|V|)*\Theta(|V| + |E|)$

Oppure applico DFS per distinguere i s.c.c. in base agli alberi di visita trovati.
Problema:
- A causa degli archi cross alcuni nodi possono avere il loro Forward() un po' in un s.c.c. e un po' in un altro.
Soluzione:
- Controllare il Back(v)(nodo v preso a caso): non è possibile che un nodo w appartenga a Back(v) e appartenga pure ad un altro s.c.c., perché deve appartenere allo stesso albero di visita di v.

Gli alberi di visita DFS sono chiusi per s.c.c. Se Tk è un albero di visita DFS allora Tk = C1k $\cup$ c2k $\cup$ ......$\cup$ Cnk      unione di s.c.c.

Lemma: Ogni s.c.c. fa parte dell'albero di visita in cui entra il primo nodo della s.c.c. scoperto durante la visita ( secondo il teorema dei cammini bianchi) 
Ovvero quando durante un DFS un nodo di una s.c.c. viene scoperto, anche tutto il resto della s.c.c. verrà scoperta ed apparterrà a quella visita DFS.

##### Trovare le s.c.c. in un grafo:
In G dovrei partire da una s.c.c. pozzo senza raggiungere altre s.c.c. (in $G^{-1}$ sarebbe una s.c.c. sorgente)
$G^{-1}$ ha la stessa s.c.c. di G.  ($G^{-1}$ è uguale a G ma con gli archi invertiti)
- Uso una prima DFS(G) per capire quali sono s.c.c sorgenti in G
- Uso una seconda DFS su $G^{-1}$ partendo dalle s.c.c. pozzo di $G^{-1}$
- Ogni albero della seconda visita è una s.c.c.
- Il nodo con tempo di fine visita più alto si trova sicuramente in una s.c.c. sorgente di G
- La seconda DFS fatta su $G^{-1}$ deve procedere in ordine di tempo di fine visita decrescente (tempi della prima DFS) (dal nodo sorgenti)
Algoritmo per calcolare Vscc con 2 DFS una su G e una su $G^{-1}$:
- Algoritmo di Kosareyu  (Complessità: $\Theta(|V| + |E|)$)
	- Prima DFS SU G e seconda DFS su $G^{-1}$ partendo dai tempi di fine visita maggiori della prima DFS. In questo modo si trovano tutte le s.c.c. essendo tutti i nodi al loro interno raggiungibili a vicenda
Algoritmo con un solo DFS su G:
- Algoritmo di Tarjan (Complessità: $\Theta(|V| + |E|)$)

---

### Grafi pesati
G = (V, E, W)       W: E --> $R^+$    (ogni arco ha un peso $\geq$ 0)

Task:
- Calcolo di alberi minimi di copertura (MST)    (grafi non orientati)
- Calcolo di cammini di peso minimo

#### Sotto-grafi e alberi di copertura
G' sottografo di G  --> G' = (V', E')     con V' $\subset$ V     E' $\subset$ E
G' sottografo di copertura se V' = V e G' è connesso
Numero minimo di archi da mettere in un sottografo di copertura? 
- |V| -1  (numero minimo che permette di raggiungere ogni nodo) (se ne ha di più si verranno a creare dei cicli)
Se il sottografo di copertura ha esattamente |V| -1 archi è un ALBERO di copertura, ovvero:
- è connesso (esiste un cammino tra ogni coppia di vertici)
- è aciclico
Un albero di copertura collega tutti i nodi del grafo con il minimo numero di archi possibile, evitando così cicli ma garantendo la connessione tra tutti i nodi.

Se in un albero di copertura T si elimina un arco tra u e v e se ne aggiunge uno da a a b (per mantenere |V| -1 archi):
- Se a $\in$ Cu(cammino da u) e b $\in$ Cv (cammino da v) o viceversa   --> allora T rimane un albero di copertura

#### Albero minimo di copertura (Minimum Spanning Tree) (MST)
Un albero minimo di copertura di G è un albero di copertura T di G tale che la somma dei pesi degli archi di T sia minima.
- $W(T')=\sum(W((u, v)))$  tale che $W(T')$ = minimo
###### Un sottografo di copertura di peso minimo è sempre un albero di copertura!
Gli MST possono non essere unici in un grafo.

Dato G = (V, E, W)
Dato A $\subset$ T con T MST   T = (V, E')
diciamo che (u, v) $\notin$ A è     SAFE     per A se A $\cup$ ((u, v)) $\subset$ T' con T' MST
ovvero che (u, v) è unibile ad A mantenendo lo stato di MST di T.

#### Codice di un generico MST:
Partendo da un insieme vuoto ricerco iterativamente ogni volta un arco SAFE per A e lo unisco, fino a quando A non avrà |V| -1 elementi (archi), avendo trovato così un MST:
```
Generic_MST(G=(V, E, W)){
	A = "vuoto"
	while(|A| < |v|-1){
		{u, v} <- Find_Safe(A)
		A <- A "Unito" {{u, v}}
	}
	return A
}
```


Come individuare un arco SAFE per un insieme A senza aver calcolato nessun MST?

##### Definizioni inerenti agli MST: 
- TAGLI DI UN GRAFO:
	- (S, V \ S) partizioni dei nodi fi G in 2 blocchi
- Un arco {u, v} ATTRAVERSA un taglio (S, V \ S) se  ($u \in S$ e $v \in V$ \ S) oppure (v $\in$ s e u $\in$ V \ S)
- A $\subset$ E RISPETTA un taglio (S, V \ S) se nessun arco di A attraversa il taglio
- Un arco {u, v} è leggero per un taglio (S, V \ S) se è di peso minimo tra tutti gli ordini che attraversano il taglio
##### Teorema:
Dato G=(V, E, W) non orientato, connesso, pesato
Dato A $\subset$ T con T MST
Dato (S, V \ S) taglio
Dato {u, v} $\in$ E {u, v} $\notin$ A
Se A rispetta (S, V \ S) e {u, v} è leggero per (S, V \ S) allora {u, v} è SAFE per A
###### Dimostrazione:
A $\subset$ T e T MST
Tesi:
- $\exists$ T' MST tale che A $\cup$ {{u, v}} $\subset$ T'
- se {u, v} $\in$ T --> A $\cup$ {{u, v}} $\subset$ T  con T MST
- se {u, v} $\notin$ T

T' è un albero (ha |v|-1 archi ed è connesso)
T' = T \ {{a, b}} $\cup$ {{u, v}}
W(T') = W(T) - W({a, b}) + W({u, v})        con {a, b} che attraversa il taglio e {u, v} leggero
W(T') $\leq$ W(T)  quindi  T' è un MST

###### Corollario sui Minimum Spanning Tree con componenti connesse:
Sia A $\subset$ T  con T MST con A composto dalle componenti connesse C1, C2,..., Ck
Se {u, v} è leggero tra tutti gli archi che connettono le componenti connesse distinte allora {u, v} è SAFE per A.

---
##### Algoritmi che implementano Minimum Spanning Tree:
- Kruskal (si basa sul precedente corollario)
- Prim (si basa sul precedente teorema)

#### Algoritmo di Kruskal
Idea:
- A = $\varnothing$  (ogni nodo sta in una componente connessa singoletto)
- Secondo il corollario tutti gli archi connettono componenti distinte quindi ne scegliamo uno di peso minimo e unisco le due componenti connesse in una nuova singola:   A <- A $\cup$ {a, d}        A={{a, d}}
- L'ideal dell'algoritmo è di iterare ciò che è definito dal corollario finché non arrivo ad un albero (che sarà un MST)
Strutture dati per implementare Kruskal:
- Ad ogni passo devo individuare un arco che:
	- pesa poco       <-- Ordine E in ordine crescente di peso
	- connette due componenti connesse
- Scandisco E in ordine crescente di pesi. Arrivati ad un arco {u, v}:
	- Se in quel momento {u, v} collega componenti connesse distinte di A allora lo aggiungo ad A
	- Altrimenti lo scarto
Devo capire come fare il test in modo efficiente:
Ho bisogno di memorizzare le componenti C1, C2,...., Ck individuate da A
- Dato {u, v} devo controllare se u e v stanno nella stessa Ci     ---> Find 
- Se u $\in$ Ci e v $\in$ Cj con i $\neq$ j devo sostituire Ci e Cj con Ci $\cup$ Cj   ---> Union

###### Codice Kruskal:
```
Kruskal(G = (V, E, W)){
	A <- "vuoto"
	Sort(E)
	for(each v "appartiene a" V){
		Make(v)
	}
	for(each {u, v} "appartiene a" E){
		if(Find(u) != Find(v)){
			A <- A U {{U, v}}
			Union(u, v)
		}
	}
	return A     --> alla fine A è un MST
}
```
Alla fine |A| = |V| - 1

Costo di m operazioni di cui n MAKE per Alberi con UnionbyRanks e Path Compression, in cui:
- n = |V|
- m = 2*|E| + (|V| - 1) + |V| = O(|E|)                   (|E| $\geq$ |V| - 1)       (|E| = $\Omega(|V|)$)
Costo totale è $O(m*\alpha(m, n))$ = $O(|E|*\alpha(|E|, |V|))$

---
#### Algoritmo di Prim
Idea: Ad ogni passo A è un albero su un sottoinsieme di nodi
Devo trovare un arco leggero che attraversa (S, V \ S). Per ogni nodo di V \ S memorizzo qual è l'arco di peso minimo che lo collega ad S. Ad ogni passo tra tutti i nodi di V \ S scelgo il nodo con chiave key minima  --> aggiungo ad A l'arco che collega {$\Pi[b]$, b}
Strutture:
- Vettore key con le chiavi dei nodi 
- $\Pi$ dei predecessori

Codice Prim:
```
Prim(G, s){
	for (each v in V){
		key[v] <- +inf
		Pi[v] <- NIL
	}
	key[s] <- 0
	Q <- V
	BuildMinHeap(Q)       ---> Theta(|V|)
	while(Q != vuoto){
		u <- ExtractMin(Q)
		for(each v in Adj[u]){
			if(v in Q && key[v] > W({u, v})){
				key[v] <- w({u, v})
				Pi[v] <- u
				DecreaseKey(Q, v)       ---> O(log|V|)   (si chiama decrease                                                            ma in realtà è remove)
			}
		}
	}
}
```
Complessità totale: 
- Con Min-heap:
	- ciclo for: $\Theta(|V|)$
	- ExtractMin: $O(|V|*log|V|)$
	- DecresaseKey(Q, v): O(log|V|)         Caso peggiore: O(|E|*log|V|)
	- Costo totale: $O(|E|*log|V|)$
- Senza Min-heap:
	- ExtractMin: $\Theta(|V|^2)$
	- ciclo for nel while: $\Theta(|E|)$
	- Costo totale: $\Theta(|V|^2)$

MST memorizzato nel $\Pi$ con i predecessori
A = A $\cup$ {{$\Pi[u]$, u}}

###### Perché esistano due MST distinti serve che ci sia un ciclo in cui ci sono almeno due archi con lo stesso peso

---
### Cammini di peso minimo 
Dato G = (V, E, W) con pesi positivi, dato s $\in$ V calcolare $\forall v \in V$  un cammino di peso minimo da s a v.

#### Algoritmo di Dijkstra (Single Source Shortest Paths) (SSSP)

Codice Dijkstra:
Praticamente è una variante di BFS in cui uso una cosa con priorità al posto di una coda
```
Dijkstra(G, s){
	for(each v in V){
		d[v] <- +inf
		Pi[v] <- NIL
	}
	d[s] <- 0
	Q <- V
	BuildMinHeap(Q)
	while(Q != vuoto){
		u <- ExtractMin(Q)
		for(each v in Adj[u]){
			if(v in Q && d[v] > d[u] + W({u, v})){
				d[v] <- d[u] + W({u, v})
				Pi[v] <- u
				DecreaseKey(Q, v)
			}
		}
	}
}			
```
Complessità:
- Con Min-heap: O(|E|*log|V|)
- Senza Min-heap: $\Theta(|V|^2)$

####  Algoritmo Floyd Warshall  (All Pairs Shortest Paths) (APSP)
Dato G = (V, E, W) per ogni coppia di nodi u, v  calcolare un cammino di peso minimo da u a v.
Per ogni u $\in$ V richiamo Dijkstra(G, u) $\Pi$u, du
$\Pi$ = matrice,   D = matrice
- Senza Min-Heap: $\Theta(|V|^3)$

Dijkstra è un algoritmo "Greedy" (goloso) ottimo che non sbaglia mai, ovvero fa scelte che sembrano ottime al momento della scelta stessa.
###### Algoritmo di Programmazione Dinamica
Per APSP Floyd Warshall $\Theta(|V|^3)$
Idea:
- Unendo due cammini minimi potrei ottenerne uno non minimo
- Quindi per unire due nodi a e c passando per b guardo tutti i punti che stanno in mezzo, trovo b, tutti i sotto cammini di un cammino minimo sono cammini minimi.
Base:
- Cammini minimi da a a b che non contengono nodi interni (Archi del grafo)
- Se ho calcolato i cammini minimi da a a b che usano come nodi interni i nodi 1, 2, ...., j
- Voglio calcolare tutti i cammini minimi solo nodi interni 1, 2,....., j, j+1

##### Peso di un cammino
Somma dei pesi degli archi che compongono il cammino.
p = $\Pi0, \Pi1, ...., \Pi n$
W(p) = $\sum W((ui, vi+1))$

Idea della programmazione dinamica di Floyd Warshall detta meglio:
k = 0, ....., |V|
Alla k-esima iterazione:
- $\forall i, j \in V$  calcolo il cammino di peso minimo da i a j contente solo nodi interni compresi tra 1 e k.
Alla k-1-esima iterazione ho calcolato:
- $\forall i, j \in V$  $Dk-1[i, j]$ peso minimo tra i pesi di tutti i cammini che collegano i a j usando come nodi interni solo quelli compresi tra 1 e k-1.

Come calcolo $Dk[i, j]$
- Se non uso k ---> $Dk[i, j]$ = $Dk-1[i, j]$
- Se uso k lo uso una volta sennò viene un loop ---> $Dk[i, j]$ = $Dk-1[i, k]$ + $Dk-1[k, j]$      (somma dei due cammini) 
$Dk[i, j]$ = min ($Dk-1[i, j]$, $Dk-1[i, k]$ + $Dk-1[k, j]$)

###### Codice Floyd-Warshall
```
Floyd-Warshall (G=(V, E, W)){
	for(i <- 1 to |V|){
		for(j <- 1 to |V|){
			D0[i, j] = W[i, j]
		}
	}
	for(k <- 1 to |V|){
		for(i <- 1 to |V|){
			Dk[i, j] = min(Dk-1[i, j], Dk-1[i, k] + Dk-1[k, j])
		}
	}
}
```
Complessità algoritmo: $O(|V|^2)$

Praticamente per avere i cammini di peso minimo nella matrice P devo fare un prodotto vettoriale con somma al posto della moltiplicazione:
$P[i, j] =$ min($W[i, k]$ + $W[k, j]$)         k $\subset [u, w]$
$P'[i, j]$ = min($P[i, j]$, $W[i, j]$)    pesi minimi di lunghezza $\leq$ 2
V2 riapplicato --> log(|V|) visite
