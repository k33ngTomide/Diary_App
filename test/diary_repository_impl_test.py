import unittest

from data.model.diary import Diary
from data.repository.diary_repository_impl import DiaryRepositoryImpl


class DiaryRepositoryImplTest(unittest.TestCase):

    def setUp(self):
        self.diary_repository = DiaryRepositoryImpl()

    def test_save_one_diary_count_is_one_test(self):
        diary = Diary()
        self.diary_repository.save(diary)
        self.assertEqual(1, self.diary_repository.count())

    def test_save_one_diary_find_diary_test(self):
        diary = Diary()
        new_diary = self.diary_repository.save(diary)
        self.assertEqual(new_diary, self.diary_repository.find_by_id(1))

    def test_update_diary_test(self):
        diary = Diary()
        diary.set_username("Muiliyu Sodiq")
        self.diary_repository.save(diary)
        self.assertEqual("Muiliyu Sodiq", self.diary_repository.find_by_id(1).get_username())

        updated_diary = Diary()
        updated_diary.set_id(1)
        updated_diary.set_username("King Akintomide")
        self.diary_repository.save(updated_diary)
        self.assertEqual("King Akintomide", self.diary_repository.find_by_id(1).get_username())

    def test_save_more_than_one_diary_count_is_accurate_test(self):
        diary = Diary()
        self.diary_repository.save(diary)
        another_diary = Diary()
        self.diary_repository.save(another_diary)
        extra_diary = Diary()
        self.diary_repository.save(extra_diary)

        self.assertEqual(3, self.diary_repository.count())

    def test_finding_a_diary_that_does_not_exist_return_null(self):
        self.assertIsNone(self.diary_repository.find_by_id(1))

    def test_delete_diary_count_reduces(self):
        diary = Diary()
        diary.set_username("Muiliyu Sodiq")
        self.diary_repository.save(diary)
        self.assertEqual("Muiliyu Sodiq", self.diary_repository.find_by_id(1).get_username())

        updated_diary = Diary()
        updated_diary.set_username("King Akintomide")
        self.diary_repository.save(updated_diary)
        self.assertEqual("King Akintomide", self.diary_repository.find_by_id(2).get_username())

        self.diary_repository.delete(diary)
        self.assertEqual(1, self.diary_repository.count())

    def test_clear_diary_test(self):
        diary = Diary()
        self.diary_repository.save(diary)
        another_diary = Diary()
        self.diary_repository.save(another_diary)
        extra_diary = Diary()
        self.diary_repository.save(extra_diary)

        self.assertEqual(3, self.diary_repository.count())

        self.diary_repository.clear()
        self.assertEqual(0, self.diary_repository.count())

    def test_all_diaries_can_be_received_test(self):
        diary = Diary()
        self.diary_repository.save(diary)
        another_diary = Diary()
        self.diary_repository.save(another_diary)
        extra_diary = Diary()
        self.diary_repository.save(extra_diary)

        self.assertEqual(3, self.diary_repository.count())

        all_diaries = [diary, another_diary, extra_diary]
        self.assertEqual(all_diaries, list(self.diary_repository.find_all()))


if __name__ == '__main__':
    unittest.main()
