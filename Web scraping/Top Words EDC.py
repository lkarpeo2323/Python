from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk

nltk.download('stopwords')
nltk.download('punkt')

def extract_top_words(url, num_keywords=10):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    word_freq = Counter(filtered_words)
    return word_freq.most_common(num_keywords)

url = 'https://essentialdata.com/the-importance-of-well-documented-om-procedures-in-automotive-manufacturing/'
print(extract_top_words(url))
