import requests
from bs4 import BeautifulSoup
import re

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

# Example usage
url = 'https://essentialdata.com/service/company-policy-writing/'  # Replace with your URL
phrases = ['technical']  # Replace with your list of phrases

frequencies = count_phrase_frequency_in_article(url, phrases)
for phrase, count in frequencies.items():
    print(f"'{phrase}' appears {count} times.")
