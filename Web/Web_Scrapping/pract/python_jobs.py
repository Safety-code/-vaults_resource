import requests
from bs4 import BeautifulSoup
import html5lib

job_url = "https://pythonjobs.github.io/"
page = requests.get(job_url)

#create beautifulsoup objects
soup = BeautifulSoup(page.content, "html5lib")
page_results = soup.find(id="content")

job_elements = page_results.find_all("div", class_="job")
   
for jobs in job_elements:
    job_title = jobs.h1.text
    job_url = jobs.a["href"]
    job_location = jobs.span.text
    
    print(f"Job Title: {job_title}" )
    print(f"URL of the Job: {job_url}")
    print(f"Remote or Onsite: {job_location}")
    print()
    
others_in_span = job_elements.find_all("span"
, class_="info")

for others in others_in_span:
    print(others.text)    
    