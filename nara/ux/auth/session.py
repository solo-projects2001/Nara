# nara/ux/auth/session.py
import uuid
from datetime import datetime, timedelta

_SESSIONS = {}

def create_session(role: str):
    sid = str(uuid.uuid4())
    _SESSIONS[sid] = {
        "role": role,
        "created": datetime.utcnow(),
        "expires": datetime.utcnow() + timedelta(hours=8),
    }
    return sid

def get_session(sid: str):
    s = _SESSIONS.get(sid)
    if not s:
        return None
    if datetime.utcnow() > s["expires"]:
        del _SESSIONS[sid]
        return None
    return s
