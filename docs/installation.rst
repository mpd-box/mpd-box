.. _installation:

Installation
############

To actually run mpb-box, you need to install on local machine **mpd** and **redis**. Then follow one of the follow.

MPD
===

Follow instructions from `Music Player Daemon official documentation <http://www.musicpd.org/doc/user/install.html>`_.

.. note::

	It is highly recommanded to install MPD using a local configuration (per user) to avoid forbidden access to music's file.
	Instruction can be found on `arch linux wiki <https://wiki.archlinux.org/index.php/Music_Player_Daemon#Local_configuration_.28per_user.29>`_ (works great on every distribution).

You can use ``mpc`` to verify your installation

.. code-block:: bash

	pi@raspberrypi ~ $ mpc status
	volume: 90%   repeat: off   random: on    single: off   consume: off

MPD should automatically start on start. If you installed it using a local configuration, make sure you did configure your ``.profile`` to launch it on login.

MPD-Box does not manage your music yet. You need to configure a path in MPD and save some files in it. We recommand to create then a symbolic link to your medias and access a USB stick.

Redis
=====

Follow instructions from `Redis Quick Start documentation <http://redis.io/topics/quickstart>`_.

MPD-Box
=======

pip
---

You can use pip to install mpd-box.

.. code-block:: bash

	pip install mpb-box

setuptools
----------

MPD-Box is available as a python module defined in ``setup.py`` on root folder. 
Use git to clone code from github repository.

.. code-block:: bash

	git clone https://github.com/mpd-box/mpd-box.git

Then install it in your python environment.

.. code-block:: bash

	cd mpd-box
	python setup.py install

Feel free to read Python documentation about `Installing Python Modules <https://docs.python.org/2/install/index.html>`_ to learn more about setup.py.

You should now be able to run mpd-box using command line. 

.. code-block:: bash

	mpd-box start

.. warning:: You system might require mpd-box to run as root to access hardware *(like NFC reader)*. To do so, just run mpd-box using ``sudo``.

Next section is about how to configure and run mpd-box.


Zeroconf (optional)
====================

It might be usefull installing `Ahari-daemon <http://avahi.org/>`_ to activate *zeroconf* and have an easy access from other devices.

This will use local hostname as a domain name on your local network. If your device is named ``MPD-Box`` (recommanded)
then you will be able to access it using MPD-Box.local as a domain name. 

Installation procedure depend on your operating system.