from flask import Flask, request, jsonify, abort
from nara.ux.whoami import whoami
from nara.core.loop import run
from nara.ux.policy import UX_POLICY
from nara.ux.web.audit import register_audit
from nara.ux.web.artifacts import register_artifacts
from nara.ux.web.graph import register_graph
from nara.ux.web.governance import register_governance
from nara.ux.web.history import register_history
from nara.ux.web.export import register_export
from nara.ux.web.theme import register_theme

app = Flask(__name__)

def _guard():
    if not UX_POLICY.get("local_only", True):
        abort(403)

@app.before_request
def before():
    _guard()

@app.route("/whoami", methods=["GET"])
def identity():
    return jsonify({"description": whoami()})

@app.route("/run", methods=["POST"])
def run_intent():
    data = request.get_json(silent=True) or {}
    intent = data.get("intent")
    if not intent:
        return jsonify({"error": "intent_required"}), 400
    return jsonify(run(intent))

register_audit(app)
register_artifacts(app)
register_graph(app)
register_governance(app)
register_history(app)
register_export(app)
register_theme(app)

def start():
    app.run(host="127.0.0.1", port=8080, debug=False)
