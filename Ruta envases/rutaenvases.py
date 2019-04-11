import csv
from collections import OrderedDict
import json

filename = "c:/users/usuario/Pycharmprojects/sensores/rutas_2/ruta_envases.csv"
filenamed = "c:/users/usuario/downloads/ruta_envases.csv"
array_arrival = []
array_departure = []
with open(filenamed, mode='r', encoding="UTF-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        if line_count == 2:
            array_arrival.append(float(row[0]))
            array_arrival.append(float(row[1])) # sacamos el arrivalpoint
            line_count += 1
        else:
            line_count += 1
print(array_arrival)
dict_stops = {}

with open(filenamed, mode='r', encoding="UTF-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    count = 0

    for row in csv_reader:

        if count == 0:
            # print(f'Column names are {", ".join(row)}')
            count += 1

        else:
            count += 1
            dict_stops[int(row[2])] = {
                'X':float(row[0]),
                'Y':float(row[1]),
                'Orden_Para' : int(row[2]),
                'POINT_X' : float(row[3]),
                'POINT_Y' : float(row[4]),
                'Tag':row[5],
                'Name':row[6],
                'refAssigne':row[7],
                'departureP':row[8],
                'arrivalPoi':row[9],
                'stops':row[10],
                'id':row[11]
            }
            if count == line_count - 1:
                array_departure.append(float(row[0]))
                array_departure.append(float(row[1]))  # sacamos el DeparturePoint
ordereddict_stops = OrderedDict(sorted(dict_stops.items()))
#print(array_departure)
array_realStops = []
count2 = 1

for i in ordereddict_stops.items():
    array_realStops.append({
        "refStop":("DepositPoint:%s" % ordereddict_stops[count2]['Tag']),
        "stopPoint":{
            "type":"Feature",
            "geometry":{
                "type":"Point",
                "coordinates":[
                    ordereddict_stops[count2]['X'],
                    ordereddict_stops[count2]['Y']
                ]
            }
        },
        'arrivalTimestamp':'',
        'departureTimestamp':''
    })
    count2+=1
    print(i)


dict_envases = {
    "arrivalPoint": {
        "type": "StructuredValue",
        "value": {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    array_arrival[0],
                    array_arrival[1]
                ]
            }
        },
        "metadata": {}
    },
    "departurePoint": {
        "type": "StructuredValue",
        "value": {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    array_departure[0],
                    array_departure[1]
                ]
            }
        },
        "metadata": {}
    },
    "realStops":{
        "type":"List",
        "value":array_realStops,
        "metadata":{}
    }
}

with open('rutaenvases.json', 'w') as outfile:
    outfile.write(json.dumps(dict_envases, indent=4))