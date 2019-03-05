import csv
from collections import defaultdict
from datetime import datetime
import sys
from xml.dom.minidom import parse, parseString
from dicttoxml import dicttoxml  # LIBRERIA A INSTALAR
import json


dailyroutevehicle = 'c:/users/usuario/downloads/dailyroutevehicle2_3_17.csv'
# fileconsole = sys.argv[1]
vehiclelist = []
vehicles = {}
with open(dailyroutevehicle, mode='r', encoding="UTF-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')

        line_count += 1

with open(dailyroutevehicle, mode='r', encoding="UTF-8-sig") as csv_file:
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
    for row in csv_reader:

        if line_count == 0:
            print(f'Column names are {", ".join(row)}')

        else:
            tempname = row[2]

            if row[2] != '':
                currentname = row[2]
            else:
                row[2] = tempname
            timestamp = datetime.strptime(row[1], '%d-%m-%Y')
            dia = str(timestamp.day)
            mes = str(timestamp.month)
            anyo = str(timestamp.year)
            # hora = str(datetime.hour)
               # minuto = str(datetime.minute)
            day = datetime.strptime(dia + "/" + mes + "/" + anyo, '%d/%m/%Y')

            try:
                source = row[3]
            except:
                source = row[3]
            try:
                dest = row[4]
            except:
                dest = row[4]
            try:
                start = row[7]
            except:
                start = row[7]
            try:
                elapsed_time = row[8]
            except:
                elapsed_time = row[8]
            time_dest = row[9]
            km_str = str(row[10])
            km_str = km_str.replace(",",".")
            print(km_str)
            km = float(km_str)
            stopped = row[11]
            coord = row[12]
            currentdate_str = ("%s-%s-%d" % (timestamp.day, timestamp.month, timestamp.year))
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
            anyo = str(timestamp.year)

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
            d[currentdate_str].append({
            "Vehicle": tempname,
            "Source": source,
            "Destination": dest,
            "Time started" : start,
            "Elapsed time" : elapsed_time,
            "Time finished" : time_dest,
            "Kilometres" : km,
            "Time stopped" : stopped,
            "Coordinates" : coord,
            })


        line_count += 1

        vehicles = {
            "Day": ("%d/%d/%s" % (timestamp.day, timestamp.month, row[5])),
            "List of vehicles": {"List":
                                     d
                                 }

        }
with open('dailyroutes.json', 'w', encoding="UTF-8") as outfile:
    outfile.write(json.dumps(d, sort_keys=True, indent=4, ensure_ascii=False))
