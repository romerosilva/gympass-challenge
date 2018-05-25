import unittest
from src.data.file_reader import FileReader
from src.repository.log_entries import LogEntriesRepository

class LogEntriesRepositoryTest(unittest.TestCase):

    def test_get_logs_skips_first_line(self):
        reader = FileReader('tests/repository/one_entry.txt')
        repository = LogEntriesRepository(reader)
        logs = list(repository.get_logs())
        self.assertTrue(len(logs) == 1)
