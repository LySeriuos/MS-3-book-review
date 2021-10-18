import os
import json
from flask import Flask, render_template, request, flash, url_for, redirect
from werkzeug.wrappers import Request, Response
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/")
def index_for_members():
    return render_template("index-for-members.html")    


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="Hello and Welcome to The Review", company=data)

"""
All the text is copied from https://www.bookbrowse.com/. 
"""


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, We recieved your message!".format
        (request.form.get("name")))
    return render_template("contact.html", page_title="About Us")





# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', page_title="Log In", error=error)    


# this is only if on test. It shouldn't be on normal basis


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)  