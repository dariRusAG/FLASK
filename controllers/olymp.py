import constants
from app import app
from flask import render_template, request


@app.route('/olymp/<ol>')
def olymp(ol):
    html = render_template('olymp.html',
                           ol=ol,
                           discription=constants.olymp_dict[ol]
                           )
    return html
