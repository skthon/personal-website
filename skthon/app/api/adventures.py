from flask import request, json, Response, Blueprint
from ..components.utils import custom_response

adventures_api = Blueprint('adventures', __name__)

@adventures_api.route('/', methods=['GET'])
def index():
    return "hello"