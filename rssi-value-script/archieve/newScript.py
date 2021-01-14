import numpy
import rssi
import csv
import sys

interface = 'wlp2s0'
squareNumber = input('Square Number: ')

rssi_scanner = rssi.RSSI_Scan(interface)

ssids = ['AP-00', 'AP-01', 'AP-02', 'AP-03',
         'AP-04', 'AP-05', 'AP-06', 'AP-07', 'AP-08']

dataCount = 0
count = 0
while True:
    ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)

    while ap_info == False:
        ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)

    while len(ap_info) != 9:
        ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)

    data = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    for i in range(len(ap_info)):
        index = int(ap_info[i]['ssid'][-1])
        data[index] = ap_info[i]

    with open(f'{sys.argv[1]}-{squareNumber}.csv', 'a', newline='') as file:
        fieldNames = ['ssid', 'quality', 'signal', 'mac', 'square']

        writer = csv.DictWriter(file, fieldnames=fieldNames)
        if dataCount == 0:
            writer.writeheader()
        for i in range(len(data)):
            writer.writerow({'ssid': data[i]['ssid'], 'quality': data[i]['quality'],
                             'signal': data[i]['signal'], 'mac': data[i]['mac'], 'square': squareNumber})
        dataCount += 9
        count += 1
        print('Data Written ' + str(dataCount) +
              ' | Iterations: ' + str(count))
