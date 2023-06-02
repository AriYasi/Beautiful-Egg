import requests
import re
from bs4 import BeautifulSoup

class BeautifulEgg:
    def __init__(self, URL):
        self.URL = URL
        
    
    def new_request(self):
        try:
            self.requestPage = requests.get(self.URL)

            if not re.search('https?://([A-Za-z_0-9.-]+).*', self.URL).group(1) == "www.newegg.com":
                raise requests.exceptions.MissingSchema

            self.soup = BeautifulSoup(self.requestPage.content, "html.parser")

            self.product_name = self.soup.find("h1", class_="product-title").text
            self.product_price = self.soup.find("div", class_="product-price").find("li", class_="price-current").text
        except requests.exceptions.MissingSchema:
            print("Error: Not a valind Newegg URL.")

    def get_product_name(self):
        return self.product_name

    def get_product_price(self):
        return self.product_price

    def __str__(self):
        return f"{self.product_name}\n{self.product_price}"