from app.search_results import Book, SearchResults
import requests
from threading import Thread
import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver, common
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class Arena(Thread):
    def __init__(self, query, num_results, base_url, borough, organisation_index, library_suffix=""):
        super().__init__()
        self.query = query
        self.num_results = num_results
        self.results = SearchResults()
        self.base_url = base_url
        self.borough = borough
        self.organisation_index = organisation_index
        self.library_suffix = library_suffix

    def run(self):
        # Run firefox in headless mode.
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

        query_terms = " AND ".join(self.query.split())
        media_terms = " OR ".join("mediaClass_index:" + media for media in ["book", "paperback", "hardback"])
        query_param = "organisationId_index:" + self.organisation_index + " AND (" + media_terms + ") AND (" + query_terms + ")"
        params = {
            "p_p_id": "searchResult_WAR_arenaportlet",
            "p_p_lifecycle": "1",
            "p_p_state": "normal",
            "p_r_p_arena_urn:arena_facet_queries": "",
            "p_r_p_arena_urn:arena_search_query": query_param,
            "p_r_p_arena_urn:arena_search_type": "solr",
            "p_r_p_arena_urn:arena_sort_advice": "field=Relevance&direction=Descending"
        }
        search_url = self.base_url + "/search?" + urllib.parse.urlencode(params)
        search_page = requests.get(search_url)
        search_soup = BeautifulSoup(search_page.content, "html.parser")
        records = search_soup.find_all("div", {"class": "arena-record-details"})
        for record in records[:self.num_results]:
            self.get_record_results_by_selenium(record, self.results.results, driver)

        driver.close()

    def get_record_results_by_selenium(self, record, results_list, driver):
        record_title_link = record.find("div", {"class": "arena-record-title"}).find( "a" )
        title = record_title_link.text
        record_url = record_title_link["href"]

        driver.get(record_url)

        # Wait for libraries to load.
        timeout_seconds = 5
        try:
            element_present = expected_conditions .presence_of_element_located((By.CLASS_NAME, 'arena-holding-link'))
            WebDriverWait(driver, timeout_seconds).until(element_present)
            libraries = driver.find_elements(By.CLASS_NAME, "arena-holding-link")
            if len(libraries) > 0:
                # Skip the first entry, it is the borough.
                libraries = [lib.text.replace(" ({})".format(self.library_suffix), "") for lib in libraries[1:]]
        except common.exceptions.TimeoutException as e:
            print(self.borough + "Arena selenium failed to get libraries: " + str(e))
            return

        # Get author details.
        author = ""
        try:
            author = driver.find_element(By.CLASS_NAME, "arena-detail-author").text
            if author.endswith(","):
                author = author[:-1]
            if author.startswith("Author: "):
                author = author[len("Author: "):]
        except common.exceptions.NoSuchElementException as e:
            pass

        # Get year details.
        year = 0
        try:
            year_text = driver.find_element(By.CLASS_NAME, "arena-detail-year").text
            if year_text.startswith("Publication year: "):
                year_text = year_text[len("Publication year: "):]
            if year_text.isdigit():
                year = int(year_text)
        except common.exceptions.NoSuchElementException as e:
            pass

        results_list.append(Book(title, author, year, self.borough, libraries, record_url))
