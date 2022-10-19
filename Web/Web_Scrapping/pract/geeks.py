from importlib.metadata import requires
import re
import requests
from bs4 import BeautifulSoup
import html5lib
import csv


# Python program to scrape website and save quotes from them

url = "http://www.values.com/inspirational-quotes"
r = requests.get(url)   

soup = BeautifulSoup(r.content, "html5lib")

#List for storing the quotes
quotes =[]
table = soup.find("div", attrs={"id":"all_quotes"})

csv_output = open('quotes.csv', 'w')
csv_write = csv.writer(csv_output)
csv_write.writerow(['theme', 'url', 'img', 'lines', 'author'])


for row in table.findAll("div", attrs={'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)
    
    
    csv_write.writerow([quote['theme'], quote['url'], quote['img'], quote['lines'], quote['author']])
    
csv_output.close()    
