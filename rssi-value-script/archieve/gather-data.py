import numpy
import rssi
import csv
import sys
from calcDis import calculateDistance

# REMEMBER: Home square = 180cm * 120cm
# 3 Vertical * 2 Horizontal

# REMEMBER: 1st arg = current square
#           2nd arg = iterations
#           3rd arg = coordinates

currentSquare = sys.argv[1]
iterations = int(sys.argv[2])
currentLocation = (int(sys.argv[3]), int(sys.argv[4]))

interface = 'wlp2s0'
rssi_scanner = rssi.RSSI_Scan(interface)
ssids = ['AP-00', 'AP-01', 'AP-02', 'AP-03',
         'AP-04', 'AP-05', 'AP-06', 'AP-07', 'AP-08']

ssidsLocs = [(2, -2), (0, 2), (7, -1), (6, 3), (12, -1),
             (15, -1), (15, 3), (20, 2), (20, -3)]

distances = calculateDistance(ssidsLocs, currentLocation)


dataCounter = 0
skipCounter = 0
for i in range(iterations):
    ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)
    print(f'Iteration: {i}. Lines: {dataCounter}')
    while ap_info == False:
        ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)
    while len(ap_info) != 9:
        print(f'Length was equal to {len(ap_info)}')
        ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)

    data = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    for i in range(9):
        index = int(ap_info[i]['ssid'][-1])
        ap_info[i]['quality'] = ap_info[i]['quality'][0: 2]
        # del ap_info[i]['mac']
        data[index] = ap_info[i]

    with open(f'home-data.csv', 'a', newline='') as file:
        fieldNames = ['ssid', 'quality', 'signal', 'distanceFromAP', 's-01', 's-02',
                      's-03', 's-04', 's-05', 's-06', 's-07', 's-08', 's-09', 's-10', 's-11']
        # fieldNames = ['ssid', 'quality', 'rssi', 'd-00', 'd-01', 'd-02', 'd-03', 'd-04', 'd-05', 'd-06', 'd-07', 'd-08',
        #               'd-08', 's-01', 's-02', 's-03', 's-04', 's-05', 's-06', 's-07', 's-08', 's-09', 's-10', 's-11']

        writer = csv.DictWriter(file, fieldnames=fieldNames)

        if dataCounter == 0:
            writer.writeheader()

        if ap_info:
            for i in range(9):

                writer.writerow({'ssid': data[i]['ssid'], 'quality': data[i]['quality'], 'signal': data[i]['signal'], 'distanceFromAP': distances[i],
                                 's-01': 0, 's-02': 1, 's-03': 0, 's-04': 0, 's-05': 0, 's-06': 0, 's-07': 0, 's-08': 0, 's-09': 0, 's-10': 0, 's-11': 0})
        else:
            skipCounter += 9
            continue
          # writer.writerow({'ssid': data[i]['ssid'], 'quality': data[i]['quality'], 'rssi': data[i] ['rssi'], 'd-00': distances[0], 'd-01': distances[1], 'd-02': distances[2], 'd-03': distances[3], 'd-04': distances[4], 'd-05': distances[5], 'd-06': distances[6], 'd-07': distances[7], 'd-08': distances[8], 's-01': 1, 's-02': 0, 's-03': 0, 's-04': 0, 's-05': 0, 's-06': 0, 's-07': 0, 's-08': 0, 's-09': 0, 's-10': 0, 's-11': 0})
    dataCounter += 9

print(f'Done, Skipped {skipCounter} lines')
