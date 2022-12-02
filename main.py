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

title_list = []
page_num = 2

while page_num != 10:
    for item in cell:
        title_list.append(item.h3.a['title'])
    url_changer(page_num)
    page_num += 1


#print(cell.h3.a['title'])