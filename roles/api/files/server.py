#!/usr/bin/env python
import os

from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongo:27017")

db = client['attendance']



@app.route("/")
def index():
    return render_template("index.html", attendees=db.students.find())




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)

