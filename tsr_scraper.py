import requests
from bs4 import BeautifulSoup
import time
import csv
from urllib.parse import urljoin


def parse_link_prefix(link):
    """
    Removes the string after 'downloads/' in a given URL to parse all item links
    """
    if "downloads/" in link:
        return link.split("downloads/")[0] + "downloads/"
    return link + "downloads/details/category/"


def scrape_tsr_links(start_page, end_page, page_url):
    """
    Scrape download links from The Sims Resource pages
    """

    base_url = page_url + "/skipsetitems/1/page/{}/cnt/3020"
    link_prefix = parse_link_prefix(page_url)

    all_links = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print(f"Starting scrape from page {start_page} to {end_page}...")

    for page_num in range(start_page, end_page + 1):
        url = base_url.format(page_num)

        try:
            print(f"Scraping page {page_num}...")
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")

            links = soup.find_all("a", href=True)

            page_links = []
            for link in links:
                href = link["href"]
                absolute_url = urljoin(url, href)

                if absolute_url.startswith(link_prefix):
                    if absolute_url not in all_links:
                        all_links.append(absolute_url)
                        page_links.append(absolute_url)

            print(f"  Found {len(page_links)} new links on page {page_num}")
            print(f"  Total unique links so far: {len(all_links)}")

            time.sleep(2)

        except requests.exceptions.RequestException as e:
            print(f"Error scraping page {page_num}: {e}")
            continue

    return all_links


def save_links_to_file(links, filename="tsr_links.txt"):
    """Save links to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        for link in links:
            f.write(link + "\n")
    print(f"\nSaved {len(links)} links to {filename}")


def save_links_to_csv(links, filename="tsr_links.csv"):
    """Save links to a CSV file"""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["URL"])
        for link in links:
            writer.writerow([link])
    print(f"Saved {len(links)} links to {filename}")


def process_url(page_url):
    if page_url.endswith("/skipsetitems/1"):
        return page_url.removesuffix("/skipsetitems/1")
    elif (
        page_url.endswith("browse/category/sims4")
        or page_url.endswith("browse/category/sims3")
        or page_url.endswith("browse/category/sims2")
        or page_url.endswith("browse/category/sims1")
    ):
        return page_url
    else:
        return 0


if __name__ == "__main__":

    print("What is the base page url of the author?")
    page_url = process_url(input())

    if page_url == 0:
        exit()

    print("What is the start page of the author?")
    start_page = int(input())

    print("What is the end page of the author?")
    end_page = int(input())

    links = scrape_tsr_links(start_page, end_page, page_url)

    print(f"\n{'='*50}")
    print(f"Scraping complete!")
    print(f"Total unique links found: {len(links)}")
    print(f"{'='*50}\n")

    # Save to both text and CSV files
    save_links_to_file(links, "tsr_links.txt")
    save_links_to_csv(links, "tsr_links.csv")

    # Display first 5 links as preview
    if links:
        print("\nFirst 5 links (preview):")
        for i, link in enumerate(links[:5], 1):
            print(f"{i}. {link}")
