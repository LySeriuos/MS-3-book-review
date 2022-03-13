from user import routes
import os
import json
from flask import (
    Flask, render_template, request,
    flash, url_for, redirect, session)
from werkzeug.wrappers import Request, Response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pprint import pprint
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/belekas")
def belenkas():
    return render_template("/signup.html")


@app.route("/reviews/")
def reviews():
    books = mongo.db.books.find()
    return render_template("reviews.html",
    page_title="Hello and Welcome to The Review", books=books)


# @app.route("/reviews/<book_name>", methods=["GET", "POST"])
# def reviews_book(book_name):
#     book = {}
#     book_name = mongo.db.books.find_one({"_id": ObjectId(book_name)})
#     if book_name == book_name["url"]:
#         book = book_name
#     critics_reviews = mongo.db.critics_reviews.find_one()
#     print(book_name["url"])
#     return render_template("book.html", book=book_name, critics_reviews=critics_reviews)

# mongo.db.books.find_one({"_id": ObjectId(book_name)})
# @app.route("/reviews/<book_name>", methods=["GET", "POST"])
# def reviews_book(book_name):
#     book = mongo.db.books.find_one({"book_name": request.form.get("book_name")})
#     book_name = mongo.db.books.find_one()
#     print(book_name)
#     return render_template("book.html", book_name=book_name)


@app.route("/reviews/<book_id>", methods=["GET", "POST"])
def reviews_book(book_id):
    book_name = mongo.db.books.find_one(ObjectId(book_id))
    results = mongo.db.critics_reviews.find()
    member_reviews = mongo.db.user_reviews.find()
    reviews = {}
    for result in results:
        if result["book_name"] == book_name["book_name"]:
            critics_reviews = result
    for member_review in member_reviews:
        if member_review["book_name"] == book_name["book_name"]:
             reviews = member_review
             print(reviews)
        else:
            reviews = {}
            flash("Is empty")
    return render_template("book.html", book_name=book_name, critics_reviews=critics_reviews, reviews=reviews)


@app.route("/about")
def about():
    return render_template("/about.html")


# Route for handling the login page logic
# Route for handling the login page logic
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        # check if user existinfg in the db
        existing_user = mongo.db.members.find_one(
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
        existing_user = mongo.db.members.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("login"))

        register = {"username": request.form.get("username").lower(),
                    "password": generate_password_hash(request.form.get("password"))
                    }
        mongo.db.members.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("member", username=session["user"]))

    return render_template("register.html")


# @app.route("/member/<username>", methods=["GET", "POST"])
# def member(username):
#     # get username from database
#     loged_user_reviews = mongo.db.user_reviews.find()
#     print(loged_user_reviews)
#     username = mongo.db.members.find_one(
#         {"username": session["user"]})["username"]
#     print(username)
#     for loged_user_review in loged_user_reviews:
#         if loged_user_review["created_by"] == username:
#             user_reviews = loged_user_review
#             print(user_reviews)
#         return render_template("member.html", username=username, user_reviews=user_reviews)
#     return redirect(url_for("login"))


@app.route("/member/<username>", methods=["GET", "POST"])
def member(username):
    # get username from database
    loged_user_review = mongo.db.user_reviews.find()
    username = mongo.db.members.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        user_reviews = list(mongo.db.user_reviews.find())
        print(user_reviews)
        return render_template("member.html", username=username, user_reviews=user_reviews)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from cookies session
    flash("you have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = {
            "book_name": request.form.get("bookName"),
            "author":  request.form.get("bookAuthor"),
            "rating": request.form.get("memberRating"),
            "review": request.form.get("review"),
            "date": request.form.get("date"),
            "time": request.form.get("time"),
            "current_book_id": request.form.get("currentBookId"),
            "created_by": session["user"]
        }
        mongo.db.user_reviews.insert_one(review)
        flash("Thank you for your review!")
        return redirect(url_for("reviews"))
    categories = mongo.db.reviews.find().sort("review_name")
    return render_template("book.html", categories=categories)

# this is only if on test. It shouldn't be on normal basis


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get('DEBUG'))
