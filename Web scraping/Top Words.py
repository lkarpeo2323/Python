import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

# Function to fetch and parse HTML content
def fetch_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch page, status code: {response.status_code}")

# Function to extract text from HTML
def extract_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract text from title, meta description, and headings
    title = soup.title.string if soup.title else ""
    meta_description = soup.find('meta', attrs={'name': 'description'})
    meta_description = meta_description['content'] if meta_description else ""
    headings = ' '.join([h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])])
    
    # Combine all text into a single string
    text = f"{title} {meta_description} {headings}"
    return text

# Function to extract keywords from text
def extract_keywords(text, num_keywords=10):
    # Clean and split text
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Remove common stopwords
    stopwords = set([
        'the', 'and', 'is', 'in', 'to', 'with', 'of', 'a', 'for', 'on', 'that', 'it', 'as', 'was', 'at', 'by', 'an', 'be', 'this', 'which', 'or', 'from'
    ])
    
    words = [word for word in words if word not in stopwords]
    
    # Count word frequencies
    word_counts = Counter(words)
    
    # Get the most common words
    keywords = word_counts.most_common(num_keywords)
    return keywords

# Main function
def main(url):
    try:
        html = fetch_html(url)
        text = extract_text(html)
        keywords = extract_keywords(text)
        
        print("Extracted Keywords:")
        for keyword, frequency in keywords:
            print(f"{keyword}: {frequency}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    url = 'https://essentialdata.com/documentation-services/clinical-documentation/'  # Replace with your URL
    main(url)
