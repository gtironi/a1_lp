import pandas as pd
import numpy as np

def csv_to_dataframe(csv_path):
    dataframe = pd.read_csv(csv_path, sep=";", index_col=None, encoding = 'cp860')
    return dataframe