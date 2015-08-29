#!/usr/bin/python
import os
import sys

from mpd import MPDClient

import zbar


SONGS = {
    '1': 'Sinsemilia/resistances/la flamme.mp3',
    '2': 'Virginie/Dreamer/10 - Un peu de moi.mp3'
}

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
        if number in SONGS:
            track = SONGS[number]
            client.connect('localhost', 6600)
            current_pos = client.status()['song']
            if song_id:
                client.deleteid(song_id)
            song_id = client.addid(track, current_pos)
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
