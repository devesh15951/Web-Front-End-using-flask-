from flask import Flask, Response, render_template, request
import pymongo
import json
from wtforms import TextField, Form

app = Flask(__name__)

try:
    connection = pymongo.MongoClient()
    testdb = connection.testdb  # doesn't have to exist
    testdb.command("buildinfo")
except:
    print("Error accessing mongoDB. Check that it's running.")
    exit()

db = connection["tama"]

query = db["meta"].find_one()

auto_data = query["groupings"]


class SearchForm(Form):
    organization = TextField(id='city_autocomplete')


@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    return Response(json.dumps(auto_data), mimetype='application/json')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    return render_template("search.html", form=form)


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("test.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
