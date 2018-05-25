from .log_entries import LogEntriesRepository
from itertools import groupby
from functools import reduce
from datetime import datetime

class StatisticsRepository:

    def __init__(self, logEntries):
        self.logEntries = logEntries
        self.timeFormat = '%H:%M:%S.%f'
        self.groups = {}
        self.keys = []

    def _calculateResult(self, records):
        sortedData = sorted(records, key=lambda record: record.code)
        self._groupByRacer(sortedData)
        result = self._sortByLastLap(self.keys, self.groups)
        return result

    def _sortByLastLap(self, keys, groups):
        result = []

        for key in keys:
            result.append(groups[key][-1])

        return sorted(result, key=lambda record: record.time)

    def _groupByRacer(self, data):
        if len(self.groups) > 0:
            return

        for k, g in groupby(data, key=lambda record: record.code):
            self.groups[k] = list(g)
            self.keys.append(k)

    def get_result(self):
        result = self._calculateResult(self.logEntries.get_logs())

        for idx, record in enumerate(result):
            yield (idx + 1, record.code, record.pilot, record.lap, self._get_total_race_time_for(record))

    def _get_total_race_time_for(self, record):
        minDate = datetime.min
        lapTimes = [item.lapTime - minDate for item in self.groups[record.code]]
        total = reduce(lambda sum, item: sum + item, lapTimes)
        minutes = int(total.seconds / 60)
        seconds = total.seconds - (minutes * 60)
        miliseconds = int(total.microseconds / 1000)
        return '{}:{}.{}'.format(minutes,seconds,miliseconds)
