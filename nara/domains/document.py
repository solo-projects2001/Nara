from nara.domains.base import ExecutionDomain

class DocumentDomain(ExecutionDomain):
    name = "document"
    subdomains = ["markdown", "latex", "mermaid", "plantuml"]

    def detect(self, intent: str) -> bool:
        return "document" in intent.lower() or "diagram" in intent.lower()

    def select_subdomain(self, intent: str) -> str:
        return "markdown"

    def runner(self, subdomain: str) -> str:
        return "renderer"

    def validator(self):
        return "render_success"

    def repair_strategy(self):
        return "syntax_repair"
