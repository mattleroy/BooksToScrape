from bs4 import BeautifulSoup
import requests
import pandas as pd

#page_var = "https://books.toscrape.com/catalogue/page-3.html"
url = "https://books.toscrape.com/"

def url_changer(page_num):
    base = "https://books.toscrape.com/catalogue/page-"
    new_url = base + f"{page_num}.html"
    return new_url

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
cell = soup.find_all(class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

link_list = []
link_list.append(cell.find_all('a', href=True)['href'])


data = {
    "Title": [],
    "Price": [],
    "In Stock": [],
    "Link": [],
}

page_num = 2

while page_num != 3:
    for item in cell:
        data["Title"].append(item.h3.a['title'])
        data["Price"].append(item.find(class_="price_color").get_text()[1:])  # [1:] Here because it added unnecessary special character at the beginning
        data["In Stock"].append(item.find(class_='instock availability').get_text().strip())
        data["Link"].append(item.find('a', href=True)['href'])



    url_changer(page_num)
    page_num += 1




#print(data)

#print(cell.h3.a['title'])