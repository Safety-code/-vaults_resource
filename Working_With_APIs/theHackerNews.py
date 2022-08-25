import json
from urllib import response
import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty'
response = requests.get(url)
print(f"Status code: {response.status_code}")

# Explore the structure of the data
response_dict = response.json()
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)


