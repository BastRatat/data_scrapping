import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd
import numpy as np

pattern_changes = '\+\d\.\d\d\%|\-\d\.\d\d\%'

url = 'https://finance.yahoo.com/quote/%5EFCHI/components?p=%5EFCHI'
driver_path = 'C:/chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

section = soup.find("section")

tr = soup.find_all("tr", class_="BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s)")

variation = []
for element in tr:
    temp = re.findall(pattern_changes, element.text)
    variation.append(temp)

variation = [element[0] for element in variation]

# clean dirty data in the list
clean_variation = []
for num in variation:
    if '+' in num:
        clean_variation.append(float(num[1:-1]))
    elif '-' in num:
        clean_variation.append(float(num[:-1]))

#clean_variation = [float(num[1:-1]) for num in variation]

symbol = []
for element in tr:
    symbol.append(element.find('td').find(
        'a', class_="C($c-fuji-blue-1-b) Cur(p) Td(n) Fw(500)").text)

prices = []
for element in tr:
    temp = re.findall(r'\d+\.\d+', element.text)
    prices.append(temp)

prices = [float(num[0]) for num in prices]

stock_dict = {
    "symbol": symbol,
    "price variation": clean_variation,
    "last prices": prices
}

stocks_df = pd.DataFrame.from_dict(stock_dict)
stocks_df.set_index('symbol')


print(stocks_df.sort_values('price variation', ascending=False))
