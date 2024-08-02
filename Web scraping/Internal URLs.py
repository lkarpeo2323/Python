import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

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
    
    # Get the base URL for resolving relative links
    base_url = urlparse(url).scheme + '://' + urlparse(url).hostname

    # Function to check if a URL is internal
    def is_internal(url, base_url):
        return urlparse(url).hostname == urlparse(base_url).hostname

    # Get all <a> tags with href attribute
    links = soup.find_all('a', href=True)
    
    internal_links = set()
    for link in links:
        href = link.get('href')
        # Resolve relative URLs to absolute URLs
        full_url = urljoin(url, href)
        if is_internal(full_url, base_url):
            internal_links.add(full_url)

    # Print internal links
    print('Internal Links:')
    for link in internal_links:
        print(link)

else:
    print(f"Failed to retrieve the webpage: Status code {response.status_code}")
