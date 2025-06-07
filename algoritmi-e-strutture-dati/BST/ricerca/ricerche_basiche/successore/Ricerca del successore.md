```
BSTSucc(x){
	if(x.right != NIL){
		return BSTSearchMin(x.right)
	}else{
		y <- x.parent
		while(y != NIL && x = y.right){
			x <- y
			y <- x.parent
		}
		return y
	}
}
```

### Vedi anche:
- [[BST/ricerca/ricerche_basiche/Costo|Costo ricerche basiche]]