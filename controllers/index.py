from app import app
from flask import render_template

import constants


@app.route('/', methods=['GET'])
# выводим форму
def index():
    html = render_template('index.html',
                           program_list=constants.programs,
                           subject_list=constants.subjects,
                           olymp_compet_list=constants.olymp_compet,
                           len=len
                           )
    return html

