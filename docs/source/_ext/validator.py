import copy
import json
from pathlib import Path

import yaml


def _load_schema():
    schema_path = Path(__file__).parent.parent.parent.parent / 'docs' / 'schema.json'
    with open(schema_path, encoding='utf-8') as f:
        return json.load(f)


def validate_dataset_info(info_path, schema=None):
    """Validate the stats block of a dataset_info.yaml against schema.json.

    Returns a list of validation error strings, empty if valid or if
    jsonschema is not installed.
    """
    try:
        import jsonschema
    except ImportError:
        return []

    if schema is None:
        schema = _load_schema()

    with open(info_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)

    if not data:
        return []

    stats = data.get('stats')
    if not stats:
        return []

    # Strip required so absence of name/reference doesn't fail
    stats_schema = copy.deepcopy(schema)
    stats_schema.pop('required', None)

    validator = jsonschema.Draft202012Validator(stats_schema)
    return [
        f"{error.json_path}: {error.message}"
        for error in validator.iter_errors(stats)
    ]
