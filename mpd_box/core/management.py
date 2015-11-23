from config import Configuration
from logger import Logger

from wsgiref.simple_server import make_server
from pyramid.response import Response
from pyramid.config import Configurator

import thread

def execute_from_command_line (args):
    """
        args = ['manage.py', 'start']
    """
    print args

    Logger().streamHandler(True)
    start_mpd_box()

def start_mpd_box():
    start_readers()
    start_server()

def start_readers():

    logger = Logger().getLogger()
    config = Configuration()

    readers = [var for var in config.iniFile.get('mpd_box','mpd_box.readers').split('\n') if var]
    logger.info(readers)

    # Dynamically load and start each reader in a thread
    # Eg : mpd_box.readers.nfc.raspberry_explorer_board
    for reader in readers:
        logger.info(reader)
        # Separate path and file name
        path, obj =  reader.rsplit('.', 1)
        # Load path mpd_box.readers.nfc
        p = __import__(path, globals(), locals(), [obj])
        # Load py file raspberry_explorer_board
        object1 = getattr(p, obj)

        logger.info('Service are running start %s thread' % obj)

        # Get Object raspberry_explorer_board from py file and execute.
        thread.start_new_thread(getattr(object1, obj),())

        logger.info('Thread is running')


def start_server():
    logger = Logger().getLogger()
    settings = Configuration()

    logger.info('Starting pyramid')

    config = Configurator(settings=settings.iniFile.items('mpd_box'))
    config.add_route('current-tag-id', '/current-tag-id')
    config.add_route('tag', '/tag/{id}')
    config.add_view('mpd_box.server.views.TAGView')
    config.scan('mpd_box.server')

    logger.info('Views are up to date')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', int(settings.iniFile.get('mpd_box','port')), app)

    logger.info('Server is now running')

    server.serve_forever()
