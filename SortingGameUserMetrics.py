import csv
import json
import sys

#filename = sys.argv[1]
filename_local = "c:/users/usuario/downloads/sortingameusermetrics.json"
with open(filename, "r") as myfile: #CAMBIAR OPCIONALMENTE filename POR filename_local Y ASIGNAR EL NOMBRE DEL ARCHIVO LOCAL A ESA VARIABLE
    data = myfile.read().replace('\n','')
    metrics_parsed = json.loads(data)

    print(metrics_parsed)

# data_items_id = ""
# for element in metrics_parsed:
#     try:
#         print(str(element['latestLevelResult']))
#         data_items_id+=str(element['latestLevelResult'])
#     except:
#         print("Fila no procesada")
#
# print(data_items_id)
# try:
#     items_json = json.loads(data_items_id)
# except:
#     print("json no procesado")


metrics_data_id = metrics_parsed
csv_file = open("metrics.csv", "w", newline='')
csvwriter = csv.writer(csv_file, delimiter=";")
count = 0

for metric in metrics_data_id:
    if count==0:
        header = metric.keys()
        # print(header)
        array = ['id','type','age','countryISO','allTimeLevelsPlayed','currentMaxLevel','currentTotalPoints','gender','latestLevelPlayed','municipalityName','latestLevelResult']
        csvwriter.writerow(array)
        count += 1
    else:

        try:
            array_valores = []
            # print(array.__len__())
            for i in range(0, array.__len__()):
                if array[i] not in metric:
                    array_valores.append('')
                else:
                    array_valores.append(metric[array[i]])

            csvwriter.writerow(array_valores)

        except:
            print("Fila no introducida.")



csv_file.close()

#print(metrics_data_id)
