from flask import Flask, request, render_template
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True


username=""
password=""
verify_password=""
email=""


@app.route("/validation", methods=['POST'])
def validation():
    usernameError=""
    passwordError=""
    verifyError=""
    emailError=""

    if username != ' ' and len(username) >2 and len(username) < 21:
        username=username
    else:
        username == ''
        usernameError = "Username should consist of 3-20 alphanumeric characters with no spaces"
    return username, usernameError

    if password != ' ' and len(password) > 2 and len(password) < 21:
        password == ''
    else:
        password == ''
        passwordError = "Password should consist of 3-20 characters with no spaces"
    return password, passwordError

    if verify_password!= ' ' and password != verify_password:
        verify_password == ''
    else:
        verify_password == ''
        verifyError = "Passwords must match"
    return verify_password, verifyError

    if len(email) > 2 and len(email) < 21 and '@' in email and '.' in email:
        email = email
    else:
        email = ''
        emailError = "Please enter a valid email (should include '@' and '.')"
    return email, emailError

    if  not usernameError and not passwordError and not verifyError and not emailError:
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html', usernameError=usernameError, passwordError=passwordError, verifyError=verifyError, emailError=emailError)



@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template('index.html')

app.run()