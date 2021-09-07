import flask # import Flask
import flask_sqlalchemy # import SQLAlchemy
from os import path
import flask_login # import LoginManager

db = flask_sqlalchemy.SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = flask.Flask(__name__)
    app.config['SECRET_KEY'] = 'random text to be secured later'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+DB_NAME
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = flask_login.LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
