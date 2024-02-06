from flask import Flask, render_template, request, url_for, redirect, abort,g, session
from werkzeug.exceptions import HTTPException
from werkzeug.utils import secure_filename
from flask_session import Session
from helper import hashPassword, verifyEmail, verifyName, allowed_file, UPLOAD_FOLDER, duplicate
from sqliteEasy import sqlEasyFlask
import os

# Start flask
app = Flask(__name__)
# Config flask sessions
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
# Get sqlite3
db = sqlEasyFlask(g,'database.db') 
# Path for images
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Maximum upload of files is 1 mb
app.config['MAX_CONTENT_LENGTH'] = 1*1000*1000 

# The database is gotten from get_db and closed with close_db
@app.route('/',methods=['POST','GET'])
def index():
    '''Index route'''
    # Check if theres a log in
    # Get the database of courses availables, but only get 10 of them
    if request.method == 'POST':
        # If the user isn't logged, send him to login
        if not session.get('user_id'):
            return redirect('/login')
        idCourse = request.form.get('id')
        # Check if the course is already in the database
        if db.query('SELECT * FROM courses_belong WHERE idUser=? AND idCourse = ?',session['user_id'],idCourse):
            redirect('/')
        # Add the course to the users
        db.query('INSERT INTO courses_belong (idUser,idCourse) VALUES (?,?)',session['user_id'],idCourse)
    
    
    # Limit the total amount of description by the last value in substring
    courses = db.query('SELECT id,idUser,name_course,thumbnail_link,SUBSTRING(description,0,200) description FROM courses')

    if session.get('user_id'):
        return render_template('index.html',user=session['user'], courses=courses)
    
    return render_template('index.html',courses=courses)


@app.route('/login',methods=['GET','POST'])
def login():
    '''Login route'''
    if session.get('user_id'):
        return redirect('/')
    if request.method == 'POST':
        print(session)
        print(request.form.get('email'))
        print(request.form.get('password'))
        
        # Check email
        if not request.form.get('email'):
            abort(400, 'Add email')
        email=verifyEmail(request.form.get('email'))
        # Get password
        password = hashPassword(request.form.get('password'))
        # Verify if the email and password exists in the db
        user_id = db.query('SELECT id, username FROM users WHERE email= ? AND password = ?',email,password)

        if not user_id:
            abort(400, 'Email or password are incorrect')
        
        user_id = user_id[0]
        print(user_id)
        print(user_id.keys())
        
        session['user_id'] = user_id['id']
        session['user'] = user_id['username']
        print(session)

        return redirect('/')
    

    return render_template('login.html')

@app.route('/signin',methods=['GET','POST'])
def signin():
    '''Sign In route'''
    if session.get('user_id'):
        return redirect('/')
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
    if request.method == 'POST':
        print(request.files)
        print(request.form)
        courseName = request.form.get('course_name')
        # Check if courseName exists
        if not courseName:
            abort(400,'Add a name to the course')

        description = request.form.get('description')
        if not description:
            abort(400, 'Add a description to the course')

        thumbnail = request.files.get('thumbnail')
        if not thumbnail.filename:
            abort(400,'Add a thumbnail')
        if thumbnail and allowed_file(thumbnail.filename):
            filename = secure_filename(thumbnail.filename)
            # check if the name is duplicated, if it is, add a value until it's not duplicated
            filename = duplicate(filename)
            print(filename)
            # Remove preffix to make it easy for Jinja to get the images
            path = os.path.join(app.config['UPLOAD_FOLDER'].removeprefix('static/'),filename)
            thumbnail.save(os.path.join('static',path))
            # Thumbnail saved
            # Record it in the database
            db.query('INSERT INTO courses (idUser,name_course,thumbnail_link,description) VALUES (?, ?, ?, ?)',
                     session['user_id'], courseName, path, description)
            print('Success!')
            return redirect('/')
    # print(courseName,thumbnail,description,sep='\n')

    if session.get('user_id'):
        return render_template('createcourse.html',user=session['user'])
    return render_template('createcourse.html')

@app.route('/logout')
def logout():
    '''Log Out'''
    session.clear()
    return redirect('/')

# Define a new id, this id will tell which course to watch 
@app.route('/course/<int:id>')
def courseId(id):
    courseData = db.query('SELECT *, users.username FROM courses JOIN users ON idUser=users.id WHERE courses.id=?',id)
    if not courseData:
        # This means there's no data in the database for that id
        abort(400,'This course does not exists')
    
    print(courseData[0].keys())

    # Check for all the data from the database
    if user:=session.get('user'):
        return render_template('course.html',user=user,courseData=courseData[0])
    return render_template('course.html',courseData=courseData[0],)




# Error handler (allows the program to give a personalized html for errors)
@app.errorhandler(HTTPException)
def apologize(e):
    '''Return personalized html for bad requests'''
    
    if session.get('user_id'):
        return render_template('apologize.html',e=e,user=session['user'])
    return render_template('apologize.html',e=e)


# Used if a request is done (proxy for sqlite3 to be used)
@app.teardown_appcontext
def close_connection(exception):
    # Close database when a request is done
   db.close_db() 

# Get current courses
@app.context_processor
def current_courses():
    # Give the offcanvas the courses that belong to that user
    if not session.get('user_id'):
        return dict(courses='')
    courses = db.query('''SELECT * FROM courses WHERE id IN (
        SELECT idCourse FROM courses_belong WHERE idUser = ?)''',session['user_id'])
    # for row in courses:
        # print(row['name_course'])
    return dict(coursesUser=courses)
    # print('List: ',coursesUser)
    