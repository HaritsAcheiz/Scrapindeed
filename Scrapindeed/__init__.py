"""
All Function and Methode used in Scrapindeed
"""
import requests
# Import Eksternal Package
import requests as re
from bs4 import BeautifulSoup

# Define parent class Scrapindeed
class Scrapindeed():

    # Define variable parent class Scrapindeed
    # def __init__(self, url, headers):
    #     self.url = url
    #     self.headers = {'User-Agent': headers}

    # Define function parent class Scrapindeed

    # get url
    def get_url(self, url, headers):
        with re.Session() as session:
            response = session.get(url, headers=headers)
        return response



