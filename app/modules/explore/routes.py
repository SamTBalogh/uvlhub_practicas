from flask import jsonify, render_template, request
from flask_wtf.csrf import validate_csrf
from wtforms.validators import ValidationError

from app.modules.explore import explore_bp
from app.modules.explore.forms import ExploreForm
from app.modules.explore.services import ExploreService


@explore_bp.route("/explore", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        query = request.args.get("query", "")
        form = ExploreForm()
        return render_template("explore/index.html", form=form, query=query)

    if request.method == "POST":
        # Validate CSRF token from JSON payload
        criteria = request.get_json()
        csrf_token = criteria.pop("csrf_token", None) if criteria else None

        try:
            validate_csrf(csrf_token)
        except ValidationError:
            return jsonify({"error": "CSRF validation failed"}), 403

        datasets = ExploreService().filter(**criteria)
        return jsonify([dataset.to_dict() for dataset in datasets])
