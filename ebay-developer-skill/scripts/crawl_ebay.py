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
    # Getting Started
    "https://developer.ebay.com/develop/guides-v2/get-started-with-ebay-apis/get-started-with-ebay-apis#understand-the-ebay-apis",
    
    # Sell APIs - Static Guides
    "https://developer.ebay.com/api-docs/sell/static/metadata/getting-metadata.html",
    "https://developer.ebay.com/api-docs/sell/static/seller-accounts/configuring-seller-accounts.html",
    "https://developer.ebay.com/api-docs/sell/static/inventory/managing-inventory-and-offers.html",
    "https://developer.ebay.com/api-docs/sell/static/inventory/managing-inventory-locations.html",
    "https://developer.ebay.com/api-docs/sell/static/orders/handling-orders.html",
    "https://developer.ebay.com/api-docs/sell/static/marketing/marketing-seller-inventory.html",
    "https://developer.ebay.com/api-docs/sell/static/feed/sell-feed.html",
    "https://developer.ebay.com/api-docs/sell/static/finances/finances-landing.html",
    "https://developer.ebay.com/api-docs/sell/static/selling-ig-landing.html",
    "https://developer.ebay.com/api-docs/sell/static/feed/fx-feeds.html",
    "https://developer.ebay.com/api-docs/sell/static/feed/lms-feeds.html",
    
    # v2 Guides (New)
    "https://developer.ebay.com/develop/guides-v2/listing-creation/listing-creation",
    "https://developer.ebay.com/develop/guides-v2/listing-metadata/listing-metadata-guide",
    "https://developer.ebay.com/develop/guides-v2/account-management/account-management-guide",
    "https://developer.ebay.com/develop/guides-v2/order-management/order-management-guide",
    "https://developer.ebay.com/develop/guides-v2/marketing-and-promotions/marketing-and-promotions-guide",
    "https://developer.ebay.com/develop/guides-v2/analytics-and-reporting/analytics-and-reporting-guide",
    "https://developer.ebay.com/develop/guides-v2/communications/sell-communications-guide",
    "https://developer.ebay.com/develop/guides-v2/other-apis/other-apis-guide",
    
    # Buy APIs (New)
    "https://developer.ebay.com/api-docs/buy/static/buying-ig-landing.html",
    "https://developer.ebay.com/api-docs/buy/static/buy-overview.html",
    "https://developer.ebay.com/api-docs/buy/static/buy-requirements.html",
    "https://developer.ebay.com/api-docs/buy/static/api-browse.html",
    "https://developer.ebay.com/api-docs/buy/static/api-deal.html",
    "https://developer.ebay.com/api-docs/buy/static/api-feed.html",
    "https://developer.ebay.com/api-docs/buy/static/api-marketing.html",
    "https://developer.ebay.com/api-docs/buy/static/api-offer.html",
    "https://developer.ebay.com/api-docs/buy/static/api-order.html",
    
    # Guides Landing
    "https://developer.ebay.com/develop/guides",
    
    # Traditional API Guides
    "https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide-landing.html",
    "https://developer.ebay.com/api-docs/user-guides/static/post-order-user-guide-landing.html",
    "https://developer.ebay.com/api-docs/user-guides/static/mip-user-guide-landing.html",
    
    # Legacy DevZone
    "https://developer.ebay.com/Devzone/return-management/Concepts/ReturnManagementAPIGuide.html",
    "https://developer.ebay.com/Devzone/product/Concepts/ProductAPIGuide.html",
    "https://developer.ebay.com/Devzone/product/CallRef/fieldindex.html#FieldIndex",
    "https://developer.ebay.com/Devzone/merchandising/docs/Concepts/merchandisingAPIGuide.html",
    
    # Platform & Notifications
    "https://developer.ebay.com/api-docs/static/platform-notifications-landing.html",
    
    # Regulatory
    "https://developer.ebay.com/develop/guides/regulated-third-party-providers-tpp",
    "https://developer.ebay.com/marketplace-account-deletion",
    
    # Grow
    "https://developer.ebay.com/grow/application-growth-check",
    "https://developer.ebay.com/grow/affiliate-program",
    "https://developer.ebay.com/grow/loyalty-program",
    
    # API Overviews
    "https://developer.ebay.com/api-docs/sell/recommendation/static/overview.html",
    "https://developer.ebay.com/api-docs/sell/marketing/static/overview.html",
    "https://developer.ebay.com/api-docs/sell/analytics/static/overview.html",
    "https://developer.ebay.com/develop/selling-apps/analytics-and-reporting"
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
