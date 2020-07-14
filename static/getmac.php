<?php
$MAC = exec('getmac');
$MAC = strtok($MAC, ' ');
echo "<pre>";print_r("MAC address of client is: $MAC");echo "</pre>"; 
?> 