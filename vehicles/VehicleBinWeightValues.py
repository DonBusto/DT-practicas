import csv
from collections import defaultdict
from datetime import datetime
import sys
from xml.dom.minidom import parse, parseString
from dicttoxml import dicttoxml  # LIBRERIA A INSTALAR
import json

filename = 'c:/users/usuario/downloads/franceeesco.csv'
filename2 = 'c:/users/usuario/downloads/vehicleBinWeightValues_TOTAL.csv'
depositpointfile = 'c:/users/usuario/downloads/Halandri_Deposit_Point_v2.csv'
# fileconsole = sys.argv[1]
vehiclelist = []
vehicles_por_dia = {}
vehicles = {}
ids = []
with open(depositpointfile, mode='r', encoding="UTF-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        else:
            ids.append(int(row[0]))
        line_count += 1

with open(filename2, mode='r', encoding="UTF-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    line_count = 0
    currentname = "ssss"
    datecount = 0
    tempday = ""
    timestamp = datetime.strptime("01/01/1990", '%d/%m/%Y')
    day = ""
    hora = ""
    minuto = ""
    inv = ""
    d = defaultdict(list)
    d_not = defaultdict(list)
    for row in csv_reader:

        if line_count == 0:
            print(f'Column names are {", ".join(row)}')

        else:
            tempname = row[0]

            if row[0] != '':
                currentname = row[0]
            else:
                row[0] = tempname
            try:
                timestamp = datetime.strptime(row[1], '%d/%m %H:%M')
                dia = str(timestamp.day)
                mes = str(timestamp.month)
                anyo = row[5]
                # hora = str(datetime.hour)
                # minuto = str(datetime.minute)
                day = datetime.strptime(dia + "/" + mes + "/" + anyo, '%d/%m/%Y')
            except:
                timestamp = datetime.strptime(row[1], '%d/%m %H:%M')
                day = datetime.strptime(row[1] + "/" + row[5], '%d/%m/%Y')
            try:
                address = int(row[2])
            except:
                address = row[2]
            try:
                bin = int(row[3])
            except:
                bin = row[3]
            try:
                weight = int(row[4])
            except:
                weight = row[4]
            try:
                year = int(row[5])
            except:
                year = row[5]
            currentdate_str = ("%d/%d/%s" % (timestamp.day, timestamp.month, row[5]))
            # vehiclelist.append({
            #     "Date" : currentdate_str,
            #     "Vehicle": tempname,
            #     "Address": address,
            #     "Bin": bin,
            #     "Weight": weight,
            # })
            if tempday != day:
                datecount += 1
            dia = str(timestamp.day)
            mes = str(timestamp.month)
            anyo = row[5]
            try:
                if int(bin) in ids:
                    inv = "Yes"
                else:
                    inv = "No"
            except:
                inv = "Error"
            # for n in range(1, len(ids)):
            #     print(bin)
            #     print(n)
            #     try:
            #         if int(bin) == int(ids[n]):
            #             inv = "Yes"
            #         else:
            #             inv = "No"
            #     except:
            #         inv = "Error"
            tempday = datetime.strptime(dia + "/" + mes + "/" + anyo, '%d/%m/%Y')
            if inv == "Yes":
                d[currentdate_str].append({
                    "Vehicle": tempname,
                    "Address": address,
                    "Bin": bin,
                    "Weight": weight,
                    "Time": datetime.strftime(timestamp, '%H:%M'),
                    "Inventory?": inv
                })
            else:
                d_not[currentdate_str].append({
                    "Vehicle": tempname,
                    "Address": address,
                    "Bin": bin,
                    "Weight": weight,
                    "Time": datetime.strftime(timestamp, '%H:%M'),
                    "Inventory?": inv
                })

        line_count += 1

        vehicles = {
            "Day": ("%d/%d/%s" % (timestamp.day, timestamp.month, row[5])),
            "List of vehicles": {"List":
                                     d
                                 }

        }
print(ids)
with open('vehicles_in_inventory.json', 'w', encoding="UTF-8") as outfile:
    outfile.write(json.dumps(d, sort_keys=True, indent=4, ensure_ascii=False))

with open('vehicles_not_in_inventory.json', 'w', encoding="UTF-8") as outfile:
    outfile.write(json.dumps(d_not, sort_keys=True, indent=4, ensure_ascii=False))
