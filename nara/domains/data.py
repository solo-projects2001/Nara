from nara.domains.base import ExecutionDomain

class DataDomain(ExecutionDomain):
    name = "data"
    subdomains = ["sql", "nosql", "graph"]

    def detect(self, intent: str) -> bool:
        return any(k in intent.lower() for k in ["sql", "query", "database"])

    def select_subdomain(self, intent: str) -> str:
        return "sql"

    def runner(self, subdomain: str) -> str:
        return "query_engine"

    def validator(self):
        return "result_set_schema"

    def repair_strategy(self):
        return "query_rewrite"
