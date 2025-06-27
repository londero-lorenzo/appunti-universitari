---
title: PHP Intestazioni
aliases:
  - PHP Intestazioni
tags:
  - php
  - php-intestazioni
created: 2025-06-21
---
## Intestazioni HTTP

PHP invia automaticamente le intestazioni (`Content-Type: text/html`).  
È possibile sovrascriverle tramite la funzione `header()`, **prima di qualsiasi output**.

### Redirezione

```php
header("Location: https://www.uniud.it/"); exit;
```

### Tipo contenuto

```php
header("Content-type: application/pdf");
```

> ⚠️ Nessun output (nemmeno spazi o errori) prima dell’uso di `header()`.


---

## 📚 Fonti e riferimenti  
Slide: `07-PHP1.pdf`  
Titoli: `Le intestazioni HTTP`
