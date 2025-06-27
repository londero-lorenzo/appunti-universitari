---
title: Config
aliases:
  - Config
tags:
  - php
  - esercizi
  - gallery-project-local
  - config
created: 2025-06-21
---
# File di configurazione: `config.php`

---

## Contenuto del file

```php
<?php
// dati di configurazione
define("DIR_IMMAGINI", "./images");

$immagini_per_riga = 5;

$formati_immagine = array(".jpg", ".gif", ".png");

$tipi_immagine = array("image/jpeg", "image/gif", "image/png");
?>
```


## Spiegazione

- **`define("DIR_IMMAGINI", "./images");`**  
    Definisce una costante chiamata `DIR_IMMAGINI` che indica la cartella relativa dove si trovano le immagini da visualizzare nella galleria.  
    Le costanti sono valori fissi e si usano senza il simbolo `$`.
    
- **`$immagini_per_riga = 5;`**  
    Variabile che indica quante immagini devono essere visualizzate per riga nella tabella della pagina indice.
    
- **`$formati_immagine`**  
    Array che contiene le estensioni dei file immagine accettati, usato per filtrare i file nella cartella immagini.
    
- **`$tipi_immagine`**  
    Array contenente i MIME type corrispondenti ai formati immagine accettati. Può essere usato per controllare il tipo di file durante l’upload o la visualizzazione.
    

---

## Note su `define()` e costanti in PHP

- La funzione `define(nome_costante, valore)` serve a creare costanti che non cambiano durante l'esecuzione dello script.
    
- Le costanti sono sempre scritte senza il simbolo `$` davanti.
    
- In PHP le variabili sono molto flessibili, quindi spesso si preferiscono variabili semplici invece di costanti, ma in questo caso si usa `define` per chiarezza e per evitare modifiche accidentali.
    

---

## Come usare il file di configurazione

Il file `config.php` viene incluso con `require_once()` all'inizio degli script PHP per centralizzare i parametri principali, rendendo facile modificare configurazioni senza toccare il codice delle funzionalità.