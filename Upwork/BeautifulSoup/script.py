import time
from bs4 import BeautifulSoup
import requests


#Taking user input to filter out unfamiliar skillls
#Taking more than one user input to filter out unfamiliar skillls

print("Put some skill that you are not farmiliar with")
unfamiliar_skill = input('>')
print(f"Filtering out...... {unfamiliar_skill}")

#Sending the output of the program to a file and automate it to run every 10 minutes, using function
def find_jobs():
      html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text

      soup = BeautifulSoup(html_text, "lxml")

      jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
      for index, job in enumerate(jobs):
            posted_date = job.find("span", class_="sim-posted").span.text
            if 'few' in posted_date:
                  company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")
                  skills = job.find("span", class_="srp-skills").text.replace(" ", "")
                  More_Info = job.header.h2.a['href']
                  if unfamiliar_skill not in skills:
                        with open(f'posts/{index}.txt', 'w')as f:
                              f.write(f"Company Name: {company_name.strip()}\n")
                              f.write(f"Required Skills: {skills.strip()}\n")
                              f.write(f"More Information: {More_Info}\n")
                        print(f'File Saved:{index}')
                                

if __name__ == '__main__':
      while True:
            find_jobs()
            time_wait=10
            print(f"Waiting.....{time_wait} seconds")
            time.sleep(time_wait)