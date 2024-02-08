
# Barbers Learning
#### Name: José de Jesús Hernández Ibarra
#### Github: codejogy
#### Edx: codejogy
#### México, Guanajuato, Irapuato
#### Date: 06/02/2024
#### Video Demo: https://youtu.be/iOVt1jA0oYo
#### Description:

This is a project called barbers learning, its an online learning platform made for barbers to give
content to other barbers, that's its main porpuse.
With the help of FLask and Jinja it was possible to make a fraction of what was planned
Initial plan


- #### Sign In

   - [x] Make users
   - [x] Log In with user
   - [x] Password between 6 to 20 chars
   - [x] Hash the password before using saving it to the database
   - [x] Check for username with no spaces, from a to z lower and upper and some signs
   - [x] Check for a name with no signs

- #### Log In
    - [x] Log In with email and password
    - [x] If no user exists, display error
    - [x] Show user in navbar and log off option

- #### Index
    - [x] Create course in navbar adds a course to the database
    
- #### Profile
    - [x] When logged in, the courses added by the user will be shown
    
- #### Create course
    - [x] Must have a name
    - [ ] Optional thumbnail *It's currently needed *
    - [x] Description
    - [ ] Verify the name exists *The courses name can repeat*
    - [ ] Use a transaction as MercadoPago API to get a course by buying it *Idea too complex for this moment*

- #### Navbar Search
    - [ ] Searching content will be displayed in /index *TODO*

- #### Error messages
   - [x] Make a page to display errors
   - [x] Use abort() to dedicate errors to a personalized page

#### Layout Design
Those designs were made in Krita, giving the first iteration of the front end
- Layout
![Layout](<LAYOUTS IMAGES/layout.png>)
- Index
![Index](<LAYOUTS IMAGES/index.png>)
- Log In
![LogIn](<LAYOUTS IMAGES/Login.png>)
- Sign In 
![SignIn](<LAYOUTS IMAGES/SignIn.png>)
- Create course 
![CreateCourse](<LAYOUTS IMAGES/createCourse.png>)
- Profile
![Profile](<LAYOUTS IMAGES/profile.png>)

The end result of each design is shown in the URL video at the top of the md

#### Database

SQLITE3 was used in this project to help save data from the users, 
in which three main tables could give the facilities to save the data.
The tables are:

- users
    | id | username | name | email | password | PRIMARY KEY (id) |
    |----|----------|------|-------|----------|------------------|
    |    |          |      |       |          |                  |
    - This table was made for storing the users when they register in Sign In page, this is all the information the database gets for
    a single user.


- courses
    | id | idUser | name_course | thumbnail_link | description | PRIMARY KEY (id) | FOREIGN KEY (idUser) REFERENCES users (id) |
    |----|--------|-------------|----------------|-------------|------------------|--------------------------------------------|
    |    |        |             |                |             |                  |                                            |
    - This table was made for saving courses, every time a user creates a course, it appends to this list

- courses_belong
    | id | idUser | idCourse | PRIMARY KEY (id) | FOREIGN KEY (idUser) REFERENCES users (id) | FOREIGN KEY (idCourse) REFERENCES courses (id) |
    |----|--------|----------|------------------|--------------------------------------------|------------------------------------------------|
    |    |        |          |                  |                                            |                                                |
    - Made for register the people who adds courses to their accounts, links the id of the user with the id of the course they got

- cards Additional table! *not implemented*
    | id | idUser | PRIMARY KEY (id) | FOREIGN KEY (idUser) REFERENCES users (id) |
    |----|--------|------------------|--------------------------------------------|
    |    |        |                  |                                            |
    - It will be useful to save the cards, even though, it could be a bad idea to make it in this way, at the end, it wasn't implemented.

### Implementation

#### Front end Templates
Once the idea was done, the next thing was to get the front end, 
the first iteration served as a guide for it. But the left blue menu idea was replaced with a left offcanvas due to its simplicity.

Bootstrap toolkit for HTML and CSS was useful for all the front end.
- layout.html

    Jinja was used to apply inheritance to all the html files that comes after this using this as a  layout.

    - **Structure**
    NavBar is used in top to get a visualization of the main pages to see.
    *Before log in*
    'Barber learning' takes you to the the main page '/'

    'Search' WIP, the intention was to search for any specific course giving the name of the course
    
    'Create course' takes you to the page where you can make a course and make it public

    'Sign in' takes you to make an account

    'Log in' takes you to log in your account

    *After Log In*

    Replaced sign in and log in with

    'User' toggler of user information such as the courses the user added

    'Log Out' clears the session

