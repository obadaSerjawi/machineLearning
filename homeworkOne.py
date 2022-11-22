import numpy as np
import pandas as pd
import glob

location = r'./*.xlsx'
ex = glob.glob(location)

pd.set_option('display.max_rows', 91)
df = pd.DataFrame()

for i in ex:
    df1 = pd.read_excel(i)
    df = pd.concat([df, df1], ignore_index=True)
df.fillna(value="N/A", inplace=True)

df.to_excel(r'./homeworkOne.xlsx')
df.head()

df["name"] = df["name"].astype("category")
df.groupby(by="name").sum()

df.groupby(by="name").count()
