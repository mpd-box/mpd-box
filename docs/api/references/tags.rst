.. _api-tags:

Tags related
============

GET /current-tag-id
-------------------

Return id of current tag. 

.. code-block:: javascript

	{
		"current-tag-id": "2499F6C5"
	}

If no tag selected, return ``current-tag-id = None``.

.. _tag-post:

POST /tag/(tag_id)
------------------

.. code-block:: bash
	
	POST /tag/2499F6C5

JSON is send as content in POST request (and not as parameters).

.. code-block:: javascript

	{
		"id": "2499F6C5",
		"random": true,
		"repeat": true,
		"songs": [
			"Folder/Artist X/Track 2.mp3", 
			"Folder/Artist X/Track 7.mp3", 
			"Folder/Artist Y/Track 42.mp3",
			...
		]
	}


Is saved in redis with key ``tags:(tag_id)``.

.. _tag-get:

GET /tag/(tag_id)
-----------------

Return description of a tag. Exact same structure as saved in REDIS

.. code-block:: bash
	
	GET /tag/2499F6C5

Return JSON structure

.. code-block:: javascript

	{
		"id": "2499F6C5",
		"random": true,
		"repeat": true,
		"songs": [
			"Folder/Artist X/Track 2.mp3", 
			"Folder/Artist X/Track 7.mp3", 
			"Folder/Artist Y/Track 42.mp3",
			...
		]
	}

If tag_id is undefined, return 404 error code.
