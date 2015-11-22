from pyramid.view import view_config, view_defaults

from pyramid.response import Response

import pyramid.httpexceptions as exc

import json
import redis

# Initialize storage
storage = redis.StrictRedis(host='localhost', port=6379, db=0)

@view_config(route_name='current-tag-id', renderer='json')
def current_tag_id(request):

    return {
        'current-tag-id': storage.get('current-tag-id')
    }

@view_defaults(route_name='tag')
class TAGView(object):
    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET', renderer='json')
    def get(self):

        obj = storage.get('tags:' + self.request.matchdict['id'])

        if not obj:
            raise exc.HTTPNotFound()
        return json.loads(obj)

    @view_config(request_method='POST', renderer='json')
    def post(self):

        obj = storage.set('tags:' + self.request.matchdict['id'], json.dumps(self.request.json_body))

        return {
            'code': 200
        }