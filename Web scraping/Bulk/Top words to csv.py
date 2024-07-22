import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
import pandas as pd

# Ensure the stopwords are downloaded
nltk.download('stopwords')

def get_top_words(url, top_n=5):
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

# Read the Excel file
file_path = 'Issues.xlsx'
data = pd.read_excel(file_path)

# Assuming the URLs are in a column named 'Page URL'
urls = data['Page URL'].tolist()

results = []
for url in urls:
    keywords = get_top_words(url)
    for word, freq in keywords:
        results.append({
            'URL': url,
            'Keyword': word,
            'Frequency': freq
        })

# Convert results to DataFrame
results_df = pd.DataFrame(results)

# Save to CSV
csv_file_path = 'top_keywords.csv'
results_df.to_csv(csv_file_path, index=False)

print(f"Results have been saved to {csv_file_path}")
