import sys, os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from .config import app_config
from .models import db

""" Initialize the flask app """
app = Flask(__name__)

""" Add configuration parameters for the app """
# todo: Add environment variable when creating the container
# app_env = os.getenv(FLASK_ENV)
FLASK_ENV = 'development'
app.config.from_object(app_config[FLASK_ENV])

""" add Songs API """
from .api.songs import songs_api as song_blueprint
app.register_blueprint(song_blueprint, url_prefix='/v1/songs')

""" Initialize the sqlalchemy """
db.init_app(app)