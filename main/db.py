import click

from enum import Enum
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
    app.cli.add_command(create_db_command)


def create_db():
    db.create_all()


@click.command('create-db')
@with_appcontext
def create_db_command():
    db.create_all()
    click.echo('Initialized the database.')


class PersonType(Enum):
    ADULT = "Adult"
    CHILD = "Child"

    @classmethod
    def choices(cls):
        return [(choice, choice.name) for choice in cls]

    @classmethod
    def coerce(cls, item):
        if item == "Adult":
            return PersonType.ADULT
        if item == "Child":
            return PersonType.CHILD
        return None

    def __str__(self):
        return str(self.value)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String, nullable=False)
    firstname = db.Column(db.String)
