## WEB SCRAPING

This project is a web scraper for extracting job postings from TimesJobs. It fetches job listings based on specific criteria and allows filtering based on skills that the user is not familiar with. The results are stored in text files for further use.

## Features

- Scrape job listings from TimesJobs.
- Extract and display job details such as company name, required skills, and more info link.
- Filter job listings based on unfamiliar skills.
- Save filtered job listings to text files.

## USAGE
Scraping Local HTML Files
The project contains various examples of how to scrape local HTML files using BeautifulSoup. The examples demonstrate:

-> Reading and printing the content of an HTML file.
-> Prettifying the HTML content.
-> Using find and find_all methods to extract specific tags.
-> Extracting and printing only the text content of tags.
-> Combining extracted data into meaningful sentences.


## SCRAPING A WEBSITE
The project includes a script to scrape job listings from TimesJobs. The script fetches the HTML content of the website and extracts job details such as company name, required skills, and the link to more information.

## 1. Filtering Job Listings
The script allows the user to input a skill they are not familiar with. It filters out job listings that require that skill and saves the filtered job details to text files.

## 2. Running the Script
To run the script and start scraping job listings, use the following command:

      python web.py

-> The script will prompt you to enter a skill you are not familiar with and will start scraping job listings. The filtered job details will be saved to text files in the postsTextsaved directory

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `lxml` library

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4 lxml

.
