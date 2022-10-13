import re
import requests
from bs4 import BeautifulSoup
import lxml

source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')

for article in soup.find('article'):
    headline = article.h2.a.text
    print(headline)
    
    summary = article.find('div', class_='entry-content').p.text
    print(summary)
    
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    
    print(yt_link)
    
    print()

headline = article.h2.a.text
print(headline)

summary = article.find('div', class_='entry-content').p.text
print(summary)

vid_src = article.find('iframe', class_='youtube-player')['src']
print(vid_src)

vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
print(vid_id)

# creating our own youtube links
yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)
print()