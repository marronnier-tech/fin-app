from flask import Flask, request, jsonify, url_for

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return {
            'page': url_for('index'),
            'ping': 'pong',
            'nyan': 'meow',
            }

@app.route('/usable')
def get_usable():
    res = {
        'year': 2021,
        'month': 3,
        'usable': 42500,
        }
    return jsonify(res)

res_detail = [{
        'id': 2,
        'category': '食費',
        'money': 4250,
        'is_plus': 'false',
        'description': '西友ネットスーパー',
        'channel': 'UFJ-VISAデビット',
        }]

@app.route('/detail/present')
def get_detail():
    res = res_detail
    return jsonify(res)

@app.route('/detail/past/<int:year>/<int:month>')
def get_past(year, month):
    res = {
            'year': year,
            'month': month,
            'details': res_detail
            }
    return jsonify(res)

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
