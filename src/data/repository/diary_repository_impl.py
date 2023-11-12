from data.repository.diary_repository import DiaryRepository


class DiaryRepositoryImpl(DiaryRepository):

    def __init__(self):
        self.__diaries = []

    def save(self, diary):
        diary_does_not_exist = diary.get_id() == 0
        if diary_does_not_exist:
            self.__save_new(diary)
        else:
            self.__update(diary)

        return diary

    def __save_new(self, diary):
        diary.set_id(self.__generate_id())
        self.__diaries.append(diary)

    def __update(self, diary):
        new_diary = self.find_by_id(diary.get_id())
        new_diary.set_username(diary.get_username())

    def __generate_id(self):
        return len(self.__diaries) + 1

    def delete(self, diary):
        found_diary = self.find_by_id(diary.get_id())
        self.__diaries.remove(found_diary)

    def count(self):
        return len(self.__diaries)

    def find_by_id(self, id):
        return next((diary for diary in self.__diaries if diary.get_id() == id), None)

    def find_all(self):
        return self.__diaries

    def clear(self):
        self.__diaries.clear()
