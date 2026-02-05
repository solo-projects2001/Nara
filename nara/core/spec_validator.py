import json
from jsonschema import validate, ValidationError

def validate_spec(spec_path: str, schema_path: str):
    with open(spec_path) as f:
        spec = json.load(f)

    with open(schema_path) as f:
        schema = json.load(f)

    try:
        validate(instance=spec, schema=schema)
    except ValidationError as e:
        raise RuntimeError(f"spec_validation_failed: {e.message}")
