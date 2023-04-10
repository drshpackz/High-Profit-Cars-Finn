## Car Information Parser
This repository contains two Python scripts for parsing information about cars from a website and collecting car IDs as links from another website.




# LinkToCarsInfo.py
This script parses information about cars from a website, such as brand, model, year, engine type, and mileage. The script uses the BeautifulSoup library to scrape the website's HTML code and extract the relevant information.

To use this script, you need to provide the URL of the website that contains the car information. The script then goes through each page of the website and extracts the relevant information about each car. The output is saved as a CSV file.

# ParseIDLinks.py
This script collects car IDs as links from a website. The script uses the Requests library to send HTTP requests to the website and the BeautifulSoup library to parse the HTML code and extract the car IDs.

To use this script, you need to provide the URL of the website that contains the car links. The script then goes through each page of the website and extracts the car IDs as links. The output is saved as a text file.
