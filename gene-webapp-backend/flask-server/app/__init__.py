from flask import Flask

app =Flask(__name__)

def create_app():
    """Initialize the flask app instance
    """
    app = Flask(__name__)
    return app