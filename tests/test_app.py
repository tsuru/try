from unittest import TestCase
import json
import os

import mock

from registration.app import app, add_user


class AppTestCase(TestCase):
    def test_index(self):
        self.app = app.test_client()
        response = self.app.get("/")
        self.assertEqual(200, response.status_code)

    def test_help(self):
        self.app = app.test_client()
        response = self.app.get("/help")
        self.assertEqual(200, response.status_code)

    @mock.patch("requests.post")
    def test_add_user(self, post_mock):
        os.environ["TSURU_HOST"] = "http://localhost"
        add_user("a@a.com", "pass", "0000")
        expected = json.dumps({
            "email": "a@a.com",
            "password": "pass",
        })
        post_mock.assert_called_with("http://localhost/users", data=expected)
