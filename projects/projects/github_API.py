from email import header
from urllib import response
from wsgiref import headers
import requests

# Making an API call and store the responses
#API call
url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Store API response in a variable.
response_dict = r.json()

#Process results
print(response_dict.keys())