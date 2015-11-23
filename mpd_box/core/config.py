import ConfigParser, os
import logging

import mpd_box 

from utils import Singleton

class Configuration(object):
    """
        Singleton to store mpd-box settings
    """
    __metaclass__ = Singleton

    def __init__(self):
        
        iniFile = ConfigParser.ConfigParser()
        iniFile.read([mpd_box.__path__[0] + '/config.default.cfg', os.path.expanduser('~/.mpd-box.cfg')])
        # config.read(['site.cfg', os.path.expanduser('~/.myapp.cfg')])

        logger = logging.getLogger('mpd-box')

        logger.info('Load init file. Sections [mpd_box]')
        logger.info(iniFile.items('mpd_box'))

        self.iniFile = iniFile