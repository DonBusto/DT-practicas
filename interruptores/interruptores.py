import csv
import json
from datetime import datetime
from collections import defaultdict

file_inter = "C:/Users/Usuario/PycharmProjects/Sensores/interruptores/Hoja2.csv"

fieldnames = ("Name", "TimeDate", "Event", "EventText")

f = open(file_inter, 'rU')
reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=",")
arraydicts_org = []
arraykeys_org = []
tempname = ''
dict_inter = {}
d = defaultdict(list)
array_inter = []

for row in reader:
    if row['Name'] != 'Name':
        try:
            if row['Name'] != '':
                # dict_inter[tempname] = {
                #     'Interruptores' : array_inter
                # }
                tempname = row['Name']
                # array_inter = []
                if row['Name'] not in arraykeys_org:
                    arraykeys_org.append(row['Name'])
            else:
                row['Name'] = tempname
            row['TimeDate'] = datetime.strptime(row['TimeDate'], "%Y-%m-%d %H:%M:%S")
            arraydicts_org.append(row)
            # array_inter.append(row)
            # print(array_inter)
            d[row['Name']].append(row)

        except:
            continue

for k in d:
    try:
        d[k] = sorted(d[k], key=lambda x: x["TimeDate"])
    except:
        continue
    for n in d[k]:
        n["TimeDate"] = datetime.strftime(n['TimeDate'], "%Y-%m-%d %H:%M:%S")

file_object = open("C:/Users/Usuario/PycharmProjects/Sensores/interruptores/datoSalida.csv", "w")
file_object.write("Name; TimeDateON; EventTextON; TimeDateOFF; EventTextOFF; Seconds elapsed\n")
print(d)
for k in d:
    counterobjects = 0
    i = 0
    try:
        for v in d[k]:
            counterobjects += 1
        for i2 in range(0, int(counterobjects / 2)):
            if d[k][i]['Event'] == '5':
                fecha1 = datetime.strptime(d[k][i]['TimeDate'], "%Y-%m-%d %H:%M:%S")
                fecha2 = datetime.strptime(d[k][i+1]['TimeDate'], "%Y-%m-%d %H:%M:%S")
                seconds_elapsed = (fecha2 - fecha1).total_seconds()
                file_object.write("%s;%s;%s;%s;%s;%d\n" % (
                d[k][i]['Name'], d[k][i]['TimeDate'], d[k][i]['EventText'], d[k][i + 1]['TimeDate'],
                d[k][i + 1]['EventText'], seconds_elapsed))
                i += 2
                print(i)
            else:
                file_object.write("%s;%s;%s;%s;%s\n" % (
                    d[k][i]['Name'], d[k][i+1]['TimeDate'], d[k][i+1]['EventText'], d[k][i]['TimeDate'],
                    d[k][i]['EventText']))
                i += 2
                print(i)


    except:
        continue

# print(dict_inter)
#hoja2json = "C:/Users/Usuario/PycharmProjects/Sensores/interruptores/Hoja2.json"
#with open(hoja2json, 'w', encoding="UTF-8") as outfile:
#    outfile.write(json.dumps(d, sort_keys=False, indent=4, ensure_ascii=False))
