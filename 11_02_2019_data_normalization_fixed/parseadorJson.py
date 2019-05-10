import csv
import json
from datetime import datetime
from collections import defaultdict

dpv5 = "C:/Users/Usuario/PycharmProjects/Sensores/11_02_2019_data_normalization_fixed/11_02_2019_data_normalization_fixed/Zamudio_Deposit_Point_v5.csv"
dptv4 = "C:/Users/Usuario/PycharmProjects/Sensores/11_02_2019_data_normalization_fixed/11_02_2019_data_normalization_fixed/Zamudio_Deposit_PointType_v4.csv"
stv4 = "C:/Users/Usuario/PycharmProjects/Sensores/11_02_2019_data_normalization_fixed/11_02_2019_data_normalization_fixed/Zamudio_SortingType_v4.csv"
v3 = "C:/Users/Usuario/PycharmProjects/Sensores/11_02_2019_data_normalization_fixed/11_02_2019_data_normalization_fixed/Zamudio_Vehicle_v3.csv"
vtv3 = "C:/Users/Usuario/PycharmProjects/Sensores/11_02_2019_data_normalization_fixed/11_02_2019_data_normalization_fixed/Zamudio_VehicleType_v3.csv"

dpv5json = "C:/Users/Usuario/PycharmProjects/Sensores/11_02_2019_data_normalization_fixed/11_02_2019_data_normalization_fixed/Zamudio_Deposit_Point_v5.json"
dptv4json = "C:/Users/Usuario/PycharmProjects/Sensores/11_02_2019_data_normalization_fixed/11_02_2019_data_normalization_fixed/Zamudio_Deposit_PointType_v4.json"
stv4json = "C:/Users/Usuario/PycharmProjects/Sensores/11_02_2019_data_normalization_fixed/11_02_2019_data_normalization_fixed/Zamudio_SortingType_v4.json"
v3json = "C:/Users/Usuario/PycharmProjects/Sensores/11_02_2019_data_normalization_fixed/11_02_2019_data_normalization_fixed/Zamudio_Vehicle_v3.json"
vtv3json = "C:/Users/Usuario/PycharmProjects/Sensores/11_02_2019_data_normalization_fixed/11_02_2019_data_normalization_fixed/Zamudio_VehicleType_v3.json"


arrayFiles = [dpv5, dptv4, stv4, v3, vtv3]
jsonArray = [dpv5json, dptv4json, stv4json, v3json, vtv3json]

i = 0
for filename in arrayFiles:
    f = open(filename, 'rU', encoding='UTF-8-sig')
    reader = csv.DictReader(f, delimiter=";")

    with open(jsonArray[i], 'w', encoding="UTF-8") as outfile:
        for row in reader:
            if i==2 or i==4 or i == 1:
                row['id'] = int(row['id'])
                if i==4:
                    row['numberOfAxes'] = int(row['numberOfAxes'])
                print(row)

            outfile.write(json.dumps(row, sort_keys=False, indent=4, ensure_ascii=True))
    i+=1