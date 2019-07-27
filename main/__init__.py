import os

from flask import Flask

from . import db, views

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=database_file
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    views.setup_views(app)

    db.init_db(app)

    return app

