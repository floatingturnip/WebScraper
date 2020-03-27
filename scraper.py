import numpy as np
import pandas as pd

import requests
from bs4 import BeautifulSoup

req = requests.get('http://worldometers.info/coronavirus/')
soup = BeautifulSoup(req.content)

table_row = soup.select('table#main_table_countries_today tr')

data = list(map(lambda x: list(map(lambda y: y.text,x.select('td, th'))), table_row))

df = pd.DataFrame(data)

# Set the column names to the first row
df.columns = df.iloc[0]
df = df.drop(0)

print(df.head(10))

df.to_csv('covid19.csv')