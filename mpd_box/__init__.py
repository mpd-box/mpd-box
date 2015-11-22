

# from pyramid.config import Configurator
# import thread

# import logging
# import logging.handlers

# def main(global_config, **settings):
#     """ 
#     	This function returns a Pyramid WSGI application.
#     """ 

#     logging.info('Starting pyramid')
    
#     logging.info(settings)


#     # Start
#     config = Configurator(settings=settings)
#     config.include('pyramid_chameleon')
    
#     config.add_route('current-tag-id', '/current-tag-id')
#     config.add_route('tag', '/tag/{id}')
#     config.add_view('mpd_box.views.TAGView')

#     config.scan()

#     readers = [var for var in config.registry.settings['mpd_box.readers'].split('\n') if var]
 
#     # Dynamically load and start each reader in a thread
#     # Eg : mpd_box.readers.nfc.raspberry_explorer_board
#     for reader in readers:
#         # Separate path and file name
#         path, obj =  reader.rsplit('.', 1)
#         # Load path mpd_box.readers.nfc
#         p = __import__(path, globals(), locals(), [obj])
#         # Load py file raspberry_explorer_board
#         object1 = getattr(p, obj)

#         logging.info('Service are running start nom reader thread')

#         # Get Object raspberry_explorer_board from py file and execute.
#         thread.start_new_thread(getattr(object1, obj),())

#     return config.make_wsgi_app()
