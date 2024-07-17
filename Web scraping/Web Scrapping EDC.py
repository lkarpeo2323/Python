import requests
from bs4 import BeautifulSoup

url = 'https://essentialdata.com/technical-writers/automotive-technical-writer/'

soup = BeautifulSoup(requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).content, 'html.parser')
print('Title:', soup.title.string.strip() if soup.title else 'No title found')
print('Meta Description:', next((meta.attrs['content'] for meta in soup.find_all('meta') if 'name' in meta.attrs and meta.attrs['name'].lower() == 'description'), 'No meta description found'))
