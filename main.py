from bs4 import BeautifulSoup
import requests
import pandas as pd
import webfunctions as wf

base = "https://books.toscrape.com/catalogue/"
page_num = 1

data = {
    "Title": [],
    "Price": [],
    "Quantity": [],
    "Link": [],
    "UPC": [],
    "Review": [],
}

section = {
    "product_page": 1,
    "categories": 2,
}

#('a', href=True)['href']

#while page_num != 2:
def scrape_data(page_num):
    page = requests.get(wf.url_changer(base + "page-", page_num))
    soup = BeautifulSoup(page.text, "html.parser")
    # Use "Section" here for further division. This way we can grab the sidebar, and product pages separately

    cell = soup.find("ul", class_="nav nav-list").li
    category = cell.find("ul")
    cat_list = []

    for li in category.find_all('li'):
        cat_list.append(li.text.strip())

    return cat_list


    #cell = soup.find_all(class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    #for item in cell:
    #    data["Link"].append(base + item.h3.find('a', href=True)['href'])
    #    data["Title"].append(item.h3.a['title'])
    #    data["Price"].append(item.find(class_="price_color").get_text()[1:])  # List slice for extra unneeded character
    #    data["Quantity"].append(item.find(class_='instock availability').get_text().strip())



    #TODO: Go through link_list and get product details from each page

    page_num += 1
scrape_data(1)
#print(data["Link"])
#print(data["Title"])
#print(data["Price"])
#print(data["Quantity"])

