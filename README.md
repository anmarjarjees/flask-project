# flask-project
 My second demonstration of using Flask Framework for my FSSD students based on Code Institute Lessons. 
 Local Installation (PC/MAC) with Virtual Environment 
 
Step1: Create the venv (in LMS videos there is no venv -> using GitPod + CI Template)
- py -m venv venv
- Or using: python -m venv venv (GitPod - Linux System)

Step2:
You might need to activate your venv
venv\Scripts\activate


OR using:  source venv/bin/activate (GitPod - Linux System)
**************************************************************************
Note: Just for the first time we do need to install flask before going to step3:
- pip install flask (OR pip3 install Flask OR pip install Flask)
Then:
- we can move it to requirements.txt
- others can use => pip install -r requirements.txt
NOTE: We can create the file "requirements.txt" now or leave for later


But both commands have to be run inside the venv (activated)
**************************************************************************

Step3: activate Lazy Coding (Refresh the webpage easily)
running the code:  py -m flask run OR flask run

Very Important Note:
running "py -m flask run" 
Give us error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory. 

REASON: 
YOU USED OTHER NAME FOR YOUR MAIN PYTHON APPLICATION!
BY DEFAULT IT SHOULD BE "app"
so in such case you have to use first: $env:FLASK_APP = "run" then  "py -m flask run" 
The code in one statement: $env:FLASK_APP = "run"; flask run


So we need to use:
For Linux and Mac:
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run

$ Or in one line: $ export FLASK_APP=run; export FLASK_ENV=development; flask run
OR: LMS: $ python run.py

For Windows cmd, use set instead of export:
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask run

For Windows PowerShell, use $env: instead of export ("run" is our main python file name):
> $env:FLASK_APP = "run"
> $env:FLASK_ENV = "development"
> flask run

We can use a semicolon to chain commands in PowerShell:
Or all in one Line: ==> $env:FLASK_APP = "run"; $env:FLASK_ENV = "development"; flask run

Note:
important to note that we should never have debug=true in a production
application or when we submit our projects for assessment. This is very
important because having debug equals true can allow arbitrary code to be run,
and so obviously this is a security flaw. It's only any good for when we're
testing our applications. So, in this video we've seen how to create a very simple website

Static folder is the folder that contains the bootstrap theme
Our folder "data" contains company.json
