import csv
import json
from collections import defaultdict
import sys

# filename = sys.argv[1]

filename_metrics = "c:/users/usuario/downloads/sortingameusermetrics.json"
with open(filename_metrics,
          "r") as myfile:  # CAMBIAR OPCIONALMENTE filename POR filename_local Y ASIGNAR EL NOMBRE DEL ARCHIVO LOCAL A ESA VARIABLE
    data = myfile.read().replace('\n', '')
    metrics_parsed = json.loads(data)

metrics_data_id = metrics_parsed
csv_file = open("metrics.csv", "w", newline='')
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

            csvwriter.writerow(array_valores)

        except:
            print("Fila no introducida.")
csv_file.close()

filename_questionnaire = "c:/users/usuario/downloads/sortinggameuserquestionnaire.json"
with open(filename_questionnaire,
          "r") as myfile:  # CAMBIAR OPCIONALMENTE filename POR filename_local Y ASIGNAR EL NOMBRE DEL ARCHIVO LOCAL A ESA VARIABLE
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
            array_valores = []
            # print(array.__len__())
            for i in range(0, array_attr_quest.__len__()):
                if array_attr_quest[i] not in question:
                    array_valores.append('')
                else:
                    array_valores.append(question[array_attr_quest[i]])

            csvwriter.writerow(array_valores)

        except:
            print("Fila no introducida.")

csv_file.close()

csv_file_metrics = open("metrics.csv", "r", newline='')

csv_file_mixed = open("metrics_mixed.csv", "w", newline='')
line_mixed = 0
d_metrics = defaultdict(list)
print(array_attr)
for line in csv_file_metrics:
    csv_file_questionnaire = open("questionnaire.csv", "r", newline='')
    str_linea_fichero = ""
    metrics_linea_array = line.split(";")
    id_analizar = metrics_linea_array[0]
    metrics_linea_array[metrics_linea_array.__len__() - 1] = metrics_linea_array[metrics_linea_array.__len__() - 1].rstrip('\r\n')
    print(metrics_linea_array)

    if line_mixed == 0:
        for attr in array_attr:
            csv_file_mixed.write(attr)
            csv_file_mixed.write(";")
        for attr_quest in array_attr_quest:
            if attr_quest not in array_attr:
                csv_file_mixed.write(attr_quest)
                csv_file_mixed.write(";")
       # csv_file_mixed.write("\n") salto de linea para atributos
        line_mixed += 1
    else:
        str_linea_fichero += line
    for line_quest in csv_file_questionnaire:
        lista_atributos_quest = line_quest.split(";")
        lista_atributos_quest[lista_atributos_quest.__len__()-1] = lista_atributos_quest[lista_atributos_quest.__len__()-1].rstrip('\r\n')
        if lista_atributos_quest[0] == id_analizar and lista_atributos_quest[0] != array_attr[0]:
            line_quest_array = line_quest.split(";")
            str_vacio_quest = ""
            for n in range(2, line_quest_array.__len__()-2):
                str_vacio_quest += line_quest_array[n] + ";"
            str_vacio_quest += line_quest_array[line_quest_array.__len__()-1]

            str_linea_fichero += str_vacio_quest
    str_linea_fichero_array = str_linea_fichero.split(";")

    str_linea_fichero = str_linea_fichero.rstrip("\n")
    if str_linea_fichero.endswith("\n"):
        csv_file_mixed.write(str_linea_fichero + "\n")
    else:
        csv_file_mixed.write(str_linea_fichero)
    csv_file_questionnaire.close()

csv_file_metrics.close()
csv_file_mixed.close()

