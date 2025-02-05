from flask import Flask, redirect, url_for, request, json, Response, jsonify
from functools import wraps
import logging

app = Flask(__name__)

file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

@app.route('/')
def get_home():
    if 'name' in request.args:
        print(request)
        return f'<h1>Welcome home {request.args['name']}</h1>'

    return '<h1>Welcome home</h1>'

@app.route('/articles')
def get_articles():
    return 'List of ' + url_for('get_articles')

@app.route('/articles/<id>')
def get_article(id):
    return f'article id: {id}'

# @app.route('/admin')
# def get_admin():
#     return redirect(url_for('get_home'))

@app.route('/echo', methods = ['POST', 'GET', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'POST':
        return 'ECHO: POST'
    if request.method == 'GET':
        return 'ECHO: GET'
    if request.method == 'DELETE':
        return 'ECHO: DELETE'
    if request.method == 'PUT':
        return 'ECHO: PUT'
    if request.method == 'PATCH':
        return 'ECHO: PATCH'

@app.route('/messages', methods = ['POST'])
def get_messages():
    if request.headers['Content-type'] == 'text/plain':
        return 'Text message: ' + request.data

    if request.headers['Content-type'] == 'application/json':
        return 'JSON message: ' + json.dumps(request.json)

    return 'content not specified'

@app.route('/hello', methods = ['GET'])
def api_hello():
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'

    return resp

@app.errorhandler(404)
def not_found():
    message = {
        'status': 404,
        'message': 'Not found ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.route('/users/<userid>', methods=['GET'])
def api_users(userid):
    users = {'1': 'john', '2': 'steve', '3': 'bill'}

    if userid in users:
        return jsonify({userid: users[userid]})
    else:
        return not_found()

def check_auth(username, password):
    return username == 'admin' and password == 'secret'

def authenticate():
    message = { 'message': 'You need to authenticate'}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Dev"'

    return resp

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization

        if not auth:
            return authenticate()

        elif not check_auth(auth.username, auth.password):
            return authenticate()

        return f(*args, **kwargs)

    return decorated

@app.route('/admin')
@require_auth
def api_admin():
    return "Shhh this is top secret spy stuff!"

@app.route('/logs', methods=['GET'])
def get_logs():
    app.logger.info('informing')
    app.logger.warning('warning')
    app.logger.error('screaming bloody murder!')

    return "check your logs\n"

if __name__ == '__main__':
    app.run(debug=True)