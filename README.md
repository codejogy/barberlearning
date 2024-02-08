# Barbers Learning
#### Name: José de Jesús Hernández Ibarra
#### Github: codejogy
#### Edx: codejogy
#### México, Guanajuato, Irapuato
#### Date: 06/02/2024
#### Video Demo: https://youtu.be/iOVt1jA0oYo
#### Description:

This is a project called Barbers Learning,  an online learning platform made for barbers to give content to other barbers; that's its main purpose. With the help of Flask and Jinja, it was possible to make a fraction of what was planned.

Initial plan

- #### Sign In

    - [x] Make users   
    - [x] Log in with the user   
    - [x] Password between 6 and 20 characters   
    - [x] Hash the password before saving it to the database.   
    - [x] Check for usernames with no spaces, from a to z, lower and upper.   
    - [x] Check for a name with no signs.

- #### Log In    

    - [x] Log in with an email and password    
    - [x] If no user exists, display an error.    
    - [x] Show user in navbar and log off option

- #### Index    

    - [x] Create course in the navbar adds a course to the database.    

- #### Profile    

    - [x] When logged in, the courses added by the user will be shown.    

- #### Create course    

    - [x] Must have a name.    
    - [ ] Optional thumbnail *It's currently needed *    
    - [x] Description    
    - [ ] Verify the name exists. *The course name can repeat.  
    - [ ] Use a transaction with MercadoPago API to get a course by purchasing it *Idea too complex for this moment*

- #### Navbar Search    

    - [ ] Searching content will be displayed in /index *TODO*

- #### Error messages   

    - [x] Make a page to display errors.   
    - [x] Use abort() to dedicate errors to a personalized page

#### Layout Design
Those designs were made in Krita, giving the first iteration of the front end.
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

SQLITE3 was used in this project to help save data from the users.in which three main tables could provide the facilities to save the data.The tables are:

- users
    | id | username | name | email | password | PRIMARY KEY (id) |
    |----|----------|------|-------|----------|------------------|
    |    |          |      |       |          |                  |

 This table was made for storing the users when they register on the Sign In page; this is all the information the database gets for    a single user.

- courses
    | id | idUser | name_course | thumbnail_link | description | PRIMARY KEY (id) | FOREIGN KEY (idUser) REFERENCES users (id) |
    |----|--------|-------------|----------------|-------------|------------------|--------------------------------------------|
    |    |        |             |                |             |                  |                                            |

 This table was made for saving courses; every time a user creates a course, it is added to this list.

- courses_belong
    | id | idUser | idCourse | PRIMARY KEY (id) | FOREIGN KEY (idUser) REFERENCES users (id) | FOREIGN KEY (idCourse) REFERENCES courses (id) |
    |----|--------|----------|------------------|--------------------------------------------|------------------------------------------------|
    |    |        |          |                  |                                            |                                                |

 Made to register the people who add courses to their accounts, it links the id of the user with the id of the course they got.

- cards Additional table! *not implemented*
    | id | idUser | PRIMARY KEY (id) | FOREIGN KEY (idUser) REFERENCES users (id) |
    |----|--------|------------------|--------------------------------------------|
    |    |        |                  |                                            |

 It will be useful to save the cards, even though it could be a bad idea to make it this way. In the end, it wasn't implemented.

## Implementation

#### Front end Templates
Once the idea was done, the next thing was to get the front end.

The first iteration served as a guide. But the left-blue menu idea was replaced with a left offcanvas due to its simplicity.

Bootstrap toolkit for HTML and CSS was useful for all the front end.
- layout.html

    Jinja was used to apply inheritance to all the HTML files that come after this, using this as a layout.

    - **Structure** 

      
    NavBar is used at the top to get a visualization of the main pages to see.    

    *Before log in*    

    'Barber learning' takes you to the main page '/'
        
    'Search' WIP, the intention was to search for any specific course, giving the name of the course.        

    'Create course' takes you to the page where you can make a course and make it public.
        
    'Sign in' takes you to make an account.

    'Log in' takes you to log in to your account.

    *After Logging In*

    Replaced sign in and log in with

    'User' toggler of user information such as the courses the user added

    'Log Out' clears the session

- apologize.html        

    flask function abort() leads to this template.
    
    **Structure**        
    
    'Code of error' shows the code of an HTML error.        
    
    'Name of error' shows the message the error carries.

    'Description' is a custom message so the user knows what went wrong.

