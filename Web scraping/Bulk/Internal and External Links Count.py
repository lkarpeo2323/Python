import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Function to check if a URL is internal
def is_internal(url, base_url):
    return urlparse(url).hostname == urlparse(base_url).hostname

# Function to get the count of internal links from a single URL
def count_internal_links(url):
    internal_links = set()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            base_url = urlparse(url).scheme + '://' + urlparse(url).hostname
            links = soup.find_all('a', href=True)
            for link in links:
                href = link.get('href')
                full_url = urljoin(url, href)
                if is_internal(full_url, base_url):
                    internal_links.add(full_url)
    except Exception as e:
        print(f"Error processing {url}: {e}")
    return len(internal_links)

# Load URLs from Excel
excel_file = 'Issues.xlsx'
sheet_name = 'Sheet2'  # Update this if the sheet name is different

df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Check if 'Page URL' column exists
if 'Page URL' not in df.columns:
    raise ValueError("The 'Page URL' column is not found in the Excel file.")

# Create a list to store results
results = []

# Iterate over URLs and get count of internal links
for url in df['Page URL'].dropna():
    print(f"Processing URL: {url}")
    count = count_internal_links(url)
    results.append((url, count))

# Print results
print('\nInternal Links Count per URL:')
for url, count in results:
    print(f"{url}: {count} internal links")

# Optionally, you can save the results to a new Excel file
results_df = pd.DataFrame(results, columns=['Page URL', 'Internal Links Count'])
results_df.to_excel('Internal_Links_Count.xlsx', index=False)
