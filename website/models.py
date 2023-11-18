# this is where we are going to create database models

from . import db # aka from website folder import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now) # what func does is it get the current date & time and it will store as default value for date & time
    #foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # id is the primary key
    # user.id is foreign key, therefore lower case.
    # foreign key is when we have a "one to many relationship. In this case, one user but many notes"


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # id is our primary key (primary key = unique identifier) to differentiate for example, two users have the same id. 
    email = db.Column(db.String(150), unique=True) # unique = True means .no user can have the same email as one another
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # when put relatioship, we are referencing the name of class, therefore capital letter.