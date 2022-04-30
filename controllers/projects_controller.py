from flask import Blueprint, render_template
from models.project_model import Project

projects_bp = Blueprint("projects", __name__, template_folder="templates")

@projects_bp.route("/projects")
def projects():
    projects = Project.query.all()
    return render_template("projects.html", projects=projects)