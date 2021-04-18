
import numpy as np
import pandas as pd

FILENAME = "world_dev_ind.csv"


if __name__ == '__main__':
  
  df = pd.read_csv(FILENAME)
  pd.set_option("display.max.columns", None)
  pd.set_option("display.precision", 2)
  print(df.describe())