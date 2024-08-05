from urllib.request import urlopen

url = 'https://essentialdata.com/service/acceptable-use-policy-writing/'
response = urlopen(url)
html = response.read().decode('utf-8')

print(html)
