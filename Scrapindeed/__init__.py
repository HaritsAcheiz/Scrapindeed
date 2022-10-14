"""
All Function and Methode used in Scrapindeed
"""

# Import Eksternal Package
import requests
from bs4 import BeautifulSoup
import cloudscraper
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



# Define parent class Scrapindeed
class Scrapindeed():

    # Define variable parent class Scrapindeed
    # def __init__(self, url, headers):
    #     self.url = url
    #     self.headers = {'User-Agent': headers}

    # Define function parent class Scrapindeed

    # def get_url(self, url, headers):
    #     with requests.Session() as session:
    #         response = session.get(url, headers=headers)
    #     session.close()
    #     return response

    # def get_url(self, url, headers, interpreter):
    #     scraper = cloudscraper.create_scraper(disableCloudflareV1 = True, interpreter=interpreter)
    #     response = scraper.get(url, headers=headers)
    #     return response

    def get_url(self, url, webdriver_path, headers):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-translate")
        options.add_argument(headers['User - Agent'])
        driver = webdriver.Firefox(executable_path=webdriver_path, options=options)
        driver.get(url)
        response = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.ID, 'jobsearch-Main')))
        parent = response.find_element(By.CSS_SELECTOR, '.jobsearch-ResultsList')
        children = parent.find_elements(By.TAG_NAME, 'li')
        result = []
        for i in children:
            data = i.find_element(By.XPATH, "//a[@class='jcs-JobTitle css-jspxzf eu4oa1w0']").get_attribute('href')
            result.append(data)

        return result
