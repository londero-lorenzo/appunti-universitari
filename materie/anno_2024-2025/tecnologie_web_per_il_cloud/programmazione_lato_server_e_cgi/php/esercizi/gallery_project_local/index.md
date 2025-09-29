---
title: Index
aliases:
  - Index
tags:
  - php
  - esercizi
  - gallery-project-local
  - index
created: 2025-06-21
---


# Pagina indice (index.php)

## Scopo
`index.php` è la pagina principale della galleria di immagini.  
Genera dinamicamente un elenco (tabella) di miniature con link alle singole immagini, organizzate in righe.

---

## Struttura del file

```php
<?php
require_once("config.php");
require_once("funzioni.php");
?>
<html>
	<head><title>.: pwlsGallery Indice :.</title></head>
	<body>
	<h1>pwlsGallery: indice delle fotografie</h1>
	<?php
	$lista_file = caricaDirectory(DIR_IMMAGINI);
	
	if (count($lista_file) > 0) {
	    echo "<table>\n", "\t<tr>\n",
	         "\t\t<td>", generaLinkImmagine(0, $lista_file[0]), "</td>\n";
	
	    for ($i = 1; $i < count($lista_file); $i++) {
	        if ($i % $immagini_per_riga == 0)
	            echo "\t</tr>\n\t<tr>\n";
	        echo "\t\t<td>", generaLinkImmagine($i, $lista_file[$i]), "</td>\n";
	    }
	    echo "\t</tr>\n</table>\n";
	} else {
	    echo "\t<p>Non &egrave; presente alcuna immagine</p>\n";
	}
	?>
	<hr/>
	<?php include("pie_pagina.php"); ?>
	</body>
</html>
```


---

## Spiegazione dettagliata

- **Inclusione di file**  
    All'inizio si includono `config.php` e `funzioni.php` usando `require_once()`, per caricare configurazioni e funzioni riutilizzabili.
    
- **Caricamento della lista immagini**  
    La funzione `caricaDirectory(DIR_IMMAGINI)` legge la cartella delle immagini e restituisce un array con i nomi dei file.
    
- **Generazione tabella immagini**  
    Se ci sono immagini, si crea una tabella HTML in cui ogni cella (`<td>`) contiene un link generato da `generaLinkImmagine()` che punta alla pagina di dettaglio per quell’immagine.
    
- **Organizzazione in righe**  
    Dopo un certo numero di immagini (`$immagini_per_riga`), si chiude la riga e se ne apre una nuova.
    
- **Messaggio in assenza di immagini**  
    Se la cartella è vuota, viene mostrato un messaggio.
    
- **Footer**  
    Alla fine viene incluso `pie_pagina.php` per inserire un eventuale piè di pagina comune.
    

---

## Note sulle funzioni e costrutti PHP utilizzati

- `require_once("file.php")`:  
    Include e interpreta il file indicato solo una volta per evitare duplicazioni.
    
- `caricaDirectory()`, `generaLinkImmagine()`:  
    Funzioni definite dall’utente nel file `funzioni.php`.
    
    - `caricaDirectory`: legge i file di una cartella.
        
    - `generaLinkImmagine`: crea il codice HTML per il link con la miniatura.
        
- `count($array)`: restituisce il numero di elementi presenti in un array.
    
- `echo`: costrutto per inviare output HTML o testo.  
    Non è una funzione, quindi non richiede parentesi.
    
- Sequenze di escape in stringhe:
    
    - `\n`: nuova linea (utile per formattare l'HTML sorgente).
        
    - `\"`: per inserire virgolette doppie all’interno di stringhe racchiuse da virgolette doppie.
        
- `die($messaggio)`: interrompe l’esecuzione dello script mostrando il messaggio fornito.