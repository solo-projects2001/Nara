# nara/ux/web/graph.py
from flask import jsonify, abort
from nara.ux.visual.system_graph import load_graph

def register_graph(app):
    @app.route("/graph/<run_id>", methods=["GET"])
    def graph(run_id):
        g = load_graph(run_id)
        if not g:
            abort(404)
        return jsonify(g)
