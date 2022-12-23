from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == "GET":
        return render_template("register.html")

@app.route('/register', methods=['POST','GET'])
def register():
    # Authenticate the user's entered email and password
    if request.method == "POST":
        return render_template("registered.html")