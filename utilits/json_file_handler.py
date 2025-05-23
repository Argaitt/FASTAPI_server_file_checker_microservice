import json
import threading
from logging.handlers import RotatingFileHandler


class JsonFilehandler(RotatingFileHandler):
    def __init__(self, *args, **kwds):
        self._lock = threading.Lock()
        super().__init__(*args, **kwds)
        self.write_array_start()

    def emit(self, record):
        with self._lock:
            if self.stream.tell() > 1:
                self.stream.write(',\n')
            super().emit(record)
            self.stream.flush()


    def close(self):
        self.write_array_end()
        super().close()

    def doRollover(self):
        with self._lock:
            self.write_array_end()
            super().doRollover()
            self.write_array_start()

    def write_array_start(self):
        with self._lock:
            if self.stream.tell() == 0:
                self.stream.write('[\n')
                self.stream.flush()
        pass

    def write_array_end(self):
        with self._lock:
            if self.stream and self.stream.tell() > 0:
                self.stream.write('\n]')
                self.stream.flush()
