import numpy
import rssi
import csv
from csv import writer
import time


def main():
    location = input("Enter your Currnet Location: ") #saving csv file based on name of location for example 'location'
    number = location[-1] # grid
    interface = 'wlp9s0' #should change to your wifi card interface

    rssi_scanner = rssi.RSSI_Scan(interface)

    # But your router name in here
    # If there is more than one add all the names seperated by commas
    ssids = ['Samir','Amir','Abdallah'] # edit name of ssids for ex tp-link123

    # ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)

    filename = "my_data_loc_" + number + ".csv" # name of file for example 'my_data_loc_1.csv'
    header = ("ssid", "quality", "signal", "mac", "Location")


    data = []
    while True:
        ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)
        for i in range(len(ap_info)):
            data.append((ap_info[i]['ssid'], ap_info[i]['quality'], ap_info[i]['signal'], ap_info[i]['mac'], "location" + location))
            # append_list_as_row(filename,data,header)
            writer(header, data, filename)
            print("Gathering..")
        time.sleep(1)
            # updater(filename)


def writer(header, data, filename):
    with open(filename, "w", newline="") as csvfile:
        movies = csv.writer(csvfile)
        movies.writerow(header)
        for x in data:
            movies.writerow(x)