- apologize.html
    
    flask function abort() leads to this template
    
    **Structure**
    
    'Code of error' shows the code of HTML error
    
    'Name of error' shows the message the error carry

    'Description' is a custom message so the user knows what went wrong


- login.html

    Displays a form with an email and password as input, needed to log in

- signin.html

    Displays a form with username, name, email, password and a password confirmation to allow the user to sign in

- index.html

    Gives you access to the main page '/' where all the courses are displayed as recommendations

- createcourse.html

    Allows a logged user to make a course in a form with course name, thumbnail and description about the course.

    All the additional content is WIP to give more customization to the user

- course.html

    Given a created course, there's a page to show all the information the used added to the course.

#### Back end Files

- sqliteEasy.py
    
    This is a module to make my own version of sqlite3 queries inspired in the CS50 package.

    To make this module I took some help of the documentation of Flask
    
    https://flask.palletsprojects.com/en/3.0.x/tutorial/database/

    Why this?
    sqlite3 package comes with a lot of handy help to avoid data corruption, one of them is once start a call for a database, make a pointer to it and query anything, it all has to happen in the same thread, the thing is Flask is multithreaded so some adjustments were made to make it simpler, that's the reason sqliteEasy exists.

    The g object restarts everytime flask ends a request, that means it detects when the database should close and should be called.

    The best way I thought about linking the g object was with OOP, so all the methods can share the same variable.

- helper.py

    This module gives a lot of functionality to app.py
    **Functions**
    
    hashPassword() -> Hashes the password the user inputs with blake2b and outputs hashed password with 20 chars length.

    verifyEmail() -> Uses the package email_validator to check if the email is a valid email

    verifyName() -> Used to check if the name the user used in the sign in page is valid, with a minimum of 2 chars and a maximum of 100 chars, all of them being a-z A-Z, spaces and the special character ' using regex

    allowed_file() -> Helps verifying if the file uploaded in the thumbnail section is actually an image, checking for allowed extensions, those are 'txt', 'pdf', 'png', 'jpg', 'jpeg' and 'gif'

    duplicate() -> Function useful to check if the name of a file has been used, if so, keep the name and increase a value at the end of the file. Needed in thumbnail section.

- database.db
    
    SQL file in which all the tables are stored

- databaseOld.db

    SQL file used for testing

- app.py

    The brain of all the project.
    The structure presented will be ordered from start of the file until the end of it.

    - **Structure**

    Start flask application, configure it to not make a permanent session and all the cookies gotten from the session will be saved in the server filesystem.

    Start sqlite3 to store and search for all the queries needed.

    Configure the direction where all the uploaded content by the user will be stored in the server and the maximum space uploaded bytes, which is 1 mb, else, is going to drop an error, this is made so the server doesn't overload with heavy thumbnails.

        - app.route('/',methods=['POST','GET'])        

            Main route

            If a POST method is sent, that means the user added a course, the next thing is linking that course to the course_belong table.
            But if a GET method is sent, then it's only a visualization of the page

        - app.route('/login',methods=['GET','POST'])

            LogIn route

            If a POST method is sent, before anything, check if user is already logged to sent him to the main route.

            Get the email and password, then check for errors in both of them verifying email and password.

            If all the validations goes OK, then a session starts
        
        - @app.route('/signin',methods=['GET','POST'])

            SignIn route

            If a POST method is sent, then is needed to validate the username, name, email, and password

            A good username consists of a set of characters with no spaces

            A good name consists of less than 100 chars and no punctuation.

            A good email needs an '@' and a '.'

            For the password to be valid, needs to be 6 to 20 chars in length

            Once it is all verified, it's inserted into users table


        - @app.route('/createcourse',methods=['GET','POST'])

            If a POST method is sent, then a request to create a course was made.

            The thumbnail file needs to be checked by various functions to ensure it's safe, the low level goes by Flask which tells if it has more bytes than it's allowed, then goes by secure_filename(), after that duplicate() checks if there's already a similar name file. 
            At the end of the validation the thumbnail saves in the server


        - @app.route('/logout')

            Clears the session
            

        - @app.route('/course/<int:id>')

            This is the route where all the made courses can be seen.

            Gives an error if the id can't be found


        - @app.errorhandler(HTTPException)
            
            This decorator helps assigning the abort() function a dedicated html page

        - @app.context_processor

            This decorator will run the below function everytime a request is done and give Jinja a new variable called coursesUser, used to display the courses a user has.

This was CS50!

***Dependencies:***
email_validator
sqlite3
flask
flask_session