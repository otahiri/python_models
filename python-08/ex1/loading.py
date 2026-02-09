import numpy as nm
import pandas
import requests
from matplotlib import pyplot as pt


def main() -> None:
    product = requests.get("https://dummyjson.com/products").json()["product"]
    data = pandas.DataFrame(product)
    data.plot.scatter(x="price", y="rating")
    pt.xlabel("Price")


if __name__ == "__main__":
    main()
