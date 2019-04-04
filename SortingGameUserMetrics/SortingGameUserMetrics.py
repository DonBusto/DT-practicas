import csv
import json
import sys

filename = sys.argv[1]
filename_local = "c:/users/usuario/downloads/sortingameusermetrics.json"
with open(filename, "r") as myfile: #CAMBIAR OPCIONALMENTE filename POR filename_local Y ASIGNAR EL NOMBRE DEL ARCHIVO LOCAL A ESA VARIABLE
    data = myfile.read().replace('\n','')
    metrics_parsed = json.loads(data)

    print(metrics_parsed)

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

print(array_attr)



for metric in metrics_data_id:
    if count==0:
        # print(header)
        csvwriter.writerow(array_attr)
        count += 1
    else:

        try:
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

#print(metrics_data_id)
