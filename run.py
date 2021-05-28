# https://flask.palletsprojects.com/en/2.0.x/quickstart/

# Create our flask main python file,
# naming convention: either app.py (recommended by default) or run.py (LMS)

# from flask import Flask.
# The capital F indicates that that's a class name.
# import the render_template() function from Flask.

# importing request library for our contact form
# request is going to handle things like finding out what method we used in the form,
# and also it will contain our form object when we've posted it.

# NOTE:
# the code below might give this error: Unable to import 'flask'pylint(import-error)
# Based on VS Code Docs:
# CTRL + SHIFT + P => Python: Selector Intperpreter
# Select the python.exe inside the venv folder


from flask import Flask, render_template, request, json, flash

# importing a function from Flask called "flash"
# flash function will help us to display a non-permanent message to the user
# this temporary message will stay until the page is refreshed or jumping to another page
# this/these message(s) is/are called "flash"

# You need to import "os" from the standard python library:
# You need this libray if you have an intention to use os environment as we are going to do
import os

# Our python file name (module) named "env.py" that contains the secret key
# We do need to import this file here but ONLY if it's exists
if os.path.exists("env.py"):
    import env

# NOTE:
# after adding the code of with "os"
# a new folder named "__pycache__" will be created by Flask automatically
# also this file is not important to be added to our repo, so we can ignore it also
# Also we can ignore the error about not using env (because it's already exists but for the secret key)

# NOTE:
# Please be carefull that pushing a file to Github then adding it .gitignore will NOT be ignore it, too late :-(

# import our json file:
# First import the JSON library because we're going to be passing the data that's coming in as JSON.
# import json
# Or we can just import from flask above


# Next, we need to create an instance of this class "Flask"
# in Flask, the convention is that our variable is called "app"
app = Flask(__name__)
# __name__ is the name of the module or the package which is a built-in python variable that refer to our current module


# ***********
# secret key: is needed to be used with flash messages (it's required)
# ***********
# RuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
# This code below for Flash Message (You can add it at end):
# To use flashed messages,
# we need to create a secret key because Flask cryptographically signs all of the messages for security.
# This might sound complicated,
# but really all we need to do, is just to provide a secret key that Flask can use to sign the messages.
# we need to say app.secret_key:
# provide a random string that Flask can use for signing.


"""
# NOTES ABOUT USING SECRET_KEY: 
1. This secret key should be hidden (not submitted to GitHub/Heroku)

2. The secret key is saved in file named "env.py" by convension to refer to the environment variables
-- So you need to create/add a file named "env.py"
-- the "env.py" python file can be used to hide any sensitive data
-- inside this file we need to add:
import os
os.environ.setdefault("SECRET_KEY", "secret_flash_key")

3. We need to add this file "env.py" to GitIgnore file
"""

# We should not use this way of coding, the secret key should be hidden:
# app.secret_key = "DON'T Put your key here!"
app.secret_key = os.environ.get("SECRET_KEY")

"""
# Using the same code: "os.environ.get()" from the imported standard libray "os"
# get() will try to get the value of "SECRET_KEY" environment library if it's exists (in our local / GitPod workspace)
# Otherwise the value will be retrieved from Heroku Config Variables
app.secret_key = os.environ.get("SECRET_KEY")
"""

# For reviewing, you can use the command: touch then file name to create a new file with linux os (GitBash)


# we use the route decorator to tell Flask what URL should trigger the function that follows.
# A decorator is a way of warpping functions (as we have learnt in Python fundamentals)


@app.route("/")  # this is the top level of our website
# The Local URL with the command: py runt.py => http://10.0.0.229:5000/
# The Local URL with the command: $env:FLASK_APP = "run"; flask run => http://127.0.0.0"5000/
# the symbol @ using the app.route() decorator.
# In Python, a decorator starts with the @ symbol,
# which is also called "Pie Notation"
# When we browse to the route directory of any website which is indicated by "/" as route argument
# Flask will trigger the index function below (underneath):
# # And, then we create a function called index,
def index():
    # For quick test
    # return "<h1>Testing<h1>"
    # Notice that Well, Flask expects it to be a directory called templates,
    # which is on the same level as our run.py file.
    # Below is the basic required line of code: return the template file index.html:

    # Notice that Flask expects to have a directory called "templates",
    # which is on the same level as our run.py file.
    # Below is the basic required line of code: return the template file index.html:
    return render_template("index.html")

