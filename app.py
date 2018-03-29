from flask import Flask, render_template, url_for
from data import Articles
app = Flask(__name__, static_folder='static', static_url_path="/static")

Articles = Articles()


@app.route('/')
def index():
    return render_template('ind_hom.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)


@app.route('/article/<string:id>')
def article_id(id):
    return render_template('article.html', id=id)


if __name__ == '__main__':
    app.run(debug=True)
