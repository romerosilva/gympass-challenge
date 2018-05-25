import os
class FileReader:

    def __init__(self, file):
        self.file = file

    def read_lines(self):
        with open(self.file,'r') as f:
            self._check_if_empty_file(f)

    def _check_if_empty_file(self, file):
        if os.fstat(file.fileno()).st_size == 0:
            raise Exception('File is empty')


