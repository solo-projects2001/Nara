# nara/contracts/schema.py
from pydantic import BaseModel

class ContractSchema(BaseModel):
    input_type: str
    output_type: str
    deterministic: bool = True
    offline_only: bool = True
