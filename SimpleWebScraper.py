import requests
from bs4 import BeautifulSoup

# Function to extract and display data from a website
def scrape_website(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        
        # Raise an error if the request failed
        response.raise_for_status()

        # Parse the website's HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all article titles or headlines based on HTML tags (this might vary depending on the website)
        # For example, assuming article titles are in <h2> tags with class 'title':
        article_titles = soup.find_all('h2', class_='title')

        # Check if any titles are found
        if not article_titles:
            print("No articles found. The website structure might be different.")
        else:
            print("Article Titles:")
            for i, title in enumerate(article_titles, start=1):
                print(f"{i}. {title.get_text()}")
    
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error: Unable to connect to the website. Details: {e}")
    except Exception as e:
        # Handle other exceptions such as parsing errors
        print(f"An error occurred: {e}")

# Main function to get user input and scrape the website
def main():
    print("Welcome to the Simple Web Scraper!")
    url = input("Enter the URL of the website to scrape: ")
    scrape_website(url)

# Start the web scraper
if __name__ == "__main__":
    main()
