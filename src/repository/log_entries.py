from ..data.model.log_entry import LogEntry
from ..data.file_reader import FileReader
import re

class LogEntriesRepository:

    def __init__(self, fileReader):
        self.reader = fileReader
        self.timeRx = '\d\d:\d\d:\d\d\.\d\d\d'
        self.codeRx = '\d\d\d'
        self.pilotRx = '[\w\.]+'
        self.lapRx = '\d'
        self.lapTimeRx = '\d:\d\d\.\d\d\d'
        self.avgSpeedRx = '[\d,]+'
        self.regex = '^({})\t+({}) .? ({})\t+({})\t+({})\t+({})$'.format(self.timeRx, self.codeRx, self.pilotRx, self.lapRx, self.lapTimeRx, self.avgSpeedRx)

    def get_logs(self):
        for idx, item in enumerate(self.reader.read_lines()):
            if idx:
                if self._isLineParseable(idx, item):
                    yield item

    def _isLineParseable(self, idx, line):
        stripped = line.strip()
        if len(stripped) == 0:
            print('Line {} is empty. Ignoring...'.format(idx + 1))
            return False

        regex = re.compile('^{}$'.format(self.regex))
        return re.match(regex, line)

