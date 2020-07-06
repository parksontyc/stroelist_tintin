import requests
from bs4 import BeautifulSoup
import time
import csv

store_name = []
store_address = []

url = "https://www.norbelbaby.com.tw/TinTin/work.jsp"

res = requests.get(url, timeout=5)

html = res.text

soup = BeautifulSoup(html.replace('\n', '').strip(), "html.parser")

items = soup.find('table', id="office").find_all("tr")

for item in items:
	store_name.append(item.td.text)
	store_address.append(item.find('td', class_="addr").text)

with open('storelist_tintin.csv', 'w', newline='',  encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    newrow = ['門市名稱', '門市地址']
    csvwriter.writerow(newrow)
    for n in range(0, len(store_name)):
        newrow.clear()
        newrow.append(store_name[n])
        newrow.append(store_address[n])
        csvwriter.writerow(newrow)	
