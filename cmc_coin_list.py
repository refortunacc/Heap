import requests
from bs4 import BeautifulSoup

cmc_url = 'https://coinmarketcap.com/all/views/all/'

request_url = requests.get(cmc_url)
page_decoded = request_url.content.decode('utf-8')
soup = BeautifulSoup(page_decoded, "lxml")
for link in soup.find_all('a', {"class": "currency-name-container link-secondary"}):
    currency = link.string
    with open('coin_list.txt', 'a') as file:
        file.write(currency + '\n')
