class menu:
    def __init__(self):
        self.options_list_dictionary = []
    
    def get_functions(self, option_index, arguments=[]):
        try:
            getattr(self, self.options_list_dictionary.values()[option_index])(arguments)
        except:
            getattr(self, self.options_list_dictionary.values()[option_index])(*arguments)

class main_menu(menu):
    def __init__(self):
        self.options_list_dictionary = {
            'Search for books': 'search_for_books'
        , 'Display local reading list': 'display_local_reading_list'
        , 'Quit': 'quit'
        }

    def search_for_books(self):
        print("searching for books")

    def display_local_reading_list(self):
        print('Display local reading list')

    def quit(self):
        print('quitting')