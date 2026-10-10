import sys
from pathlib import Path
from unittest import mock

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / 'source'))

from _ext.validator import validate_dataset_info, _load_schema, load_authors, validate_authors, validate_contributors


class TestValidateDatasetInfo:
    def test_valid_stats_no_errors(self, dataset_info_yaml_valid_stats, schema_path):
        schema = _load_schema()
        errors = validate_dataset_info(dataset_info_yaml_valid_stats, schema)
        assert errors == []

    def test_invalid_type_returns_errors(self, dataset_info_yaml_invalid_stats, schema_path):
        schema = _load_schema()
        errors = validate_dataset_info(dataset_info_yaml_invalid_stats, schema)
        assert len(errors) > 0
        assert any('six' in e or 'integer' in e or 'string' in e for e in errors)

    def test_missing_stats_block_returns_empty(self, dataset_info_yaml_empty):
        schema = _load_schema()
        errors = validate_dataset_info(dataset_info_yaml_empty, schema)
        assert errors == []

    def test_unknown_key_rejected(self, dataset_info_yaml_extra_key_stats):
        schema = _load_schema()
        errors = validate_dataset_info(dataset_info_yaml_extra_key_stats, schema)
        assert len(errors) > 0
        assert any('extra_field' in e or 'Additional' in e for e in errors)

    def test_jsonschema_not_required(self, dataset_info_yaml_invalid_stats):
        with mock.patch.dict(sys.modules, {'jsonschema': None}):
            errors = validate_dataset_info(dataset_info_yaml_invalid_stats)
        assert errors == []

    def test_load_schema_returns_dict(self):
        schema = _load_schema()
        assert isinstance(schema, dict)
        assert '$schema' in schema
        assert 'properties' in schema


class TestContributors:
    def test_valid(self, contributorsrc, authors_index):
        assert validate_contributors(contributorsrc, authors_index) == []

    def test_invalid_role_and_unknown_id(self, contributorsrc_bad, authors_index):
        errors = validate_contributors(contributorsrc_bad, authors_index)
        assert any('Wizardry' in e for e in errors)
        assert any("'ghost' not found" in e for e in errors)

    def test_authors_yaml(self, authors_yaml):
        assert validate_authors(authors_yaml) == []
        index = load_authors(authors_yaml)
        assert index['0000-0001-2345-6789'] is index['asmith']

    def test_load_authors_missing_file(self, tmp_path):
        assert load_authors(tmp_path / 'nope.yaml') == {}
