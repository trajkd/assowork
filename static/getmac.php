<?php
$MAC = exec('ifconfig en0 | awk "/ether/{print $2}"');
$MAC = strtok($MAC, ' ');
echo $MAC; 
