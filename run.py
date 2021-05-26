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
# __name__ is the name the module or the package which is a built in python variable that refer to our current module


# ******************
# NOTES TO CONSIDER:
# ******************
"""
You can run and test your application using the official instructions of "Flask/Python/Microsoft Documentation"
Please refer to my text file "Anmar.txt" or my previous example "Flask-Intro"

Or You can use these lines of code (also required to work with GitPod):

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
"""

# Needed code to run/test your app using GitPod:
# Remember that this required extra setting in Heroku
# After importing the python standard library "os" we can reference the built-in varaible "__name__"
# Check if __name__ is "__main__"

# The word "__main__" => is the name of the default module in Python
# Which is the first one that we run
if __name__ == "__main__":
    # running our application using the arguments that we set below
    # running our object "app" method run() with the following 3 parameters: host, port, and debug
    # Runs the application on a local development server.
    app.run(
        # 1) "host" parameter: Using the "os.environ.get()" from the imported standard libray "os"
        # get() will try to get the value of "IP" environment library if it's exists
        # Otherwise set a default value for the "IP" to be 0.0.0.0 which is also the default address for the local run
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

# Note: We will move "secret_key" to a different file later :-)
app.secret_key = "any_key"

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
# Terminologies: about() is a view (in flask framework)
# and about() whish is a view is a function (in python)
def about():
    return render_template("about.html")


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
        ImmutableMultiDict([('full-name', 'Sam Simpson'), ('email', 'samsimpson@idolikeflaskok.ca'), ('phone', '9051231234'), ('message', 'Just to say hi')])
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


@app.route('/careers')
def careers():
    heading_title = "Working With Us"
    # We can also add as many additional arguments here
    # and we can call them whatever we want
    # In this instance, we've added one named heading_title
    return render_template("careers.html", page_title="Career", title=heading_title)


# start bootstrap themes, free/paid bootstrap themes:
# https://startbootstrap.com/
# Choosing "clean blog"
# The link for our current theme: https://startbootstrap.com/theme/clean-blog
# download the themes
# copy the themes sub-folders into the "static" folder inside your project

# MVC: Model View Controller
