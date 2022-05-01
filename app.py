from flask import Flask, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flaskext.markdown import Markdown
from enums.error_types import ErrorType
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "root"

app.config["SQLALCHEMY_DATABASE_URI"] = "mariadb+pymysql://root:root@localhost/portfolio?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.permanent_session_lifetime = timedelta(minutes=5)

app.add_template_global(ErrorType, "ErrorType")

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
md = Markdown(app)

from models.blog_model import Blog
from models.project_model import Project
from models.user_model import User

from controllers.home_controller import home_bp
from controllers.about_controller import about_bp
from controllers.projects_controller import projects_bp
from controllers.login_controller import login_bp
from controllers.admin_controller import admin_bp

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(home_bp)
app.register_blueprint(about_bp)
app.register_blueprint(projects_bp)
app.register_blueprint(login_bp)
app.register_blueprint(admin_bp)