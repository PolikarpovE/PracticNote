import json
from Note import Note


class CatalogNotes: # Класс обработки каталога заметок
    __catalog = {'catalog': []}
    __file_name = 'catalog.json'

    def __init__(self, file_notes):
        self.__file_name = file_notes
        try:
            with open(file_notes, 'r') as catalog_file:
                tmp = json.load(catalog_file)
            for el in tmp['catalog']:
                self.__catalog['catalog'].append(Note(el['_Note__msg'], el['_Note__date_create']))

        except FileNotFoundError:
            with open(file_notes, 'w') as catalog_file:
                json.dump(self.__catalog, catalog_file)


    def __print_catalog(self):  # Выводит на печать содержимое каталога
        num = 1
        print('\n№      дата:           текст:')
        for item in self.__catalog['catalog']:
            print(f'{num} {item.to_str()}')
            num += 1
        print()

    def __add_notes(self, new_note):  # Внесение новой заметки в каталог
        self.__catalog['catalog'].append(new_note)


    def __export_to_file(self):  # Сохранение содержимого каталога в файл
        tmp_cat = {'catalog': []}
        for note in self.__catalog['catalog']:
            tmp_cat['catalog'].append(note.__dict__)
        with open(self.__file_name, 'w') as catalog_file:
            json.dump(tmp_cat, catalog_file)

    def execute_command(self, command):  # Изменение состояния каталога исходя из введенных пользователем данных
        if command[0] == 0:
            self.__export_to_file()

        if command[0] == 1:
            self.__print_catalog()

        if command[0] == 2:
            if command[2] > 0 and command[2] <= len(self.__catalog['catalog']):
                self.__catalog['catalog'][command[2] - 1] = command[1]
            else:
                print('Wrong index, canceling... \n')

        if command[0] == 3:
            self.__add_notes(command[1])

        if command[0] == 4:
            if command[2] > 0 and command[2] <= len(self.__catalog['catalog']):
                del self.__catalog['catalog'][command[2] - 1]
            else:
                print('Wrong index, canceling... \n')

