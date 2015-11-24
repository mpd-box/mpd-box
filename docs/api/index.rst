.. _api-endpoints:

API
###

MPD-Box has two distinct API to use. First one is from MPD, other one is running on Pyramid and designed to manage tags.

Cheatsheet
==========

MPD
---

MPD provide an API to control most feature. You can find `Client Libraries <http://mpd.wikia.com/wiki/Client_Libraries>`_ readdy to use and implement on your project.

MPD-Box use `python-mpd2 <http://mpd.wikia.com/wiki/ClientLib:python-mpd2>`_.

MPD-Box API
-----------

MPD-Box has a RESTFull API to control tags.

+----------+-------------------------------------------------+---------------------------------------------------------+
| Method   | URI                                             | Description                                             |
+==========+=================================================+=========================================================+
| `GET`    | :ref:`/current-id <api-tags>`                   | :ref:`Return current tag-id read by mpd-box <api-tags>` |
+----------+-------------------------------------------------+---------------------------------------------------------+
| **Tags**                                                                                                             |
+----------+-------------------------------------------------+---------------------------------------------------------+
| `POST`   | :ref:`/tag/(tag_id) <tag-post>`                 | :ref:`Create a tag <api-tags>`                          |
+----------+-------------------------------------------------+---------------------------------------------------------+
| `GET`    | :ref:`/tag/(tag_id) <tag-get>`                  | :ref:`Retrieve an existing tag <api-tags>`              |
+----------+-------------------------------------------------+---------------------------------------------------------+

Full reference
==============

.. toctree::
   :maxdepth: 1

   references/tags