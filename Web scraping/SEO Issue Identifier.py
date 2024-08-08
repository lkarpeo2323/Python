import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

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

        print("SEO Check Completed.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = 'https://essentialdata.com/service/technical-writing-documentation-services/'
check_seo_issues(url)
