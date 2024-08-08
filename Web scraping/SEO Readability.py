import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import textstat  # For readability score

def provide_recommendations(title, meta_description, h1_tag, images, keyword_density, readability_score, header_tags, internal_links):
    recommendations = []

    # Title Recommendations
    if not title:
        recommendations.append("Consider adding a <title> tag to the page. It should be unique and descriptive.")
    elif len(title) > 60:
        recommendations.append("The <title> tag is too long. Consider keeping it under 60 characters to avoid truncation in search results.")

    # Meta Description Recommendations
    if not meta_description:
        recommendations.append("Add a <meta name='description'> tag. It should be a concise summary of the page content (150-160 characters).")
    elif len(meta_description) > 160:
        recommendations.append("The meta description is too long. Consider shortening it to 150-160 characters.")

    # H1 Tag Recommendations
    if not h1_tag:
        recommendations.append("Add an <h1> tag to the page. It should include the main topic or keyword for the page.")
    elif len(h1_tag) > 70:
        recommendations.append("The <h1> tag is too long. Consider keeping it under 70 characters for better readability.")

    # Image Alt Attributes Recommendations
    if len(images) > 0:
        recommendations.append(f"{len(images)} image(s) missing 'alt' attributes. Add descriptive 'alt' text to improve accessibility and SEO.")

    # Keyword Density Recommendations
    if keyword_density < 1:
        recommendations.append("Consider increasing the keyword density for your target keywords. Aim for 1-2% density, but ensure it reads naturally.")
    
    # Readability Recommendations
    if readability_score > 8:
        recommendations.append("The content readability is low. Aim for a Flesch-Kincaid Grade Level under 8 for better accessibility.")

    # Header Tags Recommendations
    if len(header_tags) == 0:
        recommendations.append("Consider adding header tags (e.g., <h2>, <h3>) to structure the content and improve readability.")
    
    # Internal Linking Recommendations
    if len(internal_links) < 5:
        recommendations.append("Add more internal links to other relevant pages on your site to enhance site navigation and user engagement.")

    return recommendations

def check_seo_issues(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Send a GET request to the URL with headers
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error: Unable to access URL {url}. Status code: {response.status_code}")
            return

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'lxml')

        # Extract relevant elements
        title = soup.find('title').get_text(strip=True) if soup.find('title') else None
        meta_description = soup.find('meta', attrs={'name': 'description'}).get('content', '').strip() if soup.find('meta', attrs={'name': 'description'}) else None
        h1_tags = [tag.get_text(strip=True) for tag in soup.find_all('h1')]
        h1_tag = h1_tags[0] if h1_tags else None
        images = soup.find_all('img')
        content = soup.get_text()
        content_length = len(content.split())
        keywords = ["resource planning"]  # Replace with relevant keywords
        content_words = content.lower().split()
        keyword_count = sum(content_words.count(keyword.lower()) for keyword in keywords)
        keyword_density = (keyword_count / content_length) * 100 if content_length > 0 else 0
        readability_score = textstat.flesch_kincaid_grade(content)
        header_tags = soup.find_all(['h2', 'h3', 'h4', 'h5', 'h6'])
        internal_links = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag.get('href')
            if href:
                absolute_url = urljoin(url, href)
                parsed_url = urlparse(absolute_url)
                if parsed_url.netloc == urlparse(url).netloc:
                    internal_links.add(absolute_url)

        # Provide recommendations
        recommendations = provide_recommendations(title, meta_description, h1_tag, images, keyword_density, readability_score, header_tags, internal_links)
        for rec in recommendations:
            print(rec)

        print("SEO Check Completed.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = 'https://essentialdata.com/why-is-business-resource-planning-important/'
check_seo_issues(url)
