from bs4 import BeautifulSoup
import requests

response = requests.get('https://portfolio-karpel-website.netlify.app/index.html')
soup = BeautifulSoup(response.text, 'html.parser')


print(soup.title.text) #Title tag

print(soup.h1.text) #h1 tag

print(soup.h2.text) #h2 tag

