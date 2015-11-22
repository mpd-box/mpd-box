import sys
import logging
import logging.handlers

from utils import Singleton

class LoggerWriter:

    def __init__(self, level):
        # self.level is really like using log.debug(message)
        # at least in my case
        self.level = level

    def write(self, message):
        # if statement reduces the amount of newlines that are
        # printed to the logger
        if message != '\n':
            self.level(message)

    def flush(self):
        # create a flush method so things can be flushed when
        # the system wants to. Not sure if simply 'printing'
        # sys.stderr is the correct way to do it, but it seemed
        # to work properly for me.
        self.level(sys.stderr)


class Logger(object):

    __metaclass__ = Singleton

    def __init__(self):
        logger = logging.getLogger('mpd-box')
        logger.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s %(levelname)-5.5s [%(name)s][%(threadName)s] %(message)s')
            
        # CONSOLE
        self.consoleHandler = logging.StreamHandler()
        self.consoleHandler.setLevel(logging.DEBUG)
        self.consoleHandler.setFormatter(formatter)
        # logger.addHandler(self.consoleHandler)

        # Redirect print to logger
        sys.stdout = LoggerWriter(logger.info)
        sys.stderr = LoggerWriter(logger.error)

        # create console handler and set level to debug
        self.fileHandler = logging.handlers.RotatingFileHandler('/var/log/mpd-box.log', maxBytes=2000000, backupCount=5)
        self.fileHandler.setLevel(logging.DEBUG)
        self.fileHandler.setFormatter(formatter)
        # logger.addHandler(self.fileHandler)

        self.logger = logger

    def streamHandler(self, enable):
        """
            Activate console logging
        """
        if enable:
            self.logger.addHandler(self.consoleHandler)
        else:
            self.logger.removeHandler(self.consoleHandler)

    def rotatingFileHandler(self, enable):
        """
            Activate file logging
        """
        if enable:
            self.logger.addHandler(self.fileHandler)
        else:
            self.logger.removeHandler(self.fileHandler)

    def getLogger(self):
        return self.logger
