from data.repository.entry_repository import EntryRepositories


class EntryRepositoryImpl(EntryRepositories):

    def __init__(self):
        self.__entries = []

    def save(self, entry):
        entry_does_not_exist = entry.get_id() == 0
        if entry_does_not_exist:
            self.save_new(entry)
        else:
            self.update(entry)
        return entry

    def save_new(self, entry):
        entry.set_id(self.generate_id())
        self.__entries.append(entry)

    def update(self, entry):
        new_entry = self.find_by_id(entry.get_id())
        new_entry.set_title(entry.get_title())
        new_entry.set_body(entry.get_body())

    def generate_id(self):
        return len(self.__entries) + 1

    def delete(self, entry):
        found_entry = self.find_by_id(entry.get_id())
        self.__entries.remove(found_entry)

    def count(self):
        return len(self.__entries)

    def find_by_id(self, id):
        return next((entry for entry in self.__entries if entry.get_id() == id), None)

    def find_all(self):
        return self.__entries

    def clear(self):
        self.__entries.clear()
