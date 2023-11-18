from flask import Flask
from flask_sqlalchemy import SQLAlchemy # to use for database
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdfghjkl'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # to store files.
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note # to make sure we load this file and that this file runs models.py before we initialize or create database

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # where should Flask redirect if the user's not logged in but login is required
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app): # to check if database exists
    if not path.exists('website/' + DB_NAME): # if path does not exist, create the database.
        db.create_all(app=app)
        print('Created Database!')
