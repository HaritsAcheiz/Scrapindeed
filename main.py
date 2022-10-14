"""
This Code created for place to learn webscraping on indeed.com only by requests and beautifulsoup4
"""
from Scrapindeed import Scrapindeed

if __name__ == '__main__':
    url = 'https://id.indeed.com/jobs?q=data+engineer&l=Tangerang&from=searchOnHP&vjk=2d21e19686fcde5e'
    header = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64; rv: 105.0) Gecko / 20100101 Firefox / 105.0'
    }
    webdriverpath = 'C:/geckodriver-v0.31.0-win64/geckodriver.exe'
    scraper = Scrapindeed()
    response = scraper.get_url(url, webdriver_path=webdriverpath, headers=header)
    for i in response:
        print(i)
