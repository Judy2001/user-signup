from flask import Flask, request, render_template
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True


# username=""
# password=""
# verify_password=""
# email=""


@app.route("/validation", methods=['POST'])
def validation():
    username=request.form['username']
    password=request.form['password']
    verify_password=request.form['verify_password']
    email=request.form['email']

    usernameError=""
    passwordError=""
    verifyError=""
    emailError=""

    # get_info = request.form['get_info']

    if username == ' ' or len(username) <3 or len(username) >20:
        usernameError = "Username should consist of 3-20 alphanumeric characters with no spaces"
    
    if password == ' ' or len(password) <3 or len(password) >20:
        password == ''
        passwordError = "Password should consist of 3-20 characters with no spaces"

    if verify_password == ' ' or password != verify_password:
        verify_password == ''
        verifyError = "Passwords must match"

    if email == '':
        email == email
    else:
        if len(email) <3 or len(email) >20:
            emailError = "Email should be between 3 and 20 characters in length"
        elif '@' not in email or '.' not in email:
            email == ''
            emailError = "Email should include '@' and '.'"

    if  not usernameError and not passwordError and not verifyError and not emailError:
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html', usernameError=usernameError, passwordError=passwordError, 
            verifyError=verifyError, emailError=emailError, username=username, email=email)


@app.route("/")
def index():
    return render_template('index.html')

app.run()