#! python3
# lucky.py - opens several Google.com results in different tabs
__author__ = 'Cronos'

import sys
import requests
import bs4
import webbrowser

#Step 1: Get the Command Line Arguments and Request the Search Page
print("Googling...")
res = requests.get('http://www.google.com/search?q=)'+' '.join(sys.argv[1:]))
res.raise_for_status()
# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)
# TODO: Open a browser tab for each result.
linkElements = soup.select('.r a')
numOpen = min(5, len(linkElements))
for i in range(numOpen):
    webbrowser.open('http://www.google.com'+linkElements[i].get('href'))