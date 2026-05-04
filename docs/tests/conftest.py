import json
import pytest
import yaml
from pathlib import Path


@pytest.fixture
def citation_cff(tmp_path):
    data = {
        'cff-version': '1.2.0',
        'type': 'dataset',
        'title': 'My Dataset',
        'preferred-citation': {
            'authors': [
                {'family-names': 'Smith', 'given-names': 'Alice'},
                {'family-names': 'Jones', 'given-names': 'Bob'},
            ],
            'title': 'A great paper',
            'journal': 'NeuroImage',
            'year': 2023,
            'volume': 10,
            'pages': '1-10',
            'doi': '10.1234/test',
        },
    }
    p = tmp_path / 'CITATION.cff'
    p.write_text(yaml.dump(data), encoding='utf-8')
    return p


@pytest.fixture
def citation_cff_many_authors(tmp_path):
    authors = [
        {'family-names': f'Author{i}', 'given-names': f'Given{i}'}
        for i in range(7)
    ]
    data = {
        'cff-version': '1.2.0',
        'type': 'dataset',
        'title': 'Big Paper Dataset',
        'preferred-citation': {
            'authors': authors,
            'title': 'Many authors paper',
            'year': 2024,
            'doi': '10.9999/big',
        },
    }
    p = tmp_path / 'CITATION.cff'
    p.write_text(yaml.dump(data), encoding='utf-8')
    return p


@pytest.fixture
def citation_cff_no_preferred(tmp_path):
    data = {'cff-version': '1.2.0', 'type': 'dataset', 'title': 'No Cite Dataset'}
    p = tmp_path / 'CITATION.cff'
    p.write_text(yaml.dump(data), encoding='utf-8')
    return p


@pytest.fixture
def contributorsrc(tmp_path):
    data = {
        'contributors': [
            {
                'name': 'Alice Smith',
                'profile': 'https://github.com/asmith',
                'contributions': ['data', 'code'],
            },
            {
                'name': 'Bob Jones',
                'contributions': ['doc'],
            },
        ],
    }
    p = tmp_path / 'contributors.json'
    p.write_text(json.dumps(data), encoding='utf-8')
    return p


@pytest.fixture
def contributorsrc_empty(tmp_path):
    data = {'contributors': []}
    p = tmp_path / 'contributors.json'
    p.write_text(json.dumps(data), encoding='utf-8')
    return p


@pytest.fixture
def dataset_info_yaml(tmp_path):
    data = {
        'subjects': [
            {'id': 'sub-01', 'status': 'available'},
            {'id': 'sub-02', 'status': 'pending'},
        ],
        'tasks': [
            {'emoji': '🎬', 'label': 'Movie watching', 'note': 'natural stimuli'},
        ],
        'modalities': [
            {
                'emoji': '🧠',
                'label': 'fMRI',
                'components': [
                    {'label': 'BOLD', 'status': 'available'},
                    {'label': 'T1w', 'status': 'pending'},
                ],
            },
        ],
    }
    p = tmp_path / 'dataset_info.yaml'
    p.write_text(yaml.dump(data), encoding='utf-8')
    return p


@pytest.fixture
def dataset_info_yaml_empty(tmp_path):
    p = tmp_path / 'dataset_info.yaml'
    p.write_text(yaml.dump({}), encoding='utf-8')
    return p


@pytest.fixture
def dataset_info_yaml_with_stats(tmp_path):
    data = {
        'stats': {
            'subjects_n': 6,
            'neuroimaging': {
                'fmri': {'total_h': 48, 'per_subject_h': 8},
            },
            'naturalistic_stimuli': {
                'resting_state': {'total_unique': 7.5, 'per_subject_unique': 1.25},
            },
            'responses': {
                'controlled_tasks': {'total_unique': 23, 'per_subject_unique': 23},
            },
        },
        'subjects': [
            {'id': 'sub-01', 'status': 'available'},
            {'id': 'sub-02', 'status': 'available'},
        ],
        'tasks': [
            {'emoji': '🎭', 'label': 'HCP task localizers', 'note': '23 conditions'},
        ],
        'modalities': [
            {
                'emoji': '🧠',
                'label': 'Neuroimaging (fMRI)',
                'status': 'available',
                'stats_key': 'neuroimaging.fmri',
            },
            {
                'emoji': '💤',
                'label': 'Resting state',
                'stats_key': 'naturalistic_stimuli.resting_state',
                'unit': 'h',
            },
            {
                'emoji': '📊',
                'label': 'Behavior',
                'stats_key': 'responses.controlled_tasks',
            },
        ],
    }
    p = tmp_path / 'dataset_info.yaml'
    p.write_text(yaml.dump(data, allow_unicode=True), encoding='utf-8')
    return p


@pytest.fixture
def schema_path():
    return Path(__file__).parent.parent.parent / 'schema.json'


@pytest.fixture
def dataset_info_yaml_valid_stats(tmp_path):
    data = {
        'stats': {
            'subjects_n': 6,
            'neuroimaging': {'fmri': {'total_h': 54.6, 'per_subject_h': 9.1}},
            'naturalistic_stimuli': {
                'resting_state': {'total_unique': 7.5, 'per_subject_unique': 1.25},
            },
            'responses': {'controlled_tasks': {'total_unique': 21, 'per_subject_unique': 21}},
        },
    }
    p = tmp_path / 'dataset_info.yaml'
    p.write_text(yaml.dump(data), encoding='utf-8')
    return p


@pytest.fixture
def dataset_info_yaml_invalid_stats(tmp_path):
    data = {
        'stats': {
            'subjects_n': 'six',  # should be integer
            'neuroimaging': {'fmri': {'total_h': 'lots', 'per_subject_h': 9.1}},
        },
    }
    p = tmp_path / 'dataset_info.yaml'
    p.write_text(yaml.dump(data), encoding='utf-8')
    return p


@pytest.fixture
def dataset_info_yaml_extra_key_stats(tmp_path):
    data = {
        'stats': {
            'neuroimaging': {
                'fmri': {'total_h': 10.0, 'per_subject_h': 2.0, 'extra_field': 99},
            },
        },
    }
    p = tmp_path / 'dataset_info.yaml'
    p.write_text(yaml.dump(data), encoding='utf-8')
    return p
