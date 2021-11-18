from flask import Flask
from flask import request
from flask import jsonify
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return {
            'page': url_for('index'),
            'ping': 'pong',
            'nyan': 'meow',
            }

@app.route('/balance')
def get_balance():
    dic = {
        'page': url_for('get_balance'),
        'nyao': 'meow'
        }
    return jsonify(dic)

@app.route('/past/<int:year>/<int:month>')
def get_past(year, month):
    return f'Year: {year}, Month: {month}'

@app.route('/future/<int:year>/<int:month>', methods=['GET', 'POST'])
def future(year, month):
    if request.method == 'POST':
        return f'post year:{year} month:{month}'
    else:
        return f'get year: {year} month:{month}'

@app.route('/class/<int:history_id>', methods=['POST', 'PATCH'])
def classify(history_id):
    if request.method == 'POST':
        return f'post id:{history_id}'
    else:
        return f'patch id:{history_id}'


if __name__ == '__main__':
    app.run()
