---
title: PHP Variabili Predefinite
aliases:
  - PHP Variabili Predefinite
tags:
  - php
  - php-variabili-predefinite
created: 2025-06-21
---
# 🌐 Variabili predefinite

PHP espone numerose **superglobali**, ovvero array associativi disponibili in **qualsiasi parte dello script**, senza doverle dichiarare esplicitamente (`global` non necessario).

### 🔎 `$_SERVER`

Contiene **informazioni fornite dal server e dall’ambiente di esecuzione**. Esempi comuni:

| Chiave                  | Descrizione |
|--------------------------|-------------|
| `$_SERVER['PHP_SELF']`   | Restituisce il **percorso relativo del file** in esecuzione. Utile nei form per auto-submit. Es: `/index.php` |
| `$_SERVER['REQUEST_METHOD']` | Metodo HTTP usato nella richiesta (`GET`, `POST`, ecc.) |
| `$_SERVER['QUERY_STRING']`   | La stringa della query URL (es: `id=12&page=2`) |
| `$_SERVER['REMOTE_ADDR']`    | Indirizzo IP del client che ha fatto la richiesta |
| `$_SERVER['HTTP_USER_AGENT']`| Browser (e sistema operativo) del client |
| `$_SERVER['SERVER_NAME']`    | Nome host del server web (es: `localhost`) |
| `$_SERVER['SCRIPT_FILENAME']`| Percorso assoluto del file eseguito |

🔸 **Esempio pratico:**
```php
echo "Script in esecuzione: " . $_SERVER['PHP_SELF'];
```

---

### 📨 `$_GET` e `$_POST`

Contengono i **parametri ricevuti da form HTML o URL**.

- `$_GET`: per richieste via **query string** (URL)
    
    - Esempio: `pagina.php?nome=alice` → `$_GET['nome'] == "alice"`
        
- `$_POST`: per richieste via **form con metodo POST`
    

🔸 **Esempio GET**:

```php
// URL: script.php?user=luca
echo "Benvenuto " . $_GET['user'];
```


🔸 **Esempio POST**:

```php
// Da form con <input name="email">
echo "Email inviata: " . $_POST['email'];

```

---

### 🍪 `$_COOKIE`

Contiene i cookie inviati dal client:
```php
if (isset($_COOKIE['username'])) {
    echo "Bentornato, " . $_COOKIE['username'];
}
```

---

### 📦 `$_SESSION`

Contiene i dati di sessione, **persistenti tra più richieste**.

> Richiede sempre `session_start();` a inizio script.

```php
session_start();
$_SESSION['utente'] = "Mario";
echo $_SESSION['utente']; // stampa Mario
```

### 📁 `$_FILES`

Usata per la **gestione dell’upload di file** tramite form HTML:

```php
// $_FILES['nomecampo']['name'] → nome del file caricato
// $_FILES['nomecampo']['tmp_name'] → file temporaneo
```

### 📑 Altre superglobali utili

|Variabile|Descrizione|
|---|---|
|`$_ENV`|Variabili d’ambiente|
|`$_REQUEST`|Unione di `$_GET`, `$_POST` e `$_COOKIE`|
|`$_GLOBALS`|Rende accessibili le variabili globali (raro da usare)|

---

## 🧠 Nota sulla sicurezza

Quando si utilizzano queste variabili:

- **non fidarti mai del contenuto** fornito da client esterni,
    
- **valida** e **sanitizza** ogni input (es. `htmlspecialchars`, `filter_var`, ecc.),
    
- evita di usare direttamente `$_REQUEST` per non mischiare fonti di input.

---

## 📚 Esempio finale

```php
<?php
// Verifica metodo di richiesta e stampa dati
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    echo "Ricevuto via POST: " . htmlspecialchars($_POST['email']);
} else {
    echo "Compila il form";
}
?>
```

---

## 🔗 Collegamenti utili

- [Documentazione ufficiale – Superglobals](https://www.php.net/manual/en/language.variables.superglobals.php)

---

## 📚 Fonti e riferimenti  
Slide: `07-PHP1.pdf`  
Titoli: `Variabili predefinite`
