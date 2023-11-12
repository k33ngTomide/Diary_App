from abc import ABC, abstractmethod


class EntryRepositories(ABC):

    @abstractmethod
    def save(self, entry):
        pass

    @abstractmethod
    def delete(self, entry):
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
