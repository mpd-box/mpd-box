.. _api-endpoints:

API
###

MPD-Box has two distinct API to use. First one is from MPD, other one is running on Pyramid and designed to manage tags.

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
| `GET`    | /info                                           | Retrieve MPD-box current status                         |
+----------+-------------------------------------------------+---------------------------------------------------------+
| `GET`    | /current-id                                     | Return current tag-id read by mpd-box                   |
+----------+-------------------------------------------------+---------------------------------------------------------+
| **Tags**                                                                                                             |
+----------+-------------------------------------------------+---------------------------------------------------------+
| `GET`    | /tags/(tag_id)                                  | Retrieve a tag object                                   |
+----------+-------------------------------------------------+---------------------------------------------------------+
| `POST`   | /tags/(tag_id)                                  | Create a tag object                                     |
+----------+-------------------------------------------------+---------------------------------------------------------+

