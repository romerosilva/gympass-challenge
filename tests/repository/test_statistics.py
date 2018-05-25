from src.repository.statistics import StatisticsRepository
from src.repository.log_entries import LogEntriesRepository
from src.data.file_reader import FileReader
import unittest

class StatisticsRepositoryTest(unittest.TestCase):

    def test_calculateResult_returns_list_with_expected_classification(self):
        reader = FileReader('tests/repository/base.txt')
        logs = LogEntriesRepository(reader)
        stats = StatisticsRepository(logs)

        result = stats._calculateResult(list(logs.get_logs()))

        self.assertEqual(result[0].code, '038')
        self.assertEqual(result[1].code, '002')
        self.assertEqual(result[2].code, '033')
        self.assertEqual(result[3].code, '023')
        self.assertEqual(result[4].code, '015')
        self.assertEqual(result[5].code, '011')

    def test_groupByRacer_does_not_add_to_groups_if_groups_is_already_in_memory(self):
        reader = FileReader('tests/repository/base.txt')
        logs = LogEntriesRepository(reader)
        stats = StatisticsRepository(logs)

        stats._calculateResult(list(logs.get_logs()))
        stats._calculateResult(list(logs.get_logs()))
        stats._calculateResult(list(logs.get_logs()))

        self.assertEqual(6, len(stats.groups))

    def test_get_result_returns_tuple_with_expected_calculations(self):
        reader = FileReader('tests/repository/base.txt')
        logs = LogEntriesRepository(reader)
        stats = StatisticsRepository(logs)

        position, code, name, completedLaps, timeTotal = list(stats.get_result())[0]

        self.assertEqual(position, 1)
        self.assertEqual(code, '038')
        self.assertEqual(name, 'F.MASS')
        self.assertEqual(completedLaps, '4')
        self.assertEqual(timeTotal, '4:11.578')

        position, code, name, completedLaps, timeTotal = list(stats.get_result())[-1]
        self.assertEqual(position, 6)
        self.assertEqual(code, '011')
        self.assertEqual(name, 'S.VETTEL')
        self.assertEqual(completedLaps, '3')
        self.assertEqual(timeTotal, '6:27.276')
