import numpy as nm
import requests
import pandas as pd
from matplotlib import pyplot as pt


def main() -> None:
    x = 2 * nm.random.rand(100)
    y = 10 + 3 * x + nm.random.rand(100)
    a, b = nm.polyfit(x, y, 1)
    df = pd.DataFrame(data=x, columns=['Feature_X'])
    df["Target_y"] = y
    print(df)


if __name__ == "__main__":
    try:
        main()
    except ModuleNotFoundError as e:
        print(e)
