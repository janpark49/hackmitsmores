import os
from flask import Flask, session, request

app = Flask(__name__, static_url_path="/static")

#load main config
app.config.from_pyfile('../config.py') 


import smores_app.views
