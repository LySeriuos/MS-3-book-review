import os
import json
from flask import (
    Flask, render_template, request,
    flash, url_for, redirect, session)
from werkzeug.wrappers import Request, Response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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
    return render_template(
        "reviews.html", page_title="Hello and Welcome to The Review", company=data)


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
# Route for handling the login page logic
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        # check if user existinfg in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "member", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # to check if username exists in db
        existing_user = mongo.db.userrs.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("login"))

        register = {"username": request.form.get("username").lower(),
        "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("member", username=session["user"]))

    return render_template("register.html")


@app.route("/member/<username>", methods=["GET", "POST"])
def member(username):
    # get username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:        
        return render_template("member.html", username=username)
    return redirect(url_for("login"))    

# this is only if on test. It shouldn't be on normal basis


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get('DEBUG'))
