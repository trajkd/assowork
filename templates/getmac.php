<?php
$MAC = exec('getmac');
$MAC = strtok($MAC, ' ');
echo "MAC address of client is: $MAC"; 
?> 