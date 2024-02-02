from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/signin',methods=['GET','POST'])
def signin():
    return render_template('signin.html')

@app.route('/createcourse',methods=['GET','POST'])
def createCourse():
    return render_template('createcourse.html')