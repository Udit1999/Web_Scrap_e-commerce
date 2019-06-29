from product_locators.subcat_locators import ProductLocators

class ProductParser:
    def __init__(self,parent):
        self.parent = parent

    @property
    def name(self):
        locator = ProductLocators.NAME
        return self.parent.select_one(locator).string

    @property
    def number(self):
        locator = ProductLocators.NUMBER
        return int(self.parent.select_one(locator).string)
       
