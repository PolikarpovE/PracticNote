import datetime


class Note: # Заметка, индекс - индекс в списке
    __msg = None
    __date_create = None

    def __init__(self, msg = None, date_create = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')):
        self.__msg = msg
        self.__date_create = date_create

    def to_str(self):
        return f'от {self.__date_create}: {self.__msg}'