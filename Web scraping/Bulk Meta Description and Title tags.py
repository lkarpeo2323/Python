import pandas as pd
import requests
from bs4 import BeautifulSoup

# Read the Excel file
data = pd.read_excel('Issues.xlsx')

# Assuming the column containing URLs is named 'Page URL'
urls = data['Page URL']

# Loop through each URL in the 'Page URL' column
for url in urls:
    try:
        # Fetch the content from the URL
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract and print title
        title = soup.title.string.strip() if soup.title else 'No title found'
        print(title)
        
        # Extract and print meta description
        meta_description = next((meta.attrs['content'] for meta in soup.find_all('meta') if 'name' in meta.attrs and meta.attrs['name'].lower() == 'description'), 'No meta description found')
        print(meta_description)
        
    except Exception as e:
        print(f"Error fetching metadata for URL {url}: {e}")
