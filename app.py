from flask import Flask, render_template, url_for, request, jsonify, Response
import json
from wtforms import TextField, Form
from data import Articles
app = Flask(__name__, static_folder='static', static_url_path="/static")

Articles = Articles()

cities = ["Bratislava", "brajs", "bramvc",
          "Bansk Bystrica",
          "Preov",
          "Povak Bystrica",
          "ilina",
          "Koice",
          "Ruomberok",
          "Zvolen",
          "Poprad"]


class SearchForm(Form):
    autocomp = TextField(id='city_autocomplete')


@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    return Response(json.dumps(cities), mimetype='application/json')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    return render_template('ind_hom.html', form=form)


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
