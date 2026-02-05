from nara.visual.builder import build_graph
from nara.visual.ascii import render_ascii
from nara.visual.json_export import export_json

def serialize_graph(structure: dict) -> dict:
    nodes, edges = build_graph(structure)
    return {
        "ascii": render_ascii(nodes, edges),
        "json": export_json(nodes, edges),
    }
