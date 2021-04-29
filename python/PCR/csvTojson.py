# coding:UTF-8
import requests
import io
import pandas as pd
import json

PCR_TEST_CSVFILE = "https://www.mhlw.go.jp/content/pcr_tested_daily.csv"
COVID_POSITIVE_CSVFILE = "https://www.mhlw.go.jp/content/pcr_positive_daily.csv"
JSONFILE = "covid_report.json"

# get data
## PCR Test
pcr_data = requests.get(PCR_TEST_CSVFILE).content
df_pcr = pd.read_csv(io.BytesIO(pcr_data))
df_pcr = df_pcr.rename(columns={"日付": "date", "PCR 検査実施件数(単日)": "tests"})
df_pcr = df_pcr.astype({"tests": object})

## COVID Positive
covid_data = requests.get(COVID_POSITIVE_CSVFILE).content
df_covid = pd.read_csv(io.BytesIO(covid_data))
df_covid = df_covid.rename(columns={"日付": "date", "PCR 検査陽性者数(単日)": "positives"})
df_covid = df_covid.astype({"positives": object})

## merge  data
df = pd.merge(df_covid[["date", "positives"]], df_pcr[["date", "tests"]], how="left", on="date")

# write to json file
with open("../../data/PCR/" + JSONFILE, "w", encoding="utf_8") as jsonfile:
  json.dump(json.loads(df.to_json(orient="records")), jsonfile, indent=2)
