import menu
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


class Display:
    def __init__(self):
        self.current_menu = menu.MainMenu()

    def set_current_menu(self, menu):
        self.current_menu = menu

    def display_menu(self):
        for index, item in enumerate(self.current_menu.options_list_dictionary):
            print(f"{index}: {item}")

    def get_user_input(self):
        user_input = input("Select numeric option: ")
        try:
            user_input = int(user_input)
        except ValueError as ex:
            user_input = -1
        
        if user_input not in range(0, len(self.current_menu.options_list_dictionary)):
            user_input = -1
        return user_input
    
    def select_menu_option(self, option_index):
        function = self.current_menu.get_functions(option_index)
        if isinstance(function, menu.Menu):
            self.set_current_menu(function)

    def main(self):
        while(True):
            self.display_menu()
            user_input = self.get_user_input()
            clear()
            if user_input == -1:
                print("invalid option")
            else:
                self.select_menu_option(user_input)
            print()

