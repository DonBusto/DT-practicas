import csv
from datetime import datetime
import sys
from xml.dom.minidom import parse, parseString
from dicttoxml import dicttoxml  # LIBRERIA A INSTALAR
import json

# filename = input("Escribe el nombre del archivo: ")
# filename2 = 'c:/users/usuario/downloads/datos3.csv'

fileconsole = sys.argv[1]
eventslist = []
measures = {}

with open(fileconsole, mode='r', encoding="UTF-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    line_count = 0
    currentname = "ssss"

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
                tempdate = datetime.strptime(row[1], '%d/%m/%Y %H:%M')
                timestamp = tempdate.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            except:
                tempdate = datetime.strptime(row[1], '%d/%m/%Y')
                timestamp = tempdate.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            try:
                idsensor = int(row[2])
            except:
                idsensor = row[2]
            try:
                val = float(row[3])
            except:
                val = row[3]

            if idsensor not in measures.keys() and idsensor != '':
                measures[str(idsensor)] = {'name': currentname, 'values': {}}

            if timestamp != '' and idsensor != '':
                measures[str(idsensor)]['values'][timestamp] = val

            eventslist.append({
                "Description": "",
                "EventID": "",
                "EventType": "Measurement",
                "SourceID": idsensor,
                "SourcePropertyID": 1,
                "Description": "TBD",
                "Value": val,
                "EventTime": timestamp
            })
        line_count += 1

events = {
    "GIM": {
        "Building": {
            "BuildingID": "UD_ESIDE", "GSEvents": {
                "EventList": {"Event":
                                  eventslist

                              }
            }
        }
    }
}
print(measures)
print(events)
with open('events.json', 'w') as outfile:
    # json.dump(events, outfile)
    outfile.write(json.dumps(events, sort_keys=True, indent=4))

# with open('events.xml', 'w') as outfile:
#     xml_str = parseString(dicttoxml(events, custom_root='test', attr_type=False))
#     outfile.write(xml_str.toprettyxml(indent=' ' * 4))
#
# with open('sensors.json', 'w') as outfile:
#     # json.dump(measures, outfile)
#     outfile.write(json.dumps(measures, sort_keys=True, indent=4))

with open('sensors.xml', 'w') as outfile:
     xml_str = parseString(dicttoxml(measures, attr_type=False))
     print(xml_str)
     outfile.write(xml_str.toprettyxml(indent=' ' * 4))
