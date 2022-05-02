from flask import Blueprint, render_template, request, redirect, session, url_for
from models.post_model import Post
from app import db
from decorators.auth_decors import isLoggedIn
from sqlalchemy import and_

blog_bp = Blueprint("blog", __name__, template_folder="templates")

@blog_bp.route("/blog")
def blog():
    posts = Post.query.filter(Post.published==1).all()
    return render_template("blog.html", posts=posts)

@blog_bp.route("/post/<int:id>")
def post(id):
    post = Post.query.filter(id==id).first()

    return render_template("project.html", post=post)

@blog_bp.route("/edit_post/<int:id>")
@isLoggedIn
def edit_post(id):
    if session["permissions"] != 1:
        return "Error."

    post = Post.query.filter(id==id).first()

    return render_template("edit_project.html", post=post, blog_id=id)

@blog_bp.route("/update_post", methods=["POST"])
@isLoggedIn
def update_post():
    if session["permissions"] != 1:
        return "Error."

    title = request.form.get("title")
    description = request.form.get("description")
    content = request.form.get("content")
    id = request.form.get("id", type=int)

    post = Post.query.filter(Post.id==id).first()

    post.title = title
    post.description = description
    post.content = content

    db.session.commit()

    return redirect("/")

@blog_bp.route("/create_post", methods=["GET", "POST"])
@isLoggedIn
def create_post():
    if session["permissions"] != 1:
        return "Error."
    
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")

        post = Post(title=title, description=description, content=f"#{title}")

        db.session.add(post)
        db.session.commit()

        return redirect("/blog")

    return render_template("create_project.html")

@blog_bp.route("/delete_post/<int:id>")
@isLoggedIn
def delete_post(id):
    if session["permissions"] != 1:
        return "Error."
    
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()

    return redirect("/blog")