
class SearchResults:
    def __init__(self):
        self.results = []

    def __str__(self):
        return "\n\n".join( str(result) for result in self.results)

    def __iter__(self):
        return self.results.__iter__()

    def __next__(self):
        return self.results.__next__()

    def add_result(self, result):
        self.results.append(result)

    def add_results(self, search_results):
        self.results += search_results.results

    def filter(self, boroughs):
        pass

    def sort(self, sort_param):
        pass


class Book:
    def __init__(self, title, author, year, borough, libraries, url ):
        self.title = title
        self.author = author
        self.year = year
        self.borough = borough
        self.libraries = "; ".join(libraries)
        self.url = url

    def __str__(self):
        return "\n".join(["title: " + self.title,  "author: " + self.author, "year: " + str(self.year), "borough: " + self.borough, "libraries: " + self.libraries, "URL: " + self.url])
