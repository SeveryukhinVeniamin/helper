from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')

def index():
    return "Привет, Яндекс!"

@app.route('/get')
def get():
    return list(range(1, 11))

@app.route('/<int:num>')
def numbers(num):
    return list(range(5 - num, 6 + num))


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
