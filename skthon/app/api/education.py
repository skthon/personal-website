from flask import request, json, Response, Blueprint
from ..components.utils import custom_response

education_api = Blueprint('education', __name__)

@education_api.route('/', methods=['GET'])
def index():
    education_data = [
        {
            "year": "1994",
            "name": "Born",
            "institution_name": "",
            "specialization": "",
            "img_path": "",
            "university": "",
        },
        {
            "year": "2010 April",
            "name": "High School Education",
            "institution_name": "St Josephs High School",
            "specialization": "",
            "img_path": "",
            "university": "",
        },
        {
            "year": "2011 April",
            "name": "Secondary Education",
            "institution_name": "Sri Chaitanya Junior College",
            "specialization": "Mathematics, Physics and Chemistry",
            "img_path": "",
            "university": "",
        },
        {
            "year": "2012 April",
            "name": "Senior Secondary Education",
            "institution_name": "Sri Chaitanya Junior College",
            "specialization": "Mathematics, Physics and Chemistry",
            "img_path": "",
            "university": "",
        },
        {
            "year": "2016 April",
            "name": "Graduation",
            "institution_name": "VNR Vignana Jyothi Institute of Engineering & Technology",
            "specialization": "Bachelors in Electrical and Electronics Engineering",
            "university": "Jawaharlal Nehru Technological University, Hyderabad",
            "img_path": ""
        },
        {
            "year": "2016 July - 2016 December",
            "name": "Triptam Labs Private Limited",
            "institution_name": "",
            "specialization": "Software Engineer Intern",
            "university": "",
            "img_path": ""
        },
        {
            "year": "2016 December - present",
            "name": "Unwired Labs Private Limited",
            "institution_name": "",
            "specialization": "Full Stack Developer",
            "university": "",
            "img_path": ""
        }
    ]

    return custom_response(education_data, 200)