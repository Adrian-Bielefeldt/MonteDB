from wtforms import Form, HiddenField, StringField

from .db import PersonType


class PersonForm(Form):
    personID = HiddenField()
    lastname = StringField('Last Name')
    firstname = StringField('First Name')
