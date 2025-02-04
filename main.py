from flask import Flask, redirect, url_for, request

app = Flask(__name__)

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

@app.route('/admin')
def get_admin():
    return redirect(url_for('get_home'))

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

@
if __name__ == '__main__':
    app.run()