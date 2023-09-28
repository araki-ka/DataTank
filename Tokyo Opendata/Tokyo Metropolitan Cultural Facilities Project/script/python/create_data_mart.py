# coding:UTF-8
import pandas as pd
import csv

# target
EXPORT_URL = "https://www.opendata.metro.tokyo.lg.jp/seikatubunka/"
TARGET_CSV = [
  ["event/130001_bunkashisetsujigyo_event.csv", "utf8"],
  ["R5_bunkashisetsujigyo.csv", "cp932"],
]
CSV_HEADER = ["都道府県名", "市区町村名", "イベント名", "開始日", "終了日", "説明", "場所名称", "住所", "緯度", "経度", "アクセス方法", "URL", "備考",]
CSV_DROPNA = ["緯度", "経度"]
OUTPUT_DIRECTORY = "../../data/csv/"

# download and merge csv
output = pd.DataFrame(columns=CSV_HEADER)
for target_csv in TARGET_CSV:
  data = pd.read_csv(EXPORT_URL + target_csv[0], encoding=target_csv[1]).loc[:, CSV_HEADER].dropna(subset=CSV_DROPNA)
  output = pd.concat([output, data])

# exporting the csv
output.to_csv(OUTPUT_DIRECTORY + "output.csv", mode="w", index=False, quoting=csv.QUOTE_ALL)
