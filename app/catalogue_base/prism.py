from app.search_results import Book, SearchResults
from math import ceil
import requests
from threading import Thread
import urllib.parse
from bs4 import BeautifulSoup


class Prism(Thread):
    def __init__(self, query, num_results, base_url, borough):
        super().__init__()
        self.query = query
        self.num_results = num_results
        self.results = SearchResults()
        self.base_url = base_url
        self.borough = borough

    def run(self):
        pages = ceil(self.num_results / 10)
        threads = []
        for page in range(pages):
            params = {
                "query": self.query + " AND format:(book) AND NOT format:(electronic_resource) AND NOT format:(ebook)",
                "offset": page * 10
            }
            search_url = self.base_url + "items?" + urllib.parse.urlencode(params)
            threads.append(Thread(target=self.get_page_results, args=(search_url, self.results.results)))
            threads[-1].start()
        for thread in threads:
            thread.join()

    def get_page_results(self, search_url, results_list):
        search_page = requests.get(search_url)
        search_soup = BeautifulSoup(search_page.content, "html.parser")
        items = search_soup.find_all("div", {"class": "item"})
        threads = []
        for item in items:
            threads.append(Thread(target=self.get_item_result, args=(item, results_list)))
            threads[-1].start()
        for thread in threads:
            thread.join()

    def get_item_result(self, item, results_list):
        title_h2 = item.find("h2", {"class": "title"})
        title = title_h2.text.strip()
        item_url = self.base_url + title_h2.find("a")["href"]
        item_page = requests.get(item_url)
        item_soup = BeautifulSoup(item_page.content, "html.parser")

        # Get authors.
        tags = item_soup.find("div", {"class": "tagbox"}).find_all("h3")
        authors = ""
        for tag in tags:
            if tag.text == "Author":
                author_tags = tag.findNext("ul")
                if author_tags is not None:
                    author_tags = author_tags.find_all("a")
                    authors = "; ".join(author.text for author in author_tags)
                break
        # Get year.
        year = "0"
        publisher = item_soup.find("div", {"class": "publisher"})
        if publisher is not None:
            publisher_name = publisher.find("span", {"itemprop": "name"})
            if publisher_name:
                year = publisher_name.text[-4:]
        # Convert the year to a digit.
        if year.isdigit():
            year = int(year)
        else:
            # Cannot find the year.
            year = 0

        # Get libraries.
        libraries = []
        availability = item_soup.find("div", {"id": "availability"})
        if availability is not None:
            options = availability.find("ul", {"class": "options"})
            if options is not None:
                libraries = [ span.text for span in options.find_all("span", {"itemprop": "name"})]
        if len(libraries) > 0:
            results_list.append(Book(title, authors, year, self.borough, libraries, item_url))
