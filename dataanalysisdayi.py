import requests as rq
from bs4 import BeautifulSoup as bs

url = 'https://www.google.com'
response = rq.get(url)
soup = bs(response.text, 'html.parser')

#Extract title of the page
page_title = soup.title.string
print(f'Page Title: {page_title}')

#Extract specific data (e.g, all the links on the page)
all_links = soup.find_all('a')
for link in all_links:
    print(link.get('href'))