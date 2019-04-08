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
#
# metrics_data_id = routes
# csv_file = open("sampleroutes.csv", "w", newline='')
# csvwriter = csv.writer(csv_file, delimiter=";")
# count = 0
# array_attr = []
# count_first = 0
# for metric in metrics_data_id:
#     if count_first == 0:
#         header = metric.keys()
#         for element in header:
#             array_attr.append(element)
#         count_first += 1
#     else:
#         header = metric.keys()
#         for element in header:
#             if element not in array_attr:
#                 array_attr.append(element)
#         count_first += 1
# # print(array_attr)
# count_items = 0

final_template = {}

for route in routes:
    final_template['id'] = route['id']
    final_template['type'] = route['type']
    final_template['arrivalPoint'] = {'type': 'StructuredValue', 'value': {}, 'metadata': {}}
    coords = route['arrivalPoint']['coordinates']
    final_template['departurePoint'] = {'type': 'StructuredValue', 'value': {}, 'metadata': {}}
    final_template['arrivalPoint']['value'] = {'type': 'Feature',
                                               'geometry': {'type': 'Point', 'coordinates': [coords[1], coords[0]]}}
    coords_dep = route['departurePoint']['geometry']['coordinates']
    final_template['departurePoint']['value'] = {'type': 'Feature',
                                                 'geometry': {'type': 'Point',
                                                              'coordinates': [coords_dep[1], coords_dep[0]]}}
    final_template['description'] = {'type': 'String', 'value': route['description'], 'metadata': {}}
    final_template['longName'] = {'type': 'String', 'value': route['longName'], 'metadata': {}}
    final_template['realArrivalTimestamp'] = {'type': 'String', 'value': route['realArrivalTimestamp'], 'metadata': {}}
    final_template['realDepartureTimestamp'] = {'type': 'String', 'value': route['realDepartureTimestamp'],
                                                'metadata': {}}
    final_template['realPath'] = {'type': 'List', 'value': route['realPath'], 'metadata': {}}

    array_realstops_values = []
    array_realstops = route['realStops']

    # final_template['realStops']['value'] =
    for i in range(0, len(array_realstops)):
        arrayCoords = route['realStops'][i]['stopPoint']['value']['geometry']['coordinates']
        if route['realStops'][i]['refStop'] != "":
            array_realstops_values.append({
                'refStop': ('DepositPoint:%s' % route['realStops'][i]['refStop']),  # dejar vacio si no hay refstop
                'stopPoint': {
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [arrayCoords[1], arrayCoords[0]]
                    }
                },
                'arrivalTimestamp': route['realStops'][i]['realArrivalTimestamp'],
                # sustituir scheduled por real????
                'departureTimestamp': route['realStops'][i]['scheduledArrivalTimestamp']
            })
        else:
            array_realstops_values.append({
                'refStop': '',  # dejar vacio si no hay refstop
                'stopPoint': {
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [arrayCoords[1], arrayCoords[0]]
                    }
                },
                'arrivalTimestamp': route['realStops'][i]['realArrivalTimestamp'],
                # sustituir scheduled por real????
                'departureTimestamp': route['realStops'][i]['scheduledArrivalTimestamp']})

    final_template['realStops'] = {'type': 'List', 'value': array_realstops_values, 'metadata': {}}
    if route['refAssignedVehicle'] != '':
        final_template['refAssignedVehicle'] = {'type': 'String', 'value': ('Vehicle:%s' % route['refAssignedVehicle']),
                                                'metadata': {}}
    else:
        final_template['refAssignedVehicle'] = {'type': 'String', 'value': '', 'metadata': {}}
    if route['refScheduledVehicle'] != '':
        final_template['refScheduledVehicle'] = {'type': 'String',
                                                 'value': ('Vehicle:%s' % route['refScheduledVehicle']), 'metadata': {}}
    else:
        final_template['refScheduledVehicle'] = {'type': 'String', 'value': '', 'metadata': {}}
    # final_template['refScheduledVehicle'] = {'type':'String','value':('Vehicle:%s' % route['refScheduledVehicle']),'metadata':{}}
    final_template['scheduledArrivalTimestamp'] = {'type': 'String', 'value': route['scheduledArrivalTimestamp'],
                                                   'metadata': {}}
    final_template['scheduledDepartureTimestamp'] = {'type': 'String', 'value': route['scheduledDepartureTimestamp'],
                                                     'metadata': {}}
    final_template['scheduledPath'] = {'type': 'List', 'value': [], 'metadata': {}}
    # faltan scheduledStops

    array_scheduledStops_values = []
    array_scheduledStops = route['scheduledStops']

    # final_template['scheduledStops']['value'] =
    for i in range(0, len(array_scheduledStops)):
        arrayCoords = route['scheduledStops'][i]['stopPoint']['value']['geometry']['coordinates']
        if route['scheduledStops'][i]['refStop'] != "":
            array_scheduledStops_values.append({
                'refStop': ('DepositPoint:%s' % route['scheduledStops'][i]['refStop']),  # dejar vacio si no hay refstop
                'stopPoint': {
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [arrayCoords[1], arrayCoords[0]]
                    }
                },

            })
        else:
            array_scheduledStops_values.append({
                'refStop': '',  # dejar vacio si no hay refstop
                'stopPoint': {
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [arrayCoords[1], arrayCoords[0]]
                    }
                }})
    final_template['scheduledStops'] = {'type': 'List', 'value': array_scheduledStops_values, 'metadata': {}}

    final_template['shortName'] = {'type': 'String', 'value': route['shortName'], 'metadata': {}}
    final_template['vehicleType'] = {'type': 'String', 'value': route['vehicleType'], 'metadata': {}}
    salida_filename = ("%s.json" % route['id'])
    with open(salida_filename, 'w', encoding="UTF-8") as outfile:
        outfile.write(json.dumps(final_template, sort_keys=False, indent=4, ensure_ascii=False))

