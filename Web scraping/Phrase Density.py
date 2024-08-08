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
            return {}

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the <article> tag and get its text
        article = soup.find('article')
        if article is None:
            print("No <article> tag found.")
            return {}

        content = article.get_text()

        # Count total words
        total_words = len(content.split())

        # Initialize a dictionary to store the phrase density
        phrase_density = {}

        # Count occurrences of each phrase and calculate density
        for phrase in phrases:
            # Using re.IGNORECASE to make the search case-insensitive
            count = len(re.findall(re.escape(phrase), content, re.IGNORECASE))
            density = (count / total_words) * 100  # Density as a percentage
            phrase_density[phrase] = density

        return phrase_density

    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return {}

# Example usage
url = 'https://essentialdata.com/the-principles-about-a-security-procedure/'  # Replace with your URL
phrases = ['security procedure']  # Replace with your list of phrases

densities = calculate_phrase_density(url, phrases)
for phrase, density in densities.items():
    print(f"Phrase '{phrase}' density: {density:.2f}%")
