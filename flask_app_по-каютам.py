from flask import Flask, request, render_template
from flask import url_for
from flask_wtf import FlaskForm


import json
from random import choice

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
@app.route('/distribution')
def distribution():
    return render_template('distribution.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
# http://127.0.0.1:8080/distribution
