# nara/ux/web/export.py
from flask import jsonify, abort
from nara.ux.export.bundle import export_run
import os, tempfile

def register_export(app):
    @app.route("/export/<run_id>", methods=["POST"])
    def export(run_id):
        tmp = tempfile.mktemp(suffix=".zip")
        export_run(run_id, tmp)
        return jsonify({"export": tmp})
