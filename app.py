from flask import Flask, render_template, request
from otp_verification import otp_ver, otp

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == "GET":
        return render_template("register.html")

@app.route('/register', methods=['POST','GET'])
def register():
    # Authenticate the user's entered email and password
    if request.method == "POST":
        # Email with OTP link
        email = request.form.get("user_email")
        check = otp_ver(email)
        if check:
            return render_template("register.html", success = True)
        return render_template("register.html", success=False)
