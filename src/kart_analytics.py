from repository.statistics import StatisticsRepository
from repository.log_entries import LogEntriesRepository
from data.file_reader import FileReader
import sys
import os

def main(argv=[]):
    usage = 'Usage: kart_analytics.py <path-to-file>'
    if len(argv) == 0:
        print(usage)
        sys.exit(1)

    if len(argv) > 1:
        print('ERROR: Multiple arguments provided.')
        print(usage)
        sys.exit(2)

    try:
        if os.path.isfile(argv[0]):
            reader = FileReader(argv[0])
            logRepo = LogEntriesRepository(reader)
            statsRepo = StatisticsRepository(logRepo)
            print(statsRepo)
            statsRepo.print_result()

        else:
            raise Exception('Unexpected program argument. Only files are allowed.')

    except Exception as e:
        print(f'ERROR: {e}')
        sys.exit(3)

if __name__ == "__main__":
    main(sys.argv[1:])
