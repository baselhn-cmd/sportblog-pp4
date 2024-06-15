# Sport Blog

Spoort Blog is a sport news blog web site where users can find news about all sports. The goal of the Sport Blog is to send everthing news about all sports, discuss in comments and get inspired!
(Developer: Basel Hussein)


![PP4](/docs/image/responsive (21).png)


[ >>> Live live website ]()


## Table of Contents
- [**User Experience**](#user-experience)
- [**Features**](#features)
   - [Existing Features](#existing-features)
   - [Future Features](#future-features)
- [**Technical Design**](#technical-design)
   - [Agile Design](#agile-design)
   - [Data Model](#data-model)
   - [Wireframes](#wireframes)
- [**Technologies Used**](#technologies-used)
   - [Frameworks & Tools](#frameworks--tools)
- [**Validation**](#validation)
   - [Testing](#testing)
   - [Device Testing](#device-testing)
   - [Automated Testing](#automated-testing)
- [**Bugs**](#bugs)
   - [Solved Bugs](#solved-bugs)
   - [Remaining Bugs](#remaining-bugs)
- [**Deployment**](#deployment)
- [**Credits**](#credits)

## User Experience - UX

### User Stories

* As a website user, I can:

- As a site user, I can view a paginated list of posts so that I can select which post I want to view.
- As a Site User / Admin, I can view comments on an individual post so that I can read the conversation.
- As a Site User I can register an account so that I can comment on a post.
- As a Site User I can leave comments on a post so that I can interact with the listings
- As a Site User I can modify or delete my comment on a post.
- As a Site Admin I can create, read, update and delete posts so that I can manage the listings.
- As a Site Admin I can create draft posts so that I can finish writing the content later.
- As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments.

### Agile Methodology

#### Design
I have been inspired by: I Think Therefore I Blog - https://learn.codeinstitute.net/ci_program/diplomainfullstacksoftwarecommoncurriculum

#### Typography

* The fonts used for this project were from https://fonts.google.com/
### Wireframes

Wireframes for this project can be located [here](WIREFRAMES.md)

## Features

### Home Page

![Home Page]()


### About Page

![About Page]()



### Blog Page

![Blog Page]()


##

### Post Detail Page - Comments

![Post Detail Page - Comments]()

* At the bottom of this page, users can read the comments posted by other users. If the user is logged in or is a 
superuser they have access to the buttons for deleting or updating comments. But now its an error so that has to be fixt

### Edit Comments Page

![Edit Comments Page]()

* On this page, users are allowed to comment, delete and edit their own post comments. The website superuser can 
 delite ther comment. But now its an error so that has to be fixt

### Signup Page

![Signup Page]()

* On the Signup Page, a new user can sign up for the Tasty Blog website by filling out and then submitting the form. But now its an error so that has to be fixt.

### Login Page

![Login Page]()

* On the Login Page, users can log in to the website by inputting the username and password and have access 
  to website services for a user registered.

### Logout Page

![Logout Page]()

* On the Logout Page, users can confirm that they wish to exit the website.
### Navbar

![Navbar]()

* The navigation bar is present at the top of every page and houses all links to the various other pages.
* The options to Register or Log in will change to the option to log out once a user has logged in.
* Once a user has signed in, more options such as profile page and user image will be available in the navbar.
* A search icon is nested in the navbar and once clicked it will open the search box.
* The navbar is fully responsive, collapsing into a hamburger menu when the screen size becomes smaller.

![Navbar]()
* In the navbar users can access the categories list by clicking on the dropdown menu.

### Footer

![Footer]()
* On the website footer, users can see basic information about the blog such as contact, social media, 
  copyright.

## Messages and Interaction With Users
### Sign up

![Sign up]()

* When users sign up to the website they will see a message at the top of the page saying "Successfully signed in as
(username)".<br>

### Login

![Login]()

* When users sign in to the website they will see a message at the top of the page saying "Successfully signed in as
(username)".<br>

### Logout

![Logout]()

* When users log out of the website they will see a message at the top of the page saying "You have signed out".<br>


### Like Post

![Like Post]()
* *When users are logged in to the website they can like a post and they will see a message at the top of the page 
  saying "You have liked this post".<br>

### Unlike Post

![Unlike Post]()

* When users are logged in to the website they can unlike a post that has been liked by the user and they will see a message 
  at the top of the page saying "You have unliked this post".<br>

### Comment Post

![Comment Post]()

* When users are logged in to the website they can comment on a post and after they submit the comment they will see a 
  message at the top of the page saying "Your comment was sent successfully and is awaiting approval".But now its an error so that has to be fixt<br>

### Comment Post - 2

![Comment Post - 2]()

* After a user submits a comment, they will see a message over the input comment saying "Thanks (username). Your 
  comment is awaiting approval! <br>

### Delete/Edit Comment

![Delete Comment]()

* When users are logged in to the website and they have previously posted a comment or if the user is a superuser they will see the 
Delete and Edit buttons at the bottom of comments.But now its an error so that has to be fixt<br>

### Delete Comment - 1

![Delete Comment - 2]()

* If they wish to delete their comment, they can press the button Delete and a Bootstrap box model will pop up with the message 
  "Are you sure you want to delete your comment?".But now its an error so that has to be fixt<br>

### Delete Comment - 2

![Delete Comment - 3]()

* After pressing the Delete button again inside the Bootstrap box model they will see a message on the 
  top of the page, "Your comment was deleted successfully".But now its an error so that has to be fixt<br>

### Edit Comment

![Edit Comment]()

* After pressing the Update, users will see a message on the top of the page, "The comment was successfully updated".But now its an error so that has to be fixt<br>



## Admin Panel/Superuser
![No Search Found]()

* On the Admin Panel, as an admin/superuser I have full access to CRUD functionality so I can view, create, edit and
delete the following ones:
1. Posts
2. Comments
3. Author
4. Categories

*As admin/superuser I can also approve comments, approve posts and change the status and give other permissions to the users.<br>

## Technologies Used

### Languages Used

* [HTML 5](https://en.wikipedia.org/wiki/HTML/)
* [CSS 3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://www.javascript.com/)
* [Django](https://www.python.org/)
* [Python](https://www.djangoproject.com/)

#### Django Packages

* [Gunicorn](https://gunicorn.org/)<br>
   As the server for Heroku
* [Cloudinary](https://cloudinary.com/)<br>
   Was used to host the static files and media
* [Dj_database_url](https://pypi.org/project/dj-database-url/)<br>
   To parse the database URL from the environment variables in Heroku
* [Psycopg2](https://pypi.org/project/psycopg2/)<br>
   As an adaptor for Python and PostgreSQL databases
* [Summernote](https://summernote.org/)<br>
   As a text editor
* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)<br>
   For authentication, registration, account
   management
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)<br>
   To style the forms

### Frameworks - Libraries - Programs Used

* [Bootstrap](https://getbootstrap.com/)<br>
   Was used to style the website, add responsiveness and interactivity
* [Jquery](https://jquery.com/)<br>
   All the scripts were written using jquery library
* [Git](https://git-scm.com/)<br>
   Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub
* [GitHub](https://github.com/)<br>
   GitHub is used to store the project's code after being pushed from Git
* [Heroku](https://id.heroku.com)<br>
   Heroku was used to deploy the live project
* [PostgreSQL](https://www.postgresql.org/)<br>
   Database used through heroku.
* [VSCode](https://code.visualstudio.com/)<br>
   VSCode was used to create and edit the website
* [Lucidchart](https://lucid.app/)<br>
   Lucidchart was used to create the database diagram
* [PEP8](http://pep8online.com/)<br>
   PEP8 was used to validate all the Python code
* [W3C - HTML](https://validator.w3.org/)<br>
   W3C- HTML was used to validate all the HTML code
* [W3C - CSS](https://jigsaw.w3.org/css-validator/)<br>
   W3C - CSS was used to validate the CSS code
* [Fontawesome](https://fontawesome.com/)<br>
   To add icons to the website
* [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)<br>
   To check App responsiveness and debugging
* [Google Fonts](https://fonts.google.com/)<br>
   To add the 2 fonts that were used throughout the project
* [Balsamiq](https://balsamiq.com/)<br>
   To build the wireframes for the project
* [PIXLR](https://pixlr.com)<br>
   To convert the images to webp format
* [CANVA](https://www.canva.com/)<br>
   To build the logos for the project
* [Coolors](https://coolors.co/)<br>
   To build the colour palette of the project
* [Emailjs](https://www.emailjs.com/)<br>
   To send emails from the contact form


