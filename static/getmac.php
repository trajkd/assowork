<?php
$MAC = exec('ifconfig en0 | awk "/ether/{print $2}"');
$MAC = strtok($MAC, ' ');
$cookie_name = "usermac";
$cookie_value = $MAC;
setcookie($cookie_name, $cookie_value, time() + (86400 * 365000), "/");
