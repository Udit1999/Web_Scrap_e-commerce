from product_locators.sub_products import ProductLocators

class ProductParser:
    def __init__(self,parent):
        self.parent = parent

    @property
    def name(self):
        locator = ProductLocators.NAME
        return self.parent.select_one(locator).string

    @property
    def link(self):
        locator = ProductLocators.LINK
        item = self.parent.select_one(locator)
        return item.attrs['href']
