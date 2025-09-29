<?php
require("config.php");

function verify_uploaded_file($uploaded_file_cache){
	return $uploaded_file_cache["error"] === UPLOAD_ERR_OK && is_uploaded_file($uploaded_file_cache["tmp_name"]);
}


function verify_file_content_format($uploaded_file_cache){
	global $STANDARD_BOOK_PATTERN_COUNT;
	if (!verify_uploaded_file($uploaded_file_cache)){
		return false;
	}
	$content = file_get_contents($uploaded_file_cache["tmp_name"]);
	$lines = explode("\n", $content);
			
	foreach ($lines as $key => $line){
		if ($key == count($lines) -1 && $line == "")
			break;
		$columns = explode("#", $line);
		if (count($columns) !== $STANDARD_BOOK_PATTERN_COUNT)
			return false;
	}
	return true;
}





function show_file_content_as_table($uploaded_file_cache){
	global $FILE_SEPARATOR;
	global $UPLOAD_FILE_FORMAT_COLUMNS;
	if (!verify_uploaded_file($uploaded_file_cache))
		die("Impossibile mostrare il contenuto del file: errore durante il caricamento del file o file non proveniente da upload!");
	
	$content = file_get_contents($uploaded_file_cache["tmp_name"]);
	$lines = explode("\n", $content);

	$table = "<table class= 'books_table'>";
	$table =$table."<tr>";
	foreach($UPLOAD_FILE_FORMAT_COLUMNS as $head)
		$table = $table."<th>{$head}</th>";
	$table = $table."</tr>";

	foreach($lines as $key => $line){
		$row_data = explode($FILE_SEPARATOR, $line);
		$table = $table."<tr>";
		foreach($row_data as $cell_data)
			$table = $table."<td>{$cell_data}</td>";
		$table = $table."</tr>";
	}
	$tabmte = $table."</table>";

	echo $table;
}


?>
