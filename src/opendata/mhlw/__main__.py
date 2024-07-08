# Standard Library
import argparse

# Local Library
from . import const, covid_19

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="Ministry of Health, Labour and Welfare Open Data",
        usage="python -m mhlw --target {dataset_name}",
        description="厚生労働省のデータ",
        epilog="end",
        add_help=True,
    )

    parser.add_argument(
        "-T", "--target", type=str, dest="target", required=True, help="対象データセット名({})".format(const.DATASETS)
    )

    args = parser.parse_args()

    match args.target:
        case "covid_19":
            covid_19.main()
        case _:
            print(args.target, "is not found. Please select: {}".format(const.DATASETS))
