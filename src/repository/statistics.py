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
        for k, g in groupby(data, key=lambda record: record.code):
            self.groups[k] = list(g)
            self.keys.append(k)

