"""
Author : Bastien RATAT
Scraping CAC40 30 best stocks on Yahoo Finance
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import os
import datetime

pattern_changes = '\+\d\.\d\d\%|\-\d\.\d\d\%'
url = 'https://finance.yahoo.com/quote/%5EFCHI/components?p=%5EFCHI'
driver_path = 'C:/chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

# root tag for iterations
tr = soup.find_all("tr", class_="BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s)")

# scraping ans cleaning variation data
variation = []
for element in tr:
    temp = re.findall(pattern_changes, element.text)
    variation.append(temp)

variation = [element[0] for element in variation]

clean_variation = []
for num in variation:
    if '+' in num:
        clean_variation.append(float(num[1:-1]))
    elif '-' in num:
        clean_variation.append(float(num[:-1]))

# scraping stocks symbols
symbol = []
for element in tr:
    symbol.append(element.find('td').find(
        'a', class_="C($c-fuji-blue-1-b) Cur(p) Td(n) Fw(500)").text)

clean_symbol = [string[:-3] for string in symbol]

# scraping stocks last prices
prices = []
for element in tr:
    temp = re.findall(r'\d+\.\d+', element.text)
    prices.append(temp)

prices = [float(num[0]) for num in prices]

# dictionary of symbol, price variation and last price
stock_dict = {
    "symbol": clean_symbol,
    "price variation": clean_variation,
    "last prices": prices
}

# DataFrame in Pandas
stocks_df = pd.DataFrame.from_dict(stock_dict)

# create a file extension
scrap_day = datetime.date.today()

# Plot datas using sns and plt
sns.barplot(x='symbol', y='last prices', data=stocks_df, palette="Blues_d")
plt.xticks(rotation=90)
plt.xlabel('')
plt.ylabel('PRICES')
plt.title('CAC40 30 best stocks on Yahoo Finance')
plt.savefig(f"cac40_{scrap_day}.png")
plt.show()
