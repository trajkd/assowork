<?php
$MAC = exec('getmac');
$MAC = strtok($MAC, ' ');
echo "<pre> MAC address of client is:",$MAC; 
