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

        files = []
        files.append(mpd_box.__path__[0] + '/config.default.cfg')
        
        if os.path.isfile(os.path.expanduser('~/.mpd-box.cfg')):
            files.append(os.path.expanduser('~/.mpd-box.cfg'))
        elif os.path.isfile(os.path.expanduser('/etc/.mpd-box.cfg')):
            files.append(os.path.expanduser('/etc/mpd-box.cfg'))

        iniFile = ConfigParser.ConfigParser()
        iniFile.read(files)
        # config.read(['site.cfg', os.path.expanduser('~/.myapp.cfg')])

        logger = logging.getLogger('mpd-box')

        logger.info('Load init file. Sections [mpd_box]')
        logger.info(iniFile.items('mpd_box'))

        self.iniFile = iniFile