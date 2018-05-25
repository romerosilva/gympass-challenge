import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src/'
sys.path.insert(0, os.path.abspath(testdir))
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
from tests.test_kart_analytics import KartAnalyticsTest

if __name__ == "__main__":
    unittest.main()
