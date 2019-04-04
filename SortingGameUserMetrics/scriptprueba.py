import csv
import json
import requests

from collections import defaultdict
import sys

# filename = sys.argv[1]

filename_metrics_json = "c:/users/usuario/downloads/sortingameusermetrics.json"
filename_questionnaire_json = "c:/users/usuario/downloads/sortinggameuserquestionnaire.json"
filename_questionnaire_csv = "questionnaire.csv"


metrics_dict = {}
questionnaire_dict = {}
with open(filename_metrics_json,
          "r") as jsonfile:  # CAMBIAR OPCIONALMENTE filename POR filename_local Y ASIGNAR EL NOMBRE DEL ARCHIVO LOCAL A ESA VARIABLE
    data = jsonfile.read().replace('\n', '')
    metrics_parsed = json.loads(data)
    print(metrics_parsed)
    for n in metrics_parsed:
        metrics_dict[n['id']] = n



with open(filename_questionnaire_json,
          "r") as jsonfile:  # CAMBIAR OPCIONALMENTE filename POR filename_local Y ASIGNAR EL NOMBRE DEL ARCHIVO LOCAL A ESA VARIABLE
    data = jsonfile.read().replace('\n', '')
    questionnaire_parsed = json.loads(data)
    print(questionnaire_parsed)
    for n in questionnaire_parsed:
        questionnaire_dict[n['id']] = n

metrics_dict.update(questionnaire_dict)

with open('pruebametricsfinal.json', 'w', encoding="UTF-8") as outfile:
    outfile.write(json.dumps(metrics_dict, sort_keys=True, indent=4, ensure_ascii=False))



