import logging
class logger_employee():
    def __init__(self,log_file_name,log_name):
        self.logger = log_name
        self.logger.setLevel(logging.DEBUG)
        self.format = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

        self.file_handler = logging.FileHandler(log_file_name)
        self.file_handler.setFormatter(self.format)

        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(self.format)

        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.stream_handler)
    @property
    def logger(self):
        return self._logger
    @logger.setter
    def logger(self,name):
        self._logger=logging.getLogger(name)


