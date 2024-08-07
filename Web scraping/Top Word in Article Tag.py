import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def count_word_frequency_in_article(url):
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

        # Convert the content to lowercase and remove non-alphanumeric characters
        words = re.findall(r'\b\w+\b', content.lower())

        # Count the frequency of each word
        word_count = Counter(words)

        return word_count

    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return {}

# Example usage
url = 'https://essentialdata.com/service/company-policy-writing/'  # Replace with your URL

word_frequencies = count_word_frequency_in_article(url)
for word, count in word_frequencies.items():
    print(f"'{word}' appears {count} times.")
