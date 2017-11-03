from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)

application.config.from_object('config')
application.secret_key = application.config.get("SECRET_KEY")


db = SQLAlchemy(application)


from app import mod
from app import model