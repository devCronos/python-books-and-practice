#! python3
# downloads every xkcd pic
__author__ = 'Cronos'

import requests
import bs4
import os

url = 'http://www.xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    # Find the URL of the comic image.
    el = soup.select('#comic img')
    if el == []:
        print('no img sry')
    else:
        picurl = str('http:' + el[0].get('src'))
        # Download the image.
        print('Downloading image %s...' % (picurl))
        res = requests.get(picurl)
        res.raise_for_status()
        #Save the image to ./xkcd.
        imgFile = open(os.path.join('xkcd',os.path.basename(picurl)),'wb')
        for chunk in res.iter_content(1000):
            imgFile.write(chunk)
        imgFile.close()
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://www.xkcd.com' + prevLink.get('href')
print('Done.')