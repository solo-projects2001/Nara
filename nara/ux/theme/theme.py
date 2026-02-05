# nara/ux/theme/theme.py
THEMES = {
    "default": {
        "primary": "#1f2937",
        "success": "#10b981",
        "error": "#ef4444",
        "warning": "#f59e0b",
    }
}

def get_theme(name="default"):
    return THEMES.get(name, THEMES["default"])
