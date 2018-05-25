import unittest
from src.data.file_reader import FileReader
from src.data.model.log_entry import LogEntry
from src.repository.log_entries import LogEntriesRepository

class LogEntriesRepositoryTest(unittest.TestCase):

    def test_get_logs_skips_first_line(self):
        reader = FileReader('tests/repository/one_entry.txt')
        repository = LogEntriesRepository(reader)
        logs = list(repository.get_logs())
        self.assertTrue(len(logs) == 1)

    def test_get_logs_ignores_empty_lines(self):
        reader = FileReader('tests/repository/one_entry_empty_lines.txt')
        repository = LogEntriesRepository(reader)
        logs = list(repository.get_logs())
        self.assertTrue(len(logs) == 1)
