import network
import os

def openAP(apname):
	ap = network.WLAN(network.AP_IF) # create access-point interface
	ap.config(essid=apname,authmode=network.AUTH_WPA_WPA2_PSK, password="PSK_Milus-AP") # set the ESSID of the access point
	ap.active(True)         # activate the interface
	return(ap)

#ap = openAP('Milus-AP')
