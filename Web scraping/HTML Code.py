from urllib.request import urlopen

url = 'https://portfolio-karpel-website.netlify.app/index.html'
response = urlopen(url)
html = response.read().decode('utf-8')

print(html)
