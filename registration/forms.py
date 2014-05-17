from wtforms import Form, validators, TextField, PasswordField, BooleanField


class SignupForm(Form):
    email = TextField(u"Email", [validators.Required()])
    password = PasswordField(u"Password", [validators.Required()])
    password_confirmation = PasswordField(u"Password confirmation")
    identity = TextField(
        u"National Identification Number",
        [validators.Required()]
    )
    terms = BooleanField(u"I accept the Terms", [validators.Required()])
