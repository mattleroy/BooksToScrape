from bs4 import BeautifulSoup
import requests
import pandas as pd
import webfunctions as wf

base = "https://books.toscrape.com/catalogue/page-"
page_num = 1

data = {
    "Title": [],
    "Price": [],
    "Quantity": [],
    "Link": [],
}

#('a', href=True)['href']

while page_num != 10:

    page = requests.get(wf.url_changer(base, page_num))
    soup = BeautifulSoup(page.text, "html.parser")
    cell = soup.find_all(class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    for item in cell:

        data["Link"].append(item.h3.find('a', href=True)['href'])
        data["Title"].append(item.h3.a['title'])
        data["Price"].append(item.find(class_="price_color").get_text()[1:])  # List slice for extra unneeded character
        data["Quantity"].append(item.find(class_='instock availability').get_text().strip())

    page_num += 1

print(data)

