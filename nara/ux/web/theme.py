# nara/ux/web/theme.py
from flask import jsonify
from nara.ux.theme.theme import get_theme

def register_theme(app):
    @app.route("/theme", methods=["GET"])
    def theme():
        return jsonify(get_theme())
