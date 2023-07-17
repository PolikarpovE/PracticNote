from Note import Note

class UserInterface:
    __comand_list = ['Просмотр списка заметок', 'Редактирование заметки', 'Добавление заметки', 'Удаление заметки']


    def __get_num_note(self): # Получить номер заметки
        try:
            return int(input('Укажите номер заметки: '))
        except ValueError:
            return 0

    def __edit_note(self):  # Диалог редактирования заметки
        num_note = self.__get_num_note()
        if num_note:
            return (self.__new_notes_dialog(), num_note)
        return (None, 0)

    def execute_dialog(self, command):  # Обработка ответа пользователя и вызов нужного диалога
        if command == 1:
            return (1, None, 0)
        if command == 2:
            edit_result = self.__edit_note()
            return (2, edit_result[0], edit_result[1])
        if command == 3:
            return (3, self.__new_notes_dialog())
        if command == 4:
            return (4, None, self.__get_num_note())

    def __new_notes_dialog(self):  # Диалог создания заметки
        msg = input('Введите текст заметки: \n')
        return Note(msg)

    def user_dialog(self): # общение с пользователем
        num = 1
        for item in self.__comand_list:
            print(f'{num}: {item}')
            num += 1
        print('q: Выход')
        user_input = input('Введите команду: ')
        if user_input.lower() == 'q':
            return (0, None)
        try:
            result = int(user_input)
            if result > num:
                raise ValueError
            return self.execute_dialog(result)
        except ValueError:
            return (-1, None)



