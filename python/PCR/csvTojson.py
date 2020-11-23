# coding:UTF-8
import csv
import json

CSVFILE = "pcr_positive_daily.csv"
JSONFILE = "pcr_positive_daily.json"

data = []
with open("../../data/PCR/" + CSVFILE, "r", encoding="shift_jis") as csvfile:
  for row in csv.DictReader(csvfile):
    data.append({"date":row["日付"],"positive":int(row["PCR 検査陽性者数(単日)"])})
    print({"date":row["日付"],"positive":row["PCR 検査陽性者数(単日)"]})

with open("../../data/PCR/" + JSONFILE, "w", encoding="utf_8") as jsonfile:
  json.dump(data, jsonfile, indent=2)
