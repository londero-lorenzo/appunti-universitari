---
title: "Php Classi Oggetti e Namespaces Composer"
aliases: ["Php Classi Oggetti e Namespaces Composer"]
tags: [università, "tecnologie-web-per-il-cloud", "programmazione-lato-server-e-cgi", "php", "php-classi-oggetti-e-namespaces-composer"]
created: 2025-06-28
---
# Classi

**Object Oriented** è preferibile per progetti di medie/grandi dimensioni:
+ maggiore chiarezza e correttezza del codice;
+ manutenzione agevole;
+ possibilità di applicare pattern di programmazione avanzati

## Sintassi

```php
class <nome_classe> [extends <classe_madre>] {
	// proprietà
	// metodi
}
```
Le proprietà possono essere:
+ public (default)
+ protected
+ private

### Esempio di costruttore

```php
<?php
class libro {
	public $isbn, $titolo, $autore, $editore, $pagine;
	function __construct($i, $t, $a, $e, $p) {
		$this->isbn=$i;
		$this->titolo=$t;
		$this->autore=$a;
		$this->editore=$e;
		$this->pagine=$p;
	}
}
$l=new libro('8845290050','Il Signore degli anelli','John R.
R. Tolkien','Bompiani',1359);
echo $l->titolo;
echo '<pre>',var_dump($l),'</pre>';
?>
```

### Esempio di metodo


```php
class libro {
...
	function visualizza() {
		return $this->autore.". <em>".$this->titolo."</em>. 
		".$this->editore.", pp. ".$this->pagine;
	}
	function __destruct() {
		echo '<p>sto distruggendo il libro con ISBN '.$this->isbn.'</p>';
	}
}
$l=new libro('8845290050','Il Signore degli anelli','John R. R.
Tolkien','Bompiani',1359);
// invocazione del metodo:
echo $l->visualizza();

```

---
# Namespaces, Composer

## Namespaces

+ Meccanismo simile ai namespaces di XML
+ Risolve il problema della collisione fra i nomi di funzioni/classi/costanti:
	+ Si presenta soprattutto quando adottiamo librerie esterne
	+ **Esempio**: due librerie che definiscono una funzione o metodo con lo stesso nome

È possibile quindi definire uno spazio dei nomi proprio, in ogni file che appartiene ad un progetto che vogliamo rendere pubblico:
+ per codice privato non ce n'è bisogno;

### Definizione (inizio di ogni file)

```php
<?php
namespace TWC
```

**Anche sottospazi**

```php
<?php
namespace TWC\esempi\blog;
```

### Utilizzo:

+ Le funzioni/classi definite nel file con *namespaceTWC* saranno accessibili altrove con:
	+ `TWC\funzione(...);`
+ `\funzione()` si riferisce invece ad una funzione con stesso nome ma definita localmente
	+ `\TWC\funzione()` è `TWC\funzione(...);`

```php

use TWC\Esempi\Blog\MiaClasse;

$obj = new MiaClasse();

```
Oppure:
```php

$obj = new \TWC\Esempi\Blog\MiaClasse();

```
### Librerie esterne

+ PEAR
+ Composer
+ (PECL)

#### PEAR (**P**HP **E**xtension and **A**pplication **R**epository)

Mantiene un repository **globale** di librerie/applicazioni PHP sfruttabili da tutti gli utenti del sistema:
+ I pacchetti sono "validati" dai gestori (umani) di PEAR
	+ c'è un controllo di qualità, ma anche un limite ai pacchetti distribuiti

Gestisce eventuali dipendenze, ma è in via di abbandono a favore di Composer.

#### Composer

**Composer** è il gestore di dipendenze standard per PHP. Il suo compito è:
- Installare librerie e tool PHP in modo automatico e modulare

- Risolvere le dipendenze tra i vari pacchetti

- Automatizzare l'autoload delle classi definite nei package tramite PSR-4

- Garantire che lo stesso progetto sia replicabile ovunque con la stessa struttura di dipendenze

#### Principi

+ Nato per favorire lo sviluppo di un ecosistema di librerie facilmente installabili:
	+ di cui lo sviluppatore non dovrebbe vedere troppi dettagli
+ In generale le librerie:
	+ non creano file se non richiesti;
	+ hanno al massimo stato locale;
	+ non emettono output, header, ecc;
	+ non dipendono da risorse specifiche di un sistema operativo.
+ Lo sviluppatore:
	+ Stabilisce le dipendenze;
	+ Installa tutto con un comando;
	+ Include tutto con un comando;

#### Composer packages
È definito da un **vendor**, un **progetto**, una **versione**

##### Come si usa?
+ Creo la directory del mio progetto:
	+ Es. *prova*
+ Creo un file JSON in cui si dichiarano le librerie da cui dipende il mio progetto
	+ **composer.json** 
```
{
	"require":{
		"vendor/package":"versioni"
	}
}
```

**Versioni:**
+ Exact: 1.0.3
+ Range: >=2.0                         >=2.0<4.0            >=2.0  <4.0||6.0 1.0-2.0
+ Wildcard:2.0.*
+ Next significant version:
	+ ~1.3 (uguale a >=1.3<2.0.0)
	+ ~1.3.1 (uguale a >=1.3.1<1.4.0)
	+ ^1.3.1 (uguale a >=1.3.1<2.0.0)
+  Accedo poi alle classi definite nelle librerie tramite spazio dei nomi (vendor\package\...)
```
<?php
require('vendor/autoload');
$obj = new vendor\package('parametri');
$obj2= new vendor2\package3();

```
+ Se voglio distribuire il mio progetto, allora aggiungo altre informazioni al composer.json, e il mio progetto diventa a sua volta un package
```
composer.json
{
	"name" : "TecWebCloud/Esempio",
	"version" : "1.0.2"
	"require": {
		"vendor/package": "versioni"
	}
}
```

---
## 📚 Fonti e riferimenti  
Slide: `10-PHP-OO-Composer.pdf`




