ENABLED = False

def kill():
    if ENABLED:
        raise SystemExit("KILL_SWITCH_TRIGGERED")
