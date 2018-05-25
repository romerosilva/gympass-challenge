from ..data.model.log_entry import LogEntry
from ..data.file_reader import FileReader

class LogEntriesRepository:

    def __init__(self, fileReader):
        self.reader = fileReader

    def get_logs(self):
        for idx, item in enumerate(self.reader.read_lines()):
            if idx:
                line = item.strip()
                if len(line) == 0:
                    print('Line {} is empty. Ignoring...'.format(idx + 1))
                else:
                    yield item
