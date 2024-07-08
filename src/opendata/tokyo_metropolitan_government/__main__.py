# Standard Library
import argparse

# First Party Library
from . import const, cultural_facilities_project, designation_historic_site, life_and_statistics, public_facilities

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="Tokyo Metropolitan Government Open Data",
        usage="python -m mhlw --target {dataset_name}",
        description="東京都オープンデータ",
        epilog="end",
        add_help=True,
    )

    parser.add_argument("-T", "--target", type=str, dest="target", required=True, help="対象データセット名({})".format(const.DATASETS))

    args = parser.parse_args()

    match args.target:
        case "cultural_facilities_project":
            cultural_facilities_project.main()
        case "designation_historic_site":
            designation_historic_site.main()
        case "life_and_statistics":
            life_and_statistics.main()
        case "public_facilities":
            public_facilities.main()
        case _:
            print(args.target, "is not found. Please select: {}".format(const.DATASETS))