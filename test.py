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

# ({"groupings": {"$exist": True}},limit=10, no_cursor_timeout=True)
query = db["meta"].find_one()

at = query["groupings"]

print (at)
