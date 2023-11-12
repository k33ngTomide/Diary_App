from abc import ABC, abstractmethod


class DiaryRepository(ABC):

    @abstractmethod
    def save(self, diary):
        pass

    @abstractmethod
    def delete(self, diary):
        pass

    @abstractmethod
    def count(self):
        pass

    @abstractmethod
    def find_by_id(self, i):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def clear(self):
        pass
