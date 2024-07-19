from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://portfolio-karpel-website.netlify.app/index.html')
bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.h1)
print(bs.h2)
print(bs.title)
