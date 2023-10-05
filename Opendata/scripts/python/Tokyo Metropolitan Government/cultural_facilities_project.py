import sys
sys.path.append("../common/")
import utilities as util

# metadata
CSV_METADATA = {
  "target_url_list": [
    ["https://www.opendata.metro.tokyo.lg.jp/seikatubunka/event/130001_bunkashisetsujigyo_event.csv", "utf8"],
    ["https://www.opendata.metro.tokyo.lg.jp/seikatubunka/R5_bunkashisetsujigyo.csv", "cp932"],
  ],
  "header": ["都道府県名", "市区町村名", "イベント名", "開始日", "終了日", "説明", "場所名称", "住所", "緯度", "経度", "アクセス方法", "URL", "備考"],
  "dropna": ["緯度", "経度"],
}

OUTPUT_DESTINATION = "../../../data/Tokyo Metropolitan Government/Cultural Facilities Project/csv/output.csv"

# main
def main():
  # download and merge csv
  data = util.marge_csv(CSV_METADATA)

  # data preprocessing
  data["緯度"] = util.replace(data, "緯度", ",", "")

  # output data mart csv
  util.output_csv(data, OUTPUT_DESTINATION)

if __name__=="__main__":
  main()
