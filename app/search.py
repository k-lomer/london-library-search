from app.catalogues import catalogues
from app.search_results import SearchResults

class Search:
    def __init__(self, query, boroughs, num_results=5):
        self.query = query
        self.boroughs = boroughs
        self.num_results = num_results
        self.results = SearchResults()

    def do_search(self):
        for borough, catalogue in catalogues.items():
            if borough in self.boroughs:
                self.results.add_results(catalogue().get_results(self.query, self.num_results))

    def get_results(self):
        self.do_search()
        return self.results



if __name__ == "__main__":
    query = "harry potter"
    print(Search(query, ["Redbridge"]).get_results())
