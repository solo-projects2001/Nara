import ast

def analyze(path: str) -> dict:
    try:
        with open(path) as f:
            ast.parse(f.read())
        return {"ok": True}
    except SyntaxError as e:
        return {
            "ok": False,
            "type": "syntax_error",
            "line": e.lineno,
            "msg": str(e)
        }
