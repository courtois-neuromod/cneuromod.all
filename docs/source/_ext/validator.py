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


def load_authors(authors_path):
    """Load AUTHORS.yaml into an index keyed by gitid, orcid and id.

    Returns an empty dict if the file is missing or empty.
    """
    path = Path(authors_path)
    if not path.is_file():
        return {}
    with open(path, encoding='utf-8') as f:
        data = yaml.safe_load(f) or {}
    index = {}
    for author in data.get('authors', []):
        for key in ('id', 'gitid', 'orcid'):
            if author.get(key):
                index[author[key]] = author
    return index


def _validate_against(data, schema_name):
    try:
        import jsonschema
    except ImportError:
        return []
    schema_path = Path(__file__).parent.parent.parent / schema_name
    with open(schema_path, encoding='utf-8') as f:
        schema = json.load(f)
    return [
        f"{error.json_path}: {error.message}"
        for error in jsonschema.Draft202012Validator(schema).iter_errors(data)
    ]


def validate_authors(authors_path):
    """Validate AUTHORS.yaml against authors.schema.json. Returns error strings."""
    with open(authors_path, encoding='utf-8') as f:
        data = yaml.safe_load(f) or {}
    return _validate_against(data, 'authors.schema.json')


def validate_contributors(contributors_path, authors):
    """Validate a contributors.json (CRediT format).

    Checks the JSON schema (including CRediT role names) and that every
    contributor resolves to an entry of the ``authors`` index. Returns a list
    of error strings, empty if valid.
    """
    with open(contributors_path, encoding='utf-8') as f:
        data = json.load(f)
    errors = _validate_against(data, 'contributors.schema.json')
    for c in data.get('contributors', []):
        key = c.get('gitid') or c.get('orcid') or c.get('id')
        if key and key not in authors:
            errors.append(f"contributor '{key}' not found in AUTHORS.yaml")
    return errors
