from app.search_results import Book, SearchResults
import feedparser
import html
import requests
import re
import urllib.parse
from bs4 import BeautifulSoup


class SirsiDynix:
    def __init__(self, base_url, borough, query_location, library_borough_name, num_results):
        self.base_url = base_url
        self.borough = borough
        self.query_location = query_location
        self.library_borough_name = library_borough_name
        self.num_results = num_results

    def get_results(self, query):
        results = SearchResults()
        params = {
            "qu": query,
            "qf": "FORMAT	Format	BOOK	Books",
            "te": "ILS",
            "h": "1",
            "lm": self.query_location
        }
        search_url = self.base_url + "/" + urllib.parse.urlencode(params)
        feed = feedparser.parse(search_url)
        for entry in feed.entries[:self.num_results]:
            entry_details = self.get_feed_result(entry)
            results.add_result(entry_details)
        return results

    def get_feed_result(self, entry):
        title = html.unescape(entry["title"].rsplit(" / ", 1)[0])
        if title.startswith("Title "):
            title = title.replace("Title ", "", 1)
        if title.startswith("First Title value, for Searching "):
            title = title.replace("First Title value, for Searching ", "", 1)
        summary = entry["summary"].split("<br />")
        author = ""
        year = 0
        author_indicator = "by"
        date_indicator = "Publication Date"
        for s in summary:
            if s.startswith(author_indicator):
                author = html.unescape(s.partition("&#160;")[2])
                if author.endswith("."):
                    author = author[:-1]
            elif s.startswith(date_indicator):
                year = int(re.sub("\\D", "", s.partition("&#160;")[2])[-4:])
        url = entry["link"]
        entry_page = requests.get(url)
        entry_soup = BeautifulSoup(entry_page.content, "html.parser")
        libraries = set(row.find("td", {"class": "detailItemsTable_LIBRARY"}).find("div", {"class": "hidden"}).text for row in entry_soup.find_all("tr", {"class": "detailItemsTableRow"}))
        if self.library_borough_name:
            libraries = (library.replace(" (" + self.library_borough_name + ")", "") for library in libraries if library.endswith("(" + self.library_borough_name + ")") or library[-1] != ")")
        return Book(title, author, year, self.borough, libraries, url)
