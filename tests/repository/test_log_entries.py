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

    def test_get_logs_processes_all_lines(self):
        reader = FileReader('tests/repository/base.txt')
        repository = LogEntriesRepository(reader)
        logs = list(repository.get_logs())
        self.assertTrue(len(logs) == 23)

    def test_isLineParseable_returns_false_if_line_not_in_expected_format(self):
        reader = FileReader('tests/repository/one_entry.txt')
        repository = LogEntriesRepository(reader)
        line = '23:49:098.277\t038 – F.MASSA\t1\t1:02.852\t44,275'
        isParseable = repository._isLineParseable(0, line)
        self.assertFalse(isParseable)

    def test_isLineParseable_returns_true_if_line_in_expected_format(self):
        reader = FileReader('tests/repository/one_entry.txt')
        repository = LogEntriesRepository(reader)
        line = '23:49:08.277\t038 – F.MASSA\t1\t1:02.852\t44,275'
        isParseable = repository._isLineParseable(0, line)
        self.assertTrue(isParseable)

    def test_parseLine_returns_valid_LogEntry_object(self):
        reader = FileReader('tests/repository/one_entry.txt')
        repository = LogEntriesRepository(reader)
        line = '23:49:08.277\t038 – F.MASSA\t1\t1:02.852\t44,275'
        logEntry = repository._parseLine(0, line)
        self.assertTrue(type(logEntry) == type(LogEntry()))

    def test_parseLine_returns_None_if_line_has_invalid_format(self):
        reader = FileReader('tests/repository/one_entry.txt')
        repository = LogEntriesRepository(reader)
        line = '23:49:08.277\t038 – F.MASSA\t1\t1:02.852\t44?275'
        logEntry = repository._parseLine(0, line)
        self.assertIsNone(logEntry)
