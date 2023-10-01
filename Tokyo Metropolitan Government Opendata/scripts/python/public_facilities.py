# coding:UTF-8
import _utilities as util

# metadata
CSV_METADATA = {
  "target_url_list": [
    ["https://www.opendata.metro.tokyo.lg.jp/suisyoudataset/130001_public_facility.csv", "cp932"],
  ],
  "header": ["都道府県名", "市区町村名", "名称", "POIコード", "住所", "緯度", "経度", "電話番号", "利用可能曜日", "利用可能日時特記事項", "説明", "URL", "アクセス方法", "駐車場_有無", "駐車場情報", "料金_要否", "料金(詳細)"],
  "dropna": ["緯度", "経度"],
}

OUTPUT_DESTINATION = "../../data/Public Facilities/csv/output.csv"

# main
if __name__=="__main__":
  # download and merge csv
  data = util.marge_csv(CSV_METADATA)

  # data preprocessing
  data["駐車場_有無"] = data["駐車場_有無"].astype(bool)
  data["料金_要否"] = data["料金_要否"].astype(bool)

  # output data mart csv
  util.output_csv(data, OUTPUT_DESTINATION)
