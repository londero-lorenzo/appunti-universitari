---
title: Functions
aliases:
  - Functions
tags:
  - php
  - esercizi
  - gallery-project-local
  - functions
created: 2025-06-27
---
# 🔧 Funzioni PHP utili: `functions.php`

Questo file contiene le funzioni definite dall'utente, fondamentali per far funzionare la gallery. È incluso all'inizio delle pagine con `require_once("functions.php");`.

---
## 📂 caricaDirectory($dir)

```php
function caricaDirectory($dir) {
    $dh = opendir($dir) or die("Errore nell'apertura della directory ". $dir);
    $contenuto = array();
    while (($file = readdir($dh)) !== FALSE)
        if (!is_dir($file) && controllaFormato($file))
            $contenuto[] = $file;
    closedir($dh);
    return $contenuto;
}
```

Carica tutti i file presenti nella directory specificata (`$dir`) che rispettano i formati previsti.  
Usa `opendir`, `readdir`, `is_dir` e una funzione ausiliaria `controllaFormato`.

---
## 🖼️ generaLinkImmagine($indice_immagine, $file)

```php
function generaLinkImmagine($indice_immagine, $file) {
    return "<a href='view.php?immagine={$indice_immagine}'>"
         . "<img src='{DIR_IMMAGINI}/{$file}' width='80' height='60'/>"
         . "</a>";
}
```

Genera un link cliccabile con anteprima dell'immagine.  
⚠️ Attenzione: le immagini vengono solo ridimensionate **visivamente** con HTML, ma a livello di rete vengono caricate **per intero** → non efficiente.

---

## 🔗 generaLinkTestuale($indice_immagine, $testo = "")

```php
function generaLinkTestuale($indice_immagine, $testo = "") {
	return "<a href='view.php?immagine={$indice_immagine}'>"
			. $testo
			. "</a>";
}
```

Simile a `generaLinkImmagine`, ma restituisce un link testuale.  
Utile ad esempio per i collegamenti "precedente / successivo".

---

## 📁 controllaFormato($nomefile) \[originale]

```php
function controllaFormato($nomefile) {
    global $formati_immagine;
    foreach ($formati_immagine as $formato)
        if (strrpos($nomefile, $formato))
            return TRUE;
    return FALSE;
}
```

Controlla che l’estensione del file `$nomefile` corrisponda a uno dei formati immagine ammessi.  
🔍 Usa `strrpos()` per verificare se l’estensione compare alla fine del nome del file.

> ❗ _Questa funzione può fallire se l’estensione si trova in mezzo al nome file._ Un controllo più robusto sarebbe:
```php
	substr($nomefile, -strlen($formato)) === $formato
```

---

## 🧪 controllaTipo($tipo)

```php
function controllaTipo($tipo) {
    global $tipi_immagine;
    foreach ($tipi_immagine as $formato)
        if (strpos($tipo, $formato) === 0)
            return TRUE;
    return FALSE;
}
```

Verifica se il tipo MIME dell'immagine inizia con uno dei valori ammessi.  
→ Utile nei controlli sui file caricati (upload).

---

## 📚 Funzioni usate dal filesystem

- `opendir($dir)` / `readdir($fp)` / `closedir($fp)` → per leggere directory.
    
- `is_dir($path)` / `is_file()` / `is_readable()` → per verifiche sui file.
    
- `fopen()` / `fread()` / `fwrite()` / `feof()` / `fclose()` → per manipolare file.
    
- `file_get_contents()` / `file()` → metodi alternativi e più semplici.
    
- `readfile()` → stampa direttamente un file.
    
- `tempnam()` → crea file temporanei.

---
### string tempnam(string $dir, string $prefix)

Crea un **nome univoco per un file temporaneo** nella directory specificata (`$dir`), utilizzando come prefisso la stringa `$prefix`.  

⚠️ Se `$dir` non è scrivibile o non esiste, PHP proverà a usare `/tmp` come fallback (su sistemi Unix).

  **Esempio:**
  ```php
  $tmp_file = tempnam("/tmp", "img_");
  echo $tmp_file; // es. /tmp/img_ab12Cd
```

---

## 🔤 Funzioni sulle stringhe

- **Concatenazione:**  
    `"str1" . "str2"` → unisce due stringhe.  
    `$s .= "altro"` → concatenazione abbreviata.
    
- **`strpos($a, $b)`**  
    Restituisce la posizione della prima occorrenza della stringa `$b` in `$a`, o `FALSE` se non trovata.
    
- **`stripos()`** → variante _case-insensitive_.
    
- **`strrpos()` / `strripos()`** → cercano l'ultima occorrenza.
    

---

## 🔍 Note finali

Le funzioni qui definite rappresentano l’infrastruttura principale della gallery:

- Separano la logica dalla struttura HTML.
    
- Rendono il codice più modulare e leggibile.
    
- Rendono possibile il riuso (es. `generaLinkImmagine` usata sia nell’indice che nella visualizzazione).
    

✏️ Per approfondire le funzioni PHP:

- [Documentazione ufficiale PHP](https://www.php.net/manual/en/funcref.php)
- 