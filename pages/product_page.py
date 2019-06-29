from bs4 import BeautifulSoup

from product_locators.subcat_locators import AllSubCatLocators
from parsers.subproduct import ProductParser
class ProductPage:
    def __init__(self,page):
        self.soup = BeautifulSoup(page,'html.parser')

    @property
    def products(self):
        locator = AllSubCatLocators.SUB_CATS
        sub_products = self.soup.find(locator,{'data-filter-id':"1065"})
        sub_products = sub_products.select('li')
        return [ProductParser(p) for p in sub_products]