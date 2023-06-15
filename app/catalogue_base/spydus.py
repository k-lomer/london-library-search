from app.search_results import Book, SearchResults
import requests
from threading import Thread
import urllib.parse
from bs4 import BeautifulSoup


class Spydus(Thread):
    def __init__(self, query, num_results, base_url, borough):
        super().__init__()
        self.query = query
        self.num_results = num_results
        self.results = SearchResults()
        self.base_url = base_url
        self.borough = borough

    def run(self):
        params = {
            "ENTRY": self.query,
            "ENTRY_NAME": "BS",
            "ENTRY_TYPE": "K",
            "SORTS": "SQL_REL_BIB",
            "GQ": self.query,
            "NRECS": self.num_results
        }
        search_url = self.base_url + "/cgi-bin/spydus.exe/ENQ/WPAC/BIBENQ?" + urllib.parse.urlencode(params)
        search_page = requests.get(search_url)
        search_soup = BeautifulSoup(search_page.content, "html.parser")
        cards = search_soup.find_all("fieldset", {"class": "card-list"})
        threads = []
        for card in cards:
            threads.append(Thread(target=self.get_card_result, args=(card, self.results.results)))
            threads[-1].start()
        for thread in threads:
            thread.join()

    def get_card_result(self, card, results_list):
        card_title = card.find( "h2", {"class": "card-title"})
        card_title_link = card_title.find( "a" )
        item_url = self.base_url + card_title_link["href"]
        item_page = requests.get(item_url)
        item_soup = BeautifulSoup(item_page.content, "html.parser")
        record_format = item_soup.find("div", {"id", "recfrmt"}).text
        record_details = item_soup.find("div", {"id": "divtabRECDETAILS"})
        record_details_rows = record_details.find_all("div", {"class": "row"})
        if record_format == "Books":
            year = "0"
            authors = ""
            for row in record_details_rows:
                if "Main title: " in row.text:
                    title = row.find("a").text
                elif "Author: " in row.text:
                    authors = "; ".join(span.text for span in row.find_all("span", {"class":"d-block"}) )
                elif "Bookmark link: " in row.text:
                    url = row.find("a").text
                elif "Imprint: " in row.text:
                    year = row.text.split()[-1].replace(".", "")

            # Convert the year to a digit or try to get it from somewhere else.
            if not year.isdigit():
                year = item_soup.find("div", {"class": "card-text recdetails"}).find_all("span")[-1].text
            if year.isdigit():
                year = int(year)
            else:
                # Cannot find the year.
                year = 0

            availability_url = self.base_url + item_soup.find("div", {"class", "card-text mt-3"}).a["href"]
            availability_page = requests.get(availability_url)
            availability_soup = BeautifulSoup(availability_page.content, "html.parser")
            libraries = set(loc.text for loc in availability_soup.find_all("td", {"data-caption": "Location"}))

            results_list.append(Book(title, authors, year, self.borough, libraries, url))
