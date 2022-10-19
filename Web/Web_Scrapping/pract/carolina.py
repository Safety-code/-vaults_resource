#from msilib.schema import tables
import requests
from bs4 import BeautifulSoup
import lxml
import html5lib

url = "https://portal.ncbar.gov/Verification/results.aspx"
bar_page = requests.get(url)
soup = BeautifulSoup(bar_page.content, "html.parser")
#print(soup.text)

table_results = soup.find('div', id="content")
print(table_results.text.strip())
















