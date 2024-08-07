import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def count_phrase_frequency_in_article(url, phrases):
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
            print("The content fetched is not HTML.")
            return {}

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the <article> tag and get its text
        article = soup.find('article')
        if article is None:
            print("No <article> tag found.")
            return {}
        
        content = article.get_text()

        # Print the first 1000 characters of the content for debugging
        print("Content snippet:", content[:1000])

        # Initialize a dictionary to store the frequency of each phrase
        phrase_count = {phrase: 0 for phrase in phrases}

        # Count occurrences of each phrase
        for phrase in phrases:
            # Using re.IGNORECASE to make the search case-insensitive
            phrase_count[phrase] = len(re.findall(re.escape(phrase), content, re.IGNORECASE))

        return phrase_count

    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return {}

def process_excel(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file)

    # Initialize lists to store results
    results = []

    # Process each row
    for index, row in df.iterrows():
        url = row['URL']
        phrases = [row['KW']]  # Assuming 'kw' is the column with the phrases

        # Get phrase frequency for each URL
        frequencies = count_phrase_frequency_in_article(url, phrases)
        
        # Store the results
        for phrase, count in frequencies.items():
            results.append({'URL': url, 'Phrase': phrase, 'Count': count})

    # Convert results to a DataFrame and save to an Excel file
    results_df = pd.DataFrame(results)
    results_df.to_excel(output_file, index=False)

# Example usage
input_file = 'Copy of newest.xlsx'  # Replace with your input file name
output_file = 'word_counts.xlsx'  # Replace with your output file name
process_excel(input_file, output_file)
