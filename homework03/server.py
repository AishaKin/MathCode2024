import time
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Message(BaseModel):
    name: str
    text: str

db = []
for i in range(3):
    db.append({
        'name': 'Anton',
        'time': 12343,
        'text': 'text01923097'
    })

@app.get("/")
def hello():
    return "Hello, World!"

@app.post("/send")
def send_message(message: Message):
    '''
    функция для отправки нового сообщения пользователем
    :return:
    '''
    # Добавить сообщение в базу данных db
    data = message.dict()
    data['time'] = time.time()
    db.append(data)
    return {'ok': True}

@app.get("/messages")
def get_messages(after: float):
    db_after = [message for message in db if message['time'] > after]
    return {'messages': db_after}

@app.get("/status")
def print_status():
    total_users = len(set(message['name'] for message in db))
    total_messages = len(db)

    status_info = {
        "status": "Ok!",
        "current_time": time.ctime(),
        "total_users": total_users,
        "total_messages": total_messages
    }

    return status_info

@app.get('/index')
def lionel():
    return flask.render_template('index.html')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

