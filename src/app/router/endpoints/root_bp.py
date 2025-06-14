from flask import Blueprint, render_template

root_bp = Blueprint(
    "root", __name__, url_prefix="/"
)

@root_bp.route("/", methods=["GET"])
def view_root():
    return render_template(
        "layouts/main.jinja2"
    )