"""
This Code created for place to learn webscraping on indeed.com only by requests and beautifulsoup4
"""
from Scrapindeed import Scrapindeed

if __name__ == '__main__':
    url = 'https://id.indeed.com/jobs?q=data+engineer&l=Tangerang&from=searchOnHP&vjk=2d21e19686fcde5e'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
    scraper = Scrapindeed()
    response = scraper.get_url(url, headers=header)
    print(response)