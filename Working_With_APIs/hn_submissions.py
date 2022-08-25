from operator import itemgetter
from urllib import response
import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty' 
response = requests.get(url)
print(f"Status code: {response.status_code}")

# Process information about each submission.
submission_ids = response.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    response = requests.get(url)
    print(f"id: {submission_id}\tStatus code: {response.status_code}")
    response_dict = response.json()
    
    # Build a dictionary for each article.
    submission_dict={
        'title': response_dict['title'],
        'link': f'http://news.ycombinator.com/item?id={submission_ids}',
        'comments': response_dict['descendants']
    }
    
    submission_dicts.append(submission_dict)
    
    submission_dicts = sorted(submission_dict, key=itemgetter('comments'), reverse=True)
    
    for submission_dict in submission_dicts:
        print(f"Title: {submission_dict['title']}")
        print(f"Discussion link: {submission_dict['link']}")
        print(f"Comments: {submission_dict['comments']}")
        