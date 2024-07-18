from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk
import pandas as pd

# Download the stopwords list
nltk.download('stopwords')
nltk.download('punkt')

def extract_top_words(url, num_keywords=5):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    word_freq = Counter(filtered_words)
    return word_freq.most_common(num_keywords)

# Read the Excel file
file_path = 'Issues.xlsx'
data = pd.read_excel(file_path)

# Assuming the URLs are in a column named 'Page URL'
urls = data['Page URL'].tolist()

results = {}
for url in urls:
    results[url] = extract_top_words(url)

# Print results
for url, keywords in results.items():
    print(f"URL: {url}")
    for word, freq in keywords:
        print(f"  {word}: {freq}")
    print("\n")
