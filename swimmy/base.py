from .utils.logger import LoggingBase


class Base(metaclass=LoggingBase):

    def log_exception(self, val):
        self.__logger.error(val)
