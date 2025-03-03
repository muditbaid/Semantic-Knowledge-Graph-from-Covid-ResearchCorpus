import requests
from bs4 import BeautifulSoup

def scrape_text(url):
    """
    Scrapes text content from a given URL.
    
    Parameters:
    url (str): The URL of the webpage to scrape.
    
    Returns:
    str: Extracted text content.
    """
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve page: {url}")
        return ""
    
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    
    text_content = '\n'.join([para.get_text() for para in paragraphs])
    return text_content

if __name__ == "__main__":
    sample_url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    extracted_text = scrape_text(sample_url)
    print(extracted_text[:500])  # Print first 500 characters
