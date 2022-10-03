from flask import Flask 

application = Flask(__name__)

@application.route('/')    # default web page
def hello_world():
	return 'October 2,2022 - Welcome to Kevin & Kim factory'