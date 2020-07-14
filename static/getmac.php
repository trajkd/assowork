<?php
$MAC = exec('ifconfig en0 | awk "/ether/{print $2}"');
$MAC = strtok($MAC, ' ');
echo "<pre> MAC Address: ".$MAC."</pre>"; 
