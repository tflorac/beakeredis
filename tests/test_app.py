from flask import Flask, request
import unittest
from beaker.middleware import SessionMiddleware
import re
from datetime import datetime
import pytz
from dateutil import parser


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)

        session_options = {
            'session.cookie_domain': 'example.com',
            'session.cookie_expires': True,
            'session.cookie_path': '/',
            'session.httponly': True,
            'session.key': 'session_id',
            'session.secure': True,
            'session.serializer': 'json',
            'session.timeout': 600,
            'session.type': 'redis',
            'session.url': '127.0.0.1:6379'
        }

        app.wsgi_app = SessionMiddleware(app.wsgi_app, session_options)
        app.config['TESTING'] = True

        @app.route('/', methods=['GET'])
        def index():
            return 'OK'

        @app.route('/session', methods=['PUT'])
        def put_session():
            session = request.environ['beaker.session']
            session['authenticated'] = True
            session.save()
            return 'OK'

        @app.route('/session', methods=['DELETE'])
        def delete_session():
            session = request.environ['beaker.session']
            if session.get('authenticated', False):
                session.delete()
            return 'OK'

        @app.route('/private', methods=['GET'])
        def access_private():
            session = request.environ['beaker.session']
            if session.get('authenticated', False):
                return 'OK'
            return 'Forbidden', 403

        self.client = app.test_client()

    def create_session(self):
        r = self.client.put('/session')
        assert r.status_code == 200
        regexp = r'^\s+session_id\=(?P<id>[a-f0-9]{32}); Domain\=example.com; httponly; Path\=/; secure$'
        match = re.match(regexp, r.headers['set-cookie'])
        assert match is not None
        assert len(match.group('id')) == 32
        return match.group('id')

    def drop_session(self, session_id):
        headers = {'Cookie': 'session_id={0}'.format(session_id)}
        r = self.client.delete('/session', headers=headers)
        assert r.status_code == 200
        regexp = r'^\s+session_id\={0}; Domain\=example.com; expires\=(?P<expires>.+); httponly; Path\=/; secure'.format(session_id)
        match = re.match(regexp, r.headers['set-cookie'])
        assert match is not None
        now = datetime.now(tz=pytz.timezone('GMT'))
        expires = parser.parse(match.group('expires'))
        assert expires < now

    def test_app(self):
        session_id = self.create_session()
        print(session_id)
        headers = {'Cookie': 'session_id={0}'.format(session_id)}
        r2 = self.client.get('/private', headers=headers)
        assert r2.status_code == 200
        self.drop_session(session_id)
        r4 = self.client.get('/private')
        assert r4.status_code == 403
