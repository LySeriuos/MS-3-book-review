import os
import json
from flask import (
    Flask, render_template, request,
    flash, url_for, redirect, session)
from werkzeug.wrappers import Request, Response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


from user import routes


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/belekas")
def belenkas():
    return render_template("/signup.html")


@app.route("/reviews")
def reviews():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("reviews.html", page_title="Hello and Welcome to The Review", company=data)


@app.route("/reviews/<book_name>")
def reviews_book(book_name):
    book = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == book_name:
                book = obj
    tasks = mongo.db.tasks.find()            
    return render_template("book.html", book=book, tasks=tasks)


@app.route("/about")
def about():
    return render_template("/about.html")


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', page_title="Please login", error=error)


# this is only if on test. It shouldn't be on normal basis


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get('DEBUG'))
