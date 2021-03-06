import pathlib
import pandas
import sys

test_path = pathlib.Path(__file__).resolve().parent
source_path = test_path.parent.joinpath("google-books-cli")
sys.path.insert(0, source_path)

import menu


# test if convert_valid_index can convert a string to an integer
def test_convert_valid_index_to_int():
    current_menu = menu.QueryMenu()
    string_index = '1234123412345651'
    int_index = current_menu.convert_index_to_int(string_index)
    assert int_index == int(string_index)


# test if convert_valid_index returns -1 for non integer strings
def test_convert_invalid_index_to_int():
    current_menu = menu.QueryMenu()
    string_index = 'asdgdfaasdf'
    int_index = current_menu.convert_index_to_int(string_index)
    assert int_index == -1


# test if format_data_frame properly formats the author column
def test_format_data_frame():
    current_menu = menu.QueryMenu()
    index = 0
    current_menu.backend.results_list.append(
        {
            'Title': 'Just Start',
            'Authors': ['Leonard A. Schlesinger', 'Charles F. Kiefer', 'Paul B. Brown'],
            'Publisher': 'Harvard Business Press'
        }
    )
    row = current_menu.backend.results_list[index].copy()
    row['Authors'] = ', '.join(row['Authors'])
    expected_dataframe = pandas.DataFrame.from_records([row])
    test_dataframe = current_menu.format_dataframe(index, current_menu.backend.results_list)
    assert test_dataframe['Authors'].equals(expected_dataframe['Authors'])
