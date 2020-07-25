from flask import request, json, Response, Blueprint
from ..components.utils import custom_response

projects_api = Blueprint('projects', __name__)

@projects_api.route('/', methods=['GET'])
def index():
    return "hello"