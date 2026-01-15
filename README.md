# The Sims Resource Scraper

## Description
The Sims Resource Scraper is a Python script designed to scrape download links from The Sims Resource (TSR) website. It collects links to downloadable content and saves them in both text and CSV formats for easy access.

## Features
- Scrapes download links from TSR pages.
- Saves links to a text file (`tsr_links.txt`).
- Saves links to a CSV file (`tsr_links.csv`).
- Handles pagination and avoids duplicate links.

## Requirements
- Python 3.6+
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`

## Installation
1. Clone this repository or download the script.
2. Install the required dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage
1. Run the script:
   ```bash
   python tsr_scraper.py
   ```
2. Follow the prompts:
   - Enter the base page URL of the author.
   - Enter the start and end page numbers to scrape.
3. The script will scrape the links and save them to `tsr_links.txt` and `tsr_links.csv`.

## Example
```
What is the base page url of the author?
https://www.thesimsresource.com/members/AuthorName/downloads/browse/category/sims4
What is the start page of the author?
1
What is the end page of the author?
5
```

## Output
- `tsr_links.txt`: Contains all the scraped links in plain text format.
- `tsr_links.csv`: Contains all the scraped links in CSV format.

## Notes
- Ensure the base URL is correct and points to the author's download page.
- The script includes a polite delay between requests to avoid overloading the server.

## License
This project is licensed under the Copyleft License. You are free to use, modify, and distribute this software, provided that all modifications and derivatives are also licensed under the same terms.