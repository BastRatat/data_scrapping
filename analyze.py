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

index = 0
for file in dataframes['files']:
    dataframes['df'][f'df{index}'] = pd.read_csv(file)
    index += 1

print(dataframes["df"]['df0'])
