from parameterized import parameterized, parameterized_class
from nose.tools import assert_equal, assert_greater, assert_greater_equal, assert_less_equal
import app.catalogues
import app.search
from datetime import datetime


def get_catalogues():
    return [(borough,) for borough in app.catalogues.catalogues]

def run_test(borough, query, num_results):
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
    run_test(borough, query, num_results)




