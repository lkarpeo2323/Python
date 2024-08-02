import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the webpage to scrape
url = 'https://essentialdata.com/documentation-writers-everything-you-need-to-know/'

# Set up headers with a User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send a GET request with headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Get all <a> tags with href attribute
    links = soup.find_all('a', href=True)
    
    urls = []
    for link in links:
        href = link.get('href')
        # Resolve relative URLs to absolute URLs
        full_url = urljoin(url, href)
        urls.append(full_url)
        print(full_url)

    print(f'\nTotal links found: {len(urls)}')

else:
    print(f"Failed to retrieve the webpage: Status code {response.status_code}")
