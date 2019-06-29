import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


from pages.sitemap_page import ProductPage

def get_page_source(n):

    wd = webdriver.Firefox(executable_path = r"webdriver/geckodriver.exe")
    url = 'https://www.harveynorman.com.au/sitemap'

    wd.get(url)

    html_page = wd.page_source

    wd.quit()
    return html_page
n = 1006233
page_content = get_page_source(n)
page = ProductPage(page_content)
print(f"lenght:{len(page.products)}")

product_links = {}
for product in page.products:
    print(product.name)
    product_links[product.name] = [product.link]


df = pd.DataFrame.from_dict(product_links).transpose()
df.to_csv(r"Data/product_links.csv")
