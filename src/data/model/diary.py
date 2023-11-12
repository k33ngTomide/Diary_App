
class Diary:

    def __init__(self):
        self.__id = 0
        self.__username = ""
        self.__password = ""
        self.__is_locked = False

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def is_locked(self):
        return self.__is_locked

    def set_locked(self, locked):
        self.__is_locked = locked

    def __str__(self):
        return super().__str__()


