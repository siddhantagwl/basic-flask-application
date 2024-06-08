from flask import Flask
from board import pages
from board.views import views

def create_app():
    app = Flask(__name__)

    app.register_blueprint(pages.bp)
    app.register_blueprint(views)

    return app
