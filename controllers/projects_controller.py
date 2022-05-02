from flask import Blueprint, render_template, request, redirect, session, url_for
from models.project_model import Project
from app import db
from decorators.auth_decors import isLoggedIn
from sqlalchemy import and_
import markdown

projects_bp = Blueprint("projects", __name__, template_folder="templates")

@projects_bp.route("/projects")
def projects():
    projects = None

    if "username" in session:
        projects = Project.query.all()
    else:
        projects = Project.query.filter(Project.published==1).all()

    return render_template("projects.html", projects=projects)

@projects_bp.route("/project/<int:id>")
def project(id):
    project = Project.query.filter(Project.id==id).first()

    if "username" not in session and project.published != 1:
        return "Not enough permissions."

    html_content = markdown.markdown(project.content)

    return render_template("project.html", project=project, html_content=html_content)

@projects_bp.route("/edit_project/<int:id>")
@isLoggedIn
def edit_project(id):
    if session["permissions"] != 1:
        return "Error."

    project = Project.query.filter(id==id).first()

    return render_template("edit_project.html", project=project, project_id=id)

@projects_bp.route("/update_project", methods=["POST"])
@isLoggedIn
def update_project():
    if session["permissions"] != 1:
        return "Error."

    title = request.form.get("title")
    description = request.form.get("description")
    content = request.form.get("content")
    id = request.form.get("id", type=int)

    project = Project.query.filter(Project.id==id).first()

    project.title = title
    project.description = description
    project.content = content

    db.session.commit()

    return redirect("/")

@projects_bp.route("/create_project", methods=["GET", "POST"])
@isLoggedIn
def create_project():
    if session["permissions"] != 1:
        return "Error."
    
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")

        project = Project(title=title, description=description, content=f"#{title}")

        db.session.add(project)
        db.session.commit()

        return redirect("/projects")

    return render_template("create_project.html")

@projects_bp.route("/delete_project/<int:id>")
@isLoggedIn
def delete_project(id):
    if session["permissions"] != 1:
        return "Error."
    
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()

    return redirect("/projects")