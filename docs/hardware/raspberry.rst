.. _raspberry:

Raspberry Pi
############

This page explain how to install MPD-Box on a Raspberry Pi.

Required hardware :

	- Raspberry Pi
	- SD Card (8go min)
	- USB Adapter for power supply
	- Ethernet cable (USB wifi card also works)
	- NFC explorer board
	- Some NFC chip (one included with NFC explorer, your credit card works too)

Operating System
================

Any linux distribution is good. We recommand to visit `raspbian official website <http://www.raspbian.org>`_ and download the latest version.

Copy it on your SD card, then plug it on your raspberry. Turn it on, and you should have a debian runnning :)

Activate NFC explorer board
===========================

To be able to use the NFC reader, you have to activate the SPI connector.

Open a terminal and write :

.. code-block:: bash

	$> sudo raspi-config

The option to activate SPI can be found as follows: ``Advanced Options`` > ``SPI`` > ``<Yes>``.

Now reboot your Raspberry Pi by typing the following command:
sudo reboot

Install MPD-Box
===============

Follow the instruction from the :ref:`installation section <installation>`. 
You should then be able to use it now.