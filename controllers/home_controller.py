from flask import Blueprint, render_template
from app import db
from models.pinned_model import PinnedProject, PinnedPost
from models.post_model import Post
from models.project_model import Project

home_bp = Blueprint("home", __name__, template_folder="templates")

@home_bp.route("/")
def home():
    pinned_projects = db.session.query(PinnedProject, Project).join(Project).all()
    pinned_posts = PinnedPost.query.all()

    return render_template("home.html", pinned_projects=pinned_projects, pinned_posts=pinned_posts)