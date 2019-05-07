from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

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

    if len(username) < 3 or len(username) > 20:
        username_error = "Please enter a username between 3 and 20 characters in length"
        username = ''

    if len(password) < 3 or len(password) > 20:
        password_error = "Please entere a password between 3 and 20 characters in length"

    if password == '':
        password_error = "Please enter a valid password"

    if verify != password:
        verify_error = "Passwords do not match"

    else:
        return redirect('/welcome')

    return render_template('register.html', username=username, email=email, username_error=username_error, password_error=password_error, verify_error=verify_error)
    
    #you're crazy get rid of your html form validation and go all snake like


    #if form submission not valid, reject and re-render
        
    #error for user provides an email, but it's not valid
   

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')



    
app.run()
