<?php
$file = fopen("text/geo.2013-01-01_00-09.txt", "r") or exit("Unable to open file!");
//Output a line of the file until the end is reached



$i = 1;
//$fp = file_get_contents('text/geo.2013-01-01_00-09.txt', true);
while(! feof($file)) {
    $contents = fread($file,150000);
	$test = file_get_contents($contents, true);
	parse_str($test);
    file_put_contents('new_'.$i.'.txt',$contents);
	$contents = fread($file,150000);
	parse_str($test);
	
    $i++;
}

/*
<?php
$handle = @fopen("/tmp/inputfile.txt", "r");
if ($handle) {
    while (($buffer = fgets($handle, 4096)) !== false) {
        echo $buffer;
    }
    if (!feof($handle)) {
        echo "Error: unexpected fgets() fail\n";
    }
    fclose($handle);
}
?>

/*while(!feof($file))
  {
 echo fgets($file). "<br>";
  }
fclose($file);
?>



<?php
/*
$str = "first=value&arr[]=foo+bar&arr[]=baz";
parse_str($str);
echo $first;  // value
echo $arr[0]; // foo bar
echo $arr[1]; // baz

parse_str($str, $output);
echo $output['first'];  // value
echo $output['arr'][0]; // foo bar
echo $output['arr'][1]; // baz

?>*/