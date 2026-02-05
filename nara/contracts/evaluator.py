from nara.contracts.violations import ContractViolation

def evaluate_preconditions(contract, context: dict):
    for pre in contract.preconditions:
        if not pre.check(context):
            raise ContractViolation("precondition", pre.description)

def evaluate_postconditions(contract, context: dict):
    for post in contract.postconditions:
        if not post.check(context):
            raise ContractViolation("postcondition", post.description)

def evaluate_invariants(contract, context: dict):
    for inv in contract.invariants:
        if not inv.check(context):
            raise ContractViolation("invariant", inv.description)
