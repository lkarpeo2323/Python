import requests
from bs4 import BeautifulSoup

url = 'https://portfolio-karpel-website.netlify.app/index.html'

soup = BeautifulSoup(requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).content, 'html.parser')

#Title
print('Title:', soup.title.string.strip() if soup.title else 'No title found') 

#Meta Description
print('Meta Description:', next((meta.attrs['content'] for meta in soup.find_all('meta') if 'name' in meta.attrs and meta.attrs['name'].lower() == 'description'), 'No meta description found'))

#h1
print(soup.h1)

#h2
print(soup.h2)

#h3
print(soup.h3)
