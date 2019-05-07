import csv
import json
from datetime import datetime

organic2018 = "C:/Users/Usuario/PycharmProjects/Sensores/rutasCamiones/organic2018_PDCs_withSTs_fixed.csv"

paper2018 = "C:/Users/Usuario/PycharmProjects/Sensores/rutasCamiones/paper2018_PDCs_withSTs_fixed.csv"
residual2018 = "C:/Users/Usuario/PycharmProjects/Sensores/rutasCamiones/residual2018_PDCs_withSTs_fixed.csv"

f = open(organic2018, 'rU')
reader = csv.DictReader(f, delimiter=";")
arraydicts_org = []
array_fechas_org = []
arraykeys_org = []
for row in reader:
    fecha = datetime.strptime(row['Fecha'], '%d/%m/%Y %H:%M:%S')
    fecha_sinhoras = datetime.strftime(fecha, '%d/%m/%Y')
    key = [row['Vehiculo'], fecha_sinhoras]
    if key not in arraykeys_org:
        arraykeys_org.append(key)
    arraydicts_org.append(row)
    array_fechas_org.append(fecha)

dict_fechaspordia_org = {}
for k in arraykeys_org:
    arrayfechas = []
    for row in arraydicts_org:

        fecha = datetime.strptime(row['Fecha'], '%d/%m/%Y %H:%M:%S')
        fecha_sinhoras = datetime.strftime(fecha, '%d/%m/%Y')
        if fecha_sinhoras == k[1] and k[0] == row['Vehiculo']:
            arrayfechas.append(fecha)

    dict_fechaspordia_org[(k[0], k[1])] = arrayfechas

for k in arraykeys_org:
    entrada = {}
    entrada['id'] = k[0] + ":" + k[1]
    entrada['type'] = 'Route'
    entrada['arrivalPoint'] = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': []
        }
    }
    entrada['departurePoint'] = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': []
        }
    }
    entrada["description"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }
    entrada["longName"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }
    maxfecha = datetime.strftime((max(dict_fechaspordia_org[(k[0], k[1])])), "%Y-%m-%dT%H:%M:%S+00:00")
    minfecha = datetime.strftime((min(dict_fechaspordia_org[(k[0], k[1])])), "%Y-%m-%dT%H:%M:%S+00:00")
    arrayStops = []
    for n in arraydicts_org:
        fecha_parsed = datetime.strptime(n['Fecha'], '%d/%m/%Y %H:%M:%S')
        if n['Vehiculo'] == k[0] and fecha_parsed in dict_fechaspordia_org[(k[0], k[1])]:
            arrayStops.append({
                "refStop": ("DepositPoint:%s" % n['Tag']),
                "stopPoint": {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [

                        ]
                    }
                },
                "arrivalTimestamp": datetime.strftime(fecha_parsed, "%Y-%m-%dT%H:%M:%S+00:00"),
                "departureTimestamp": ""
            })

    entrada["realArrivalTimestamp"] = {
        "type": "String",
        "value": maxfecha,
        "metadata": {}
    }
    entrada["realDepartureTimestamp"] = {
        "type": "String",
        "value": minfecha,
        "metadata": {}
    }
    entrada['realPath'] = {
        "type": "List",
        "value": [],
        "metadata": {}
    }

    entrada['realStops'] = {
        "type": "List",
        "value": arrayStops,
        "metadata": {}
    }
    entrada['refAssignedVehicle'] = {
        "type": "String",
        "value": ("Vehicle:%s" % k[0]),
        "metadata": {}
    }
    entrada['refScheduledVehicle'] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }
    entrada["scheduledArrivalTimestamp"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }
    entrada["scheduledDepartureTimestamp"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }
    entrada["scheduledPath"] = {
        "type": "List",
        "value": [],
        "metadata": {}
    }
    entrada["scheduledStops"] = {
        "type": "List",
        "value": [],
        "metadata": {}
    }
    entrada["shortName"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }

    entrada["vehicleType"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }

    fechasinbarras_datetime = datetime.strptime(k[1], "%d/%m/%Y")
    fechasinbarras = datetime.strftime(fechasinbarras_datetime, "%d%m%Y")
    organicjson = ("C:/Users/Usuario/PycharmProjects/Sensores/rutasCamiones/rutasMatricula/organic/%s%s.json" % (
        k[0], fechasinbarras))
    with open(organicjson, 'w', encoding="UTF-8") as outfile:
        outfile.write(json.dumps(entrada, sort_keys=False, indent=4, ensure_ascii=False))

