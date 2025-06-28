---
title: "Php Configurazione di Php"
aliases: ["Php Configurazione di Php"]
tags: [università, "tecnologie-web-per-il-cloud", "programmazione-lato-server-e-cgi", "php", "php-configurazione-di-php"]
created: 2025-06-27
---


# Parametri di funzionamento di PHP

Sono impostati in un file ***php.ini*** che contiene numerose direttive:

**Esempio:** 
+ memoria massima utilizzabile dallo script;
+ dimensione massima di un corpo HTTP accettata;
+ file di log;
+ ecc...

## Direttive per la visualizzazione degli errori

PHP consente di sovrascrivere alcune direttive nel php.ini direttamente in uno script:
+ Funzione **`ini_set()`**
+ Le modifiche saranno valide solo per quello script

### In testa allo script:
+ `ini_set('display_errors', 1);`
+ `ini_set('display_startup_errors', 1);`
+ `error_reporting(COSA_MOSTRARE);`

**Cosa mostrare ?**
+ Flag binari che identificano errori veri e propri;
+ Warning;
+ Variabili non dichiarate.
	+ `E_ALL`
	+ `E_ERROR`
	+ `E_WARNING`
	+ `E_PARSE`
	+ `E_NOTICE`
+ Per non mostrare le *notice*:
	+ `error_reporting(E_ALL & ~E_NOTICE);`

---
## 📚 Fonti e riferimenti  
Slide: `10-PHP-OO-Composer.pdf`
