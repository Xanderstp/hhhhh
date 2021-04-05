from flask import Flask, request, render_template
from flask import url_for
from flask_wtf import FlaskForm


import json
from random import randint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
@app.route('/member')
def members():
    with open("templates/info-json.json", encoding='utf-8') as file:
        data = json.load(file)
        n = len(data['info']) - 1
        member = data['info'][randint(0, n)]
        member['specialty'] = sorted(member['specialty'])
    return render_template('member.html', member=member)


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=8080, host='127.0.0.1')
# http://127.0.0.1:8080/member
