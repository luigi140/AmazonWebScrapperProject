from bs4 import BeautifulSoup
import requests
import time


def check_price():
    url = 'https://www.amazon.ca/Adidas-ORIGINALS-Mens-Smith-White/dp/B0931VFWQF/ref=sr_1_1_sspa?keywords=stan%2Bsmith%2Bmen&qid=1663198015&sprefix=stan%2B%2Caps%2C127&sr=8-1-spons&th=1&psc=1'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    page = requests.get(url, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').text
    price = soup2.find(class_='a-offscreen').text

    price = price.strip()[1:]
    title = title.strip()

    print(title)
    print(price)

    import datetime

    today = datetime.date.today()

    import csv

    data = [title, price, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


while (True):
    check_price()
    time.sleep(86400)

import pandas as pd

df = pd.read_csv(r'C:\Users\Darshan Punjabi\AmazonWebScraperDataset.csv')

print(df)
