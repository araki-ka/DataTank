# coding:UTF-8
import requests
import io
import pandas as pd
import json

CSVFILE = "https://www.mhlw.go.jp/content/pcr_positive_daily.csv"
JSONFILE = "pcr_positive_daily.json"

# get CSV data
data = requests.get(CSVFILE).content
df = pd.read_csv(io.BytesIO(data))
df = df.rename(columns={"日付": "date", "PCR 検査陽性者数(単日)": "positives"})

# write to json file
with open("../../data/PCR/" + JSONFILE, "w", encoding="utf_8") as jsonfile:
  json.dump(json.loads(df.to_json(orient="records")), jsonfile, indent=2)
