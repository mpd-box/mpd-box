#!/usr/bin/python
import hashlib
import os
import sys
from uuid import UUID

from mpd import MPDClient

import zbar
from kintoclient import Collection

shingle = Collection('shingle', bucket="mpd-box",
                     server_url='https://kinto.dev.mozaws.net/v1',
                     load=False)

song_id = None
client = MPDClient()

# create a Processor
proc = zbar.Processor()

# configure the Processor
proc.parse_config('enable')

# initialize the Processor
if os.path.lexists('/dev/video1'):
    device = '/dev/video1'
else:
    device = '/dev/video0'
if len(sys.argv) > 1:
    device = sys.argv[1]
proc.init(device)

# enable the preview window
proc.visible = True


# setup handler
def mpd_handler(proc, image, _):
    global song_id

    for symbol in image:
        number = symbol.data
        print number
        track_id = str(UUID(hashlib.md5(number).hexdigest()))
        track_id = track_id[0:14] + '4' + track_id[15:19] + '8' + track_id[20:]
        try:
            track = shingle.get_record(track_id).data['uri']
        except Exception as e:
            import traceback
            traceback.print_exc()
            sys.exit(1)
        else:
            client.connect('localhost', 6600)
            current_pos = client.status()['song']
            if song_id:
                client.deleteid(song_id)
            try:
                song_id = client.addid(track, current_pos)
            except Exception as e:
                print "An error occured: %s" % e
            else:
                client.playid(song_id)
            client.disconnect()

# on read, start the mpd handler.
proc.set_data_handler(mpd_handler)

# initiate scanning
proc.active = True

# Wait until we close the window.
try:
    proc.user_wait()
except zbar.WindowClosed:
    pass