# print(dict_fechaspordia_org[('1541CLM', '27/12/2018')])

f = open(paper2018, 'rU')
reader = csv.DictReader(f, delimiter=";")
arraydicts_paper = []
array_fechas_paper = []
arraykeys_paper = []
for row in reader:
    fecha = datetime.strptime(row['Fecha'], '%d/%m/%Y %H:%M:%S')
    arraydicts_paper.append(row)
    fecha_sinhoras = datetime.strftime(fecha, '%d/%m/%Y')
    key = [row['Vehiculo'], fecha_sinhoras]
    if key not in arraykeys_paper:
        arraykeys_paper.append(key)
    array_fechas_paper.append(fecha)


dict_fechaspordia_paper = {}
for k in arraykeys_paper:
    arrayfechas = []
    for row in arraydicts_paper:

        fecha = datetime.strptime(row['Fecha'], '%d/%m/%Y %H:%M:%S')
        fecha_sinhoras = datetime.strftime(fecha, '%d/%m/%Y')
        if fecha_sinhoras == k[1] and k[0] == row['Vehiculo']:
            arrayfechas.append(fecha)

    dict_fechaspordia_paper[(k[0], k[1])] = arrayfechas

for k in arraykeys_paper:
    entrada = {}
    entrada['id'] = k[0] + ":" + k[1]
    entrada['type'] = 'Route'
    entrada['arrivalPoint'] = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': []
        }
    }
    entrada['departurePoint'] = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': []
        }
    }
    entrada["description"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }
    entrada["longName"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }
    maxfecha = datetime.strftime((max(dict_fechaspordia_paper[(k[0], k[1])])), "%Y-%m-%dT%H:%M:%S+00:00")
    minfecha = datetime.strftime((min(dict_fechaspordia_paper[(k[0], k[1])])), "%Y-%m-%dT%H:%M:%S+00:00")
    arrayStops = []
    for n in arraydicts_paper:
        fecha_parsed = datetime.strptime(n['Fecha'], '%d/%m/%Y %H:%M:%S')
        if n['Vehiculo'] == k[0] and fecha_parsed in dict_fechaspordia_paper[(k[0], k[1])]:
            arrayStops.append({
                "refStop": ("DepositPoint:%s" % n['Tag']),
                "stopPoint": {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [

                        ]
                    }
                },
                "arrivalTimestamp": datetime.strftime(fecha_parsed, "%Y-%m-%dT%H:%M:%S+00:00"),
                "departureTimestamp": ""
            })

    entrada["realArrivalTimestamp"] = {
        "type": "String",
        "value": maxfecha,
        "metadata": {}
    }
    entrada["realDepartureTimestamp"] = {
        "type": "String",
        "value": minfecha,
        "metadata": {}
    }
    entrada['realPath'] = {
        "type": "List",
        "value": [],
        "metadata": {}
    }

    entrada['realStops'] = {
        "type": "List",
        "value": arrayStops,
        "metadata": {}
    }
    entrada['refAssignedVehicle'] = {
        "type": "String",
        "value": ("Vehicle:%s" % k[0]),
        "metadata": {}
    }
    entrada['refScheduledVehicle'] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }
    entrada["scheduledArrivalTimestamp"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }
    entrada["scheduledDepartureTimestamp"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }
    entrada["scheduledPath"] = {
        "type": "List",
        "value": [],
        "metadata": {}
    }
    entrada["scheduledStops"] = {
        "type": "List",
        "value": [],
        "metadata": {}
    }
    entrada["shortName"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }

    entrada["vehicleType"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }

    fechasinbarras_datetime = datetime.strptime(k[1], "%d/%m/%Y")
    fechasinbarras = datetime.strftime(fechasinbarras_datetime, "%d%m%Y")
    paperjson = ("C:/Users/Usuario/PycharmProjects/Sensores/rutasCamiones/rutasMatricula/paper/%s%s.json" % (
        k[0], fechasinbarras))
    with open(paperjson, 'w', encoding="UTF-8") as outfile:
        outfile.write(json.dumps(entrada, sort_keys=False, indent=4, ensure_ascii=False))




