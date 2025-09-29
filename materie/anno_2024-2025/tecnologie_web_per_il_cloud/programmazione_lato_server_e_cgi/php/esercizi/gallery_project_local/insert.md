---
title: Insert
aliases:
  - Insert
tags:
  - php
  - esercizi
  - gallery-project-local
  - insert
created: 2025-06-21
---
# 🖼️ Inserimento immagini – `insert.html` + `insert.php`

Questa parte dell'applicazione permette agli utenti di **caricare nuove immagini** nella galleria. È composta da due file principali:

- `insert.html`: modulo HTML per la selezione e l’invio del file.
    
- `insert.php`: script PHP che elabora il caricamento.
    

---

## 🔧 Funzionalità supportate

- Caricamento di file tramite form HTML (`multipart/form-data`)
    
- Verifica **del tipo MIME** e dell’estensione
    
- Salvataggio dell’immagine nella directory predefinita
    
- (opzionalmente) Autenticazione utente
    
- Riscontro visivo all'utente sull'esito dell’operazione
    

---

## 📄 Il modulo HTML – `insert.html`

```html
<html>
<head><title>.: pwlsGallery inserisci :.</title></head>
<body>
<form method="post" action="insert.php" enctype="multipart/form-data">
  Username: <input type="text" name="user" />
  Password: <input type="password" name="password" /><br />
  File da caricare: <input type="file" name="nomefile"/><br/>
  <input type="submit" name="invia" value="Invia"/>
</form>
</body>
</html>
```

### 🔐 Note:

- `enctype="multipart/form-data"` è **obbligatorio** per inviare file.
    
- I campi `user` e `password` sono utilizzati per un’autenticazione **semplice**, verificata lato server.

---

## 📜 Lo script PHP – `insert.php`

```php
<?php
require_once("config.php");
require_once("functions.php");

// ✅ Controllo autenticazione (facoltativo ma consigliato)
if ($_POST['user'] != $USER || $_POST['password'] != $PASSWORD)
  die("Non puoi!");

// ✅ Verifica che un file sia stato ricevuto
if (!isset($_FILES["nomefile"])) 
  die("File non ricevuto\n");

// 📦 Recupero dati del file caricato
$tmp_nome = $_FILES["nomefile"]["tmp_name"];
$tipo = $_FILES["nomefile"]["type"];
$nome = $_FILES["nomefile"]["name"];

// ✅ Validazione formato e tipo MIME
if (!controllaTipo($tipo) || !controllaFormato($nome))
  die("File di tipo sconosciuto\n");

// ✅ Spostamento del file nella galleria
if (move_uploaded_file($tmp_nome, DIR_IMMAGINI . "/" . $nome))
  echo "<p>Inserimento effettuato, torna all'<a href=\"index.php\">indice</a></p>\n";
else
  echo "<p>Non sono riuscito a spostare il file, controlla i permessi </p>\n";
?>

```

---

## ⚠️ Note di sicurezza

### 🔒 Autenticazione

Il controllo su `$_POST["user"]` e `$_POST["password"]` **evita che chiunque possa caricare file arbitrari**. Le credenziali vanno definite nel file `config.php`:

```php
`$USER = "admin"; $PASSWORD = "supersegreto";`
```

### 📁 Permessi di scrittura

Per permettere il caricamento nella cartella `immagini`, assicurarsi che essa abbia i permessi giusti:

```bash
chmod a+w images/
```

Meglio ancora: assegnarla al gruppo di Apache (es. `www-data`) con:

```bash
sudo chown :www-data images/
sudo chmod 775 images/
```

---

## 📦 Variabile superglobale `$_FILES`

Contiene informazioni dettagliate sul file inviato:

- `$_FILES["nomefile"]["name"]` → nome originale
    
- `$_FILES["nomefile"]["type"]` → tipo MIME
    
- `$_FILES["nomefile"]["tmp_name"]` → percorso temporaneo
    
- `$_FILES["nomefile"]["size"]` → dimensione in byte

---

## ✅ Funzione utile: `move_uploaded_file()`

Serve a **spostare** in modo sicuro il file caricato dal server nella directory desiderata:

```php
move_uploaded_file($tmp_nome, DESTINAZIONE)
```

Restituisce `true` in caso di successo.

---

## 🚫 Altri rischi da mitigare

| Problema                    | Soluzione consigliata                            |
| --------------------------- | ------------------------------------------------ |
| Upload da parte di chiunque | Autenticazione via form                          |
| File dannosi / eseguibili   | Controllare tipo e formato                       |
| Directory visibili dal web  | Disabilitare l'autoindex nel file `.htaccess`    |
| Inclusione file sensibili   | Evitare estensioni `.txt`, `.conf`, `.inc`, ecc. |

## 📁 Output atteso

Dopo l’invio, l’utente riceve:

- Un messaggio di conferma
    
- Un link per tornare all’indice (`index.php`)
    

---

## 📚 Fonti e riferimenti

- Slide: `08-PHP-gallery.pdf`
    
- Titoli: `Galleria immagini`, `Upload e sicurezza`, `Form e file`