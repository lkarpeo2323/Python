import pandas as pd
import requests
from bs4 import BeautifulSoup

# Function to get title and meta description from a URL
def get_meta_data(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.title.string.strip() if soup.title else 'No title found'
        
        meta_description = next(
            (meta.attrs['content'] for meta in soup.find_all('meta') if 'name' in meta.attrs and meta.attrs['name'].lower() == 'description'),
            'No meta description found'
        )
        
        return title, meta_description
    except Exception as e:
        return f"Error: {e}", f"Error: {e}"

# Read the Excel file
file_path = 'Issues.xlsx'
data = pd.read_excel(file_path)

# Assuming the URLs are in a column named 'Page URL'
urls = data['Page URL']

# Prepare the results list
results = []

# Loop through each URL and fetch the meta data
for url in urls:
    title, meta_description = get_meta_data(url)
    results.append({
        'URL': url,
        'Title': title,
        'Meta Description': meta_description
    })

# Convert results to DataFrame
results_df = pd.DataFrame(results)

# Save to CSV
csv_file_path = 'meta_data_results.csv'
results_df.to_csv(csv_file_path, index=False)

print(f"Results have been saved to {csv_file_path}")
