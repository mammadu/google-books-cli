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
            'Enter query': 'enter_query'
            , 'Return to main menu': 'return_to_main_menu'
        }
    
    def enter_query(self):
        title = input("enter title: ")
        print(title)

    def return_to_main_menu(self):
        return main_menu()