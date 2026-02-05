# nara/ux/auth/guard.py
from flask import request, abort
from nara.ux.auth.session import get_session

def require_session(min_role=None):
    sid = request.headers.get("X-NARA-SESSION")
    if not sid:
        abort(401)
    sess = get_session(sid)
    if not sess:
        abort(401)
    return sess
