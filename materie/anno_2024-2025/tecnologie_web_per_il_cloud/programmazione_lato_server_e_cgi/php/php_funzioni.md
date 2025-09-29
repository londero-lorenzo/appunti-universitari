---
title: PHP Funzioni
aliases:
  - PHP Funzioni
tags:
  - php
  - php-funzioni
created: 2025-06-27
---
# 🔧 Funzioni in PHP

## Dichiarazione

```php
function nomeFunzione($arg1, $arg2) {
    // corpo funzione
    return $valore;
}
```


- Le variabili dichiarate all'interno sono **locali**.
    
- Le **variabili globali** definite fuori dalla funzione devono essere importate con `global`.

### Esempio

```php
$cambio = 1.106;

// Non funziona (scope locale)
function eurodollaro($val) {
    return $val * $cambio;
}

// Funziona (uso di global)
function eurodollaro($val) {
    global $cambio;
    return $val * $cambio;
}

echo eurodollaro(1200);
```

---

## Funzioni predefinite in PHP

PHP offre **centinaia di funzioni predefinite** pronte all’uso, che coprono tantissimi ambiti:

- Funzioni native del linguaggio per gestione stringhe, array, file, ecc.
    
- Funzioni specifiche per interfacce con database, elaborazione immagini, gestione sessioni, ecc.
    

Queste funzioni spesso **restituiscono un valore** che può essere salvato in una variabile o ignorato se non serve.

### Utilizzo base

```php
$variabile = funzione($parametro1, $parametro2, …);
```

---

### Alcune funzioni utili e importanti

- **`echo`**
    
    - Non è una vera funzione ma un costrutto del linguaggio,
        
    - Non richiede parentesi tonde,
        
    - Serve a stampare output direttamente nella pagina.
    
```php
echo "Ciao mondo!";
```
- **`print()`**
    
    - Funzione simile a `echo`, ma è un vero e proprio funzione,
        
    - Può essere usata con parentesi,
        
    - Ritorna sempre 1, quindi può essere usata in espressioni.
        
- **`phpinfo()`**
    
    - Stampa una pagina HTML completa con informazioni dettagliate sulla configurazione di PHP,
        
    - Utile per debugging e controllo ambiente di esecuzione.
    
```php
phpinfo();
```
- **`isset($var)`**
	- Ritorna `TRUE` se la variabile esiste e non è `NULL`,
	    
	- Utile per controllare la presenza di variabili o parametri.
	
```php
if (isset($_POST['username'])) {
    // esegui qualcosa
}
```
- **`die($messaggio)` / `exit($messaggio)`**
	- Termina immediatamente l’esecuzione dello script,
	    
	- Può stampare un messaggio di errore prima di fermare tutto.
	
```php
if (!$connessione) {
    die("Errore di connessione al database");
}

```


----

## 📚 Fonti e riferimenti  
Slide: `07-PHP1.pdf`  
Titoli: `Dichiarare funzioni`, `Funzioni predefinite`, `Alcune funzioni utili`
