from flask import Flask, render_template, request
from flask.helpers import make_response
from markupsafe import escape
app = Flask(__name__)
with open("static/users.txt") as f:
    users = f.readlines()
userpass = []
userdict = {}
for i in range(len(users)):
    userpass.append(users[i].split(","))
for i in range(len(users)):
    userdict[userpass[i][0]] = userpass[i][1]
print(userpass)
print(userdict)
print(users)
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/register", methods = ["POST", "GET"])
def register():
    if request.method == "POST":
        user = request.form["nm"]
        password = request.form["pw"]
        resp = make_response(render_template("readcookie.html"))
        resp.set_cookie('user', user)
        resp.set_cookie('pass', password)
        return resp
@app.route("/home")
def home():
    name = request.cookies.get("user")
    password = request.cookies.get("pass")
    if name in userdict:
        if password == userdict[name]:
            return(render_template("home.html",user=name))
        else:
            return("Incorrect password")
    else:
        return("<script>window.location.href = '/'</script>")