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
