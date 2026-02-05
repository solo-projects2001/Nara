# nara/generation/languages/types.py
from enum import Enum

class LanguageDomain(str, Enum):
    PYTHON = "python"
    SQL = "sql"
    JAVASCRIPT = "javascript"
    SHELL = "shell"
    RUST = "rust"
