from flask import jsonify
from nara.ux.history.runs import list_runs


def register_history(app):
    """
    Fix: Flask endpoint collision.
    Explicit unique endpoint name required.
    """

    @app.route("/history/runs", methods=["GET"], endpoint="history_runs")
    def history_runs():
        return jsonify(list_runs())
