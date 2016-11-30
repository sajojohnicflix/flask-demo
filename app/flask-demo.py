from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/faizal')
def hello_idiot():
    return 'Poda Potta!'

if __name__ == '__main__':
    app.run()
