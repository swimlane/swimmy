from .utils.logger import LoggingBase
from .config import Config


class Base(metaclass=LoggingBase):

    __instance = None
    config = Config()

    @property
    def instance(self):
        if not self.__instance:
            from .instance import SwimlaneInstance
            try:
                # Connecting to the desired Swimlane instance
                self.__instance = SwimlaneInstance(**Base.config.swimlane)
            except:
                raise Exception('Please make sure you have the correct authentication credentials to your Swimlane instance.')
        return self.__instance

    def log_exception(self, val):
        self.__logger.error(val)
