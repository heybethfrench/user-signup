from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


def is_email(string):
    atsign_index = string.find('@')
    atsign_present = atsign_index >= 0
    if not atsign_present:
        return False
    else:
        domain_dot_index = string.find('.', atsign_index)
        domain_dot_present = domain_dot_index >= 0
        return domain_dot_present


@app.route('/')
def index():
    return render_template('register.html')


@app.route('/register', methods = ['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20:
        username_error = "Please enter a username between 3 and 20 characters in length"

    if not email == '' and not is_email(email):
        email_error = "this is not an email"

    if len(password) < 3 or len(password) > 20:
        password_error = "Please enter a password between 3 and 20 characters in length"

    if password == '':
        password_error = "Please enter a valid password"

    if username == '':
        username_error = "Please enter a valid username"

    if verify != password:
        verify_error = "Passwords do not match"

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)

    return render_template('register.html', username=username, email=email, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route('/welcome')
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)

if __name__ == "__main__":    
    app.run()
