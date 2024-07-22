import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def get_top_words(url, top_n=10):
    # Fetch the content from the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    text = soup.get_text()

    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    word_counts = Counter(words)

    top_words = word_counts.most_common(top_n)

    return top_words

url = 'https://portfolio-karpel-website.netlify.app/index.html'
top_words = get_top_words(url)

print(f"Top words in {url}:")

for word, count in top_words:
    print(f"{word}: {count}")
