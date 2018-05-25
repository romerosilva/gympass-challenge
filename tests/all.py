import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src/'
sys.path.insert(0, os.path.abspath(testdir))
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
from tests.test_kart_analytics import KartAnalyticsTest
from tests.data.test_file_reader import FileReaderTest
from tests.repository.test_log_entries import LogEntriesRepositoryTest
from tests.repository.test_statistics import StatisticsRepositoryTest


if __name__ == "__main__":
    unittest.main()
