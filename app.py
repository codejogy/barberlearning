from flask import Flask, render_template, request, url_for, redirect, abort,g
from werkzeug.exceptions import HTTPException
from flask_session import Session
import sqlite3
from helper import hashPassword, verifyEmail, verifyName
from sqliteEasy import sqlEasyFlask
# Start flask
app = Flask(__name__)
# Get sqlite3
db = sqlEasyFlask(g,'database.db') 

# The database is gotten from get_db and closed with close_db
@app.route('/')
def index():
    '''Index route'''
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    '''Login route'''
    if request.method == 'POST':
        ...
    request.form.get('username')

    return render_template('login.html')

@app.route('/signin',methods=['GET','POST'])
def signin():
    '''Sign In route'''
    if request.method == 'POST':
        username = request.form.get('username')
        # Check if username has no spaces
        if  username.strip() == '':
            print(username.strip())
            abort(400,'Bad username. Input a username')
        if ' ' in username:
            abort(400,'Bad username. Don\' use spaces in username')
        # Check if username in db
        if db.query('SELECT username FROM users WHERE username = ?',username):
            # This means this is not an empty list
            # Give an error saying this user is cannot be used
            abort(400,'This user is already registered')
        
        name =  verifyName(request.form.get('name'))
        # Verify name
        if name == '':
            # Bad name
            abort(400,'Bad name. Please be sure of the spaces and not getting 100+ chars in name, dont use punctuation')
        
        email = verifyEmail(request.form.get('email'))
        # Validate email
        if email == '':
            # Not a valid email
            abort(400,'Not a valid email')

        password = request.form.get('password')
        # Check if there's between 6 and 20 chars, else, error
        if not 6 <= len(password) <= 20:
            abort(400,'Please use a password from 6 to 20 characters')

        passwordConfirm = request.form.get('confirmPassword')
        # Hash both passwords
        password = hashPassword(password)
        passwordConfirm = hashPassword(passwordConfirm)
        # Check if both hashes are the same
        if password != passwordConfirm:
            abort(400,'The passwords are not the same')
        # Save the user in a database
        db.query('INSERT INTO users (username,name,email,password) VALUES (?,?,?,?)',username,name,email,password)

        print(username, name, email, password, passwordConfirm)
        print('Success!')
        return redirect('/login')

        
    return render_template('signin.html')

@app.route('/createcourse',methods=['GET','POST'])
def createCourse():
    '''Create course route'''
    return render_template('createcourse.html')


# Error handler (allows the program to give a personalized html for errors)
@app.errorhandler(HTTPException)
def apologize(e):
    '''Return personalized html for bad requests'''
    return render_template('apologize.html',e=e)


# Used if a request is done (proxy for sqlite3 to be used)
@app.teardown_appcontext
def close_connection(exception):
    # Close database when a request is done
   db.close_db() 