# nara/ux/visual/view.py
from nara.ux.visual.system_graph import load_graph

def render_graph(run_id):
    graph = load_graph(run_id)
    if not graph:
        return "No graph available"
    return graph.get("ascii", "")
