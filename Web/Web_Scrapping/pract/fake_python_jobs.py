from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

 # create beasutifulsoup object
soup = BeautifulSoup(page.content, "html.parser")

#Finding elements by ID
results = soup.find(id="ResultsContainer")

print(results.prettify())

#Finding elements by HTML class
job_elements = results.find_all("div", class_="card-content")

#Looping through all the job elements in that class in the div tag
for job_element in job_elements:
    print(job_element, end="\n"*2)
    
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    
    # Extract text from HTML elements
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    
# Passing a function to beautifulsoup method
python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
print(len(python_jobs))

python_jobs_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]

for job_element in python_jobs_elements:
    #---snip---
    # Extracting attributes from html elements
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
        
#Alternative for extracting second attribute link
    link_url = job_element.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")








