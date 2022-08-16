import requests
from bs4 import BeautifulSoup



base_url = "http://pythonjobs.github.io/"
page = requests.get(base_url)
soup = BeautifulSoup(page.content, "html.parser")
page_results = soup.find(id="content")

#print(page_results.prettify)

jobs = soup.find_all("section", class_= "job_list")
for job in jobs:    
    job_title = job.find("h1")
    job_detail = job.find("p", class_="detail")
    other_info = job.find("span", class_="info") 
       
    print(job_title.text)
    print(job_detail.text)
    print(other_info.text)
    

