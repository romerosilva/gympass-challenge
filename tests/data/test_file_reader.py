import unittest
from src.data.file_reader import FileReader

class FileReaderTest(unittest.TestCase):

    def test_reading_empty_file_raises_exception(self):
        reader = FileReader('tests/data/empty.txt')
        with self.assertRaises(Exception):
            list(reader.read_lines())

