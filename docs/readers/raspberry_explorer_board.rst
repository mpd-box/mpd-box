.. _raspberry_explorer_board:

Raspberry Explorer Board 
########################

This reader has been design to work with the NF explorer Board.

Installation
------------

This reader require you to install a python library to allow MPD-Box accessing the hardware : **nxppy**

.. code-block:: bash

	pip install nxppy

This can take few minutes since your rapsberry needs to compile it.

Configuration
-------------

In your configuration file, add ``mpd_box.readers.nfc.raspberry_explorer_board``:

.. code-block:: bash

	[mpd_box]
	# List of readers to activate
	mpd_box.readers = 
		mpd_box.readers.nfc.raspberry_explorer_board

Behaviour
---------

Put a tag, music start. Remove it, music stop.