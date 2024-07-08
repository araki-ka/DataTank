# Standard Library
import csv
from logging import exception

# First Party Library
from utils import csv_util

# Local Library
from . import const

# const
PCR_CSV_METADATA = {
    "target_url_list": [["https://www.mhlw.go.jp/content/001060467.csv", "utf8"]],
    "header": ["日付", "PCR 検査実施人数(単日)"],
    "dropna": ["日付"],
}
PCR_RENAMED_HEADER = {"日付": "date", "PCR 検査実施人数(単日)": "tests"}
POSITIVE_CSV_METADATA = {
    "target_url_list": [["https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv", "utf8"]],
    "header": ["Date", "ALL"],
    "dropna": ["Date"],
}
POSITIVE_RENAMED_HEADER = {"Date": "date", "ALL": "positives"}
COVID_19_OUTPUT_CSV = const.OUTPUT_DESTINATION.format("opendata/mhlw/covid_19.csv")


# main
def main():
    # download csv and merge data
    pcr_data = csv_util.marge_csv(PCR_CSV_METADATA)
    positive_data = csv_util.marge_csv(POSITIVE_CSV_METADATA)

    # data preprocessing
    pcr_data = pcr_data.rename(columns=PCR_RENAMED_HEADER)
    pcr_data.fillna(0, inplace=True)
    pcr_data = pcr_data.astype({"tests": "int64"})
    positive_data = positive_data.rename(columns=POSITIVE_RENAMED_HEADER)
    positive_data = positive_data.astype({"positives": "int64"})
    data = csv_util.join_csv(pcr_data, "left", positive_data, "date")

    # output csv
    try:
        csv_util.output_csv(data, COVID_19_OUTPUT_CSV)
    except csv.Error as e:
        exception(e)
