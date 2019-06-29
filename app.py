import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


from pages.product_page import ProductPage

def get_page_source(url):

    wd = webdriver.Firefox(executable_path = r"webdriver/geckodriver.exe")
    # url = 'https://www.harveynorman.com.au/computers-tablets/computers/laptops'

    wd.get(url)

    html_page = wd.page_source

    wd.quit()
    return html_page

link_df = pd.read_csv(r'Data/product_links.csv').iloc[1:,:]

number_of_product_in_each_category = []
for product_number in range(len(link_df)):
    pName = link_df.iloc[product_number,0]
    pUrl = link_df.iloc[product_number,1]
    print(f'Name:{pName} URL: {pUrl}')
    page_content = get_page_source(pUrl)
    page = ProductPage(page_content)


    try:
        for product in page.products:
            print(f'{product.name}  {product.number}')
            number_of_product_in_each_category.append([pName,product.name,product.number])
    except:
        print("This one is not a product")

df = pd.DataFrame(number_of_product_in_each_category,columns = ['Category','Sub-Category','Number_of_Products'])
df.to_csv(r"Data/product_stock.csv")
