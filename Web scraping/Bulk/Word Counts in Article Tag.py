import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

def get_total_word_count_in_article(url):
    try:
        # Define headers to mimic a real browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        
        # Fetch the content from the URL
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        # Ensure we have HTML content
        if 'text/html' not in response.headers.get('Content-Type', ''):
            print(f"The content fetched from {url} is not HTML.")
            return 0

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the <article> tag and get its text
        article = soup.find('article')
        if article is None:
            print(f"No <article> tag found in {url}.")
            return 0
        
        content = article.get_text()

        # Convert the content to lowercase and split into words
        words = re.findall(r'\b\w+\b', content.lower())

        # Return the total word count
        return len(words)

    except requests.RequestException as e:
        print(f"Error fetching the URL {url}: {e}")
        return 0

def process_urls_from_excel(excel_file, output_csv):
    # Read the spreadsheet
    df = pd.read_excel(excel_file)
    
    # Check if 'URL' column exists
    if 'URL' not in df.columns:
        print("The 'URL' column is missing in the spreadsheet.")
        return
    
    # Process each URL
    results = []
    for url in df['URL']:
        word_count = get_total_word_count_in_article(url)
        results.append({'URL': url, 'Word Count': word_count})
    
    # Convert results to DataFrame
    results_df = pd.DataFrame(results)
    
    # Save results to CSV
    results_df.to_csv(output_csv, index=False)
    print(f"Results saved to {output_csv}")

# Example usage
excel_file = 'URLs.xlsx'  # Replace with the path to your Excel file
output_csv = 'word_counts.csv'  # Replace with your desired output CSV file name
process_urls_from_excel(excel_file, output_csv)
