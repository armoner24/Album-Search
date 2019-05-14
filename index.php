<html>
<head>
<title>Album Search</title>
<style>
body {background-color: powderblue;}
div.a {position: fixed; text-align: center; bottom: 30px; left: 710px;}
div.b {position: fixed; text-align: center; bottom: 10px; left: 780px;}
</style>
</head>
<body>
<h1 align='center'>Search the Album</h1>
<?php
if(isset($_POST['album'])){
	$alb=$_POST['album'];
	echo "Given query is: ";
	echo $alb;
	echo nl2br("\r\n");
	echo nl2br("\r\n");
	echo nl2br("Searching...\r\n");
	echo nl2br("\r\n");
	echo nl2br("Matching found in-\r\n");
	echo nl2br("\r\n");

}
$tmp = exec("python search.py $alb");
echo $tmp;
?>
<div class="a">Hosted and Created by AADITYA VAIDYA</div>
<div class="b">(c) Copyright 2018</div>
</body>
</html>

