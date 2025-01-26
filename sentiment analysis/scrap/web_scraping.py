import requests
from bs4 import BeautifulSoup
import certifi
import csv

# Function to scrape data from a website
def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data from the webpage as needed
        # For example, let's extract all the links on the page
        links = [a['href'] for a in soup.find_all('a', href=True)]

        return links
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

# Function to save data to a CSV file
def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write the header if needed
        # csv_writer.writerow(['Column1', 'Column2', ...])

        # Write data to the CSV file
        for row in data:
            csv_writer.writerow([row])

if __name__ == "__main__":
    # URL to scrape data from
    target_url = "https://www.nltk.org/"

    # Call the scraping function
    scraped_data = scrape_website(target_url)

    if scraped_data:
        # Specify the CSV file name
        csv_filename = "scraped_data.csv"

        # Call the function to save data to CSV
        save_to_csv(scraped_data, csv_filename)

        print(f"Data successfully scraped and saved to {csv_filename}")
    else:
        print("Error in scraping data.")
