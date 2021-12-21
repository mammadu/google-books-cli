import gb
import pandas
from datetime import datetime

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
        print('Display local reading list')

    def quit(self):
        print('quitting')
        quit()

class query_menu(menu):
    def __init__(self):
        self.options_list_dictionary = {
            'Enter new query': 'enter_query'
            , 'Add title to favorites': 'add_to_favorites'
            , 'Return to main menu': 'return_to_main_menu'
        }
        self.backend = gb.gb()
    
    def add_to_favorites(self):
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
                df = pandas.DataFrame(row)
                df.to_csv("favorites.csv", index=False, mode='a')
                print(df)
            else:
                print("invalid index")



    def enter_query(self):
        title = input("enter title: ")
        self.backend.results_of_query(title)


    def return_to_main_menu(self):
        return main_menu()