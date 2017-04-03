import requests
from bs4 import BeautifulSoup
file=open('output.txt','w')

def trade_spider(max_pages):

    page = 0  # craigslist starts at page 0
    while page <= max_pages:
        url = 'http://orlando.craigslist.org/search/cto?s' + str(
            page)  # this is for cars in the orlando area, replace link with w/e
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)  # my computer yelled at me if 'lxml' wasn't included. your mileage may vary
        for link in soup.findAll('a', {'class': 'hdrlnk'}):
            href = 'http://orlando.craigslist.org/search/cto?s0' + link.get(
                'href')  # use the same link as your 'url' variable + '0' at
            # the end
            title = link.string
            file.write(title + '\n')
            file.write(href + '\n')
        page += 100  # craigslist pages go 0, 100, 200, etc


trade_spider(1)
file.close()