from time import sleep
import requests
from bs4 import BeautifulSoup
import lxml


def parsePrice():
    r = requests.get('https://finance.yahoo.com/quote/META?p=META')
    soup = BeautifulSoup(r.text, 'lxml')
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px) W(100%)'})
    return price[0].find('span').text
while True:
    print('The current price: ' +str(parsePrice()))
    sleep(5)