# And this function is also called a view.
# So let's create another route() decorator and another view (function) for this decorator.
# We're going to bind that to a view that we'll call about().


@app.route('/about')
# The URL with the command: py runt.py => http://10.0.0.229:5000/about
# The URL with the command: $env:FLASK_APP = "run"; flask run => http://127.0.0.0:5000/about
# Terminologies: about() is a view (in flask framework)
# and about() whish is a view is a function (in python)
def about():
    # let's now try the same code as we did in our previous project but with the data from LMS Json file:
    # initialize an empty list (array) called "data"
    data = []
    # We were doing reading from files,
    # with open ("data/company.json", "r") as json_data.
    # first argument: data/company.json for the json file full path
    # second argument: r for reading
    # we can refer to this file as "json_data" which a name that we pick for the info we receive from this file
    # We can omit the second argument "r" for reading a file because it's "read" by default
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)

    # print(type(data)) # <class 'list'>
    # adding another additional variable/parameter to render_template
    # creating a standard python list for practising adding other arguments => company
    # in our template (about.html) file we can refer to the json data as "company"
    # notice that not all passing parameters are used, "page_title" is not used in the about page
    return render_template("about.html", page_title="About", company=data)


# View for the form
# now this one is different request, it's not a GET request, it's a POST request
# By default, a route only answers to GET requests.
# You can use the methods argument of the route() decorator to handle different HTTP methods.
# We need to define a function to handle the form input and display the result within the same contact.html file

# We need to use these two methods for the same page "contact":
# GET => to be used to get the contact form elements (the template)
# POST => to send the form info after sumbitting the form
@app.route('/contact', methods=["GET", "POST"])  # the url: /contact
def contact():  # the view is contact based on the link we put in the the new recent return code:

    # We DO HAVE to check if the form is submitted:
    if request.method == "POST":
        # Code for learning:
        # ******************
        # Then we're just going to print in the debugger window "Hello just for testing!"
        print("Hello just for testing!")
        # for more testing:
        print(request.form)
        """
        ImmutableMultiDict([('full-name', 'Sam Simpson'), ('email', 'samsimpson@idolikeflaskok.ca'),
                           ('phone', '9051231234'), ('message', 'Just to say hi')])
        """
        name = request.form['full-name']
        email = request.form['email']
        phone = request.form['phone']
        msg = request.form['message']

        # The code below for flash message:
        # Calling flash() function
        # We can add one or more messages as we like:
        # Using f-string to fromat our output
        flash(f"Thank you {name}, we have received your message")
        flash(f"We will use this email \"{email}\" to send you our flyers")
        flash(
            f"We will call you to this phone number {phone} for any new update")

    return render_template("contact.html")


# You can add variable sections to a URL by marking sections with <variable_name>.
# Your function then receives the <variable_name> as a keyword argument
# example:
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % escape(username)

# Blow: <member_url> is "JUST" a placeholder for the "real value" to be attached to URL
# Creating a new route decorator for about page when we click on any member name to load its json info in a new page:
@app.route('/about/<member_url>')
# The function "member()" will display the specific info of the passed argument:
# or we can use:
# @app.route("/about/<member_url>")
# Create a new view, which is going to be: about_member
# When we look at our about URL with something after it, that's going to be passed in to this view
# We can use the following code if we used @app.route("/about/<member_url>"):
# def about_member(member_url):
# Or:
def about_member(member_url):
    # Step1: we need to retreive the entire JSON file and save it into a list again
    # Step2: retreive the info of that specific item in this list
    # Step3: passing the info about that specific member (object) to our template "member.html"

    # initialize an empty list (array) called "data"
    data = []  # data list is empty to receive the json data
    # Just as we did in our about view,
    # we're going to open our company.json file for reading and refer to that as json_data.
    # Don't forget that we can omit the "r" for reading a file because it's reading by default
    with open("data/company.json", "r") as json_data:
        # We'll then create another variable inside
        # where we pass the data that we've passed through and converted into JSON.
        data = json.load(json_data)

     # So we'll create an empty object "dictionary" named "member", which we're going to use to store our data for the clicked member.
    # this value will be used in case if the name doesn't exist
    member = {}
    # So we created an empty object named "member", which
    # We need to iterate through every JSON object inside our data list
    # And now what we're going to do is iterate through that data array that we've created.
    for obj in data:
        # for testing:
        # print(obj['name'])
        # print(obj['url'])
        # notice that we used obj.name and we received an error
        # AttributeError: 'dict' object has no attribute 'name'
        # so we had to use obj['name'] instead of obj.name
        # (Refer to our lecture of working with dictionaries in Python fundamentals)
        if member_url == obj['url']:
            member = obj
            # for testing:
            print("member object: ", member)

    return render_template("member.html", member=member)


