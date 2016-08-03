from flask import Flask

def factory(config):

    app = Flask(__name__)

    if config:
        app.config.from_object(config)

    return app
