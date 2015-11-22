# -*- coding: utf-8 -*-
from mpd import MPDClient

from mpd_box.core.config import Configuration
from mpd_box.core.logger import Logger


import logging
import json
import nxppy
import redis
import time

# Need to be same name as file
def raspberry_explorer_board():

    logger = Logger().getLogger()
    config = Configuration()
    # Connect to MPD
    client = MPDClient() 
    client.connect("localhost", int(config.iniFile.get('mpd','port')))

    # Connect to NFC Explorer board
    logger.info('Connect to nxppy Mifare')
    mifare = nxppy.Mifare()

    # Initialize storage
    logger.info('Connect to Redis')
    storage = redis.StrictRedis(host='localhost', port=int(config.iniFile.get('redis','port')), db=0)

    # Count pauses to make sure it is not a error reading
    nbPause = 0
    # Keep previous uid to compare with current one
    previous_uid = None
    # Data from taf
    data = None

    if mifare is None:
        logger.info("Error while loading NFC Explorer Board")
    else:
        logger.info("Reader NFC Raspberry is now running")

        while True:
            try:
                uid = mifare.select()
                if uid is not None:
                    if uid == previous_uid:
                        nbPause = 0
                        if data:
                            status = client.status()
                            if status['state'] == 'stop':
                                logger.info("Play")
                                storage.set('current-tag-id', uid)
                                client.play(0)
                            if status['state'] == 'pause':
                                logger.info("Continue")
                                storage.set('current-tag-id', uid)
                                client.pause(0)
                        else:
                            pass
                    else:
                        previous_uid = uid

                        logger.info("New chip detected : %s" % uid)
                        # Save current-tag-id in memory to be used by services
                        storage.set('current-tag-id', uid)

                        # Stop mpd and 
                        client.stop()   
                        client.clear()

                        # Get from storage list of songs to play
                        tag = storage.get("tags:" + uid)

                        if tag is None:
                            logger.info("Unknown chip %s" % uid)
                            data = None
                        else:
                            # Load data
                            data = json.loads(tag)

                            logger.info(data)

                            # Configure MPD server
                            client.random(1 if data['random'] else 0)
                            client.repeat(1 if data['repeat'] else 0)

                            # Add songs
                            for song in data['songs']:
                                client.add(song)

                            if data['random']:
                                client.shuffle()

                            client.play(0)
                    
            except nxppy.SelectError:

                # Random error reading. Avoi
                if nbPause == 2:
                    nbPause = 0
                    # If play then 
                    if client.status()['state'] == 'play':
                        logger.info("Detect missing chip")
                        logger.info("Pause")
                        storage.delete('current-tag-id')
                        client.pause(1)
                    # If us
                    elif previous_uid and not data:
                        previous_uid = None
                        storage.delete('current-tag-id')
                else:
                    nbPause = nbPause + 1
            except Exception as e:
                logger.critical('Exception')
                logger.critical('%s' % str(e))
