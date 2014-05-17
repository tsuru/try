from unittest import TestCase

import wtforms

from registration.forms import SignupForm


class SignupFormTestCase(TestCase):
    def test_should_be_a_wtform(self):
        self.assertTrue(issubclass(SignupForm, wtforms.Form))

    def test_fields(self):
        fields = {
            "email": wtforms.TextField,
            "password": wtforms.PasswordField,
            "password_confirmation": wtforms.PasswordField,
            "identity": wtforms.TextField,
            "terms": wtforms.BooleanField,
        }
        for field, cls in fields.items():
            self.assertEqual(cls, getattr(SignupForm, field).field_class)

    def test_required(self):
        form = SignupForm()
        form.process()
        self.assertFalse(form.validate())
        expected = {
            'email': [u'This field is required.'],
            'identity': [u'This field is required.'],
            'password': [u'This field is required.'],
            'terms': [u'This field is required.']
        }
        self.assertDictEqual(form.errors, expected)
