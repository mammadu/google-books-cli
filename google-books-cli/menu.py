import gb_backend
import pandas
from datetime import datetime
import pathlib

source_path = pathlib.Path(__file__).resolve().parent

reading_list_location = str(source_path.joinpath("reading_list.csv"))


class Menu:
    def __init__(self):
        self.options_list_dictionary = []

    def get_functions(self, option_index, arguments=[]):
        try:
            return getattr(self, list(self.options_list_dictionary.values())[option_index])(arguments)
        except Exception:
            return getattr(self, list(self.options_list_dictionary.values())[option_index])(*arguments)


class MainMenu(Menu):
    def __init__(self):
        self.options_list_dictionary = {
            'Search for books': 'search_for_books'
            , 'Display local reading list': 'display_local_reading_list'
            , 'Quit': 'quit'
        }

    def search_for_books(self):
        return QueryMenu()

    def display_local_reading_list(self):
        return ReadingListMenu()

    def quit(self):
        print('quitting')
        quit()


class SubMenu(Menu):
    def display_reading_list(self):
        print("Current reading list")
        dataframe = pandas.read_csv(reading_list_location)
        formatted_index = (f"{i}:" for i in range(len(dataframe)))
        dataframe.set_index(formatted_index, inplace=True)
        print(dataframe)

    def return_to_main_menu(self):
        return MainMenu()


class QueryMenu(SubMenu):
    def __init__(self):
        self.options_list_dictionary = {
            'Enter new query': 'enter_query'
            , 'Add title to reading list': 'add_to_reading_list'
            , 'Return to main menu': 'return_to_main_menu'
        }
        self.backend = gb_backend.GbBackend()

    def enter_query(self):
        title = input("enter title: ")
        self.backend.results_of_query(title)

    def convert_index_to_int(self, index):
        try:
            index = int(index)
        except ValueError:
            index = -1
        return index

    def format_dataframe(self, index, backend_results_list):
        row = backend_results_list[index]
        row['Date added'] = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        row['Authors'] = ', '.join(row['Authors'])
        dataframe = pandas.DataFrame.from_records([row])
        return dataframe

    def dataframe_to_csv(self, dataframe, read_list_location):
        with open(read_list_location, 'a') as file:
            dataframe.to_csv(file, index=False, mode='a', header=file.tell() == 0)

    def add_to_reading_list(self):
        if len(self.backend.results_list) == 0 or list(self.backend.results_list[0].keys())[0] == 'error code':
            print('you must first enter a valid query')
        else:
            self.backend.print_results_list()
            print()
            string_index = input("select index of title: ")
            index = self.convert_index_to_int(string_index)
            if index != -1 and index in range(len(self.backend.results_list)):
                dataframe = self.format_dataframe(index, self.backend.results_list)
                self.dataframe_to_csv(dataframe, reading_list_location)
                self.display_reading_list()
            else:
                print("invalid index")


class ReadingListMenu(SubMenu):
    def __init__(self):
        self.options_list_dictionary = {
            'Display reading list': 'display_reading_list'
            , 'Sort titles': 'sort_titles'
            , 'Remove title from reading list': 'remove_title'
            , 'Return to main menu': 'return_to_main_menu'
        }

    def sort_titles(self):
        print('This feature is not yet implemented')

    def remove_title(self):
        print('This feature is not yet implemented')
