from src.kart_analytics import main
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
