from flask import Blueprint, render_template
from decorators.auth_decors import isLoggedIn

admin_bp = Blueprint("admin", __name__, template_folder="templates")

@admin_bp.route("/admin")
@isLoggedIn
def admin():
    return render_template("admin.html")