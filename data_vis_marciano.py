import pandas as pd
import data_cleaner

df = data_cleaner.csv_to_dataframe("censo_escolar_2021.csv")

print(df.head())

