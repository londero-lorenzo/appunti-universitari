---
title: Indice
aliases:
  - Indice
tags:
  - php
  - esercizi
  - negozio
  - indice
created: 2025-06-21
---
# index.php – Pagina Indice (Vetrina Prodotti)

---

## 1. Inclusione file di configurazione e funzioni


```php
require_once("config.php"); 
require("funzioni.php");
```

- `config.php` contiene variabili e costanti globali (es. nome negozio, azienda).
    
- `funzioni.php` contiene funzioni PHP di supporto (es. per leggere i prodotti).
    
- `require_once` garantisce che il file venga incluso una sola volta per evitare ridondanze.
    
- `require` include il file ogni volta, ma in questo caso non causa problemi.


---

## 2. Inizio pagina HTML e titolo dinamico

```php
<html>
	<head>
	<title><?php echo $NOMENEGOZIO; ?></title>
	<link rel="stylesheet" type="text/css" href="stile.php" />
	</head>
<body>

```
- Il titolo della pagina è dinamico e viene preso dalla variabile `$NOMENEGOZIO` definita in `config.php`.
    
- Il CSS è generato da `stile.php` — una pagina PHP che restituisce il CSS, permettendo styling dinamico.


---

## 3. Intestazione e menu di navigazione

```php
<div id="intestazione">
  <h1><?php echo $NOMENEGOZIO; ?></h1>
  <h2>di <?php echo $AZIENDA; ?></h2>
  <div id="menu">
    <a href="index.php">Home</a>
    <a href="inserisci.php">Inserisci</a>
    <a href="prodotti.php">Magazzino</a>
  </div>
</div>
```

- Viene mostrato il nome del negozio e il nome dell’azienda (entrambi dinamici).
    
- Il menu permette di navigare tra:
    
    - Home (pagina indice)
        
    - Inserisci (pagina per aggiungere prodotti)
        
    - Magazzino (pagina per vedere tutti i prodotti)
        

---

## 4. Visualizzazione prodotti

```php
<div id="negozio">
<?php
$contenuto = leggi(1, $NPRODOTTI);
if (count($contenuto) > 0) {
  foreach ($contenuto as $prod) {
    $img="<img src='". $prod[5]."' height='80' />";
    echo "<div class=\"prodotto\">\n<h3>", $prod[2], "</h3>\n";
    echo "<p>", $img, "<em>Descrizione:</em>", $prod[3], "</p>\n";
    echo "<p><em>Prezzo:</em>", $prod[4], " - ";
    echo "<p class=\"info\">Inserito il: ", $prod[1], " da ", $AZIENDA, "</p>\n<hr /></div>\n";
  }
}
?>
</div>

```

- `leggi($da, $quanti)` è una funzione che legge dal database (file) un certo numero di prodotti.
	    
    - `$da=1` indica da quale prodotto iniziare (1° prodotto)
    - `$quanti=$NPRODOTTI` indica quanti prodotti leggere (definito in `config.php`)
    
- Se ci sono prodotti (`count($contenuto) > 0`), si itera l’array con `foreach`.
    
- Ogni prodotto è un array `$prod` che contiene (in ordine):
	    
    - id prodotto
    - data inserimento
    - titolo
    - descrizione
    - prezzo
    - percorso immagine
    
- Per ogni prodotto si stampa:
	    
    - titolo (`<h3>`)
    - immagine ridimensionata in altezza a 80 px
    - descrizione
    - prezzo
    - informazioni aggiuntive (data e azienda)

---

## 5. Chiusura pagina

```php
<hr/>
</body>
</html>
```
- Una linea orizzontale di separazione.
    
- Chiusura tag `body` e `html`.
    

---

## Note importanti

- **CSS dinamico:** usare `stile.php` per poter variare dinamicamente l’aspetto (es. colori o layout basati su variabili PHP).
    
- **Funzione `leggi`:** la chiave del caricamento dati, da implementare nel file funzioni.php.
    
- **Uso di `echo` con più argomenti:** PHP permette di passare più parametri ad `echo` senza concatenare manualmente, utile per migliorare leggibilità e prestazioni.
    
- **Il layout prodotto usa div con classe CSS:** utile per stilizzare ogni prodotto come una scheda o box.