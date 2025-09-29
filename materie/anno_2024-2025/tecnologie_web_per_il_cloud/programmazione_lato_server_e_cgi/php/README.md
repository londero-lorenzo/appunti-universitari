---
title: "Readme"
aliases: ["Readme"]
tags: [università, "tecnologie-web-per-il-cloud", "programmazione-lato-server-e-cgi", "php", "README"]
created: 2025-06-27
---
# 📦 Modulo PHP

Questo modulo raccoglie i principali concetti teorici e pratici del linguaggio **PHP**, con particolare attenzione all’interazione lato server per la generazione dinamica delle pagine web, alla gestione dello stato (es. cookie), all’uso di funzioni predefinite e alla modularizzazione del codice.

## 📚 Contenuti

| File                                                    | Argomento trattato                                                                             |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| [Introduzione al PHP](./php_introduzione.md)            | Introduzione generale a PHP: struttura di base, sintassi, modalità di esecuzione               |
| [Variabili predefinite](./php_variabili_predefinite.md) | Panoramica delle variabili superglobali (`$_GET`, `$_POST`, `$_SERVER`, ecc.)                  |
| [Funzioni](./php_funzioni.md)                           | Definizione e uso delle funzioni, scoping delle variabili, funzioni predefinite                |
| [Inclusione di file](./php_include.md)                  | Inclusione di file (`include`, `require`, `*_once`), esempi pratici e modularità               |
| [Intestazioni HTTP](./php_intestazioni.md)              | Gestione delle intestazioni HTTP (`header()`), redirezioni, invio di contenuti non HTML        |
| [Cookie](./php_cookie.md)                               | Uso dei cookie: creazione, lettura, cancellazione; implicazioni sulla sicurezza e stato utente |

## 🧩 Struttura consigliata

Questi appunti sono pensati per essere usati **insieme ad esercizi pratici**, come quelli sulla galleria di immagini e sul negozio online. Ogni file affronta un argomento isolato, ma molte funzionalità sono collegate tra loro.

## 🔗 Collegamenti utili

- [Manuale PHP ufficiale](https://www.php.net/manual/it/)
- [Cheat Sheet PHP](https://www.phpcheatsheets.com/)
- [W3Schools PHP](https://www.w3schools.com/php/)

## 📌 Note

- Tutti gli esempi usano la sintassi `<?php ... ?>`.
- Evita nomi di file `.inc` o `.txt` per contenere codice PHP: rischi che vengano letti dal browser.
- Ricorda che molte funzioni PHP devono essere usate **prima di ogni output**, come `header()` o `setcookie()`.

