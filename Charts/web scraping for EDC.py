import requests
from bs4 import BeautifulSoup

url = 'https://essentialdata.com/technical-writers/automotive-technical-writer/'

try:
    # Fetch the content from the URL
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract title
        title = soup.title.string.strip() if soup.title else 'No title found'

        # Extract meta description
        meta_description = 'No meta description found'
        for meta in soup.find_all('meta'):
            if 'name' in meta.attrs and meta.attrs['name'].lower() == 'description':
                meta_description = meta.attrs['content']
                break

        # Print the extracted metadata
        print('Title:', title)
        print('Meta Description:', meta_description)

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Failed to fetch URL: {e}")
