import sys
sys.path.append("../common/")
import utilities as util

# metadata
PCR_CSV_METADATA = {
  "target_url_list": [
    ["https://www.mhlw.go.jp/content/001060467.csv", "utf8"]
  ],
  "header": ["日付","PCR 検査実施人数(単日)"],
  "dropna": ["日付"],
}

POSITIVE_CSV_METADATA = {
  "target_url_list": [
    ["https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv", "utf8"]
  ],
  "header": ["Date", "ALL"],
  "dropna": ["Date"],
}

OUTPUT_DESTINATION = "../../../data/MHLW/COVID-19/csv/output.csv"

# main
def main():
  # download and merge csv
  pcr_data = util.marge_csv(PCR_CSV_METADATA)
  positive_data = util.marge_csv(POSITIVE_CSV_METADATA)

  # data preprocessing
  pcr_data = pcr_data.rename(columns={"日付": "date", "PCR 検査実施人数(単日)": "tests"})
  pcr_data.fillna(0, inplace=True)
  pcr_data = pcr_data.astype({"tests": "int64"})
  positive_data = positive_data.rename(columns={"Date": "date", "ALL": "positives"})
  positive_data = positive_data.astype({"positives": "int64"})
  data = util.join_csv(pcr_data, "left", positive_data, "date")

  # output data mart csv
  util.output_csv(data, OUTPUT_DESTINATION)

if __name__=="__main__":
  main()
