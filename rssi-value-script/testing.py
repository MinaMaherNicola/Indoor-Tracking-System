import numpy
import rssi
import csv

interface = 'wlp2s0'
squareNumber = input('Square Number: ')
data_type = 'Gathering'

rssi_scanner = rssi.RSSI_Scan(interface)

# But your router name in here
# If there is more than one add all the names seperated by commas
ssids = ['AP-00', 'AP-01', 'AP-02', 'AP-03', 'AP-04', 'AP-05', 'AP-06'] # edit name of ssids for ex tp-link123

ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)

with open('data.csv', 'a', newline='') as file:
  fieldNames = ['ssid', 'quality', 'signal', 'mac', 'square', 'data-type']

  writer = csv.DictWriter(file, fieldnames=fieldNames)

  writer.writeheader()
  print(ap_info)
  for i in range(len(ap_info)):
    writer.writerow({'ssid': ap_info[i]['ssid'], 'quality': ap_info[i]['quality'], 'signal': ap_info[i]['signal'], 'mac': ap_info[i]['mac'], 'square': squareNumber, 'data-type': data_type})

  