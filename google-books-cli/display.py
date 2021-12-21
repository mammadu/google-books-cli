import menu

class display:
    def __init__(self):
        self.current_menu = menu.main_menu()

    def set_current_menu(self, menu):
        self.current_menu = menu

    def display_menu(self):
        for index, item in enumerate(self.current_menu.options_list_dictionary):
            print(f"{index}: {item}")

    def get_user_input(self):
        user_input = input("Select numeric option: ")
        user_input = int(user_input)
        return user_input
    
    def select_menu_option(self, option_index):
        func = self.current_menu.get_functions(option_index)
        if type(func) == menu:
            self.set_current_menu(func)

    def main(self):
        while(True):
            self.display_menu()
            user_input = self.get_user_input()
            self.select_menu_option(user_input)

