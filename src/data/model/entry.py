from datetime import datetime


class Entry:

    def __init__(self):
        self.__id = 0
        self.__title = ""
        self.__body = ""
        self.__created_date = datetime.now()
        self.__owner_name = ""

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_body(self):
        return self.__body

    def set_body(self, body):
        self.__body = body

    def get_created_date(self):
        return self.__created_date

    def set_created_date(self, created_date):
        self.__created_date = created_date

    def get_owner_name(self):
        return self.__owner_name

    def set_owner_name(self, owner_name):
        self.__owner_name = owner_name

    def __str__(self):
        return (f"Entry(id={self.__id}, "
                f"title='{self.__title}', "
                f"body='{self.__body}', "
                f"createdDate={self.__created_date}, "
                f"ownerName='{self.__owner_name}')")
