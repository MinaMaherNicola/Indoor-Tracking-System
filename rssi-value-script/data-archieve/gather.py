import numpy
import rssi
import csv
import sys

# REMEMBER: Home square = 180cm * 120cm
# 3 Vertical * 2 Horizontal

# REMEMBER: 1st arg = current square
#           2nd arg = iterations
#           3rd arg = coordinates

currentSquare = sys.argv[1]
iterations = int(sys.argv[2])

interface = 'wlp2s0'
rssi_scanner = rssi.RSSI_Scan(interface)
ssids = ['AP-00', 'AP-01', 'AP-02', 'AP-03',
         'AP-04', 'AP-05', 'AP-06', 'AP-07', 'AP-08']
# get SSIDS data
# get best mac addrress
# Write data into columns not rows


for i in range(iterations):
    # try:
    ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)
    while ap_info == False:
        print('Value was false')
        ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)

    while len(ap_info) != 9:
        print('Length was less than 9')
        ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)

    RSSIs = []
    maxRSSI = -101
    bestMAC = ''

    data = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    for j in range(9):
        if (maxRSSI < ap_info[j]['signal']):
            maxRSSI = ap_info[j]['signal']
            bestMAC = ap_info[j]['mac']

        index = int(ap_info[j]['ssid'][-1])
        data[index] = ap_info[j]

    # if not data[0]['signal']:
    #     continue

    for j in range(9):
        # ERRORS HERE!
        try:
            RSSIs.append(data[j]['signal'])

        except:
            print('Line 54 resulted in an error')
            continue

    with open(f'home-grid-v1.1.csv', 'a', newline='') as file:
        fieldNames = ['square', 'AP-00', 'AP-01', 'AP-02', 'AP-03',
                      'AP-04', 'AP-05', 'AP-06', 'AP-07', 'AP-08', 'bestMAC']

        writer = csv.DictWriter(file, fieldnames=fieldNames)

        if i == 0:
            writer.writeheader()

        if ap_info:
            try:
                writer.writerow({'square': currentSquare, 'AP-00': RSSIs[0], 'AP-01': RSSIs[1], 'AP-02': RSSIs[2], 'AP-03': RSSIs[3],
                                 'AP-04': RSSIs[4], 'AP-05': RSSIs[5], 'AP-06': RSSIs[6], 'AP-07': RSSIs[7], 'AP-08': RSSIs[8], 'bestMAC': bestMAC})
            except:
                print('Line 71 resulted in an error')
                continue
        else:
            continue
    print(f'Lines Written: {i}')
    # except:
    #     print('ERROR OCCURED')
    #     continue
