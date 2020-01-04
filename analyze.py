"""
Author : Bastien RATAT
Analyzing CAC40 30 best stocks on Yahoo Finance
"""

import re
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import os
import datetime


cwd = os.getcwd()
# C:\Users\Bastien\Desktop\Python\data_scrapping

_, file_extension = os.path.splitext(
    'C:/Users/Bastien/Desktop/Python/data_scrapping/2020-01-03.csv')


dataframes = {
    "dates": [],
    "files": [],
    "df": {}
}
for file in os.listdir(cwd):
    file_name, file_extension = os.path.splitext(f'C:/Users/Bastien/Desktop/Python/data_scrapping/{file}')
    if file_extension == '.csv':
        temp = re.findall(r'\d+\-\d+\-\d+', file_name)[0]
        dataframes['dates'].append(temp)
        dataframes['files'].append(f"{temp}.csv")

index_1 = 0
for file in dataframes['files']:
    dataframes['df'][f'df{index_1}'] = pd.read_csv(file)
    dataframes['df'][f'df{index_1}'] = dataframes['df'][f'df{index_1}'].set_index("symbol")
    index_1 += 1

index_2 = 0
for date in dataframes["dates"]:
    dataframes['df'][f'df{index_2}'] = dataframes['df'][f'df{index_2}'].rename(columns={"last prices":
                                                                                        f"last prices {date}"})
    index_2 += 1

print(dataframes['df']['df0'])
print(dataframes['df']['df1'])
