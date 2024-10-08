import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def calculate_phrase_density(url, phrases):
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
            return {}, 0

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the <article> tag and get its text
        article = soup.find('article')
        if article is None:
            print("No <article> tag found.")
            return {}, 0

        content = article.get_text()

        # Count total words
        total_words = len(content.split())

        # Initialize dictionaries to store counts and phrase density
        phrase_counts = {}
        phrase_density = {}

        # Count occurrences of each phrase and calculate density
        for phrase in phrases:
            count = len(re.findall(re.escape(phrase), content, re.IGNORECASE))
            phrase_counts[phrase] = count
            density = (count / total_words) * 100  # Density as a percentage
            phrase_density[phrase] = density

        return phrase_counts, total_words

    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return {}, 0

def process_excel(file_path):
    # Load the Excel file
    df = pd.read_excel(file_path)

    # Check if required columns exist
    if 'URL' not in df.columns or 'Keyword' not in df.columns:
        print("Error: The Excel file must contain 'URL' and 'Keyword' columns.")
        return

    # Initialize lists to store results
    results = []

    # Iterate through each row in the DataFrame
    for _, row in df.iterrows():
        url = row['URL']
        phrases = [row['Keyword']]
        
        # Calculate phrase density and total word count
        counts, total_words = calculate_phrase_density(url, phrases)
        
        for phrase in phrases:
            count = counts.get(phrase, 0)
            density = (counts.get(phrase, 0) / total_words) * 100 if total_words > 0 else 0
            results.append({
                'URL': url,
                'Keyword': phrase,
                'Count': count,
                'Total Words': total_words,
                'Density (%)': density
            })
    
    # Create a DataFrame for the results
    results_df = pd.DataFrame(results)
    
    # Save results to a new Excel file
    results_df.to_excel('seo_analysis_results.xlsx', index=False)
    print("SEO analysis completed and results saved to 'seo_analysis_results.xlsx'.")

# Example usage
file_path = 'thinker.xlsx'  # Replace with your Excel file path
process_excel(file_path)
