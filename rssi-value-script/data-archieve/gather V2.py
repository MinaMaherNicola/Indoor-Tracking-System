import numpy
import rssi
import csv
import sys

# REMEMBER: 1st arg = current square
#           2nd arg = iterations

currentSquare = sys.argv[1]
iterations = int(sys.argv[2])

interface = 'wlp2s0'
rssi_scanner = rssi.RSSI_Scan(interface)
ssids = ['AP-00', 'AP-01', 'AP-02', 'AP-03',
         'AP-04', 'AP-05', 'AP-06', 'AP-07', 'AP-08']

for i in range(iterations):
    ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)
    while ap_info == False:
        print('Value was false')
        ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)

    while len(ap_info) != 9:
        print('Length was less than 9')
        ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)

    RSSIs = []

    data = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    for j in range(9):

        index = int(ap_info[j]['ssid'][-1])
        data[index] = ap_info[j]

    for j in range(9):
        # ERRORS HERE!
        try:
            RSSIs.append(data[j]['signal'])

        except:
            print('Line 54 resulted in an error')
            continue

    with open(f'college-a-1.csv', 'a', newline='') as file:
        fieldNames = ['square', 'AP-00', 'AP-01', 'AP-02', 'AP-03',
                      'AP-04', 'AP-05', 'AP-06', 'AP-07', 'AP-08']

        writer = csv.DictWriter(file, fieldnames=fieldNames)

        if i == 0:
            writer.writeheader()

        if ap_info:
            try:
                writer.writerow({'square': currentSquare, 'AP-00': RSSIs[0], 'AP-01': RSSIs[1], 'AP-02': RSSIs[2], 'AP-03': RSSIs[3],
                                 'AP-04': RSSIs[4], 'AP-05': RSSIs[5], 'AP-06': RSSIs[6], 'AP-07': RSSIs[7], 'AP-08': RSSIs[8]})
            except:
                print('Line 71 resulted in an error')
                continue
        else:
            continue
    print(f'Lines Written: {i}')
