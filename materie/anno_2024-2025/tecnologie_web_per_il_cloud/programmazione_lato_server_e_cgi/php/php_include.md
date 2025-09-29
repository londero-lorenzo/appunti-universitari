---
title: PHP Include
aliases:
  - PHP Include
tags:
  - php
  - php-include
created: 2025-06-27
---
# 📂 Inclusione di file e intestazioni HTTP

## Inclusione di file

Permette di modularizzare il codice (es. header, menu, footer):

```php
include("file.php");        // include semplice
include_once("file.php");   // include solo se non già incluso
require("file.php");        // come include ma fatale in caso di errore
```

> NB: I file inclusi devono avere codice PHP valido.

### Esempio

```php
<?php include("menu.php"); ?> <div>Contenuto pagina</div>
```

---

## Differenze tra `include`, `include_once` e `require`

| Funzione         | Descrizione                                                                          | Cosa succede se il file non viene trovato                                                                  |
| ---------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **include**      | Inserisce e interpreta il file specificato ogni volta che viene chiamato.            | Genera un **warning**, ma lo script continua.                                                              |
| **include_once** | Come `include`, ma include il file **una sola volta** anche se richiamato più volte. | Stessa gestione errori di `include` (warning).                                                             |
| **require**      | Inserisce e interpreta il file specificato ogni volta che viene chiamato.            | Genera un **errore fatale (fatal error)** e blocca l’esecuzione dello script se il file non viene trovato. |
| **require_once** | Come `require`, ma include il file **una sola volta** anche se richiamato più volte. | Stessa gestione errori di `require` (fatal error).                                                         |

---

### Quando usare cosa

- Usa **`require`** se il file è **essenziale** per il funzionamento dello script: senza quel file lo script non deve continuare.
    
- Usa **`include`** se il file è **opzionale** o il mancato caricamento non deve fermare tutto.
    
- Usa le versioni **_once** per evitare inclusioni multiple accidentali di uno stesso file, ad esempio con librerie o definizioni di funzioni/classi.


---

### Esempi rapidi

```php
include("config.php");       // se manca, script continua ma avvisa
require("funzioni.php");     // se manca, script si ferma subito

include_once("libreria.php"); // include solo una volta
require_once("database.php"); // include solo una volta ed è essenziale
```

---

## Esempio pratico di inclusione di file in PHP

L’uso di `include` e `require` è fondamentale per organizzare meglio il codice PHP, specialmente in applicazioni complesse. Permette di **modularizzare** il sito o l’applicazione, evitando duplicazioni e facilitando la manutenzione.

### Contesto dell’esempio

In un sito web tipico, alcune parti sono ripetute su molte pagine, come:

- L’**header** o banner (logo, intestazione)
    
- Il **menu di navigazione**
    
- Il footer (non mostrato nell’esempio)


Invece di riscrivere lo stesso codice HTML e PHP in ogni pagina, si crea un file separato per ogni sezione:

- `funzioni.php`: contiene funzioni PHP riutilizzabili (ad esempio per connettersi al database, funzioni di utilità, ecc.)
    
- `banner.php`: codice HTML e PHP per la testata (header) del sito
    
- `menu.php`: codice per il menu di navigazione


### Come funziona l’inclusione

Nel file principale della pagina:
```php
<?php include("funzioni.php") ?>
<html>
<head>…</head>
<body>
  <div id="banner">
    <?php include("banner.php") ?>
  </div>
  <div id="menu">
    <?php include("menu.php") ?>
  </div>
  <div id="body">
    … contenuto specifico della pagina …
  </div>
</body>
</html>
```

- All’inizio viene incluso `funzioni.php`, così tutte le funzioni definite sono disponibili durante l’esecuzione della pagina.
    
- Nei punti in cui si vuole inserire un elemento ripetuto, come il banner o il menu, si richiama `include` con il file corrispondente.
    
- Il server carica e interpreta il contenuto di quei file, **inserendolo** nel punto esatto in cui è stata fatta la chiamata `include`.
    
- Questo rende il codice più modulare, riutilizzabile e più facile da aggiornare: cambiando una sola volta `menu.php`, si aggiorna il menu su tutte le pagine.

---

### Vantaggi

- Riduci la duplicazione di codice
    
- Faciliti la manutenzione
    
- Migliori la leggibilità del codice
    
- Permetti a più sviluppatori di lavorare su parti separate senza conflitti


---

## 📚 Fonti e riferimenti  
Slide: `07-PHP1.pdf`  
Titoli: `Inclusione di file`