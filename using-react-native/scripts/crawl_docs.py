"""
React Native Documentation Crawler
Fetches documentation from official sources and saves as markdown files
"""
import os
import time
import requests
from bs4 import BeautifulSoup
import re

# Configuration
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KNOWLEDGE_DIR = os.path.join(SKILL_DIR, "knowledge")
DELAY = 1.0  # Seconds between requests

# Documentation sources organized by category
DOCS_SOURCES = {
    "core": [
        {
            "name": "expo_getting_started",
            "url": "https://docs.expo.dev/get-started/introduction/",
            "title": "Expo Getting Started"
        },
        {
            "name": "expo_environment_setup",
            "url": "https://docs.expo.dev/get-started/set-up-your-environment/",
            "title": "Expo Environment Setup"
        },
        {
            "name": "expo_router",
            "url": "https://docs.expo.dev/router/introduction/",
            "title": "Expo Router Introduction"
        },
        {
            "name": "expo_eas_build",
            "url": "https://docs.expo.dev/build/introduction/",
            "title": "EAS Build Introduction"
        },
        {
            "name": "expo_eas_submit",
            "url": "https://docs.expo.dev/submit/introduction/",
            "title": "EAS Submit to App Stores"
        },
        {
            "name": "react_native_core_components",
            "url": "https://reactnative.dev/docs/components-and-apis",
            "title": "React Native Core Components"
        },
        {
            "name": "react_native_platform_specific",
            "url": "https://reactnative.dev/docs/platform-specific-code",
            "title": "Platform Specific Code"
        },
    ],
    "firebase": [
        {
            "name": "firebase_getting_started",
            "url": "https://rnfirebase.io/",
            "title": "React Native Firebase Overview"
        },
        {
            "name": "firebase_auth",
            "url": "https://rnfirebase.io/auth/usage",
            "title": "Firebase Authentication"
        },
        {
            "name": "firebase_firestore",
            "url": "https://rnfirebase.io/firestore/usage",
            "title": "Cloud Firestore"
        },
        {
            "name": "firebase_messaging",
            "url": "https://rnfirebase.io/messaging/usage",
            "title": "Firebase Cloud Messaging"
        },
        {
            "name": "firebase_analytics",
            "url": "https://rnfirebase.io/analytics/usage",
            "title": "Firebase Analytics"
        },
    ],
    "navigation": [
        {
            "name": "navigation_getting_started",
            "url": "https://reactnavigation.org/docs/getting-started",
            "title": "React Navigation Getting Started"
        },
        {
            "name": "navigation_stack",
            "url": "https://reactnavigation.org/docs/native-stack-navigator",
            "title": "Stack Navigator"
        },
        {
            "name": "navigation_tabs",
            "url": "https://reactnavigation.org/docs/bottom-tab-navigator",
            "title": "Tab Navigator"
        },
        {
            "name": "navigation_drawer",
            "url": "https://reactnavigation.org/docs/drawer-navigator",
            "title": "Drawer Navigator"
        },
        {
            "name": "navigation_deep_linking",
            "url": "https://reactnavigation.org/docs/deep-linking",
            "title": "Deep Linking"
        },
    ],
    "ui": [
        {
            "name": "paper_getting_started",
            "url": "https://callstack.github.io/react-native-paper/docs/guides/getting-started",
            "title": "React Native Paper Getting Started"
        },
        {
            "name": "paper_theming",
            "url": "https://callstack.github.io/react-native-paper/docs/guides/theming",
            "title": "React Native Paper Theming"
        },
        {
            "name": "gluestack_overview",
            "url": "https://gluestack.io/ui/docs/overview/introduction",
            "title": "Gluestack UI Overview"
        },
        {
            "name": "tamagui_intro",
            "url": "https://tamagui.dev/docs/intro/introduction",
            "title": "Tamagui Introduction"
        },
    ],
    "patterns": [
        {
            "name": "reanimated_fundamentals",
            "url": "https://docs.swmansion.com/react-native-reanimated/docs/fundamentals/getting-started",
            "title": "Reanimated Getting Started"
        },
        {
            "name": "gesture_handler",
            "url": "https://docs.swmansion.com/react-native-gesture-handler/docs/fundamentals/about-handlers",
            "title": "Gesture Handler Fundamentals"
        },
    ]
}

def clean_text(text):
    """Clean and normalize text content."""
    # Remove excessive whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' {2,}', ' ', text)
    return text.strip()

def html_to_markdown(soup, title):
    """Convert HTML soup to simple markdown."""
    # Find main content area
    main = soup.find('main') or soup.find('article') or soup.find('div', class_='markdown') or soup.find('body')
    
    if not main:
        return f"# {title}\n\nContent could not be extracted."
    
    # Remove navigation, footer, scripts
    for tag in main.find_all(['nav', 'footer', 'script', 'style', 'aside']):
        tag.decompose()
    
    # Convert to text with basic formatting
    lines = []
    lines.append(f"# {title}\n")
    
    for element in main.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'pre', 'code', 'ul', 'ol', 'li']):
        if element.name == 'h1':
            lines.append(f"\n## {element.get_text(strip=True)}\n")
        elif element.name == 'h2':
            lines.append(f"\n### {element.get_text(strip=True)}\n")
        elif element.name == 'h3':
            lines.append(f"\n#### {element.get_text(strip=True)}\n")
        elif element.name == 'h4':
            lines.append(f"\n##### {element.get_text(strip=True)}\n")
        elif element.name == 'p':
            text = element.get_text(strip=True)
            if text:
                lines.append(f"{text}\n")
        elif element.name == 'pre':
            code = element.get_text()
            lines.append(f"\n```\n{code}\n```\n")
        elif element.name == 'li':
            text = element.get_text(strip=True)
            if text:
                lines.append(f"- {text}")
    
    content = '\n'.join(lines)
    return clean_text(content)

def fetch_page(url, title):
    """Fetch a documentation page and convert to markdown."""
    print(f"  Fetching: {title}")
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; SkillCrawler/1.0)'
        }
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return html_to_markdown(soup, title)
        else:
            print(f"    Warning: Status {response.status_code}")
            return None
    except Exception as e:
        print(f"    Error: {e}")
        return None

def save_markdown(category, name, content):
    """Save markdown content to file."""
    category_dir = os.path.join(KNOWLEDGE_DIR, category)
    os.makedirs(category_dir, exist_ok=True)
    
    filepath = os.path.join(category_dir, f"{name}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"    Saved: {category}/{name}.md")

def main():
    print("=" * 60)
    print("React Native Documentation Crawler")
    print("=" * 60)
    
    total = sum(len(pages) for pages in DOCS_SOURCES.values())
    fetched = 0
    failed = []
    
    print(f"Total pages to fetch: {total}\n")
    
    for category, pages in DOCS_SOURCES.items():
        print(f"\n=== {category.upper()} ({len(pages)} pages) ===")
        
        for page in pages:
            # Check if already exists
            filepath = os.path.join(KNOWLEDGE_DIR, category, f"{page['name']}.md")
            if os.path.exists(filepath):
                print(f"  Skipping {page['name']} (exists)")
                fetched += 1
                continue
            
            content = fetch_page(page['url'], page['title'])
            if content:
                save_markdown(category, page['name'], content)
                fetched += 1
            else:
                failed.append(page['name'])
            
            time.sleep(DELAY)
    
    print("\n" + "=" * 60)
    print(f"Crawl complete!")
    print(f"Fetched: {fetched}/{total}")
    if failed:
        print(f"Failed ({len(failed)}): {', '.join(failed)}")

if __name__ == "__main__":
    main()
