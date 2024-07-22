import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords

# Ensure the stopwords are downloaded
nltk.download('stopwords')

def get_top_words(url, top_n=10):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # Fetch the content from the URL
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the text from the page, filtering out scripts, styles, and irrelevant sections
        for element in soup(['script', 'style', 'header', 'footer', 'nav', 'aside']):
            element.decompose()

        text = soup.get_text(separator=' ')

        # Remove non-alphabetic characters and split the text into words
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in words if word not in stop_words]

        # Count the occurrences of each word
        word_counts = Counter(filtered_words)

        # Get the most common words
        top_words = word_counts.most_common(top_n)

        return top_words

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve {url}. Error: {e}")
        return []

# Example usage
url = 'https://essentialdata.com/what-is-medical-writing/'
top_words = get_top_words(url)

print(f"Top words in {url}:")

for word, count in top_words:
    print(f"{word}: {count}")
