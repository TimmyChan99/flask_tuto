from flask import Flask, redirect, url_for,

app = Flask(__name__)

@app.route('/')
def get_home():
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

if __name__ == '__main__':
    app.run()