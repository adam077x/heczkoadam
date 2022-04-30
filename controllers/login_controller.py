from flask import Blueprint, render_template, request, session, redirect, url_for
from models.user_model import User
#from enums.error_types import ErrorType

login_bp = Blueprint("login", __name__, template_folder="templates")

@login_bp.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter(User.username==username).first()
         
        if user != None:
            if user.password == password:
                session["username"] = username
                return redirect("/")
            else:
                return render_template("login.html", error=ErrorType.INVALID_PASSWORD)
        else:
            return render_template("login.html", error=ErrorType.USER_NOT_FOUND)

    return render_template("login.html")