# for metric in metrics_data_id:
#     if count == 0:
#         # print(header)
#         csvwriter.writerow(array_attr)
#         count += 1
#     else:
#         try:
#             salida_dict = {}
#             array_valores = []
#             # print(array.__len__())
#             for i in range(0, array_attr.__len__()):
#                 if array_attr[i] not in metric:
#                     array_valores.append('')
#                 else:
#                     array_valores.append(metric[array_attr[i]])
#             #dict_routes[array_valores[0]].append({
#             string_realstops = str(routes[count_items]['realStops'])
#             string_realstops = string_realstops.replace('scheduledArrivalTimestamp', 'arrivalTimestamp')
#             string_realstops = string_realstops.replace('realArrivalTimestamp', 'departureTimestamp')
#             string_realstops = string_realstops.replace("\'", '\"')
#             dict_realstops = json.loads(string_realstops)
#
#
#
#             salida_dict.update({
#
#                 "id": routes[count_items]['id'],
#                 "type": array_valores[1],
#                 "arrivalPoint": {
#                     'type': "StructuredValue",
#                     "value": {
#                         "type" : "Feature",
#                         'geometry': {
#                             'type': routes[count_items]['arrivalPoint']['type'],
#                             'coordinates': [routes[count_items]['arrivalPoint']['coordinates'][1],
#                                             routes[count_items]['arrivalPoint']['coordinates'][0]]
#
#                         }
#                     },
#                     "metadata": {}
#                 },
#                 "departurePoint": {
#                     'type': "StructuredValue",
#                     "value": {
#                         "type" : "Feature",
#                         'geometry': {
#                             'type': routes[count_items]['departurePoint']['geometry']['type'],
#                             'coordinates': [routes[count_items]['departurePoint']['geometry']['coordinates'][1],
#                                             routes[count_items]['departurePoint']['geometry']['coordinates'][0]]
#
#                         }
#                     },
#                     "metadata": {}
#                 },
#                 "description": {
#                     "type": "String",
#                     "value": routes[count_items]['description'],
#                     "metadata": {}
#                 },
#                 "longName": {
#                     "type": "String",
#                     "value": routes[count_items]['longName'],
#                     "metadata": {}
#                 },
#                 "realArrivalTimestamp": {
#                     "type": "String",
#                     "value": routes[count_items]['realArrivalTimestamp'],
#                     "metadata": {}
#                 },
#                 "realDepartureTimestamp": {
#                     "type": "String",
#                     "value": routes[count_items]['realDepartureTimestamp'],
#                     "metadata": {}
#                 },
#                 "realPath": {
#                     "type": "List",
#                     "value": routes[count_items]['realPath'],
#                     "metadata": {}
#                 },
#                 "realStops": {
#                     "type": "List",
#                     "value2": dict_realstops,
#
#                     "value" : {
#                         "arrivalTimestamp" : dict_realstops[0]['arrivalTimestamp'],
#                         "departureTimestamp": dict_realstops[0]['departureTimestamp'],
#                         "refStop": dict_realstops[0]['refStop'],
#                         "stopPoint": {}
#
#             },
#                     "metadata": {}
#                 },
#                 "refAssignedVehicle": {
#                     "type": "String",
#                     "value": "Vehicle:" + routes[count_items]['refAssignedVehicle'],
#                     "metadata": {}
#                 },
#                 "refScheduledVehicle": {
#                     "type": "String",
#                     "value": "Vehicle:" + routes[count_items]['refScheduledVehicle'],
#                     "metadata": {}
#                 },
#                 "scheduledArrivalTimestamp": {
#                     "type": "String",
#                     "value": routes[count_items]['scheduledArrivalTimestamp'],
#                     "metadata": {}
#                 },
#                 "scheduledDepartureTimestamp": {
#                     "type": "String",
#                     "value": routes[count_items]['scheduledDepartureTimestamp'],
#                     "metadata": {}
#                 },
#                 "scheduledPath": {
#                     "type": "List",
#                     "value": routes[count_items]['scheduledPath'],
#                     "metadata": {}
#                 },
#                 "scheduledStops": {
#                     "type": "List",
#                     "value": routes[count_items]['scheduledStops'],
#                     "metadata": {}
#                 },
#                 "shortName": {
#                     "type": "String",
#                     "value": routes[count_items]['shortName'],
#                     "metadata": {}
#                 },
#                 "vehicleType": {
#                     "type": "String",
#                     "value": routes[count_items]['vehicleType'],
#                     "metadata": {}
#                 }
#
#             })
#             csvwriter.writerow(array_valores)
#
#             print(count_items)
#             salida_filename = ("%s.json" % routes[count_items]['id'])
#             with open(salida_filename, 'w', encoding="UTF-8") as outfile:
#                 outfile.write(json.dumps(salida_dict, sort_keys=False, indent=4, ensure_ascii=False))
#             count_items += 1
#         except:
#             print("Fila no introducida.")
#             count_items += 1
#
# csv_file.close()
#
# with open('pruebadict.json', 'w', encoding="UTF-8") as outfile:
#     outfile.write(json.dumps(routes, sort_keys=True, indent=4, ensure_ascii=False))
#
# with open('realstops.json', 'w', encoding="UTF-8") as outfile:
#     outfile.write(json.dumps(dict_realstops, sort_keys=True, indent=4, ensure_ascii=False))
#
# with open('dictroutes_official.json', 'w', encoding="UTF-8") as outfile:
#     outfile.write(json.dumps(dict_routes, sort_keys=False, indent=4, ensure_ascii=False))
