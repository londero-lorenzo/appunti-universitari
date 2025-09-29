<?php
// Includiamo il file di configurazione
require_once("config.php");

/**
 * Carica i file presenti nella directory specificata,
 * filtrando solo quelli con formati validi definiti in $formati_immagine.
 *
 * @param string $dir - Path della directory da analizzare
 * @return array - Elenco dei file validi
 */
function caricaDirectory($dir) {
    $dh = opendir($dir) or die("Errore nell'apertura della directory: " . $dir);
    $contenuto = array();

    while (($file = readdir($dh)) !== false) {
        if (!is_dir($file) && controllaFormato($file)) {
            $contenuto[] = $file;
        }
    }

    closedir($dh);
    return $contenuto;
}

/**
 * Controlla se il nome del file corrisponde a uno dei formati validi.
 *
 * @param string $nomefile
 * @return bool
 */
function controllaFormato($nomefile) {
    global $formati_immagine;
    foreach ($formati_immagine as $formato) {
        if (strrpos($nomefile, $formato) !== false) {
            return true;
        }
    }
    return false;
}

/**
 * Controlla se il tipo MIME è tra quelli consentiti.
 *
 * @param string $tipo
 * @return bool
 */
function controllaTipo($tipo) {
    global $tipi_immagine;
    foreach ($tipi_immagine as $formato) {
        if (strpos($tipo, $formato) === 0) {
            return true;
        }
    }
    return false;
}

/**
 * Genera un link HTML con una miniatura dell’immagine.
 * La miniatura è ottenuta semplicemente ridimensionando l'immagine originale via HTML.
 *
 * @param int $indice_immagine
 * @param string $file - nome del file immagine
 * @return string - tag <a> contenente un'immagine ridotta
 */
function generaLinkImmagine($indice_immagine, $file) {
	$src = DIR_IMMAGINI . '/' . $file;
	return "<a href='view.php?immagine={$indice_immagine}'>"
	     . "<img src='{$src}' width='80' height='60'/>"
	     . "</a>";

}

/**
 * Genera un link HTML testuale per una specifica immagine.
 *
 * @param int $indice_immagine
 * @param string $testo - testo da visualizzare nel link
 * @return string - tag <a>
 */
function generaLinkTestuale($indice_immagine, $testo = "") {
	return "<a href='view.php?immagine={$indice_immagine}'>"
			. $testo
			. "</a>";
}
?>
