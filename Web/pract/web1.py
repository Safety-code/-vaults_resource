import string
from unittest import result
import requests
from bs4 import BeautifulSoup
#from urllib.request import urlopen


url = "http://realpython.github.io/fake-jobs"
#URL = "http://umat.edu.gh/staffinfo"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

job_elements = soup.find_all("div", class_="card-content")
for job in job_elements:
    title_element = job.find("h2", class_="title")
    company_element = job.find("h3", class_="company")
    location_element = job.find("p", class_="location")
    
    link_url = job.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")
    
    # links = job.find_all("a")[1]
    # for link in links:
    #     link_url = link["href"]
    # print(f"Apply here: {link_url}\n")
    
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    
    print(job, end="\n"*2)

print(soup.contents)
print(results.prettify)

#Find Elements by Class Name and Text Content
python_jobs = results.find_all("h2", string="Senior Python Developer")
print(python_jobs)

#Pass a function to a beautifulsoup object
python_jobs = results.find_all(
    "h2",string=lambda text: "python" in text.lower())

print(len(python_jobs))
# #identify error conditions

python_jobs = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

print(python_jobs)

#extract attributes from html elements








