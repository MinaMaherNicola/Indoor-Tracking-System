import numpy
import rssi

interface = 'wlp2s0'

rssi_scanner = rssi.RSSI_Scan(interface)

# But your router name in here
# If there is more than one add all the names seperated by commas
ssids = ['Maher Nicola']

ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)

print(ap_info)