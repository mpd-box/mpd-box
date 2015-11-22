.. _run:

Run
###

Console
-------

You can run MPD-Box using command line ``mpd-box``.

.. code-block:: bash

	mpd-box start

Daemon
------

To run as daemon.
	
.. code-block:: bash

	mpd-box start --daemonize
	mpd-box restart
	mpd-box stop

As a service
------------

You can run MPD-Box as a unix service. 
Copy mpd-box-daemon script to ``/etc/init.d`` directory.

.. code-block:: bash

	sudo cp <mpd_box_path>/scripts/mpd-box-daemon /etc/init.d/mpd-box

You can now use service command line to controle mpd-box.

.. code-block:: bash
	
	sudo service mpd-box start
	sudo service mpd-box status
	sudo service mpd-box restart
	sudo service mpd-box stop

It will automatically start on system launch. Logs can be consulted in ``/var/log/mpd-box.log``.