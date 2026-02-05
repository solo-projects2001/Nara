# nara/ux/web/audit.py
from flask import jsonify
from nara.ux.audit.timeline import timeline
from nara.ux.audit.failures import failures

def register_audit(app):
    @app.route("/audit/timeline", methods=["GET"])
    def audit_timeline():
        return jsonify(timeline())

    @app.route("/audit/failures", methods=["GET"])
    def audit_failures():
        return jsonify(failures())
