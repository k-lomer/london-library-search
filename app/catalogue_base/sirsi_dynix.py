from app.search_results import Book, SearchResults
import feedparser
import html
import requests
import re
import urllib.parse
from bs4 import BeautifulSoup
import charset_normalizer


class SirsiDynix:
    def __init__(self, base_url, borough, query_location, library_borough_name, query_location_is_lm=True, library_suffix_enforced=True):
        self.base_url = base_url
        self.borough = borough
        self.query_location = query_location
        self.query_location_is_lm = query_location_is_lm
        self.library_suffix_enforced = library_suffix_enforced
        self.library_borough_name = library_borough_name
        self.library_substitutions = {
            "1:HARFF": "Coombes Croft Library (Haringey)",
            "Hounslow Library": "Hounslow Hounslow Library"
        }

    def get_results(self, query, num_results):
        results = SearchResults()
        params = {
            "qu": query,
            "qf": "FORMAT	Format	BOOK	Books",
            "te": "ILS",
            "h": "1",
        }
        location_params = {}
        if self.query_location_is_lm:
            location_params["lm"] = self.query_location
        else:
            location_params["qf"] = self.query_location
        search_url = self.base_url + "/" + urllib.parse.urlencode(params) + "&" + urllib.parse.urlencode(location_params)
        feed = feedparser.parse(search_url)
        for entry in feed.entries[:num_results]:
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

        # Get author if still needed.
        if len(author) == 0:
            author_select = entry_soup.select( "div.text-p.PERSONAL_AUTHOR")
            if len(author_select) > 0:
                author = ";".join([a.text for a in author_select])
        if len(author) == 0:
            author_select = entry_soup.select("div.text-p.INITIAL_AUTHOR_SRCH")
            if len(author_select) > 0:
                author = "; ".join([a.text for a in author_select])
        if len(author) == 0:
            author_select = entry_soup.select("div.text-p.AUTHOR")
            if len(author_select) > 0:
                author = "; ".join([a.text for a in author_select])

        # Get libraries.
        libraries = set(row.find("td", {"class": "detailItemsTable_LIBRARY"}).find("div", {"class": "hidden"}).text for row in entry_soup.find_all("tr", {"class": "detailItemsTableRow"}))
        libraries = [lib.strip() for lib in libraries]
        libraries = [self.library_substitutions[lib]if lib in self.library_substitutions else lib for lib in libraries]
        if len(self.library_borough_name) > 0:
            if self.library_borough_name.endswith(")"):
                if self.library_suffix_enforced:
                    libraries = [library.replace(" " + self.library_borough_name, "") for library in libraries if library.endswith(self.library_borough_name)]
                else:
                    libraries = [library.replace(" " + self.library_borough_name, "") for library in libraries]
            else:
                libraries = [library.replace(self.library_borough_name + " ", "", 1) for library in libraries if library.startswith(self.library_borough_name)]
        libraries = [lib.strip() for lib in libraries]
        return Book(title, author, year, self.borough, libraries, url)
