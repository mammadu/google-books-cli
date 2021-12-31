import pathlib
import sys
import json

source_path = str(pathlib.Path(__file__).resolve().parent.parent.joinpath("google-books-cli"))
sys.path.insert(0, source_path)

import gb_backend


def parse_data_setup(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    backend = gb_backend.gb_backend()
    backend.parse_data(data)
    return backend.results_list

#test if parse_data properly fills gb_backend.results_list
def test_parse_data_good_value():
    results_list = parse_data_setup("good_query.json")
    expected_results_list = [
        {'Title': 'Start with Why', 'Authors': ['Simon Sinek'], 'Publisher': 'Penguin'}
        , {'Title': 'Start', 'Authors': ['Jon Acuff'], 'Publisher': 'Ramsey Press'}
        , {'Title': 'Just Start', 'Authors': ['Leonard A. Schlesinger', 'Charles F. Kiefer', 'Paul B. Brown'], 'Publisher': 'Harvard Business Press'}
        , {'Title': 'Start Late, Finish Rich', 'Authors': ['David Bach'], 'Publisher': 'Currency'}
        , {'Title': 'Start Something That Matters', 'Authors': ['Blake Mycoskie'], 'Publisher': 'Random House'}
        ]

    assert results_list == expected_results_list

