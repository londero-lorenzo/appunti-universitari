<?php
require("functions.php");
?>
<html>
	<head>
		<title>TWC_2019_Apello1</title>
		<link rel="stylesheet" href="styles.css">
	</head>
	<body>
		<?php 
			if ($_SERVER["REQUEST_METHOD"] === "GET"){
		?>
			<form action="#" method = "post" enctype="multipart/form-data">
				<label for= "formatted_file">Inserisci file con le informazioni dei libri da anlizzare</label><br>
				<input id = "formatted_file" name= "formatted_file" type= "file"><br>
				<input name="submit" type="submit" value= "Carica!">	
			</form>

		<?php
			}else{
			#var_dump($_FILES);
			if (!isset($_FILES["formatted_file"]))
				die("Nessun file caricato!");
			if (!verify_file_content_format($_FILES["formatted_file"]))
				die("Fortmato file non valido: pattern non riconosciuto!");
			show_file_content_as_table($_FILES["formatted_file"]);
			}
		?>
	</body>

</html>
