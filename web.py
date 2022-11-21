#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import re

import os

if not os.path.isfile('./Prices.csv'):
    with open(r"Prices.csv", mode = "w+") as file:
        pass

with open(r"Prices.csv", mode = "r") as file:
    lines = file.readlines()
    prices = dict()
    for line in lines:
        temp = line.split(",")
        prices[temp[0]] = temp[1]


URLlist = [
"https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=10173348&Area=search&mdiv=403&oid=1_1&cid=index&kw=%E5%B0%8F%E7%B1%B3%E6%89%8B%E7%92%B06",
"https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=10526883&Area=search&mdiv=403&oid=1_1&cid=index&kw=iphone%2014%20pro%20max",
"https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=10608572&Area=search&mdiv=403&oid=1_3&cid=index&kw=XM5",
"https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=10666753&Area=search&mdiv=403&oid=1_7&cid=index&kw=dyson"
]

priceList = list()

driver = webdriver.Chrome()

for url in URLlist:

    driver.get(url)
    block = driver.find_element(By.CLASS_NAME, "special")
    price = re.search("[0-9,]+", block.text).group(0)
    price = price.replace(",","")
    if url not in prices.keys():
        print("New data established")
        prices[url] = price
    else:
        if(price <= prices[url]):
            print("New price same or below history low price :", price)
            prices[url] = price




with open(r"Prices.csv", mode = "w+",newline="") as file:
    for key, value in prices.items():
        file.writelines(key + "," + value+"\n")