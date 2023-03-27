from app.catalogues import catalogues
from app.search_results import SearchResults

class Search:
    def __init__(self, query, boroughs):
        self.query = query
        self.boroughs = boroughs
        self.num_results = 2
        self.results = SearchResults()

    def do_search(self):
        for borough, catalogue in catalogues.items():
            if borough in self.boroughs:
                self.results.add_results(catalogue(self.num_results).get_results(self.query))

    def get_results(self):
        self.do_search()
        return self.results



if __name__ == "__main__":
    query = "book"
    print(Search(query, ["Croydon"]).get_results())
