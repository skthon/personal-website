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
app.register_blueprint(song_blueprint, url_prefix='/songs')

""" add Work API """
from .api.work import work_api as work_blueprint
app.register_blueprint(work_blueprint, url_prefix='/work')

""" add education API """
from .api.education import education_api as education_blueprint
app.register_blueprint(education_blueprint, url_prefix='/education')

""" add adventures API """
from .api.adventures import adventures_api as adventures_blueprint
app.register_blueprint(adventures_blueprint, url_prefix='/adventures')

""" add activities API """
from .api.activities import activities_api as activities_blueprint
app.register_blueprint(activities_blueprint, url_prefix='/activities')

""" add projects API """
from .api.projects import projects_api as projects_blueprint
app.register_blueprint(projects_blueprint, url_prefix='/projects')


@app.route('/')  
def home():  
    return "hello"

""" Initialize the sqlalchemy """
db.init_app(app)