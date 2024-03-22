# save this as app.py
import time
import flask
from flask import Flask, abort
from pydantic import BaseModel

app = Flask(__name__)
db = []


@app.route("/")
def hello():
    return "Hello, World!"

class data1(BaseModel):
    name: str
    text: str


@app.route("/send", methods=['POST'])
def send_message():
    data = flask.request
    n = data.data

    try:
        n = data1.model_validate_json(n)
        if n.name == '' or n.text == '':
            return abort(400)
    except ValueError:
        return abort(400)

    data = flask.request.json
    text = data['text']
    name = data['name']
    message = {
        'text': text,
        'name': name,
        'time': time.time()
    }
    db.append(message)

    if text == '\help':
        bot = {'text': 'Для работы с мессенджером запустите server.py, sender.py, receiver.py.\n\
Проверьте, что сервер находится в запущенном состоянии до запуска остальных программ.\n\
Напишите через слеш интересующие вас разделы: status, messages, send, index\n',
                        'name': 'bot', 'time': time.time()
               }
        db.append(bot)
    return {'ok': True}

@app.route("/messages")
def get_messages():
    try:
        after = float(flask.request.args['after'])
    except:
        abort(400)
    db_after = []
    for message in db:
        if message['time'] > after:
            db_after.append(message)
    return {'messages': db_after}

@app.route("/status")
def print_status():
    total_users = len(set(message['name'] for message in db))
    total_messages = len(db)
    info1 = ['city: Москва', 'postalCode: 117198']
    info2 = ['Number of users:', '----------------', total_users,'--------------------', 'Number of messages: ','--------------------', total_messages]
    info = ['Name: Аиша', '----------', 'ADDRESS:', '--------', info1, 'INFO:', '-----', info2]
    return info

@app.route('/index')
def lionel(): 
    return flask.render_template('index.html')
print(print_status())
app.run()