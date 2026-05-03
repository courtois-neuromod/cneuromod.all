import json
import pytest
import yaml


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
    p = tmp_path / '.all-contributorsrc'
    p.write_text(json.dumps(data), encoding='utf-8')
    return p


@pytest.fixture
def contributorsrc_empty(tmp_path):
    data = {'contributors': []}
    p = tmp_path / '.all-contributorsrc'
    p.write_text(json.dumps(data), encoding='utf-8')
    return p


@pytest.fixture
def dataset_info_yaml(tmp_path):
    data = {
        'subjects': [
            {'id': 'sub-01', 'status': 'available'},
            {'id': 'sub-02', 'status': 'pending'},
        ],
        'duration': {
            'n_sessions_min': 5,
            'n_sessions_max': 10,
            'hours_per_participant': 8,
            'hours_total': 48,
        },
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
