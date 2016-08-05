from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from .models import db
from .models.auth import User, Role


def factory(config):
    """
    Flask Application Factory function

    Generate a new Flask application through this function by specifying
    a config object.

    Args:
        config: The configuration class to be used.
    """

    app = Flask(__name__)

    config = config or 'etc.config.DefaultConfig'
    app.config.from_object(config)

    auth_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, auth_datastore)

    return app
