import csv
from collections import defaultdict

zamudio_deposit_point = "Zamudio_Deposit_Point_v5.csv"
dicts_depositpoint = {}
with open(zamudio_deposit_point, mode='r', encoding="UTF-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            dicts_depositpoint.update({
                row[0]: row[4]
            })
print(dicts_depositpoint)

filename = "residuos_tags_pdc_lecturas_RESTO_2018.csv"
array_attr = []
diccionario_excel = []
diccionario_prueba = {}
with open(filename, mode='r', encoding="UTF-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            array_attr = row
            array_attr[len(array_attr) - 1] = 'refSortingType'
            print(f'Column names are {", ".join(row)}')
            line_count += 1

        else:
            if row[3] in dicts_depositpoint.keys():
                diccionario_excel.append({
                #diccionario_prueba[row[3]] = {
                    'Id': row[0],
                    'Vehiculo': row[1],
                    'Fecha': row[2],
                    'Tag': row[3],
                    'Tipo Residuo': row[4],
                    'Tipo Contenedor': row[5],
                    'Frecuencia RSU': row[6],
                    'Municipio': row[7],
                    'Poligono': row[8],
                    'Ruta': row[9],
                    'Peso': row[10],
                    'refSortingType': dicts_depositpoint[row[3]]
                })
            else:
               diccionario_excel.append({
               #diccionario_prueba[row[3]] = {
                    'Id': row[0],
                    'Vehiculo': row[1],
                    'Fecha': row[2],
                    'Tag': row[3],
                    'Tipo Residuo': row[4],
                    'Tipo Contenedor': row[5],
                    'Frecuencia RSU': row[6],
                    'Municipio': row[7],
                    'Poligono': row[8],
                    'Ruta': row[9],
                    'Peso': row[10],
                    'refSortingType': ''
                })


print(diccionario_prueba)

print(array_attr)

with open(("%s_ACTUALIZADO.csv" % filename), 'w',newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=array_attr, delimiter=";")
    writer.writeheader()
    for data in diccionario_excel:
        writer.writerow(data)
