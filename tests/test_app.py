from unittest import TestCase

from registration.app import app


class AppTestCase(TestCase):
    def test_index(self):
        self.app = app.test_client()
        response = self.app.get("/")
        self.assertEqual(200, response.status_code)

    def test_help(self):
        self.app = app.test_client()
        response = self.app.get("/help")
        self.assertEqual(200, response.status_code)

