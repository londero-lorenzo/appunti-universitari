---
title: PHP Cookie
aliases:
  - PHP Cookie
tags:
  - php
  - php-cookie
created: 2025-06-27
---
# 🍪 Cookie in PHP

## Creazione

```php
setcookie("nome", "valore", time() + 3600);  // valido per 1 ora
```


- Va chiamata **prima di ogni output**.
    
- Per cancellare un cookie:


```php
setcookie("nome", "", time() - 3600);
```

---
## Lettura

I cookie sono disponibili in `$_COOKIE`:

```php
if (isset($_COOKIE["utente"])) {     echo "Bentornato, " . $_COOKIE["utente"]; }
```

---

## Esempio completo

```php
<?php
$saluto = "Benvenuto!";
if (isset($_COOKIE["precedente"])) {
    $saluto = "Bentornato!";
}

setcookie("precedente", time(), time() + 120);
?>

<h1><?php echo $saluto ?></h1>
<p>Data attuale: <?php echo date("d/m/Y H:i:s", time()); ?></p>

<?php
if ($saluto == "Bentornato!") {
    echo "Visita precedente: " . date("d/m/Y H:i:s", $_COOKIE["precedente"]);
}
?>
```

## Funzioni correlate

- `time()` → timestamp attuale (secondi dal 1/1/1970).
    
- `date(format, timestamp)` → formatta la data.

---

## 📚 Approfondimenti consigliati

- [Funzioni e variabili globali](./php_funzioni.md)
- [Inclusione file e header HTTP](./php_include.md)
- [Che cosa sono i Cookie?](../cookie.md)


---

## 📚 Fonti e riferimenti  
Slide: `07-PHP1.pdf`  
Titoli: `I cookie`, `Esercizio 8`, `Esercizio 8: note su data e ora`  
