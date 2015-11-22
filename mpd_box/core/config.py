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
        iniFile.readfp(open(mpd_box.__path__[0] + '/config.ini'))
        # config.read(['site.cfg', os.path.expanduser('~/.myapp.cfg')])

        logger = logging.getLogger('mpd-box')

        logger.info('Load init file. Sections [mpd_box:manage]')
        logger.info(iniFile.items('mpd_box:manage'))

        self.iniFile = iniFile