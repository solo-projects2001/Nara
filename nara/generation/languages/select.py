# nara/generation/languages/select.py
from nara.generation.languages.types import LanguageDomain

def select_language(domain: str) -> LanguageDomain:
    d = domain.strip().lower()

    if d == "data":
        return LanguageDomain.SQL

    if d == "shell":
        return LanguageDomain.SHELL

    if d == "analysis":
        return LanguageDomain.PYTHON

    return LanguageDomain.PYTHON
