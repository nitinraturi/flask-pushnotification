from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_ngrok import run_with_ngrok

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # run_with_ngrok(app)
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    db.init_app(app)

    # blueprint for non-auth parts of app
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subscription_token = db.Column(db.String(400), unique=True)

    def __init__(self, subscription_token):
        self.subscription_token = subscription_token

    def __repr__(self):
        return "<User %r>" % self.id
