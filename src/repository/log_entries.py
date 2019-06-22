from data.model.log_entry import LogEntry
from data.file_reader import FileReader
from datetime import datetime
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
        self.regex = f'^({self.timeRx})\t+({self.codeRx}) .? ({self.pilotRx})\t+({self.lapRx})\t+({self.lapTimeRx})\t+({self.avgSpeedRx})$'

    def get_logs(self):
        for idx, item in enumerate(self.reader.read_lines()):
            if idx:
                parsed = self._parseLine(idx, item) if self._isLineParseable(idx, item) else None
                if parsed:
                    yield parsed

    def _isLineParseable(self, idx, line):
        stripped = line.strip()
        if len(stripped) == 0:
            print(f'Line {idx + 1} is empty. Ignoring...')
            return False

        regex = re.compile(self.regex)
        match = re.match(regex, line)

        if not match:
            print(f'Line {idx + 1} could not be parsed. Invalid format. Ignoring...')

        return match

    def _parseLine(self, idx, line):
        try:
            regex = re.compile(self.regex)
            groups = re.search(regex, line)
            logEntry = LogEntry()
            logEntry.time = datetime.strptime(groups[1], '%H:%M:%S.%f')
            logEntry.code = groups[2]
            logEntry.pilot = groups[3]
            logEntry.lap = groups[4]

            adjustedLapTime = f'0{groups[5]}'
            logEntry.lapTime = datetime.strptime(adjustedLapTime, '%M:%S.%f')
            adjustedAvgSpeed = groups[6].replace(',','.')
            logEntry.avgSpeed = float(adjustedAvgSpeed)

            return logEntry
        except Exception as e:
            print(f'Failed to parse line {idx + 1}: {e}')

        return None
