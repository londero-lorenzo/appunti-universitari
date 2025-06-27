---
title: View
aliases:
  - View
tags:
  - php
  - esercizi
  - gallery-project-local
  - view
created: 2025-06-27
---
# 📸 `visualizza.php` — Visualizzazione dell'immagine selezionata

Questo script gestisce la **visualizzazione di una singola immagine** all'interno della galleria, partendo dall'indice fornito via `GET`. Mostra anche i **link per navigare** all'immagine precedente e successiva.

---

## 📥 Inclusione di file esterni


```php
include_once("config.php");
include_once("funzioni.php");
```

> ✅ Includiamo i file che contengono la **configurazione globale** e le **funzioni di supporto**.  
> Il suffisso `_once` garantisce che ogni file venga caricato **una sola volta**, evitando duplicazioni indesiderate.

---

## ❗ Controllo parametro `immagine`

```php
if (!isset($_GET["immagine"])) {
    die("Errore: stai cercando di accedere alla pagina in modo scorretto\n");
}
```

> 💡 Lo script **termina immediatamente** se non è presente il parametro `immagine` nella query string (es. `?immagine=2`).  
> Questo impedisce accessi non previsti o errori.

---

## 📦 Caricamento immagini

```php
$immagine = $_GET["immagine"];
$lista_file = caricaDirectory(DIR_IMMAGINI);
```

> 🔄 Carichiamo la lista dei file validi nella cartella `DIR_IMMAGINI` (es. `./immagini`), filtrandoli con le estensioni ammesse.  
> La funzione `caricaDirectory()` è definita in `funzioni.php`.

---

## 🛡️ Verifica della validità dell’indice

```php
if (!isset($lista_file[$immagine])) {
    die("Errore: immagine non valida o inesistente.");
}
```

> 🧱 Serve a garantire che **l’indice fornito corrisponda effettivamente a un’immagine** nella lista.  
> Protegge contro accessi a indici fuori range o manomissioni.

---

## 🖼️ Visualizzazione immagine

```php
echo "<img src=\"" . DIR_IMMAGINI . "/" . htmlspecialchars($lista_file[$immagine]) . "\"/>";
```

> L'immagine viene mostrata nel corpo della pagina.  
> 🔐 Usiamo `htmlspecialchars()` per evitare problemi di **XSS** (cross-site scripting).
> 	Quando si costruisce un sito dinamico, è fondamentale **proteggere l'applicazione da attacchi XSS (Cross-Site Scripting)**.  Nel nostro caso, stiamo generando l’HTML per mostrare un'immagine, includendo nel codice HTML **il nome del file** caricato dal server.

---

## 🔄 Navigazione immagini

```php
if ($immagine > 0)
    echo "<td>" . generaLinkTestuale($immagine - 1, "Precedente") . "</td>";

if ($immagine < count($lista_file) - 1)
    echo "<td>" . generaLinkTestuale($immagine + 1, "Successiva") . "</td>";
```

> Mostriamo **i pulsanti di navigazione** a seconda della posizione corrente.  
> Le funzioni di supporto `generaLinkTestuale()` producono i link con query string modificata.

---

## 🧱 Inclusione del piè di pagina

```php
include("pie_pagina.php");
```

> Se presente, questo file può contenere **informazioni statiche o stilistiche di chiusura**, come copyright.