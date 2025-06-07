```
BSTPred(x){
	if(x.left != NIL){
		return BSTSearchMax(x.left)
	}else{
		y <- x.parent
		while(y != NIL && x = y.left){
			x <- y
			y <- x.parent
		}
		return y
	}
}
```

### Vedi anche:
- [[BST/ricerca/ricerche_basiche/Costo|Costo ricerche basiche]]