import re
from flask import Flask
from flask import request, render_template, session
from flask import redirect, url_for
from flask_session import Session
from flask_mail import Mail,Message
import hashlib
import os
from string_utility import *
import cryptocode

#Store the data on memory(volatile)
data_dict={}
#init the flask app instance
app=Flask(name)
#session configuration
app.config['SESSION PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'

