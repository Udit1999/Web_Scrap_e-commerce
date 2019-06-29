from bs4 import BeautifulSoup

from product_locators.all_product_locators import AllProductPageLocators
from parsers.product import ProductParser
class ProductPage:
    def __init__(self,page):
        self.soup = BeautifulSoup(page,'html.parser')

    @property
    def products(self):
        locator = AllProductPageLocators.SUB_PRODUCTS
        sub_products = self.soup.select(locator)
        return [ProductParser(p) for p in sub_products]