
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from _collections import Counter
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    user_string = '안녕 반가워 만나서 반가워 정말정말이야 반가워 정말'
    counter = dict(Counter(user_string))
    result = json.dumps(counter)
    return result

