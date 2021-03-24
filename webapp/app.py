import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print('TEST_PORT=')
    for k, v in os.environ.items():
        print(f'{k}={v}')
    return 'Hello world!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
