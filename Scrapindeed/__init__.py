"""
All Function and Methode used in Scrapindeed
"""
import requests
# Import Eksternal Package
import requests as re
from bs4 import BeautifulSoup
import cloudscraper


# Define parent class Scrapindeed
class Scrapindeed():

    # Define variable parent class Scrapindeed
    # def __init__(self, url, headers):
    #     self.url = url
    #     self.headers = {'User-Agent': headers}

    # Define function parent class Scrapindeed

    # get url
    def get_url(self, url, headers):
        scraper = cloudscraper.create_scraper(disableCloudflareV1 = True)
        response = scraper.get(url)
        response = BeautifulSoup(response.text, 'html.parser')
        # with re.Session() as session:
        #     response = session.get(url, headers=headers)
        #     response = BeautifulSoup(response.text, 'html.parser')
        return response