@app.route('/careers')
def careers():
    heading_title = "Working With Us"
    # We can also add as many additional arguments here
    # and we can call them whatever we want
    # In this instance, we've added one named heading_title
    return render_template("careers.html", page_title="Career", title=heading_title)


# ******************
# NOTES TO CONSIDER:
# ******************
"""
You can run and test your application using the official instructions of "Flask/Python/Microsoft Documentation"
Please refer to my text file "Anmar.txt" or my previous example "Flask-Intro" or my pdf lecture file

Or You can use these lines of code (also required to work with GitPod if you want to follow the CI instructions):
Or if you run: python run.py
the __name__ value will be "__main__"

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
"""

# Needed code to run/test your app using GitPod:
# Remember that this required extra setting in Heroku
# After importing the python standard library "os" we can reference the built-in varaible "__name__"
# The __name__ is a special built-in variable which evaluates to the name of the current module.
# Check if __name__ is "__main__"

# Review:
# Python files are called modules and they are identified by the .py file extension.
# A module can define functions, classes, and variables.

# The word "__main__" => is the name of the default module in Python
# Which is the first one that we run, so if this has not been imported, which it won't be, then it's going to be run directly.

# For Testing:
print(f"__name__ value before if: {__name__}")  # __name__ value before if: run
if __name__ == "__main__":
    # For Testing:
    print(f"__name__ value inside if: {__name__}")
    # running our application using the arguments that we set below
    # running our object "app" method run() with the following 3 parameters: host, port, and debug
    # Runs the application on a local development server.
    app.run(
        # 1) "host" parameter: Using the "os.environ.get()" from the imported standard libray "os"
        # get() will try to get the value of "IP" environment library if it's exists
        # Otherwise set a default value for the "IP" to be 0.0.0.0
        host=os.environ.get("IP", "0.0.0.0"),
        # 2) "port" parameter: Using the "os.environ.get()" from the imported standard libray "os"
        # get() will try to get the value of "PORT" environment library if it's exists
        # Otherwise set a default value for the "PORT" to be "5000" which is common port used by Flask
        # Notice that we are casting the final returned value as an integer
        port=int(os.environ.get("PORT", "5000")),
        # 3) Specify the debug=True (for sure to be in development mode for easy debuging)
        debug=True)

    # IMPORTANT NOTE: We should never have debug=True in a production application or when you submit your project
    # When debug=True => this can allow arbitrary code to be run and it's a security flaw.
    # So we need to change it to be debug="False" before submiting our project

# Then you can run your app:
# python3 run.py OR python run.py OR py run.py
# Notice that app.py is the main python file name

# Conclusions:
"""
- Every module which is just a Python file has a special attribute called __name__
- The value of __name__ attribute is set to "__main__" when module is run as main program using: python3 run.py OR python run.py OR py run.py
- Otherwise, if you run your program using: $env:FLASK_APP = "run"; flask run
 the value of __name__ is set to contain the name of the module which is in our case is "run"
- We use if __name__ == "__main__" block to prevent (certain) code from being run when the module is imported or in production
"""

# start bootstrap themes, free/paid bootstrap themes:
# https://startbootstrap.com/
# Choosing "clean blog"
# The link for our current theme: https://startbootstrap.com/theme/clean-blog
# download the themes
# copy the themes sub-folders into the "static" folder inside your project

# MVC: Model View Controller
