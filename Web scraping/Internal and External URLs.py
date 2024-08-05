from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def count_urls_with_selenium(page_url):
    try:
        # Setup Selenium WebDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(page_url)

        # Get page content
        page_content = driver.page_source
        driver.quit()

        # Parse the HTML content
        soup = BeautifulSoup(page_content, 'html.parser')

        # Get the base URL
        base_url = urlparse(page_url)
        base_url_netloc = base_url.netloc

        # Initialize counters
        internal_urls = set()
        external_urls = set()

        # Find all anchor tags
        for anchor in soup.find_all('a', href=True):
            href = anchor['href']
            # Resolve relative URLs to absolute URLs
            full_url = urljoin(page_url, href)
            parsed_url = urlparse(full_url)
            url_netloc = parsed_url.netloc

            # Check if the URL is internal or external
            if url_netloc == base_url_netloc:
                internal_urls.add(full_url)
            else:
                external_urls.add(full_url)

        # Print the results
        print(f"Internal URLs ({len(internal_urls)}):")
        for url in internal_urls:
            print(url)

        print(f"\nExternal URLs ({len(external_urls)}):")
        for url in external_urls:
            print(url)

        return len(internal_urls), len(external_urls)

    except Exception as e:
        print(f"Error: {e}")
        return 0, 0

# Example usage
if __name__ == "__main__":
    url = 'https://essentialdata.com'  # Replace with the URL you want to analyze
    internal_count, external_count = count_urls_with_selenium(url)
    print(f"\nTotal Internal URLs: {internal_count}")
    print(f"Total External URLs: {external_count}")
