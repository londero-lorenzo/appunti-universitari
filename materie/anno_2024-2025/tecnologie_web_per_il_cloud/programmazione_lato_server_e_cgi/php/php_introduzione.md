---
title: PHP Introduzione
aliases:
  - PHP Introduzione
tags:
  - php
  - php-introduzione
created: 2025-06-21
---
# 🐘 Introduzione a PHP

PHP è un linguaggio interpretato, progettato per il web, open source, multipiattaforma e molto usato per creare pagine dinamiche.

---

## 📜 Cenni storici

- Nato come *Personal Home Page Tools* (PHP Tools), oggi è acronimo di **PHP: Hypertext Preprocessor**
- Attualmente alla **versione 8.x**
- Ampia collezione di librerie per:
  - gestione stringhe,
  - accesso a database (MySQL, PostgreSQL, ecc.),
  - gestione XML, cookie, immagini dinamiche e molto altro.

---

## 📚 Documentazione e supporto

- Sito ufficiale: [https://www.php.net](https://www.php.net)
- Documentazione anche in italiano
- Community:
  - [Stack Overflow – tag PHP](https://stackoverflow.com/questions/tagged/php)

---

## ⚙️ Caratteristiche principali

- Linguaggio interpretato
- Sintassi derivata dal C
- Utilizzabile sia in modo **procedurale** che **object-oriented**
- Il separatore tra istruzioni è il `;` (punto e virgola)
- Utilizzabile **embedded in HTML**:

```php
<?php
   echo "Ciao mondo!";
?>
```

---

## 🧪 Sintassi base

### ✅ Commenti


```php
// commento su una riga

/* commento su    più righe */
```
### 📦 Tipi di dati

- **Scalari**:
    - `bool`, `int`, `float`, `string`
        
- **Compositi**:
    - `array` (indicizzati e associativi)
        
    - `object`
    
- Conversione automatica tra tipi, se sensata


### 💲 Variabili

- Prefisso `$`
    
- Non è necessaria la dichiarazione preventiva
    
- Esempi:

```php
$a = "prova";
$b = 18; $c = $b + 77;
```


### 🔒 Costanti

```php
define("NOME", valore);
```

---

## 🛠️ Strutture di controllo

### Condizionali

```php
if ($x > 10) {
  echo "maggiore di 10";
} else {
  echo "non maggiore";
}

```

### Selezione multipla

```php
switch($var) {
  case 1: echo "uno"; break;
  case 2: echo "due"; break;
  default: echo "altro";
}
```

### Cicli

```php
for ($i = 0; $i < 10; $i++) { echo $i; }
while ($x > 0) { $x--; }
```

---

## 🛎️ Funzioni utili

| Funzione    | Descrizione                            |
| ----------- | -------------------------------------- |
| `echo`      | Stampa a video (senza parentesi)       |
| `phpinfo()` | Mostra info complete su PHP e ambiente |
| `isset($x)` | Verifica se una variabile è definita   |
| `die()`     | Termina esecuzione, stampa messaggio   |

---

## 🧾 Interazione con l’utente: variabili predefinite

PHP fornisce un insieme di **variabili predefinite** che permettono di:

- leggere i **parametri passati tramite URL o form** (`$_GET`, `$_POST`)
- accedere a **dati del server e del client** (`$_SERVER`)
- gestire **cookie, sessioni e file upload**

Queste variabili sono disponibili **ovunque nello script**, senza bisogno di dichiarazione, e costituiscono la base per qualunque forma di interazione dinamica.

📄 Per un approfondimento dettagliato sulle variabili predefinite, consulta il file:

👉 [`php_variabili_predefinite.md`](./php_variabili_predefinite.md)


---

## 🧪 Primo test

1. Posizionati nella document root (es. `/var/www/html`)
    
2. Crea un file con `nano es1.php`:
    
```php
<?php echo "Ciao dal server!"; ?>
```
    
3. Salva (`Ctrl+X`, `Y`, `Invio`)
    
4. Accedi da browser: `http://<ip-istanza>/es1.php`
    

> Se hai creato il file nella tua home, spostalo con:  
> `mv es1.php /var/www/html/`


---

## 🔁 Ciclo di vita degli script PHP

- Ogni richiesta HTTP genera **una nuova esecuzione** dello script
    
- Non esiste persistenza automatica tra richieste (senza sessioni o DB)
    
- Lo script viene eseguito **completamente server-side**
    
- L’output risultante è sempre HTML (o altro contenuto web)

---
## 📚 Fonti e riferimenti

- Slide: `03-php-intro.pdf`
    
- Titolo: `Introduzione a PHP`

