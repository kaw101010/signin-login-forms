from flask import Flask, render_template, request, redirect, session
from otp_verification import otp_ver, otp
from bcrypt import hashpw, checkpw, gensalt
import mysql.connector as msc
from config import mysql_password, db, user_name

app = Flask(__name__)

app.config['SECRET_KEY'] = '[_=@`*-&2\>!{1#&/d^(?~.'
# Initiate the SQL connection
connection = msc.connect(host = "localhost", user = user_name, passwd = mysql_password, database=db, auth_plugin='mysql_native_password')
cursor = connection.cursor()


@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "GET":
        return redirect('/register')

@app.route('/register', methods=['POST','GET'])
def register():
    # Authenticate the user's entered email and password
    if request.method == "POST":
        # Email with OTP link
        email = request.form.get("user_email")
        session['email'] = email
        # Encrypt the password with Blowfish encryption algorithm
        hash = hashpw(request.form.get('user_pw').encode('UTF-8'),gensalt())
        session['hash'] = hash
        # Check if email entered by user already exists.
        existing_email = 'SELECT email FROM users WHERE email=%s'
        val = (email,)
        cursor.execute(existing_email, val)
        result = cursor.fetchall()
        if len(result) > 0:
            return render_template('register.html', email_unique = False)
        code = otp_ver(email)
        session['code'] = code
        # To allow user to enter OTP
        return render_template("register.html", otp_ = True)
    else:
        return render_template("register.html")

@app.route('/otp_check', methods=['POST','GET'])
def otpChecker():
    if request.method == 'POST':
        num_digits_otp = 5
        otp_user = ''
        # Check for OTP entered by user
        for i in range(1, num_digits_otp+1):
            otp_user += request.form.get('otp-'+str(i))
        if session['code'] == otp_user:
            # User registered
            values = (session['email'], session['hash'])
            # Insert the user records into SQL table
            q = 'INSERT INTO users (email, pwhash) VALUES (%s, %s);'
            cursor.execute(q, values)
            # Commit the changes to SQL table
            connection.commit()
            return render_template('register.html', otp_=False, success=True)
        else:
            return render_template('register.html', otp=True, success=False)

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        info_query = 'SELECT email, pwhash FROM users;'
        cursor.execute(info_query)
        # Check whether user is already registered by matching email and password
        info = cursor.fetchall()
        for i in info:
            if i[0] == request.form.get('user_email') and checkpw(request.form.get('user_pw').encode('utf-8'),i[1].encode('UTF-8')):
                # Show user that he is logged in
                return render_template('register.html', logged_in = True)
        # Show user that he is not logged in
        return render_template('login.html',fail = True)