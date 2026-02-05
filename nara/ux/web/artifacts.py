# nara/ux/web/artifacts.py
from flask import jsonify, abort
from nara.ux.artifacts.browser import list_runs, list_files

def register_artifacts(app):
    @app.route("/artifacts/runs", methods=["GET"])
    def runs():
        return jsonify(list_runs())

    @app.route("/artifacts/<run_id>/files", methods=["GET"])
    def files(run_id):
        return jsonify(list_files(run_id))
