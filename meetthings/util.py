import json
import os

from typing import Optional, List, Any  # noqa


def load_schema(name: str) -> dict:
    here, _ = os.path.split(__file__)
    api_path = os.path.join(here, "schema", name + ".json")
    with open(api_path, "r") as f:
        schema = json.load(f)

    return schema


def get_validators(field_schema: dict):
    field_validators_schema = field_schema.get("validators")

    if field_validators_schema is not None:
        field_validators = [
            getattr(validator, "validators")(**args)
            for validator, args in field_validators_schema.items()
        ]
        return field_validators
