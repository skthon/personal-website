from flask import request, json, Response, Blueprint
from ..components.utils import custom_response

work_api = Blueprint('work', __name__)

@work_api.route('/', methods=['GET'])
def index():
    return custom_response({'jwt_token': "hello"}, 201)