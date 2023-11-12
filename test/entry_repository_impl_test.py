import unittest

from data.model.entry import Entry
from data.repository.entry_repository_impl import EntryRepositoryImpl


class EntryRepositoryImplTest(unittest.TestCase):

    def setUp(self):
        self.entry_repository = EntryRepositoryImpl()

    def test_save_entry_count_increases(self):
        entry = Entry()
        self.entry_repository.save(entry)
        self.assertEqual(1, self.entry_repository.count())

    def test_save_one_diary_find_entry_test(self):
        entry = Entry()
        new_entry = self.entry_repository.save(entry)
        self.assertEqual(new_entry, self.entry_repository.find_by_id(1))

    def test_update_entry_test(self):
        entry = Entry()
        entry.set_title("The bad day the devil Drink Water")
        entry.set_body("Omo on this blessed day, the devil was thirsty")
        self.entry_repository.save(entry)
        self.assertEqual("The bad day the devil Drink Water", self.entry_repository.find_by_id(1).get_title())
        self.assertEqual("Omo on this blessed day, the devil was thirsty",
                         self.entry_repository.find_by_id(1).get_body())

        update_entry = Entry()
        update_entry.set_id(1)
        update_entry.set_title("It was the last day the Devil Drank Water")
        update_entry.set_body("The bad day the devil Drink Water, Omo on this blessed day, the devil was thirsty")
        self.entry_repository.save(update_entry)
        self.assertEqual("It was the last day the Devil Drank Water", self.entry_repository.find_by_id(1).get_title())
        self.assertEqual("The bad day the devil Drink Water, Omo on this blessed day, the devil was thirsty",
                         self.entry_repository.find_by_id(1).get_body())

    def test_finding_a_entry_that_does_not_exist_return_null(self):
        self.assertIsNone(self.entry_repository.find_by_id(1))

    def test_more_entries_increases_count(self):
        entry = Entry()
        entry.set_title("The bad day the devil Drink Water")
        entry.set_body("Omo on this blessed day, the devil was thirsty")
        self.entry_repository.save(entry)

        update_entry = Entry()
        update_entry.set_title("It was the last day the Devil Drank Water")
        update_entry.set_body("The bad day the devil Drink Water, Omo on this blessed day, the devil was thirsty")
        self.entry_repository.save(update_entry)

        self.assertEqual(2, self.entry_repository.count())

    def test_delete_entry_reduces_count(self):
        entry = Entry()
        entry.set_title("The bad day the devil Drink Water")
        entry.set_body("Omo on this blessed day, the devil was thirsty")
        self.entry_repository.save(entry)

        update_entry = Entry()
        update_entry.set_title("It was the last day the Devil Drank Water")
        update_entry.set_body("The bad day the devil Drink Water, Omo on this blessed day, the devil was thirsty")
        self.entry_repository.save(update_entry)

        self.assertEqual(2, self.entry_repository.count())

        self.entry_repository.delete(entry)
        self.assertEqual(1, self.entry_repository.count())

    def test_clear_entry_test(self):
        entry = Entry()
        new_entry = Entry()
        extra_entry = Entry()
        self.entry_repository.save(entry)
        self.entry_repository.save(new_entry)
        self.entry_repository.save(extra_entry)

        self.assertEqual(3, self.entry_repository.count())

        self.entry_repository.clear()
        self.assertEqual(0, self.entry_repository.count())

    def test_all_entries_can_be_received_test(self):
        entry = Entry()
        new_entry = Entry()
        extra_entry = Entry()
        self.entry_repository.save(entry)
        self.entry_repository.save(new_entry)
        self.entry_repository.save(extra_entry)

        self.assertEqual(3, self.entry_repository.count())

        all_entries = [entry, new_entry, extra_entry]
        self.assertEqual(all_entries, list(self.entry_repository.find_all()))


if __name__ == '__main__':
    unittest.main()
