from src.kart_analytics import main
from src.repository.statistics import StatisticsRepository
from unittest.mock import patch
import unittest
import sys

class KartAnalyticsTest(unittest.TestCase):

    def test_main_with_no_args_exits_with_code_1(self):
        with self.assertRaises(SystemExit) as cm:
            argv = []
            main(argv)
            self.assertEqual(1,cm.exception.code)

    def test_main_with_multiple_args_exits_with_code_2(self):
        with self.assertRaises(SystemExit) as cm:
            argv = ['Arg1', 'Arg2']
            main(argv)
            self.assertEqual(2,cm.exception.code)

    def test_main_with_non_file_argument_exits_with_code_3(self):
        with self.assertRaises(SystemExit) as cm:
            argv = ['Arg1']
            main(argv)
            self.assertEqual(3,cm.exception.code)

    @patch('repository.statistics.StatisticsRepository.print_result')
    def test_main_with_valid_file_as_argument_calls_print_result(self,mock):
        mock.return_value = ''
        print(mock)
        argv = ['tests/repository/base.txt']
        main(argv)
        mock.assert_called()
