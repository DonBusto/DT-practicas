import csv
import json
import requests

from collections import defaultdict
import sys

# filename = sys.argv[1]

filename_metrics_json = "c:/users/usuario/downloads/sortingameusermetrics.json"
filename_metrics_csv = "metrics.csv"
filename_questionnaire_csv = "questionnaire.csv"
dict_metrics = defaultdict(list)
dict_mixed = defaultdict(list)

with open(filename_metrics_json,
          "r") as jsonfile:  # CAMBIAR OPCIONALMENTE filename POR filename_local Y ASIGNAR EL NOMBRE DEL ARCHIVO LOCAL A ESA VARIABLE
    data = jsonfile.read().replace('\n', '')
    metrics_parsed = json.loads(data)
    print(metrics_parsed)



metrics_data_id = metrics_parsed
csv_file = open(filename_metrics_csv, "w", newline='')
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

ids = []
for metric in metrics_data_id:
    if count == 0:
        # print(header)
        csvwriter.writerow(array_attr)
        count += 1
    else:

        try:
            ids.append(metric[array_attr[0]])
            array_valores = []
            # print(array.__len__())
            for i in range(0, array_attr.__len__()):
                if array_attr[i] not in metric:
                    array_valores.append('')
                else:
                    array_valores.append(metric[array_attr[i]])

            dict_metrics[array_valores[0]].append({
                array_attr[x]: array_valores[x] for x in range(0, len(array_valores))
            })
            csvwriter.writerow(array_valores)

        except:
            print("Fila no introducida.")
csv_file.close()
dict_quest = defaultdict(list)
filename_questionnaire = "c:/users/usuario/downloads/sortinggameuserquestionnaire.json"
with open(filename_questionnaire,
          "r") as myfile:
    data = myfile.read().replace('\n', '')
    questionnaire_parsed = json.loads(data)

questionnaire_data_id = questionnaire_parsed

csv_file = open("questionnaire.csv", "w", newline='')
csvwriter = csv.writer(csv_file, delimiter=";")
count = 0
array_attr_quest = []

count_first = 0
for question in questionnaire_data_id:
    if count_first == 0:
        header = question.keys()
        for element in header:
            array_attr_quest.append(element)
        #   array_attr.append(element)
        count_first += 1
    else:
        header = question.keys()
        for element in header:
            if element not in array_attr_quest:
                array_attr_quest.append(element)
                # array_attr.append(element)
        count_first += 1

for question in questionnaire_data_id:
    if count == 0:
        # print(header)
        csvwriter.writerow(array_attr_quest)
        count += 1
    else:

        try:
            ids.append(question[array_attr_quest[0]])
            array_valores_quest = []
            # print(array.__len__())
            for i in range(0, array_attr_quest.__len__()):
                if array_attr_quest[i] not in question:
                    array_valores_quest.append('')
                else:
                    array_valores_quest.append(question[array_attr_quest[i]])
            dict_quest[array_valores_quest[0]].append({
                array_attr_quest[x]: array_valores_quest[x] for x in range(0, len(array_valores_quest))
            })
            csvwriter.writerow(array_valores_quest)

        except:
            print("Fila no introducida.")

csv_file.close()

array_attr_global = []
for n in array_attr:
    array_attr_global.append(n)
for n in array_attr_quest:
    array_attr_global.append(n)

dict_mixed = dict(dict_metrics)

for element in dict_mixed.keys():
    dict_mixed[element].append(dict_quest[element])

# with open("metrics_mixed.csv", 'wb') as csv_file:
#     w = csv.DictWriter(csv_file, dict_quest.keys())
#     w.writeheader()
#     w.writerow(dict_quest)
# for element in dict_metrics.keys():
#     if element in dict_quest.keys():
#         csvwriter.writerow(element[x for x in range (0, len(array_attr))])
#     else:
#         print("error")

jsonexportado = 'json_total_quest.json'

with open('pruebametrics.json', 'w', encoding="UTF-8") as outfile:
    outfile.write(json.dumps(dict_metrics, sort_keys=True, indent=4, ensure_ascii=False))

with open('prueba_quest.json', 'w', encoding="UTF-8") as outfile:
    outfile.write(json.dumps(dict_quest, sort_keys=True, indent=4, ensure_ascii=False))

with open(jsonexportado, 'w', encoding="UTF-8") as outfile:
    outfile.write(json.dumps(dict_mixed, sort_keys=True, indent=4, ensure_ascii=False))

with open(jsonexportado,
          "r") as jsonfile:  # CAMBIAR OPCIONALMENTE filename POR filename_local Y ASIGNAR EL NOMBRE DEL ARCHIVO LOCAL A ESA VARIABLE
    data = jsonfile.read().replace('\n', '')
    mixed_parsed = json.loads(data)
    print(mixed_parsed)

filename_mixed_csv = 'metrics_mixed.csv'

mixed_data_id = mixed_parsed
csv_file = open(filename_mixed_csv, "w", newline='')
csvwriter = csv.writer(csv_file, delimiter=";")
count = 0
array_attr = []
count_first = 0
for element in mixed_data_id:
    if count_first == 0:
        header = element.keys()
        for element in header:
            array_attr.append(element)
        count_first += 1
    else:
        header = element.keys()
        for element in header:
            if element not in array_attr:
                array_attr.append(element)
        count_first += 1

ids = []
for element in mixed_data_id:
    if count == 0:
        # print(header)
        csvwriter.writerow(array_attr)
        count += 1
    else:

        try:
            ids.append(element[array_attr[0]])
            array_valores = []
            # print(array.__len__())
            for i in range(0, array_attr.__len__()):
                if array_attr[i] not in element:
                    array_valores.append('')
                else:
                    array_valores.append(element[array_attr[i]])
            csvwriter.writerow(array_valores)

        except:
            print("Fila no introducida.")
csv_file.close()