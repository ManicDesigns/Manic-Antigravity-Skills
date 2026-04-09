import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from markdownify import markdownify as md

# Configuration
BASE_URL = "https://developer.ebay.com"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "knowledge")
DELAY = 1.0  # Seconds between requests

# Targeted URLs from User Request
TARGET_URLS = [
    "https://developer.ebay.com/develop/api/sell/inventory_mapping",
    "https://developer.ebay.com/develop/api/sell/catalog#sell-catalog-product-getproduct",
    "https://developer.ebay.com/develop/api/sell/catalog#sell-catalog-search-search",
    "https://developer.ebay.com/develop/api/sell/negotiation",
    "https://developer.ebay.com/develop/api/sell/identity_api#sell-identity_api--getuser",
    "https://developer.ebay.com/develop/api/sell/error_codes",
    "https://developer.ebay.com/develop/guides-v2/authorization#overview",
    "https://developer.ebay.com/develop/guides-v2/listing-creation#overview",
    "https://developer.ebay.com/develop/guides-v2/listing-management#api-use-case",
    "https://developer.ebay.com/develop/guides-v2/listing-metadata-guide#api-use-cases",
    "https://developer.ebay.com/develop/guides-v2/account-management-guide#error-handling",
    "https://developer.ebay.com/develop/guides-v2/analytics-and-reporting-guide#error-handling",
    "https://developer.ebay.com/develop/guides-v2/analytics-and-reporting-guide#overview",
    "https://developer.ebay.com/develop/guides-v2/sell-communications-guide#api-use-cases",
    "https://developer.ebay.com/develop/guides-v2/order-management-guide#overview",
    "https://developer.ebay.com/develop/guides-v2/marketing-and-promotions-guide#api-use-cases",
    "https://developer.ebay.com/develop/guides-v2/other-apis-guide#api-use-case",
    "https://developer.ebay.com/develop/guides-v2/digital-signatures-for-apis#apis-in-scope",
    "https://developer.ebay.com/develop/guides-v2/marketplace-user-account-deletion#overview"
]

visited = set()

def fetch_page(url):
    """Fetches a page with rate limiting."""
    print(f"Fetching: {url}")
    try:
        response = requests.get(url, timeout=15) # Increased timeout
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed: {response.status_code} for {url}")
            return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None
    finally:
        time.sleep(DELAY)

def infer_category(url):
    """Infers a category from the URL."""
    if "sell" in url:
        return "sell"
    elif "buy" in url:
        return "buy"
    elif "grow" in url:
        return "grow"
    elif "devzone" in url.lower():
        return "legacy_devzone"
    elif "guides" in url:
        return "guide"
    else:
        return "general"

def save_markdown(category, title, html_content, original_url):
    """Saves HTML content as Markdown."""
    if not html_content:
        return
        
    # Improved markdownify with code block safety
    markdown = md(html_content, heading_style="ATX", code_language="json")
    
    # Clean up filename
    safe_title = "".join([c if c.isalnum() else "_" for c in title]).lower()[:100] # Limit length
    filename = f"{category}_{safe_title}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"Source: {original_url}\n\n")
        f.write(markdown)
    print(f"Saved: {filename}")

def parse_and_process(url):
    """Parses page, saves content, and finds next links."""
    html = fetch_page(url)
    if not html:
        return

    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract Title
    title = soup.title.string.strip() if soup.title else "Untitled"
    if "eBay Developers Program" in title:
        title = title.replace(" | eBay Developers Program", "").strip()
    
    # Extract Main Content
    # eBay docs structure varies. Try to grab the most relevant container.
    content = soup.find('div', class_='id-docs-content')
    if not content:
         content = soup.find('div', id='mainContent')
    if not content:
        content = soup.find('main')
    if not content:
        content = soup.body

    category = infer_category(url)
    save_markdown(category, title, str(content), url)

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    for url in TARGET_URLS:
        clean_url = url.split('#')[0] # Remove anchors for fetching
        if clean_url not in visited:
            visited.add(clean_url)
            parse_and_process(clean_url)

if __name__ == "__main__":
    main()
