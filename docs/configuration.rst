.. _configuration:

Configuration
#############

MPD-Box use `python ConfigParser module <https://docs.python.org/2/library/configparser.html>`_ to store and read app config file.

Default configuration is saved in ``mpd_box/config.default.cfg`` but is override by ``~/.mpd-box.cfg``

You can read default config file to learn about MPD-Box, but main properties are the followong :


.. code-block:: bash

	[mpd_box]
	# List of readers to activate
	mpd_box.readers = 
		mpd_box.readers.nfc.raspberry_explorer_board

	# Port to access MPD-Box services
	port = 6543

	[mpd]
	# Redefine port to access MPD
	# default : 6600
	port = 6600

	[redis]
	# Redefine port to access Redis
	# default : 6379
	port = 6379

.. warning::

	If run as administrator, ``~`` is relative to root user, probably ``/root``.