f = open(residual2018, 'rU')
reader = csv.DictReader(f, delimiter=";")
arraydicts_res = []
arraykeys_res = []
array_fechas_res = []
for row in reader:
    fecha = datetime.strptime(row['Fecha'], '%d/%m/%Y %H:%M:%S')
    fecha_sinhoras = datetime.strftime(fecha, '%d/%m/%Y')
    key = [row['Vehiculo'], fecha_sinhoras]
    if key not in arraykeys_res:
        arraykeys_res.append(key)
    arraydicts_res.append(row)
    array_fechas_res.append(fecha)

dict_fechaspordia_res = {}
for k in arraykeys_res:
    arrayfechas = []
    for row in arraydicts_res:

        fecha = datetime.strptime(row['Fecha'], '%d/%m/%Y %H:%M:%S')
        fecha_sinhoras = datetime.strftime(fecha, '%d/%m/%Y')
        if fecha_sinhoras == k[1] and k[0] == row['Vehiculo']:
            arrayfechas.append(fecha)

    dict_fechaspordia_res[(k[0], k[1])] = arrayfechas

for k in arraykeys_res:
    entrada = {}
    entrada['id'] = k[0] + ":" + k[1]
    entrada['type'] = 'Route'
    entrada['arrivalPoint'] = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': []
        }
    }
    entrada['departurePoint'] = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': []
        }
    }
    entrada["description"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }
    entrada["longName"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }
    maxfecha = datetime.strftime((max(dict_fechaspordia_res[(k[0], k[1])])), "%Y-%m-%dT%H:%M:%S+00:00")
    minfecha = datetime.strftime((min(dict_fechaspordia_res[(k[0], k[1])])), "%Y-%m-%dT%H:%M:%S+00:00")
    arrayStops = []
    for n in arraydicts_res:
        fecha_parsed = datetime.strptime(n['Fecha'], '%d/%m/%Y %H:%M:%S')
        if n['Vehiculo'] == k[0] and fecha_parsed in dict_fechaspordia_res[(k[0], k[1])]:
            arrayStops.append({
                "refStop": ("DepositPoint:%s" % n['Tag']),
                "stopPoint": {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [

                        ]
                    }
                },
                "arrivalTimestamp": datetime.strftime(fecha_parsed, "%Y-%m-%dT%H:%M:%S+00:00"),
                "departureTimestamp": ""
            })

    entrada["realArrivalTimestamp"] = {
        "type": "String",
        "value": maxfecha,
        "metadata": {}
    }
    entrada["realDepartureTimestamp"] = {
        "type": "String",
        "value": minfecha,
        "metadata": {}
    }
    entrada['realPath'] = {
        "type": "List",
        "value": [],
        "metadata": {}
    }

    entrada['realStops'] = {
        "type": "List",
        "value": arrayStops,
        "metadata": {}
    }
    entrada['refAssignedVehicle'] = {
        "type": "String",
        "value": ("Vehicle:%s" % k[0]),
        "metadata": {}
    }
    entrada['refScheduledVehicle'] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }
    entrada["scheduledArrivalTimestamp"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }
    entrada["scheduledDepartureTimestamp"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }
    entrada["scheduledPath"] = {
        "type": "List",
        "value": [],
        "metadata": {}
    }
    entrada["scheduledStops"] = {
        "type": "List",
        "value": [],
        "metadata": {}
    }
    entrada["shortName"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }

    entrada["vehicleType"] = {
        "type": "String",
        "value": "",
        "metadata": {}
    }

    fechasinbarras_datetime = datetime.strptime(k[1], "%d/%m/%Y")
    fechasinbarras = datetime.strftime(fechasinbarras_datetime, "%d%m%Y")
    resjson = ("C:/Users/Usuario/PycharmProjects/Sensores/rutasCamiones/rutasMatricula/residual/%s%s.json" % (
        k[0], fechasinbarras))
    with open(resjson, 'w', encoding="UTF-8") as outfile:
        outfile.write(json.dumps(entrada, sort_keys=False, indent=4, ensure_ascii=False))
