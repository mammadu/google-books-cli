import menu

class display:
    def __init__(self):
        self.current_menu = menu.main_menu()

    def display_menu(self):
        for index, item in enumerate(self.current_menu.options_list_dictionary):
            print(f"{index}: {item}")