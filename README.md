
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
    - This table was made for...


- courses_belong
    | id | idUser | name_course | thumbnail_link | description | PRIMARY KEY (id) | FOREIGN KEY (idUser) REFERENCES users (id) |
    |----|--------|-------------|----------------|-------------|------------------|--------------------------------------------|
    |    |        |             |                |             |                  |                                            |

    - And this is useful for ...

- courses
    | id | idUser | idCourse | PRIMARY KEY (id) | FOREIGN KEY (idUser) REFERENCES users (id) | FOREIGN KEY (idCourse) REFERENCES courses (id) |
    |----|--------|----------|------------------|--------------------------------------------|------------------------------------------------|
    |    |        |          |                  |                                            |                                                |
    - This is for..-

- cards Additional table! *not implemented*
    | id | idUser | PRIMARY KEY (id) | FOREIGN KEY (idUser) REFERENCES users (id) |
    |----|--------|------------------|--------------------------------------------|
    |    |        |                  |                                            |

### Implementation

#### Front end Templates
- layout.html
- apologize.html
- login.html
- signin.html
- index.html
- createcourse.html
- course.html

#### Back end Files
- .gitignore
- sqliteEasy.py
- helper.py
- database.db
- databaseOld.db
- app.py