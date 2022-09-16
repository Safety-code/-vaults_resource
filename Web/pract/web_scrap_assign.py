from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

#print(soup.find_all("a"))
for link in soup.find_all("a"):
    link_url = url + link["href"]
    print(link_url)

