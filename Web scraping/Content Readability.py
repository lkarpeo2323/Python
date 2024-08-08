import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import textstat  # For readability score

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

        # Check for missing or duplicate meta titles
        title = soup.find('title')
        if not title:
            print("SEO Issue: Missing <title> tag")
        else:
            title_text = title.get_text(strip=True)
            print(f"Title: {title_text}")

        # Check for missing meta descriptions
        meta_description = soup.find('meta', attrs={'name': 'description'})
        if not meta_description:
            print("SEO Issue: Missing <meta name='description'> tag")
        else:
            meta_description_content = meta_description.get('content', '').strip()
            print(f"Meta Description: {meta_description_content}")

        # Check for missing or multiple H1 tags
        h1_tags = soup.find_all('h1')
        if not h1_tags:
            print("SEO Issue: Missing <h1> tag")
        elif len(h1_tags) > 1:
            print(f"SEO Issue: Multiple <h1> tags found ({len(h1_tags)} found)")
        else:
            print(f"H1 Tag: {h1_tags[0].get_text(strip=True)}")

        # Check for missing alt attributes in images
        images = soup.find_all('img')
        missing_alt = [img for img in images if not img.get('alt')]
        if missing_alt:
            print(f"SEO Issue: {len(missing_alt)} image(s) missing 'alt' attribute")

        # Check for broken internal links
        internal_links = set()
        broken_links = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag.get('href')
            if href:
                absolute_url = urljoin(url, href)
                parsed_url = urlparse(absolute_url)
                if parsed_url.netloc == urlparse(url).netloc:
                    internal_links.add(absolute_url)
                    try:
                        link_response = requests.head(absolute_url, headers=headers, allow_redirects=True)
                        if link_response.status_code != 200:
                            broken_links.add(absolute_url)
                    except requests.RequestException as e:
                        broken_links.add(absolute_url)

        if broken_links:
            print(f"SEO Issue: {len(broken_links)} broken internal link(s) found")
            for link in broken_links:
                print(f"Broken Link: {link}")

        # Content Length
        content = soup.get_text()
        content_length = len(content.split())
        if content_length < 300:
            print("SEO Issue: Content is too short. Consider adding more content.")

        # Keyword Density
        keywords = ["resource planning"]  # Replace with relevant keywords
        content_words = content.lower().split()
        keyword_count = sum(content_words.count(keyword.lower()) for keyword in keywords)
        keyword_density = (keyword_count / content_length) * 100
        if keyword_density < 1:
            print(f"SEO Issue: Low keyword density for keywords {keywords}. Consider including them more frequently.")

        # Readability
        readability_score = textstat.flesch_kincaid_grade(content)
        print(f"Readability Score (Flesch-Kincaid): {readability_score}")
        if readability_score > 8:
            print("SEO Issue: Content readability is low. Consider simplifying the language.")

        # Header Tags
        headers = soup.find_all(['h2', 'h3', 'h4', 'h5', 'h6'])
        if not headers:
            print("SEO Issue: Missing subheaders. Consider adding header tags to organize content.")

        # Internal Linking
        internal_links = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag.get('href')
            if href:
                absolute_url = urljoin(url, href)
                parsed_url = urlparse(absolute_url)
                if parsed_url.netloc == urlparse(url).netloc:
                    internal_links.add(absolute_url)
        if len(internal_links) < 5:
            print("SEO Issue: Low number of internal links. Consider adding more internal links to improve site navigation.")

        print("SEO Check Completed.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = 'https://essentialdata.com/why-is-business-resource-planning-important/'
check_seo_issues(url)
