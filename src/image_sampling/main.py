# Standard Library
import csv
import os
from logging import exception

# Third Party Library
import cv2 as cv
import numpy as np


def image_to_csv(image_file):
    # Read Image File
    img = cv.imread(image_file)

    # Sampling
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    ret, img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

    # Array to Numpy
    img_array = np.asarray(img)

    # Output CSV
    results = []
    for y in range(img_array.shape[0]):
        for x in range(img_array.shape[1]):
            if img_array[y][x][0] != 255 and img_array[y][x][1] != 255 or img_array[y][x][2] != 255:
                results.append(
                    {
                        "x": x,
                        "y": y,
                    }
                )
    try:
        with open(
            "./data/image_sampling/{}.csv".format(os.path.splitext(os.path.basename(image_file))[0]),
            "w",
            encoding="utf-8",
        ) as out:
            writer = csv.DictWriter(out, fieldnames=["x", "y"], delimiter=",", quoting=csv.QUOTE_ALL)
            writer.writeheader()
            writer.writerows(results)
            print("* CSV出力が完了しました")
    except csv.Error as e:
        exception(e)
