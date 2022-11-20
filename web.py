#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import re

import os

if not os.path.isfile('./listPrice.csv'):
    with open(r"listPrice.csv", mode = "w+") as file:
        pass

with open(r"listPrice.csv", mode = "r") as file:
    lines = file.readlines()
    print(lines)
    prices = dict()
    for line in lines:
        print(line)
        prices[line[0]] = line[1]
    
    

driver = webdriver.Chrome()

url = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=10173348&Area=search&mdiv=403&oid=1_1&cid=index&kw=%E5%B0%8F%E7%B1%B3%E6%89%8B%E7%92%B06"

driver.get(url)

block = driver.find_element(By.CLASS_NAME, "special")

price = re.search("[0-9]+", block.text).group(0)

print(price)

if url not in prices.keys():
    print("New data established")
    prices[url] = price
else:
    if (price <= prices[url]):
        print("New price same or below history low price :", price)
        prices[url] = price

print("----------------------")
print(prices)

with open(r"listPrice.csv", mode = "w+",newline="") as file:
    for key, value in prices.items():
        file.writelines(key + "," + value)