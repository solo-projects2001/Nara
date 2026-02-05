# nara/ux/web/governance.py
from flask import jsonify, abort
from nara.ux.governance.approval import list_requests
from nara.ux.freeze.viewer import list_freezes

def register_governance(app):
    @app.route("/governance/approvals", methods=["GET"])
    def approvals():
        return jsonify(list_requests())

    @app.route("/governance/freezes", methods=["GET"])
    def freezes():
        return jsonify(list_freezes())
