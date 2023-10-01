# coding:UTF-8
import _utilities as util

# metadata
CSV_METADATA = {
  "target_url_list": [
    ["https://www.opendata.metro.tokyo.lg.jp/kyouiku/130001culturalproperty.csv", "cp932"],
  ],
  "header": ["都道府県名", "市区町村名", "名称", "文化財分類", "住所", "緯度", "経度", "所有者等", "文化財指定日", "備考"],
  "dropna": ["緯度", "経度"],
}

OUTPUT_DESTINATION = "../../data/Designation Historic Site/csv/output.csv"

# main
if __name__=="__main__":
  # download and merge csv
  data = util.marge_csv(CSV_METADATA)

  # data preprocessing
  data["名称"] = util.strip(data, "名称")
  data = util.distinct(data)

  # output data mart csv
  util.output_csv(data, OUTPUT_DESTINATION)
