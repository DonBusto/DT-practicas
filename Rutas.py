import json
import csv
from collections import defaultdict

orig_filename = 'routes.json'
dict_routes = defaultdict(list)
routes = {}
with open(orig_filename,
          "r") as jsonfile:
    data = jsonfile.read().replace('\n', '')
    routes = json.loads(data)
    print(routes)

metrics_data_id = routes
csv_file = open("sampleroutes.csv", "w", newline='')
csvwriter = csv.writer(csv_file, delimiter=";")
count = 0
array_attr = []
count_first = 0
for metric in metrics_data_id:
    if count_first == 0:
        header = metric.keys()
        for element in header:
            array_attr.append(element)
        count_first += 1
    else:
        header = metric.keys()
        for element in header:
            if element not in array_attr:
                array_attr.append(element)
        count_first += 1
# print(array_attr)
count_items = 0
for metric in metrics_data_id:
    if count == 0:
        # print(header)
        csvwriter.writerow(array_attr)
        count += 1
    else:
        try:
            salida_dict = {}
            array_valores = []
            # print(array.__len__())
            for i in range(0, array_attr.__len__()):
                if array_attr[i] not in metric:
                    array_valores.append('')
                else:
                    array_valores.append(metric[array_attr[i]])
            #dict_routes[array_valores[0]].append({
            salida_dict.update({

                "id": routes[count_items]['id'],
                "type": array_valores[1],
                "arrivalPoint": {
                    'type': "StructuredValue",
                    "value": {
                        "type" : "Feature",
                        'geometry': {
                            'type': routes[count_items]['arrivalPoint']['type'],
                            'coordinates': [routes[count_items]['arrivalPoint']['coordinates'][1],
                                            routes[count_items]['arrivalPoint']['coordinates'][0]]

                        }
                    },
                    "metadata": {}
                },
                "departurePoint": {
                    'type': "StructuredValue",
                    "value": {
                        "type" : "Feature",
                        'geometry': {
                            'type': routes[count_items]['departurePoint']['geometry']['type'],
                            'coordinates': [routes[count_items]['departurePoint']['geometry']['coordinates'][1],
                                            routes[count_items]['departurePoint']['geometry']['coordinates'][0]]

                        }
                    },
                    "metadata": {}
                },
                "description": {
                    "type": "String",
                    "value": routes[count_items]['description'],
                    "metadata": {}
                },
                "longName": {
                    "type": "String",
                    "value": routes[count_items]['longName'],
                    "metadata": {}
                },
                "realArrivalTimestamp": {
                    "type": "String",
                    "value": routes[count_items]['realArrivalTimestamp'],
                    "metadata": {}
                },
                "realDepartureTimestamp": {
                    "type": "String",
                    "value": routes[count_items]['realDepartureTimestamp'],
                    "metadata": {}
                },
                "realPath": {
                    "type": "List",
                    "value": routes[count_items]['realPath'],
                    "metadata": {}
                },
                "realStops": {
                    "type": "List",
                    "value": routes[count_items]['realStops'],
                    "metadata": {}
                },
                "refAssignedVehicle": {
                    "type": "String",
                    "value": "Vehicle:" + routes[count_items]['refAssignedVehicle'],
                    "metadata": {}
                },
                "refScheduledVehicle": {
                    "type": "String",
                    "value": "Vehicle:" + routes[count_items]['refScheduledVehicle'],
                    "metadata": {}
                },
                "scheduledArrivalTimestamp": {
                    "type": "String",
                    "value": routes[count_items]['scheduledArrivalTimestamp'],
                    "metadata": {}
                },
                "scheduledDepartureTimestamp": {
                    "type": "String",
                    "value": routes[count_items]['scheduledDepartureTimestamp'],
                    "metadata": {}
                },
                "scheduledPath": {
                    "type": "List",
                    "value": routes[count_items]['scheduledPath'],
                    "metadata": {}
                },
                "scheduledStops": {
                    "type": "List",
                    "value": routes[count_items]['scheduledStops'],
                    "metadata": {}
                },
                "shortName": {
                    "type": "String",
                    "value": routes[count_items]['shortName'],
                    "metadata": {}
                },
                "vehicleType": {
                    "type": "String",
                    "value": routes[count_items]['vehicleType'],
                    "metadata": {}
                }

            })
            csvwriter.writerow(array_valores)

            print(count_items)
            salida_filename = ("%s.json" % routes[count_items]['id'])
            with open(salida_filename, 'w', encoding="UTF-8") as outfile:
                outfile.write(json.dumps(salida_dict, sort_keys=False, indent=4, ensure_ascii=False))
            count_items += 1
        except:
            print("Fila no introducida.")
            count_items += 1

csv_file.close()

with open('pruebadict.json', 'w', encoding="UTF-8") as outfile:
    outfile.write(json.dumps(routes, sort_keys=True, indent=4, ensure_ascii=False))

with open('dictroutes_official.json', 'w', encoding="UTF-8") as outfile:
    outfile.write(json.dumps(dict_routes, sort_keys=False, indent=4, ensure_ascii=False))
