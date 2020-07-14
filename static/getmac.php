<?php
$MAC = exec('getmac');
$MAC = strtok($MAC, ' ');
echo $MAC; 
