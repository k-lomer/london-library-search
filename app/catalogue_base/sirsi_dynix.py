from app.search_results import Book, SearchResults
import feedparser
import html
import requests
import re
import urllib.parse
from bs4 import BeautifulSoup


class SirsiDynix:
    def __init__(self, base_url, additional_path_entry, borough, num_results, additional_query_params={}):
        self.base_url = base_url
        self.additional_path_entry = additional_path_entry
        self.borough = borough
        self.num_results = num_results
        self.additional_query_params = additional_query_params

    def get_results(self, query):
        results = SearchResults()
        params = {
            "qu": query,
            "qf": "FORMAT	Format	BOOK	Books",
            "te": "ILS",
            "h": "1",
            **self.additional_query_params
        }
        search_url = self.base_url + "/client/rss/hitlist/" + self.additional_path_entry + "/" + urllib.parse.urlencode(params)
        feed = feedparser.parse(search_url)
        for entry in feed.entries[:self.num_results]:
            entry_details = self.get_feed_result(entry)
            results.add_result(entry_details)
        return results

    def get_feed_result(self, entry):
        title = html.unescape(entry["title"].rsplit(" / ", 1)[0])
        if title.startswith("Title "):
            title = title.replace("Title ", "", 1)
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
        libraries = set( row.find("td", {"class": "detailItemsTable_LIBRARY"}).find("div", {"class": "hidden"}).text for row in entry_soup.find_all("tr", {"class": "detailItemsTableRow"}) )
        libraries = (library.replace(" (" + self.borough + ")", "") for library in libraries)
        return Book(title, author, year, self.borough, libraries, url)

class LlcSirsiDynix(SirsiDynix):
    def __init__(self, borough, additional_path_entry, borough_search_param, num_results):
        super().__init__("https://llc.ent.sirsidynix.net.uk", additional_path_entry, borough, num_results, {"lm": borough_search_param})
