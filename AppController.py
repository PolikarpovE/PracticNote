class AppController:  # Контроллер приложения
    __user_interface = None
    __app_body = None
    __catalog = None

    def __init__(self, new_body, new_interface, new_catalog):
        self.__app_body = new_body
        self.__user_interface = new_interface
        self.__catalog = new_catalog

    def start(self):  # Работа приложения
        while True:
            user_input = self.__user_interface.user_dialog()
            if user_input[0] > 0:
                self.__catalog.execute_command(user_input)
            elif user_input[0] < 0:
                print('Wrong input! Try aggain\n')
            else:
                self.__catalog.execute_command(user_input)
                print('Good luck!')
                break