from flask import Blueprint, render_template

views_bp = Blueprint(
    "views", __name__, url_prefix="/"
)

@views_bp.route("/", methods=["GET"])
def view_root():
    """ Root View """
    return render_template(
        "layouts/main.jinja2", type_sidenav = "standard")

@views_bp.route("/login", methods=["GET"])
def view_login():
    """ Login View """
    return render_template("layouts/login.jinja2")

@views_bp.route("/register", methods=["GET"])
def view_register():
    """ Register View """
    return render_template("layouts/register.jinja2")