import netifaces
def getClientMac():
	return netifaces.ifaddresses('wlan0')[netifaces.AF_LINK]['addr']