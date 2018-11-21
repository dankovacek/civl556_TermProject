
import urllib2
from bs4 import BeautifulSoup

import requests


base_url = 'http://www.wesm.ph/inner.php/downloads/final_gwap/'

r = requests.get(base_url)
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))
