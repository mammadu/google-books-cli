import gb_backend
import pandas
from datetime import datetime

reading_list_location = "reading_list.csv"

class menu:
    def __init__(self):
        self.options_list_dictionary = []
    
    def get_functions(self, option_index, arguments=[]):
        try:
            return getattr(self, list(self.options_list_dictionary.values())[option_index])(arguments)
        except:
            return getattr(self, list(self.options_list_dictionary.values())[option_index])(*arguments)

class main_menu(menu):
    def __init__(self):
        self.options_list_dictionary = {
            'Search for books': 'search_for_books'
            , 'Display local reading list': 'display_local_reading_list'
            , 'Quit': 'quit'
        }

    def search_for_books(self):
        return query_menu()

    def display_local_reading_list(self):
        return reading_list_menu()

    def quit(self):
        print('quitting')
        quit()

class query_menu(menu):
    def __init__(self):
        self.options_list_dictionary = {
            'Enter new query': 'enter_query'
            , 'Add title to reading list': 'add_to_reading_list'
            , 'Return to main menu': 'return_to_main_menu'
        }
        self.backend = gb_backend.gb_backend()
    
    def add_to_reading_list(self):
        if len(self.backend.results_list) == 0:
            print('you must first enter a query')
        else:
            self.backend.print_results_list()
            print()
            index = input("select index of title: ")
            try:
                index = int(index)
            except ValueError as ex:
                index = -1
            if index != -1 and index in range(len(self.backend.results_list)):
                row = self.backend.results_list[index]
                row['Date added'] = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
                row['Authors'] = ', '.join(row['Authors'])
                dataframe = pandas.DataFrame.from_records([row])
                with open(reading_list_location, 'a') as file:
                    dataframe.to_csv(file, index=False, mode='a', header=file.tell()==0)
                print(dataframe)
            else:
                print("invalid index")

    def enter_query(self):
        title = input("enter title: ")
        self.backend.results_of_query(title)

    def return_to_main_menu(self):
        return main_menu()

class reading_list_menu(menu):
    def __init__(self):
        self.options_list_dictionary = {
            'Display reading list': 'display_reading_list'
            , 'Sort titles': 'sort_titles'
            , 'Remove title from reading list': 'remove_title'
            , 'Return to main menu': 'return_to_main_menu'
        }
    
    def display_reading_list(self):
        df = pandas.read_csv(reading_list_location)
        formatted_index = (f"{i}:" for i in range(len(df)))
        df.set_index(formatted_index, inplace=True)
        print(df)

    def sort_titles(self):
        print('sort titles')

    def remove_title(self):
        print('remove title')
    
    def return_to_main_menu(self):
        return main_menu()