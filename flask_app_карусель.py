from flask import Flask, request, render_template
from flask import url_for
from flask_wtf import FlaskForm
from werkzeug.utils import redirect

import json
from random import randint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

photos = ['mars-1.jpg', 'mars-2.jpg', 'mars-3.jpg']
@app.route('/carousel', methods=['POST', 'GET'])
def carousel():
    global photos
    if request.method == 'GET':
        return render_template('carousel.html', photos=photos, title="Пейзажи Марса")
    elif request.method == 'POST':
        photos.append(request.files['file'].filename)
        return redirect('/carousel')


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=8080, host='127.0.0.1')
# http://127.0.0.1:8080/carousel
