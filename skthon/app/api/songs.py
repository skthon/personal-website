from flask import request, json, Response, Blueprint
from ..models.SongsModel import SongsModel, SongsSchema
from ..components.utils import custom_response

songs_api = Blueprint('songs', __name__)
songs_schema = SongsSchema()

@songs_api.route('/', methods=['GET'])
def index():
    return "hello"