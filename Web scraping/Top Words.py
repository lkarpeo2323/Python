from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk

# Download the stopwords list
nltk.download('stopwords')
nltk.download('punkt')

def extract_keywords(url, num_keywords=10):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()

    # Tokenize and remove stopwords
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    # Count word frequencies
    word_freq = Counter(filtered_words)
    return word_freq.most_common(num_keywords)

url = 'https://portfolio-karpel-website.netlify.app/index.html'
print(extract_keywords(url))
