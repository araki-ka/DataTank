# coding:UTF-8
import pandas as pd
import csv

def download_csv(target_csv, csv_charset, csv_header, csv_dropna):
  return pd.read_csv(target_csv, encoding=csv_charset).loc[:, csv_header].dropna(subset=csv_dropna)

def marge_csv(csv_metadata):
  output = pd.DataFrame(columns=csv_metadata["header"])
  for target_csv in csv_metadata["target_url_list"]:
    data = download_csv(target_csv[0], target_csv[1], csv_metadata["header"], csv_metadata["dropna"])
    return pd.concat([output, data])

def replace(data, column, trim_strings):
  return data[column].str.replace(trim_strings, "")

def strip(data, column):
  return data[column].str.strip()

def distinct(data):
  return data.drop_duplicates()

def output_csv(data, output_destination):
  data.to_csv(output_destination, mode="w", index=False, quoting=csv.QUOTE_ALL, encoding="utf-8")
