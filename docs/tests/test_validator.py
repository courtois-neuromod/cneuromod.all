import sys
from pathlib import Path
from unittest import mock

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / 'source'))

from _ext.validator import validate_dataset_info, _load_schema


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
