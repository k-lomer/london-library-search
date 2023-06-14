from app.catalogues import catalogues
from app.search_results import SearchResults

class Search:
    def __init__(self, query, boroughs, num_results=5):
        self.catalogues = [catalogues[borough](query, num_results) for borough in boroughs if borough in catalogues]


    def get_results(self):
        for cat in self.catalogues:
            cat.start()
        for cat in self.catalogues:
            cat.join()
        results = SearchResults()
        for cat in self.catalogues:
            results.add_results(cat.results)
        return results


if __name__ == "__main__":
    query = "harry potter"
    print(Search(query, ["Redbridge"]).get_results())
