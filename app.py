from flask import Flask, request, jsonify, url_for
from assets.database import db_session
from assets.models import Data

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return {
            'page': url_for('index'),
            'ping': 'pong',
            'nyan': 'meow',
            }

@app.route('/usable/present')
def get_usable():
    res = {
        'year': 2021,
        'month': 3,
        'usable': 42500,
        }
    return jsonify(res)

@app.route('/usable/<int:year>/<int:month>')
def future_usable(year, month):
    res = {
            'year': year,
            'month': month,
            'usable': 70300,
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

@app.route('/detail/present/used')
def get_detail_used():
    res = res_detail
    return jsonify(res)

@app.route('/detail/present/plan')
def get_detail_plan():
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

@app.route('/detail/category/<int:id>', methods=['POST'])
def set_category(id):
    return '', 201

res_category = [{
    'category': '医療費',
    'subtotal': 50300,
    'rate': 30,
    }]

@app.route('/category/past/<int:year>')
def past_category_year(year):
    res = {
            'year': year,
            'categories': res_category,
            }
    return jsonify(res)

@app.route('/category/past/<int:year>/<int:month>')
def past_category_month(year, month):
    res = {
            'year': year,
            'month': month,
            'categories': res_category,
            }
    return jsonify(res)

@app.route('/plan/repeat', methods=['POST', 'PATCH'])
def repeat():
    if request.method == 'POST':
        return '', 201
    else:
        return '', 201

@app.route('/plan/shot', methods=['POST', 'PATCH'])
def shot():
    if request.method == 'POST':
        return '', 201
    else:
        return '', 201

@app.route('/income/repeat', methods=['GET'])
def income():
    res = {
            'income': 203323,
            }
    return jsonify(res)

@app.route('/income/shot', methods=['POST'])
def income_shot():
    return '', 201

@app.route('/user', methods=['GET', 'POST', 'PATCH'])
def user_info():
    if request.method == 'GET':
        data = db_session.query(Data.name, Data.article, Data.timestamp).all()
        return data
    elif request.method == 'POST':
        return '', 201
    else:
        res = {
                'user_id': 1,
                'email': 'test@github.com',
                'pass': '********'
                }
        return '', 201
                
if __name__ == '__main__':
    app.run()
