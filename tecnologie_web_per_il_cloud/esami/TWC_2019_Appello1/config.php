<?php
error_reporting(E_ALL);
ini_set("display_errors", 1);
$FILE_SEPARATOR = "#";
$UPLOAD_FILE_FORMAT = "isbn#titolo#autore#data di pubblicazione#editore#numero di pagine";
$UPLOAD_FILE_FORMAT_COLUMNS = explode($FILE_SEPARATOR ,$UPLOAD_FILE_FORMAT);
$STANDARD_BOOK_PATTERN_COUNT = count($UPLOAD_FILE_FORMAT_COLUMNS);

?>