- login.html

    Displays a form with an email and password as input, needed to log in.

- signin.html

    Displays a form with a username, name, email, password, and password confirmation to allow the user to sign in.

- index.html

    Gives you access to the main page '/' where all the courses are displayed as recommendations.

- createcourse.html

    Allows a logged-in user to make a course in a form with a course name, thumbnail, and description about the course.

    All the additional content is WIP to give more customization to the user.

- course.html

    Given a created course, there's a page to show all the information added to the course.

#### Back end Files

- sqliteEasy.py        

    This is a module to make my own version of sqlite3 queries inspired by the CS50 package.
        
    To make this module, I took some help from the documentation of Flask.        

    https://flask.palletsprojects.com/en/3.0.x/tutorial/database/

        
    Why this?
    sqlite3 package comes with a lot of handy features to avoid data corruption. One of them is that once you start a call to a database, make a cursor to it, and query anything, it all has to happen in the same thread. The thing is, Flask is multithreaded, so some adjustments were made to make it simpler. That's the reason sqliteEasy exists.

    The g object restarts every time flask ends a request, which means it detects when the database should close and should be called.

    The best way I thought about linking the g object was with OOP, so all the methods could share the same variable.

- helper.py

    This module gives a lot of functionality to app.py    

    **Functions**

    hashPassword() -> Hashes the password the user inputs with blake2b and outputs a hashed password with a length of 20 characters.

        verifyEmail() -> Uses the package email_validator to check if the email is a valid email.

        verifyName() -> Used to check if the name the user used in the sign in page is valid, with a minimum of 2 characters and a maximum of 100 characters, all of them being a-z A-Z, spaces, and the special character ' using regex.

        allowed_file() -> function helps verify if the file uploaded in the thumbnail section is actually an image, checking for allowed extensions, which are 'txt', 'pdf', 'png', 'jpg', 'jpeg' and 'gif'

        duplicate() -> a useful function to check if the name of a file has been used; if so, keep the name and increase a value at the end of the file. Needed in the thumbnail section.

    - database.db 

          SQL file in which all the tables are stored

    - databaseOld.db

        SQL file is used for testing.

    - app.py

        The brain of all the project.
        The structure presented will be ordered from the start of the file until the end of it.

        - **Structure**

        Start flask application, configure it to not make a permanent session, and all the cookies gotten from the session will be saved in the server filesystem.

        Start sqlite3 to store and search for all the queries needed.

        Configure the direction where all the uploaded content by the user will be stored on the server and the maximum space uploaded bytes, which is 1 mb; otherwise, it is going to drop an error. This is made so the server doesn't overload with heavy thumbnails.

        - app.route('/',methods=['POST','GET'])        

                Main route

                If a POST method is sent, that means the user added a course; the next thing is linking that course to the course_belong table.
                
                But if a GET method is sent, then it's only a visualization of the page.

        - app.route('/login',methods=['GET','POST'])

                LogIn route

                If a POST method is sent, before anything, check if the user is already logged in to send him to the main route.

                Get the email and password, then check for errors in both of them verifying the email and password.

                If all the validations go OK, then a session starts.

        - @app.route('/signin',methods=['GET','POST'])

                SignIn route

                If a POST method is sent, then it is needed to validate the username, name, email, and password.

                A good username consists of a set of characters with no spaces.

                A good name consists of less than 100 characters and no punctuation.

                A good email needs an '@' and a '.'

                For the password to be valid, it needs to be 6 to 20 characters in length.

                Once it is all verified, it's inserted into the users table.

        - @app.route('/createcourse',methods=['GET','POST'])

                If a POST method is sent, then a request to create a course is made.

                The thumbnail file needs to be checked by various functions to ensure it's safe. The low level goes by Flask, which tells if it has more bytes than it's allowed, then goes by secure_filename(), and after that, duplicate() checks if there's already a similar name file.            At the end of the validation, the thumbnail is saved on the server.

        - @app.route('/logout')

                Clears the session            

        - @app.route('/course/\<int:id\>')

                This is the route where all the courses can be seen.

                Gives an error if the id can't be found

        - @app.errorhandler(HTTPException)                      

                This decorator helps assign the abort() function a dedicated HTML page.

        - @app.context_processor

                This decorator will run the below function every time a request is made and give Jinja a new variable called coursesUser, used to display the courses a user has.

This was CS50!

***Dependencies:***

email_validator

sqlite3

flask

flask_session
