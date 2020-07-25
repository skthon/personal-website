from flask import request, json, Response, Blueprint
from ..components.utils import custom_response

activities_api = Blueprint('activities', __name__)

@activities_api.route('/', methods=['GET'])
def index():
    return "hello"