from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock

from application import app, db
from application.routes import Qrand

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = 'sqlite:///')

        return app

    def setUp(self):
        db.create_all()
        db.session.add(Qrand(qran_num='test num', qran_meal='debug', qran_what='what'))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):

    

    def test_pbj(self):
        with requests_mock.mock() as m:
            m.get("http://qrandom-qran:5000/qran", text = '4000')
            m.get("http://qrandom-meal:5000/meal", text = 'pbj')
            m.post("http://qrandom-whatudone:5000/whatudone", text = 'random number 4000 advises pbj!')
            
            response = self.client.get(url_for('index'))
            self.assertIn(b'random number 4000 advises pbj!', response.data)
            
            self.assertIn(b'eating a debug randomised by test num caused what', response.data)