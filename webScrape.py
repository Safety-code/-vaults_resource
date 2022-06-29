from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())
#print(soup.replace_with_template())
print(soup.find_all("img"))
#print(soup.find_all.__str__())  
print(soup.find_all("title"))
#print(soup.prettify())

image1, image2 = soup.find_all("img")
print(image1.name)
print(image2["src"])
print(soup.title.string) 

print(soup.find_all("img", src="/static/dionysus.jpg"))



 


