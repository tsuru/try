from flask.ext import wtf
import wtforms


class SignupForm(wtf.Form):
    email = wtforms.TextField(u"Email")
    password = wtforms.PasswordField(u"Password")
    password_confirmation = wtforms.PasswordField(u"Password confirmation")
    identity = wtforms.TextField(u"National Identification Number")
    terms = wtforms.BooleanField(u"I accept the Terms")
