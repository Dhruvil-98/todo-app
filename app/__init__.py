from flask import Flask

# Remove unused import
# from .routes import some_route


def create_app():
    app = Flask(__name__)
    return app
