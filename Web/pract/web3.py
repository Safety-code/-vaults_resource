from os import spawnle
import requests
from bs4 import BeautifulSoup
import bs4



url = "https://nostarch.com/"
re = requests.get(url)
re.raise_for_status()
noStarchsoup = bs4.BeautifulSoup(re.text)
type(noStarchsoup)

exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select("#author")

print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

print()

pelems = exampleSoup.select("p")
print(str(pelems[0]))
print(pelems[0].getText())
print(str(pelems[1]))
print(elems[1].getText())
print(str(elems[1]))

#Getting data from elements's attributes
soupexample = open("example.html")
soup = bs4.BeautifulSoup(soupexample.read())
#soup.read()
spanelem = soup.select("span")[0]
print(str(spanelem))
print(spanelem.getText("id"))
print(spanelem.get("some_nonexsitent_addr")) == None
print(spanelem.attrs)



