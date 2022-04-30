from flask import Flask, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from controllers.home_controller import bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.blog_model import Blog

app.register_blueprint(bp)