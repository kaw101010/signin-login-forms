from flask import Flask, render_template, request, flash
from otp_verification import otp_ver, otp

app = Flask(__name__)

app.config['SECRET_KEY'] = '[_=@`*-&2\>!{1#&/d^(?~.'

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "GET":
        return render_template("register.html")

@app.route('/register', methods=['POST','GET'])
def register():
    global code
    # Authenticate the user's entered email and password
    if request.method == "POST":
        # Email with OTP link
        email = request.form.get("user_email")
        code = otp_ver(email)
        # To allow user to enter OTP
        return render_template("register.html", otp_ = True)

@app.route('/otp_check', methods=['POST','GET'])
def otpChecker():
    if request.method == 'POST':
        num_digits_otp = 5
        otp_user = ''
        # Check for OTP entered by user
        for i in range(1, num_digits_otp+1):
            otp_user += request.form.get('otp-'+str(i))
        if code == otp_user:
            # User registered
            return render_template('register.html', otp_=False, success=True)
        else:
            return render_template('register.html', otp=True, success=False)

