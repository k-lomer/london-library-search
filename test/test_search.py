from parameterized import parameterized
from nose.tools import assert_equal, assert_greater, assert_greater_equal, assert_less_equal, assert_true
import app.catalogues
import app.search
from datetime import datetime


def get_catalogues():
    return [(borough,) for borough in app.catalogues.catalogues]


def run_single_borough_query(borough, query, num_results):
    results = app.search.Search(query, [borough], num_results).get_results()
    assert_greater(len(results), 0, "No search results got")
    for result in results:
        assert_greater(len(result.title), 0, "No title got")
        assert_greater_equal(result.year, 0, "Invalid year")
        current_year = datetime.now().year
        assert_less_equal(result.year, current_year, "Year is in the future")
        assert_equal(result.borough, borough, "Borough differs")
        assert_greater(len(result.url), 0, "No url got")
        if len(result.libraries) == 0:
            print(result.url)
        assert_greater(len(result.libraries), 0, "No libraries got")


@parameterized(get_catalogues)
def test_catalogues(borough):
    query = "Harry Potter"
    num_results = 5
    run_single_borough_query(borough, query, num_results)


def test_all_catalogues():
    query = "Harry Potter"
    num_results = 5
    boroughs = app.catalogues.catalogues.keys()
    results = app.search.Search(query, boroughs, num_results).get_results()
    # Check there is a result from each borough.
    for borough in boroughs:
        found = False
        for result in results:
            if result.borough == borough:
                found = True
                break
        assert_true(found, "No results found for borough: " + borough)





