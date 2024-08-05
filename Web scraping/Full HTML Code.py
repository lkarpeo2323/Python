from urllib.request import urlopen

url = 'hhttps://essentialdata.com/service/acceptable-use-policy-writing/'
response = urlopen(url)
html = response.read().decode('utf-8')

print(html)
