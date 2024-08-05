import pandas as pd
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import nltk

# Ensure you have the necessary NLTK data
nltk.download('punkt')

def get_total_word_count(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # Fetch the content of the page
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching the page {url}: {e}")
        return 0

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text from the HTML
    text = soup.get_text()

    # Tokenize the text
    words = word_tokenize(text)

    # Count the total number of words
    total_word_count = len([word for word in words if word.isalpha()])

    return total_word_count

# Load the Excel file
excel_file = 'Mom.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')

# Ensure there is a 'URL' column in the DataFrame
if 'URL' not in df.columns:
    raise ValueError("The Excel file must contain a column named 'URL'.")

# Create a new column for word counts
df['Word Count'] = df['URL'].apply(get_total_word_count)

# Save the results to a new Excel file
output_file = 'Mom_with_word_counts.xlsx'
df.to_excel(output_file, index=False)

print(f"Word counts have been added to {output_file}")
