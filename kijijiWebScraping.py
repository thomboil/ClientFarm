import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.kijiji.ca/'

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}

r = requests.get('https://www.kijiji.ca/b-grand-montreal/creation-de-site-web/k0l80002?sort=relevancyDesc&gpTopAds=y')
soup = BeautifulSoup(r.content, 'html.parser')

productlist = soup.find_all('div', class_ = 'search-item')
productlinks = []

for item in productlist:
    #for link in item.find_all('div', class_='title'):
    print(productlist)