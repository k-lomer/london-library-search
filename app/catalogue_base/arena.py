from app.search_results import Book, SearchResults
import random
import requests
import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver, common
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class Arena:
    def __init__(self, base_url, borough, organisation_index, num_results, library_suffix=""):
        self.base_url = base_url
        self.borough = borough
        self.organisation_index = organisation_index
        self.num_results = num_results
        self.use_selenium = True
        self.library_suffix = library_suffix

    def get_results(self, query):
        results = SearchResults()
        query_terms = " AND ".join(query.split())
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
        print(search_url)
        search_page = requests.get(search_url)
        session_id = ""
        jsession_ids = [cookie.split("=")[-1] for cookie in search_page.headers["set-cookie"].split(";") if cookie.startswith("JSESSIONID")]
        if len(jsession_ids) > 0:
            session_id = jsession_ids[0]
        search_soup = BeautifulSoup(search_page.content, "html.parser")
        records = search_soup.find_all("div", {"class": "arena-record-details"})
        for record in records[:self.num_results]:
            if self.use_selenium:
                record_details = self.get_record_results_by_selenium(record)
            else:
                record_details = self.get_record_result_by_requests(record, session_id)
            if record_details is not None:
                results.add_result(record_details)
        return results

    def get_record_results_by_selenium(self, record):
        record_title_link = record.find("div", {"class": "arena-record-title"}).find( "a" )
        title = record_title_link.text
        record_url = record_title_link["href"]

        # Run firefox in headless mode.
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.get(record_url)

        # Get author details.
        author = ""
        try:
            author = driver.find_element(By.CLASS_NAME, "arena-detail-author").text
            if author.endswith(","):
                author = author[:-1]
            if author.startswith("Author: "):
                author = author[len("Author: "):]
        except common.exceptions.NoSuchElementException as e:
            print(self.borough + "Arena selenium failed to get author: " + str(e))


        # Get year details.
        year = 0
        try:
            year_text = driver.find_element(By.CLASS_NAME, "arena-detail-year").text
            if year_text.startswith("Publication year: "):
                year_text = year_text[len("Publication year: "):]
            if year_text.isdigit():
                year = int(year_text)
        except common.exceptions.NoSuchElementException as e:
            print(self.borough + "Arena selenium failed to get year: " + str(e))

        # Wait for libraries to load.
        libraries = []
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

        driver.close()
        return Book(title, author, year, self.borough, libraries, record_url)

    # DOES NOT WORK, DO NOT USE
    def get_record_result_by_requests(self, record, session_id):
        print("get_record_result_by_requests IMPLEMENTATION DOES NOT WORK")
        record_title_link = record.find("div", {"class": "arena-record-title"}).find( "a" )
        title = record_title_link.text
        record_url = record_title_link["href"]
        record_page = requests.get(record_url, cookies={"COOKIE_SUPPORT": "true", "GUEST_LANGUAGE_ID": "en_GB", "JSESSIONID": session_id})
        record_soup = BeautifulSoup(record_page.content, "html.parser")
        author = ""
        record_author_details = record_soup.find("div", {"class": "arena-detail-author"})
        if record_author_details is not None:
            author_value = record_author_details.find("span", {"class": "arena-value"})
            if author_value is not None:
                author = author_value.text
        if author.endswith(","):
            author = author[:-1]
        year = 0
        record_year_details = record_soup.find("div", {"class": "arena-detail-year"})
        if record_year_details is not None:
            year_value = record_year_details.find("span", {"class": "arena-value"})
            if year_value is not None:
                year_text = year_value.text
                if year_text.isdigit():
                    year = int(year_text)

        # Follow the breadcrumbs to find the libraries...
        # DOES NOT WORK! POSSIBLY AN ISSUE WITH THE COOKIES?
        libraries_url = self.base_url + "/results?random=" + "{:.17f}".format(random.random()) # yes really.
        print( libraries_url)
        # Crate the back URL.
        record_url_params = urllib.parse.parse_qs(urllib.parse.urlparse(record_url).query)
        # Get the libraries.
        libraries_request_params = {
            "p_p_id": "crDetailWicket_WAR_arenaportlet",
            "p_p_lifecycle": "2",
            "p_p_state": "normal",
            "p_p_mode": "view",
            "p_p_resource_id": "/crDetailWicket/?wicket:interface=:2:recordPanel:holdingsPanel::IBehaviorListener:0:",
            "p_p_cacheability": "cacheLevelPage",
            "_crDetailWicket_WAR_arenaportlet_back_url": record_url_params["_crDetailWicket_WAR_arenaportlet_back_url"][0],
            "": ""
        }
        libraries_request_headers = {
            "Accept": "text/xml",
            "Accept-Endcoding": "gzip,deflate,br",
            "Accept-Language": "en-GB,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "libraries.lambeth.gov.uk",
            "Origin": "https://libraries.lambeth.gov.uk",
            "Referer": record_url,
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Wicket-Ajax": "true"
        }

        libraries_response = requests.post(libraries_url, json=libraries_request_params, headers=libraries_request_headers, cookies={"COOKIE_SUPPORT": "true", "GUEST_LANGUAGE_ID": "en_GB", "JSESSIONID": session_id})
        libraries_soup = BeautifulSoup(libraries_response.content, "html.parser")
        child_views = libraries_soup.find_all("div", {"class": "arena-holding-child-view"})
        libraries = []
        return Book(title, author, year, self.borough, libraries, record_url)
