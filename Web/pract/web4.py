from cgitb import html
from gettext import find
from re import U
from time import time, time_ns
import requests
from bs4 import BeautifulSoup
import bs4

print("Put some skills that you are farmiliar with")
unfarmiliar_skill = input(">")
print(f"Filtering out {unfarmiliar_skill}")


def find_jobs():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    soupobj = BeautifulSoup(html_text, "lxml")
    jobs = soupobj.find_all("li", class_="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        published_date = job.find("span", class_="sim-posted").span.text
        if "few" in published_date:
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")
            skills = job.find("span", class_="srp-skills").text.replace(" ", "")
            more_info = job.header.h2.a["href"]
            if unfarmiliar_skill not in skills:
                with open(f"posts/{index}.txt", "w") as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Skills Requirement: {skills.strip()}\n")
                    f.write(f"More Info: {more_info}")
                print(f"File saved: {index}")
                
if __name__ == "--main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting for {time_wait} minutes.....")
        time.sleep(time_wait * 60)
            
    

       
