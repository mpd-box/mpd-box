export KINTO_USER=user
export KINTO_PASS=pass

echo '{"data": {}}' | http PUT https://kinto.dev.mozaws.net/v1/buckets/mpd-box --auth ${KINTO_USER}:${KINTO_PASS}
echo '{"data": {}, "permissions": {"read": ["system.Everyone"]}}' | http PUT https://kinto.dev.mozaws.net/v1/buckets/mpd-box/collections/shingle --auth ${KINTO_USER}:${KINTO_PASS}
echo '{"data": {"uri": "Sinsemilia/resistances/la flamme.mp3"}}' | http PUT https://kinto.dev.mozaws.net/v1/buckets/mpd-box/collections/shingle/records/c4ca4238-a0b9-4382-8dcc-509a6f75849b --auth ${KINTO_USER}:${KINTO_PASS}
echo '{"data": {"uri": "Virginie/Dreamer/10 - Un peu de moi.mp3"}}' | http PUT https://kinto.dev.mozaws.net/v1/buckets/mpd-box/collections/shingle/records/c81e728d-9d4c-4f63-8f06-7f89cc14862c --auth ${KINTO_USER}:${KINTO_PASS}
