<?php
// Inclusione dei file di configurazione e delle funzioni
include_once("config.php");
include_once("functions.php");

// Verifica che il parametro 'immagine' sia stato passato tramite GET
if (!isset($_GET["immagine"])) {
    die("Errore: stai cercando di accedere alla pagina in modo scorretto\n");
}

$immagine = $_GET["immagine"];

// Carica la lista dei file presenti nella directory immagini
$lista_file = caricaDirectory(DIR_IMMAGINI);

// Verifica che l'indice richiesto sia valido
if (!isset($lista_file[$immagine])) {
    die("Errore: immagine non valida o inesistente.");
}
?>

<html>
<head>
    <title><?php echo "Immagine: " . htmlspecialchars($immagine); ?></title>
</head>
<body>

<!-- Visualizzazione dell'immagine selezionata -->
<?php
echo "<img src=\"" . DIR_IMMAGINI . "/" . htmlspecialchars($lista_file[$immagine]) . "\" alt=\"Immagine numero $immagine\"/>";
?>

<!-- Navigazione: link all'immagine precedente e successiva -->
<table>
    <tr>
        <?php
        if ($immagine > 0) {
            echo "<td>" . generaLinkTestuale($immagine - 1, "Precedente") . "</td>";
        }
        if ($immagine < count($lista_file) - 1) {
            echo "<td>" . generaLinkTestuale($immagine + 1, "Successiva") . "</td>";
        }
        ?>
    </tr>
</table>

<!-- Inclusione del pie di pagina -->
<?php include("footer.php"); ?>

</body>
</html>
