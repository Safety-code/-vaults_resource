import requests
from bs4 import BeautifulSoup
import bs4
import sys
import webbrowser


#Opening several google search results
print("Googling.....") #displaying text while downloading the google page
re =  requests.get("https://www.google.com/search?q="+"".join(sys.argv[1:]))
re.raise_for_status()

#Retrieve top search results links
soupobj = bs4.BeautifulSoup(re.text)

#Open a browser tab for each search results
linkelems = soupobj.select(".r a")
numopen =min(5, len(linkelems))
for i in range(numopen):
    opentab = webbrowser.open("https://www.google.com" +linkelems[i].get("href"))


