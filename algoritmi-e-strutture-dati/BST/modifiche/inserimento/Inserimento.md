Modifica la struttura di un [[albero_binario_di_ricerca|Albero binario di ricerca]], T, inserendo un nodo 'z' in modo che rispetti la [[albero_binario_di_ricerca#Definizione|proprietà BFS]]


## Pseudo codice

```
InsertBST(T, z){
	y <- NIL
	x <- T.root
	while (x != NIL){
		if (x.key > z.key){
			y <- x
			x <- x.left
		}else{
			x <- x.right
		}
	}
	z.parent <- y
	if (y = NIL){
		T.root <- z
	}else if (y.key > z.key){
		y.left <- z
	}else{
		y.right <- z
	}
}
```

Questa procedura riceve un nodo `z` per il quale `z.key=v, z.left=NIL e z.right=NIL`; essa modifica T e qualche attributo di `z` in modo che `z` sia inserito in una posizione appropriata nell’albero.
`InsertBST` inizia dalla radice dell’albero e il puntatore `x` traccia un cammino semplice in discesa
cercando un NIL da sostituire con l’elemento di input. La procedura mantiene anche un puntatore inseguitore `y` che punta al padre di `x`. Dopo l’inizializzazione, le righe 4-11 del ciclo while spostano questi due puntatori verso il basso, andando a sinistra o a destra a seconda dell’esito del confronto fra `z.key` e `x.key`, finché a`x`non viene assegnato il valore NIL. Ci serve un puntatore inseguitore `y` perché, quando arriviamo a trovare il NIL dove mettere `z`, la ricerca e andata un passo oltre il nodo che deve essere modificato. Le righe 12-19 impostano i puntatori che
servono a inserire `z`.
