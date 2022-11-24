from app import app
from flask import render_template, request

import constants


@app.route('/hello', methods=['GET'])
def hello():
    # для каждого передаваемого параметра формы нужно задать значение по умолчание,
    # на случай если пользователь ничего не введет
    name = ""
    gender = ""
    program_id = 0

    # список из номеров выбранных пользователем дисциплин
    subject_id = []

    # список из выбранных пользователем дисциплин
    subjects_select = []

    # список из номеров выбранных пользователем олимпиад и конкурсов
    olymp_compet_id = []

    # список из выбранных пользователем олимпиад и конкурсов
    olymp_compet_select = []

    name = request.values.get('username')
    gender = request.values.get('gender')
    program_id = request.values.get('program')
    subject_id = request.values.getlist('subject[]')
    olymp_compet_id = request.values.getlist('olymp_compet[]')

    # формируем список из выбранных пользователем дисциплин
    subjects_select = [constants.subjects[int(i)] for i in subject_id]
    # формируем список из выбранных пользователем олимпиад и конкурсов
    olymp_compet_select = [constants.olymp_compet[int(i)] for i in olymp_compet_id]

    html_hello = render_template('hello.html',
                                 name=name,
                                 gender=gender,
                                 program=constants.programs[int(program_id)],
                                 program_list=constants.programs,
                                 len=len,
                                 subjects_select=subjects_select,
                                 subject_list=constants.subjects,
                                 olymp_compet_select=olymp_compet_select,
                                 olymp_compet_list=constants.olymp_compet
                                 )

    html_index = render_template('index_h.html',
                                 name=name,
                                 gender=gender,
                                 program=constants.programs[int(program_id)],
                                 program_list=constants.programs,
                                 len=len,
                                 subjects_select=subjects_select,
                                 subject_list=constants.subjects,
                                 olymp_compet_select=olymp_compet_select,
                                 olymp_compet_list=constants.olymp_compet
                                 )

    return html_index + html_hello
