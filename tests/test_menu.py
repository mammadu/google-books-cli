import pathlib
import sys

source_path = str(pathlib.Path(__file__).resolve().parent.parent.joinpath("google-books-cli"))
sys.path.insert(0, source_path)

import menu

def test_convert_valid_index_to_int():
    current_menu = menu.query_menu()
    string_index = '1234123412345651'
    int_index = current_menu.convert_index_to_int(string_index)
    
    assert int_index == int(string_index)

def test_convert_invalid_index_to_int():
    current_menu = menu.query_menu()
    string_index = 'asdgdfaasdf'
    int_index = current_menu.convert_index_to_int(string_index)
    
    assert int_index == -1
